# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_settings.ui'
#
# Created: Mon Dec 16 16:51:32 2013
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
        Settings.resize(292, 201)
        self.gridLayout = QtGui.QGridLayout(Settings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(Settings)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtGui.QLabel(Settings)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.saveSelectionInProject = QtGui.QCheckBox(Settings)
        self.saveSelectionInProject.setChecked(True)
        self.saveSelectionInProject.setObjectName(_fromUtf8("saveSelectionInProject"))
        self.gridLayout.addWidget(self.saveSelectionInProject, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.rubberWidth = QtGui.QDoubleSpinBox(Settings)
        self.rubberWidth.setToolTip(_fromUtf8(""))
        self.rubberWidth.setDecimals(1)
        self.rubberWidth.setSingleStep(1.0)
        self.rubberWidth.setProperty("value", 2.0)
        self.rubberWidth.setObjectName(_fromUtf8("rubberWidth"))
        self.gridLayout.addWidget(self.rubberWidth, 3, 1, 1, 1)
        self.scale = QtGui.QSpinBox(Settings)
        self.scale.setMinimum(1)
        self.scale.setMaximum(50)
        self.scale.setProperty("value", 5)
        self.scale.setObjectName(_fromUtf8("scale"))
        self.gridLayout.addWidget(self.scale, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Settings)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)
        self.rubberColor = QtGui.QLabel(Settings)
        self.rubberColor.setText(_fromUtf8(""))
        self.rubberColor.setObjectName(_fromUtf8("rubberColor"))
        self.gridLayout.addWidget(self.rubberColor, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Settings)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.dockArea = QtGui.QComboBox(Settings)
        self.dockArea.setObjectName(_fromUtf8("dockArea"))
        self.dockArea.addItem(_fromUtf8(""))
        self.dockArea.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.dockArea, 0, 1, 1, 1)
        self.useDualView = QtGui.QCheckBox(Settings)
        self.useDualView.setObjectName(_fromUtf8("useDualView"))
        self.gridLayout.addWidget(self.useDualView, 1, 1, 1, 1)

        self.retranslateUi(Settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "teamtraining :: settings", None))
        self.label_2.setText(_translate("Settings", "Rubberband size", None))
        self.label.setText(_translate("Settings", "Rubberband color", None))
        self.saveSelectionInProject.setText(_translate("Settings", "save selection in project", None))
        self.label_3.setText(_translate("Settings", "Scaling", None))
        self.label_4.setText(_translate("Settings", "Dock area", None))
        self.dockArea.setItemText(0, _translate("Settings", "left", None))
        self.dockArea.setItemText(1, _translate("Settings", "right", None))
        self.useDualView.setText(_translate("Settings", "use dual view", None))

