# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_itembrowser.ui'
#
# Created: Tue Apr 10 10:52:52 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_itembrowser(object):
    def setupUi(self, itembrowser):
        itembrowser.setObjectName(_fromUtf8("itembrowser"))
        itembrowser.resize(283, 179)
        itembrowser.setWindowTitle(_fromUtf8("Item Browser"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.browseFrame = QtGui.QFrame(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseFrame.sizePolicy().hasHeightForWidth())
        self.browseFrame.setSizePolicy(sizePolicy)
        self.browseFrame.setAutoFillBackground(False)
        self.browseFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.browseFrame.setObjectName(_fromUtf8("browseFrame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.browseFrame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.currentPosLabel = QtGui.QLabel(self.browseFrame)
        self.currentPosLabel.setToolTip(_fromUtf8(""))
        self.currentPosLabel.setAccessibleName(_fromUtf8(""))
        self.currentPosLabel.setAccessibleDescription(_fromUtf8(""))
        self.currentPosLabel.setText(_fromUtf8("0/0"))
        self.currentPosLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentPosLabel.setObjectName(_fromUtf8("currentPosLabel"))
        self.gridLayout_2.addWidget(self.currentPosLabel, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(self.browseFrame)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.previousButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousButton.sizePolicy().hasHeightForWidth())
        self.previousButton.setSizePolicy(sizePolicy)
        self.previousButton.setMaximumSize(QtCore.QSize(21, 16777215))
        self.previousButton.setToolTip(_fromUtf8(""))
        self.previousButton.setAccessibleName(_fromUtf8(""))
        self.previousButton.setAccessibleDescription(_fromUtf8(""))
        self.previousButton.setText(_fromUtf8("<"))
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.gridLayout.addWidget(self.previousButton, 1, 0, 1, 1)
        self.listCombo = QtGui.QComboBox(self.widget)
        self.listCombo.setToolTip(_fromUtf8(""))
        self.listCombo.setAccessibleName(_fromUtf8(""))
        self.listCombo.setAccessibleDescription(_fromUtf8(""))
        self.listCombo.setEditable(True)
        self.listCombo.setObjectName(_fromUtf8("listCombo"))
        self.gridLayout.addWidget(self.listCombo, 1, 1, 1, 1)
        self.nextButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMaximumSize(QtCore.QSize(21, 16777215))
        self.nextButton.setToolTip(_fromUtf8(""))
        self.nextButton.setAccessibleName(_fromUtf8(""))
        self.nextButton.setAccessibleDescription(_fromUtf8(""))
        self.nextButton.setText(_fromUtf8(">"))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.gridLayout.addWidget(self.nextButton, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.browseFrame)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.panCheck = QtGui.QCheckBox(self.widget_2)
        self.panCheck.setText(QtGui.QApplication.translate("itembrowser", "pan", None, QtGui.QApplication.UnicodeUTF8))
        self.panCheck.setChecked(True)
        self.panCheck.setObjectName(_fromUtf8("panCheck"))
        self.gridLayout_4.addWidget(self.panCheck, 0, 0, 1, 1)
        self.scaleCheck = QtGui.QCheckBox(self.widget_2)
        self.scaleCheck.setText(QtGui.QApplication.translate("itembrowser", "scale", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleCheck.setObjectName(_fromUtf8("scaleCheck"))
        self.gridLayout_4.addWidget(self.scaleCheck, 0, 1, 1, 1)
        self.editFormButton = QtGui.QToolButton(self.widget_2)
        self.editFormButton.setToolTip(_fromUtf8(""))
        self.editFormButton.setAccessibleDescription(_fromUtf8(""))
        self.editFormButton.setText(_fromUtf8("..."))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editFormButton.setIcon(icon)
        self.editFormButton.setObjectName(_fromUtf8("editFormButton"))
        self.gridLayout_4.addWidget(self.editFormButton, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.browseFrame, 0, 1, 1, 1)
        itembrowser.setWidget(self.dockWidgetContents)

        self.retranslateUi(itembrowser)
        QtCore.QMetaObject.connectSlotsByName(itembrowser)

    def retranslateUi(self, itembrowser):
        pass

