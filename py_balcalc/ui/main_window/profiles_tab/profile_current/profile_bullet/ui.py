# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import qtawesome as qta
from PySide6 import QtCore, QtGui, QtWidgets


class Ui_bullet(object):
    def setupUi(self, bullet):
        bullet.setObjectName("bullet")
        bullet.resize(500, 188)
        self.gridLayout = QtWidgets.QGridLayout(bullet)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.bulletGroupBox = QtWidgets.QGroupBox(bullet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulletGroupBox.sizePolicy().hasHeightForWidth())
        self.bulletGroupBox.setSizePolicy(sizePolicy)
        self.bulletGroupBox.setMinimumSize(QtCore.QSize(500, 188))
        self.bulletGroupBox.setStyleSheet("")
        self.bulletGroupBox.setCheckable(True)
        self.bulletGroupBox.setObjectName("bulletGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.bulletGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.weight = QtWidgets.QDoubleSpinBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weight.sizePolicy().hasHeightForWidth())
        self.weight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.weight.setFont(font)
        self.weight.setDecimals(2)
        self.weight.setMaximum(1000.0)
        self.weight.setSingleStep(0.01)
        self.weight.setProperty("value", 69.0)
        self.weight.setObjectName("weight")
        self.gridLayout_4.addWidget(self.weight, 1, 1, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setObjectName("label_77")
        self.gridLayout_4.addWidget(self.label_77, 4, 0, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setObjectName("label_74")
        self.gridLayout_4.addWidget(self.label_74, 1, 0, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setObjectName("label_73")
        self.gridLayout_4.addWidget(self.label_73, 0, 0, 1, 1)
        self.bulletName = QtWidgets.QLineEdit(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulletName.sizePolicy().hasHeightForWidth())
        self.bulletName.setSizePolicy(sizePolicy)
        self.bulletName.setStyleSheet("")
        self.bulletName.setText("")
        self.bulletName.setMaxLength(20)
        self.bulletName.setFrame(True)
        self.bulletName.setObjectName("bulletName")
        self.gridLayout_4.addWidget(self.bulletName, 0, 1, 1, 3)
        self.dragType = QtWidgets.QComboBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragType.sizePolicy().hasHeightForWidth())
        self.dragType.setSizePolicy(sizePolicy)
        self.dragType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dragType.setStyleSheet("")
        self.dragType.setObjectName("dragType")
        self.gridLayout_4.addWidget(self.dragType, 4, 1, 1, 3)
        self.label_78 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy)
        self.label_78.setObjectName("label_78")
        self.gridLayout_4.addWidget(self.label_78, 5, 0, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setObjectName("label_75")
        self.gridLayout_4.addWidget(self.label_75, 2, 0, 1, 1)
        self.dragEditor = QtWidgets.QPushButton(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragEditor.sizePolicy().hasHeightForWidth())
        self.dragEditor.setSizePolicy(sizePolicy)
        self.dragEditor.setIcon(qta.icon('mdi6.tune', color='white', color_disabled='grey'))
        self.dragEditor.setObjectName("dragEditor")
        self.gridLayout_4.addWidget(self.dragEditor, 5, 4, 1, 1)
        self.diameter = QtWidgets.QDoubleSpinBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diameter.sizePolicy().hasHeightForWidth())
        self.diameter.setSizePolicy(sizePolicy)
        self.diameter.setDecimals(3)
        self.diameter.setSingleStep(0.001)
        self.diameter.setProperty("value", 0.224)
        self.diameter.setObjectName("diameter")
        self.gridLayout_4.addWidget(self.diameter, 2, 3, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setObjectName("label_76")
        self.gridLayout_4.addWidget(self.label_76, 2, 2, 1, 1)
        self.length = QtWidgets.QDoubleSpinBox(self.bulletGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setDecimals(2)
        self.length.setSingleStep(0.01)
        self.length.setProperty("value", 0.9)
        self.length.setObjectName("length")
        self.gridLayout_4.addWidget(self.length, 2, 1, 1, 1)
        self.dragFuncData = QtWidgets.QLineEdit(self.bulletGroupBox)
        self.dragFuncData.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dragFuncData.sizePolicy().hasHeightForWidth())
        self.dragFuncData.setSizePolicy(sizePolicy)
        self.dragFuncData.setObjectName("dragFuncData")
        self.gridLayout_4.addWidget(self.dragFuncData, 5, 1, 1, 3)
        self.widget = QtWidgets.QWidget(self.bulletGroupBox)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dfDataEditor = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dfDataEditor.sizePolicy().hasHeightForWidth())
        self.dfDataEditor.setSizePolicy(sizePolicy)
        self.dfDataEditor.setText("")
        self.dfDataEditor.setIcon(qta.icon('mdi6.pencil', color='white', color_disabled='grey'))
        self.dfDataEditor.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.dfDataEditor.setObjectName("dfDataEditor")
        self.gridLayout_2.addWidget(self.dfDataEditor, 0, 2, 1, 1)
        self.addDrag = QtWidgets.QToolButton(self.widget)
        self.addDrag.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDrag.sizePolicy().hasHeightForWidth())
        self.addDrag.setSizePolicy(sizePolicy)
        self.addDrag.setMinimumSize(QtCore.QSize(0, 0))
        self.addDrag.setText("")
        self.addDrag.setIcon(qta.icon('mdi6.plus', color='white', color_disabled='grey'))
        self.addDrag.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.addDrag.setObjectName("addDrag")
        self.gridLayout_2.addWidget(self.addDrag, 0, 0, 1, 1)
        self.removeDrag = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeDrag.sizePolicy().hasHeightForWidth())
        self.removeDrag.setSizePolicy(sizePolicy)
        self.removeDrag.setMinimumSize(QtCore.QSize(0, 0))
        self.removeDrag.setText("")
        self.removeDrag.setIcon(qta.icon('mdi6.minus', color='white', color_disabled='grey'))
        self.removeDrag.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.removeDrag.setObjectName("removeDrag")
        self.gridLayout_2.addWidget(self.removeDrag, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 4, 4, 1, 1)
        self.gridLayout.addWidget(self.bulletGroupBox, 0, 0, 1, 1)

        self.retranslateUi(bullet)
        self.dragType.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(bullet)

    def retranslateUi(self, bullet):
        _translate = QtCore.QCoreApplication.translate
        bullet.setWindowTitle(_translate("bullet", "Form"))
        self.bulletGroupBox.setTitle(_translate("bullet", "Bullet"))
        self.label_77.setText(_translate("bullet", "Drag function:"))
        self.label_74.setText(_translate("bullet", "Weight:"))
        self.label_73.setText(_translate("bullet", "Name:"))
        self.label_78.setText(_translate("bullet", "DF info:"))
        self.label_75.setText(_translate("bullet", "Length:"))
        self.dragEditor.setToolTip(_translate("bullet", "Edit drag function"))
        self.dragEditor.setText(_translate("bullet", "Calculator"))
        self.label_76.setText(_translate("bullet", "Diameter:"))
        self.dfDataEditor.setToolTip(_translate("bullet", "Edit selected"))
        self.addDrag.setToolTip(_translate("bullet", "Add new"))
        self.removeDrag.setToolTip(_translate("bullet", "Remove selected"))
