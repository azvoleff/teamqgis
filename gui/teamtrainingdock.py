#-----------------------------------------------------------
#
# teamtraining is a QGIS plugin which allows you to browse a multiple selection.
#
# Copyright    : (C) 2013 Denis Rouzaud
# Email        : denis.rouzaud@gmail.com
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this progsram; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

from PyQt4.QtCore import SIGNAL, pyqtSlot, pyqtSignal, Qt
from PyQt4.QtGui import QDockWidget, QIcon, QAction
from qgis.core import QgsPoint, QgsRectangle, QgsFeatureRequest, QgsFeature
from qgis.gui import QgsRubberBand, QgsMessageViewer
from qgis.utils import iface

from ..core.mysettings import MySettings
from ..ui.ui_teamtraining import Ui_teamtraining

from dualview import ViewWindow

class teamtrainingDock(QDockWidget, Ui_teamtraining):
    dockRemoved = pyqtSignal(str)

    def __init__(self, iface, layer, currentFeature):
        self.iface = iface
        self.layer = layer
        self.renderer = self.iface.mapCanvas().mapRenderer()
        self.settings = MySettings()
        QDockWidget.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("teamtraining: %s" % layer.name())
        if layer.hasGeometryType() is False:
            self.panCheck.setChecked(False)
            self.panCheck.setEnabled(False)
            self.scaleCheck.setChecked(False)
            self.scaleCheck.setEnabled(False)

        self.previousButton.setArrowType(Qt.LeftArrow)
        self.nextButton.setArrowType(Qt.RightArrow)
        icon = QIcon(":/plugins/teamtraining/icons/openform.svg")
        self.editFormButton.setIcon(icon)

        # actions
        icon = QIcon(":/plugins/teamtraining/icons/action.svg")
        self.actionButton.setIcon(icon)
        self.attrAction = layer.actions()
        actions = [self.attrAction[i] for i in range(self.attrAction.size())]
        preferredAction = layer.customProperty("teamtrainingPreferedAction", "")
        if preferredAction not in actions:
            dfltAction = self.attrAction.defaultAction()
            if dfltAction > len(actions):
                preferredAction = self.attrAction[dfltAction].name()
        preferredActionFound = False
        for i, action in enumerate(actions):
            qAction = QAction(QIcon(":/plugins/teamtraining/icons/action.svg"), action.name(), self)
            qAction.triggered.connect(lambda: self.doAction(i))
            self.actionButton.addAction(qAction)
            if action.name() == preferredAction:
                self.actionButton.setDefaultAction(qAction)
                preferredActionFound = True
        if len(actions) == 0:
            self.actionButton.setEnabled(False)
        elif not preferredActionFound:
            self.actionButton.setDefaultAction(self.actionButton.actions()[0])

        self.rubber = QgsRubberBand(self.iface.mapCanvas())
        self.selectionChanged()
        if currentFeature == self.listCombo.currentIndex():
            self.on_listCombo_currentIndexChanged(currentFeature)
        else:
            self.listCombo.setCurrentIndex(currentFeature)
        self.layer.layerDeleted.connect(self.close)
        self.layer.selectionChanged.connect(self.selectionChanged)
        self.layer.layerModified.connect(self.layerChanged)
        self.layer.editingStopped.connect(self.layerSaved)

    def updateFieldComboBoxes(self):
        fieldNameMap = self.layer.dataProvider().fieldNameMap()
        for fieldName in fieldNameMap.keys():
            self.fieldOneNameComboBox.addItem("%s"%fieldName)
            self.fieldTwoNameComboBox.addItem("%s"%fieldName)
            self.fieldThreeNameComboBox.addItem("%s"%fieldName)

        feature = self.getCurrentItem()

        fieldOneNameCurrentIndex = feature.fieldNameIndex(self.fieldOneNameComboBox.currentText())
        self.fieldOneValueComboBox.setEnabled(True)
        self.fieldOneValueComboBox.addItem(feature.attribute(self.fieldOneNameComboBox.currentText()))

        fieldTwoNameCurrentIndex = feature.fieldNameIndex(self.fieldTwoNameComboBox.currentText())
        self.fieldTwoValueComboBox.setEnabled(True)
        self.fieldTwoValueComboBox.addItem(feature.attribute(self.fieldTwoNameComboBox.currentText()))

        # fieldOneNameCurrentIndex = feature.fieldNameIndex(self.fieldOneNameComboBox.currentText())
        # self.fieldOneValueComboBox.setEnabled(True)
        # self.fieldOneValueComboBox.addItem(feature.attribute(self.fieldOneNameComboBox.currentText()))

    def getUniqueFieldValues(self, fieldIndex):
        uValues = []
        ft = QgsFeature()
        while self.layer.dataProvider().nextFeature(ft):
            atMap = ft.attributeMap()
            if atMap.values()[fieldIndex].toString() not in uValues:
                uValues.append(atMap.values()[fieldIndex].toString())
        return uValues

    def setRubber(self, feature):
        self.rubber.setColor(self.settings.value("rubberColor"))
        self.rubber.setWidth(self.settings.value("rubberWidth"))
        ##self.rubber.setLineStyle(Qt.DotLine)
        self.rubber.setBrushStyle(Qt.NoBrush)
        self.rubber.setToGeometry(feature.geometry(), self.layer)

    def closeEvent(self, e):
        self.rubber.reset()
        self.layer.layerDeleted.disconnect(self.close)
        self.layer.selectionChanged.disconnect(self.selectionChanged)
        if self.settings.value("saveSelectionInProject"):
            self.layer.setCustomProperty("teamtrainingSelection", repr([]))
        self.dockRemoved.emit(self.layer.id())
          
    def selectionChanged(self):
        self.cleanBrowserFields()
        self.rubber.reset()
        nItems = self.layer.selectedFeatureCount()
        if nItems < 2:
            self.close()
            self.layer.emit(SIGNAL("browserNoItem()"))
            return
        self.browseFrame.setEnabled(True)
        self.subset = self.layer.selectedFeaturesIds()
        if self.settings.value("saveSelectionInProject"):
            self.layer.setCustomProperty("teamtrainingSelection", repr(self.subset))
        for fid in self.subset:
            self.listCombo.addItem("%u" % fid)
        self.setRubber(self.getCurrentItem())
        self.updateFieldComboBoxes()

    def layerChanged(self):
        self.applyChangesButton.setEnabled(True)

    def layerSaved(self):
        self.applyChangesButton.setEnabled(False)

    def cleanBrowserFields(self):
        self.currentPosLabel.setText('0/0')
        self.listCombo.clear()
        self.fieldOneNameComboBox.clear()
        self.fieldTwoNameComboBox.clear()
        self.fieldThreeNameComboBox.clear()
          
    def panScaleToItem(self, feature):
        if self.panCheck.isChecked() is False:
            return
        featBobo = feature.geometry().boundingBox()
        # if scaling and bobo has width and height (i.e. not a point)
        if self.scaleCheck.isChecked() and featBobo.width() != 0 and featBobo.height() != 0:
            featBobo.scale(self.settings.value("scale"))
            ul = self.renderer.layerToMapCoordinates(self.layer, QgsPoint(featBobo.xMinimum(), featBobo.yMaximum()))
            ur = self.renderer.layerToMapCoordinates(self.layer, QgsPoint(featBobo.xMaximum(), featBobo.yMaximum()))
            ll = self.renderer.layerToMapCoordinates(self.layer, QgsPoint(featBobo.xMinimum(), featBobo.yMinimum()))
            lr = self.renderer.layerToMapCoordinates(self.layer, QgsPoint(featBobo.xMaximum(), featBobo.yMinimum()))
            x = (ul.x(), ur.x(), ll.x(), lr.x())
            y = (ul.y(), ur.y(), ll.y(), lr.y())
            x0 = min(x)
            y0 = min(y)
            x1 = max(x)
            y1 = max(y)
        else:
            panTo = self.renderer.layerToMapCoordinates(self.layer, featBobo.center())
            mapBobo = self.iface.mapCanvas().extent()
            xshift = panTo.x() - mapBobo.center().x()
            yshift = panTo.y() - mapBobo.center().y()
            x0 = mapBobo.xMinimum() + xshift
            y0 = mapBobo.yMinimum() + yshift
            x1 = mapBobo.xMaximum() + xshift
            y1 = mapBobo.yMaximum() + yshift
        self.iface.mapCanvas().setExtent(QgsRectangle(x0, y0, x1, y1))
        self.iface.mapCanvas().refresh()

    def getCurrentItem(self):
        i = self.listCombo.currentIndex()
        if i == -1:
            return None
        f = QgsFeature()
        if self.layer.getFeatures(QgsFeatureRequest().setFilterFid(self.subset[i])).nextFeature(f):
            return f
        else:
            raise NameError("feature not found")

    def doAction(self, i):
        f = self.getCurrentItem()
        self.actionButton.setDefaultAction(self.actionButton.actions()[i])
        self.layer.setCustomProperty("teamtrainingPreferedAction", self.attrAction[i].name())
        self.attrAction.doActionFeature(i, f)

    def doTranslate(self, trans):
        # Based on the "doaffine" function in the qgsAffine plugin
        warn = QgsMessageViewer()
        if (self.layer.geometryType() == 2):
            start=1
        else:
            start=0
        if (not self.layer.isEditable()):
            warn.setMessageAsPlainText("Layer not in edit mode.")
            warn.showMessage()
        else:
            feature = self.getCurrentItem()
            result = feature.geometry()
            i = start
            vertex = result.vertexAt(i)
            fid = feature.id()
            while (vertex != QgsPoint(0, 0)):
                newx = vertex.x() + trans[0] * float(self.settings.value("xres"))
                newy = vertex.y() + trans[1] * float(self.settings.value("yres"))
                result.moveVertex(newx, newy, i)
                i += 1
                vertex = result.vertexAt(i)
            self.layer.changeGeometry(fid, result)
            self.iface.mapCanvas().refresh()
            self.rubber.reset()
            self.setRubber(feature)

    @pyqtSlot(name="on_previousButton_clicked")
    def previousFeature(self):
        i = self.listCombo.currentIndex()
        n = max(0, i-1)
        self.listCombo.setCurrentIndex(n)
        self.saveCurrentFeature(n)

    @pyqtSlot(name="on_nextButton_clicked")
    def nextFeature(self):
        i = self.listCombo.currentIndex()
        c = self.listCombo.count()
        n = min(i+1, c-1)
        self.listCombo.setCurrentIndex(n)
        self.saveCurrentFeature(n)

    @pyqtSlot(int, name="on_listCombo_activated")
    def saveCurrentFeature(self, i):
        if self.settings.value("saveSelectionInProject"):
            self.layer.setCustomProperty("teamtrainingCurrentItem", i)

    @pyqtSlot(int, name="on_listCombo_currentIndexChanged")
    def on_listCombo_currentIndexChanged(self, i):
        feature = self.getCurrentItem()
        if feature is None: 
            return
        self.rubber.reset()
        if self.listCombo.count() > 1:
            self.setRubber(feature)
        # scale to feature
        self.panScaleToItem(feature)
        # Update browser
        self.currentPosLabel.setText("%u/%u" % (i+1, len(self.subset)))
        # emit signal
        self.layer.emit(SIGNAL("browserCurrentItem(long)"), feature.id())
        if self.settings.value("useDualView"):
            # dv = ViewWindow(iface.activeLayer())
            # dv.show()
            pass
          
    @pyqtSlot(int, name="on_panCheck_stateChanged")
    def on_panCheck_stateChanged(self, i):
        if self.panCheck.isChecked():
            self.scaleCheck.setEnabled(True)
            feature = self.getCurrentItem()
            if feature is None:
                return
            self.panScaleToItem(feature)
        else:
            self.scaleCheck.setEnabled(False)
               
    @pyqtSlot(int, name="on_scaleCheck_stateChanged")
    def on_scaleCheck_stateChanged(self, i):
        if self.scaleCheck.isChecked():
            feature = self.getCurrentItem()
            if feature is None: 
                return
            self.panScaleToItem(feature)

    @pyqtSlot(name="on_editFormButton_clicked")
    def openFeatureForm(self):
        self.iface.openFeatureForm(self.layer, self.getCurrentItem())

    @pyqtSlot(name="on_translateRightButton_clicked")
    def doTranslateRight(self):
        self.doTranslate((1, 0))

    @pyqtSlot(name="on_translateLeftButton_clicked")
    def doTranslateLeft(self):
        self.doTranslate((-1, 0))

    @pyqtSlot(name="on_translateUpButton_clicked")
    def doTranslateUp(self):
        self.doTranslate((0, 1))

    @pyqtSlot(name="on_translateDownButton_clicked")
    def doTranslateDown(self):
        self.doTranslate((0, -1))

    @pyqtSlot(name="on_applyChangesButton_clicked")
    def applyChanges(self):
        self.layer.commitChanges()
        self.layer.startEditing()
        self.layer.updateExtents()
        self.iface.mapCanvas().refresh()
