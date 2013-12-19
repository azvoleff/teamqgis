# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_settings.ui'
#
# Created: Thu Dec 19 15:33:12 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(325, 395)
        self.gridLayout = QtGui.QGridLayout(Settings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.useDualView = QtGui.QCheckBox(Settings)
        self.useDualView.setMaximumSize(QtCore.QSize(16777215, 17))
        self.useDualView.setObjectName(_fromUtf8("useDualView"))
        self.gridLayout.addWidget(self.useDualView, 2, 1, 1, 1)
        self.readClassesCSV = QtGui.QPushButton(Settings)
        self.readClassesCSV.setObjectName(_fromUtf8("readClassesCSV"))
        self.gridLayout.addWidget(self.readClassesCSV, 12, 0, 1, 1)
        self.yres = QtGui.QDoubleSpinBox(Settings)
        self.yres.setMaximumSize(QtCore.QSize(16777215, 20))
        self.yres.setDecimals(4)
        self.yres.setMinimum(0.0)
        self.yres.setMaximum(600.0)
        self.yres.setProperty("value", 30.0)
        self.yres.setObjectName(_fromUtf8("yres"))
        self.gridLayout.addWidget(self.yres, 7, 1, 1, 1)
        self.rubberWidth = QtGui.QDoubleSpinBox(Settings)
        self.rubberWidth.setMaximumSize(QtCore.QSize(16777215, 20))
        self.rubberWidth.setToolTip(_fromUtf8(""))
        self.rubberWidth.setDecimals(1)
        self.rubberWidth.setSingleStep(1.0)
        self.rubberWidth.setProperty("value", 2.0)
        self.rubberWidth.setObjectName(_fromUtf8("rubberWidth"))
        self.gridLayout.addWidget(self.rubberWidth, 4, 1, 1, 1)
        self.xres = QtGui.QDoubleSpinBox(Settings)
        self.xres.setMaximumSize(QtCore.QSize(16777215, 20))
        self.xres.setDecimals(4)
        self.xres.setMinimum(0.0)
        self.xres.setMaximum(600.0)
        self.xres.setProperty("value", 30.0)
        self.xres.setObjectName(_fromUtf8("xres"))
        self.gridLayout.addWidget(self.xres, 8, 1, 1, 1)
        self.scale = QtGui.QSpinBox(Settings)
        self.scale.setMaximumSize(QtCore.QSize(16777215, 20))
        self.scale.setMinimum(1)
        self.scale.setMaximum(1000)
        self.scale.setProperty("value", 40)
        self.scale.setObjectName(_fromUtf8("scale"))
        self.gridLayout.addWidget(self.scale, 3, 1, 1, 1)
        self.saveSelectionInProject = QtGui.QCheckBox(Settings)
        self.saveSelectionInProject.setMaximumSize(QtCore.QSize(16777215, 17))
        self.saveSelectionInProject.setChecked(True)
        self.saveSelectionInProject.setObjectName(_fromUtf8("saveSelectionInProject"))
        self.gridLayout.addWidget(self.saveSelectionInProject, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 20, 1, 1, 1)
        self.scalinglabel = QtGui.QLabel(Settings)
        self.scalinglabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.scalinglabel.setObjectName(_fromUtf8("scalinglabel"))
        self.gridLayout.addWidget(self.scalinglabel, 3, 0, 1, 1)
        self.rubbersizelabel = QtGui.QLabel(Settings)
        self.rubbersizelabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.rubbersizelabel.setObjectName(_fromUtf8("rubbersizelabel"))
        self.gridLayout.addWidget(self.rubbersizelabel, 4, 0, 1, 1)
        self.allowedclasslabel = QtGui.QLabel(Settings)
        self.allowedclasslabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.allowedclasslabel.setObjectName(_fromUtf8("allowedclasslabel"))
        self.gridLayout.addWidget(self.allowedclasslabel, 9, 0, 1, 2)
        self.xshiftlabel = QtGui.QLabel(Settings)
        self.xshiftlabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.xshiftlabel.setObjectName(_fromUtf8("xshiftlabel"))
        self.gridLayout.addWidget(self.xshiftlabel, 8, 0, 1, 1)
        self.yshiftlabel = QtGui.QLabel(Settings)
        self.yshiftlabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.yshiftlabel.setObjectName(_fromUtf8("yshiftlabel"))
        self.gridLayout.addWidget(self.yshiftlabel, 7, 0, 1, 1)
        self.rubberbandcolorlabel = QtGui.QLabel(Settings)
        self.rubberbandcolorlabel.setMinimumSize(QtCore.QSize(145, 21))
        self.rubberbandcolorlabel.setMaximumSize(QtCore.QSize(145, 21))
        self.rubberbandcolorlabel.setObjectName(_fromUtf8("rubberbandcolorlabel"))
        self.gridLayout.addWidget(self.rubberbandcolorlabel, 6, 0, 1, 1)
        self.dockarealabel = QtGui.QLabel(Settings)
        self.dockarealabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dockarealabel.setObjectName(_fromUtf8("dockarealabel"))
        self.gridLayout.addWidget(self.dockarealabel, 0, 0, 1, 1)
        self.rubberColor = QtGui.QLabel(Settings)
        self.rubberColor.setMinimumSize(QtCore.QSize(144, 21))
        self.rubberColor.setMaximumSize(QtCore.QSize(144, 24))
        self.rubberColor.setText(_fromUtf8(""))
        self.rubberColor.setObjectName(_fromUtf8("rubberColor"))
        self.gridLayout.addWidget(self.rubberColor, 6, 1, 1, 1)
        self.dockArea = QtGui.QComboBox(Settings)
        self.dockArea.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dockArea.setObjectName(_fromUtf8("dockArea"))
        self.dockArea.addItem(_fromUtf8(""))
        self.dockArea.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.dockArea, 0, 1, 1, 1)
        self.saveClassesCSV = QtGui.QPushButton(Settings)
        self.saveClassesCSV.setObjectName(_fromUtf8("saveClassesCSV"))
        self.gridLayout.addWidget(self.saveClassesCSV, 12, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 13, 1, 2, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.removeClassButton = QtGui.QPushButton(Settings)
        self.removeClassButton.setEnabled(False)
        self.removeClassButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.removeClassButton.setObjectName(_fromUtf8("removeClassButton"))
        self.gridLayout_2.addWidget(self.removeClassButton, 1, 2, 1, 1)
        self.addClassLineEdit = QtGui.QLineEdit(Settings)
        self.addClassLineEdit.setEnabled(True)
        self.addClassLineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.addClassLineEdit.setText(_fromUtf8(""))
        self.addClassLineEdit.setObjectName(_fromUtf8("addClassLineEdit"))
        self.gridLayout_2.addWidget(self.addClassLineEdit, 1, 0, 1, 1)
        self.addClassButton = QtGui.QPushButton(Settings)
        self.addClassButton.setEnabled(False)
        self.addClassButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.addClassButton.setObjectName(_fromUtf8("addClassButton"))
        self.gridLayout_2.addWidget(self.addClassButton, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 10, 0, 1, 2)
        self.classesListWidget = QtGui.QListWidget(Settings)
        self.classesListWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
        self.classesListWidget.setDragEnabled(True)
        self.classesListWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.classesListWidget.setObjectName(_fromUtf8("classesListWidget"))
        self.gridLayout.addWidget(self.classesListWidget, 11, 0, 1, 2)

        self.retranslateUi(Settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "teamqgis :: settings", None))
        self.useDualView.setText(_translate("Settings", "use dual view", None))
        self.readClassesCSV.setText(_translate("Settings", "Read classes from CSV", None))
        self.saveSelectionInProject.setText(_translate("Settings", "save selection in project", None))
        self.scalinglabel.setText(_translate("Settings", "Scaling", None))
        self.rubbersizelabel.setText(_translate("Settings", "Rubberband size", None))
        self.allowedclasslabel.setText(_translate("Settings", "Allowed classes:", None))
        self.xshiftlabel.setText(_translate("Settings", "X shift", None))
        self.yshiftlabel.setText(_translate("Settings", "Y shift", None))
        self.rubberbandcolorlabel.setText(_translate("Settings", "Rubberband color", None))
        self.dockarealabel.setText(_translate("Settings", "Dock area", None))
        self.dockArea.setItemText(0, _translate("Settings", "left", None))
        self.dockArea.setItemText(1, _translate("Settings", "right", None))
        self.saveClassesCSV.setText(_translate("Settings", "Save classes to CSV", None))
        self.removeClassButton.setText(_translate("Settings", "-", None))
        self.addClassLineEdit.setPlaceholderText(_translate("Settings", "Click to enter a new class name...", None))
        self.addClassButton.setText(_translate("Settings", "+", None))

