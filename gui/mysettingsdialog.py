#-----------------------------------------------------------
#
# teamqgis is a QGIS plugin which allows you to browse a multiple selection.
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

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QSizePolicy
from qgis.gui import QgsMessageBar

from ..qgissettingmanager import SettingDialog

from ..core.mysettings import MySettings

from ..ui.ui_settings import Ui_Settings


class MySettingsDialog(QDialog, Ui_Settings, SettingDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.settings = MySettings()
        SettingDialog.__init__(self, self.settings)

        self.bar = QgsMessageBar()
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.layout().addWidget(self.bar, 0, 0, 1, 2)

        # self.classesListWidget.itemActivated.connect(self.classesListWidget_itemActivated)
        self.addClassLineEdit.textEdited.connect(self.addClassLineEdit_textEdited)
        #self.addClassLineEdit.focusOutEvent = self.addClassLineEdit_focusOutEvent

    # def classesListWidget_itemActivated(self):
    #     self.removeClassButton.setEnabled(True)

    def addClassLineEdit_textEdited(self):
        self.addClassButton.setEnabled(True)

    # Commented out as need to figure out how to keep the focusOut from acting 
    # when the addClassButton is clicked (making it so the field clears before 
    # the class is added)
    # def addClassLineEdit_focusOutEvent(self, event):
    #     print event
    #     self.addClassButton.setEnabled(False)
    #     self.addClassLineEdit.clear()

    @pyqtSlot(name="on_removeClassButton_clicked")
    def removeClassButton_clicked(self):
        self.classesListWidget.takeItem(self.classesListWidget.currentRow())

    @pyqtSlot(name="on_addClassButton_clicked")
    def addClassButton_clicked(self):
        newClass = self.addClassLineEdit.text()
        if newClass != "":
            existingClasses = [self.classesListWidget.item(n).text() for n in range(self.classesListWidget.count())]
            print existingClasses
            if newClass in existingClasses:
                self.bar.pushMessage("Error", '"%s" already in allowed classes list'%newClass, level=QgsMessageBar.WARNING, duration=3)
            else:
                self.classesListWidget.addItem(newClass)
        self.addClassButton.setEnabled(False)
        self.addClassLineEdit.clear()

    @pyqtSlot(int, name="on_classesListWidget_currentRowChanged")
    def classesListWidget_currentRowChanged(self):
        if self.classesListWidget.count() > 0:
            self.removeClassButton.setEnabled(True)
        else:
            self.removeClassButton.setEnabled(False)

        #self.layer.setCustomProperty('teamqgis' + nameComboBox.objectName(), nameComboBox.currentText())
