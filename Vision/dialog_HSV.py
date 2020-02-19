# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_HSV.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_HSV(object):
    def setupUi(self, Dialog_HSV):
        Dialog_HSV.setObjectName("Dialog_HSV")
        Dialog_HSV.resize(637, 418)
        self.layoutWidget = QtWidgets.QWidget(Dialog_HSV)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 79, 484, 200))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_2)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalSlider_H = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_H.setMaximum(255)
        self.horizontalSlider_H.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_H.setObjectName("horizontalSlider_H")
        self.verticalLayout_2.addWidget(self.horizontalSlider_H)
        self.label_H = QtWidgets.QLabel(self.frame_2)
        self.label_H.setObjectName("label_H")
        self.verticalLayout_2.addWidget(self.label_H)
        self.horizontalSlider_S = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_S.setMaximum(255)
        self.horizontalSlider_S.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_S.setObjectName("horizontalSlider_S")
        self.verticalLayout_2.addWidget(self.horizontalSlider_S)
        self.label_S = QtWidgets.QLabel(self.frame_2)
        self.label_S.setObjectName("label_S")
        self.verticalLayout_2.addWidget(self.label_S)
        self.horizontalSlider_V = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider_V.setMaximum(255)
        self.horizontalSlider_V.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_V.setObjectName("horizontalSlider_V")
        self.verticalLayout_2.addWidget(self.horizontalSlider_V)
        self.label_V = QtWidgets.QLabel(self.frame_2)
        self.label_V.setObjectName("label_V")
        self.verticalLayout_2.addWidget(self.label_V)
        self.horizontalLayout.addWidget(self.frame_2)
        self.widget = QtWidgets.QWidget(Dialog_HSV)
        self.widget.setGeometry(QtCore.QRect(400, 330, 195, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.Button_reset = QtWidgets.QPushButton(self.widget)
        self.Button_reset.setObjectName("Button_reset")
        self.horizontalLayout_2.addWidget(self.Button_reset)

        self.retranslateUi(Dialog_HSV)
        self.buttonBox.accepted.connect(Dialog_HSV.accept)
        self.buttonBox.rejected.connect(Dialog_HSV.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_HSV)

    def retranslateUi(self, Dialog_HSV):
        _translate = QtCore.QCoreApplication.translate
        Dialog_HSV.setWindowTitle(_translate("Dialog_HSV", "Dialog"))
        self.label_title.setText(_translate("Dialog_HSV", "HSV Color Values"))
        self.label_H.setText(_translate("Dialog_HSV", "H"))
        self.label_S.setText(_translate("Dialog_HSV", "S"))
        self.label_V.setText(_translate("Dialog_HSV", "V"))
        self.Button_reset.setText(_translate("Dialog_HSV", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_HSV = QtWidgets.QDialog()
    ui = Ui_Dialog_HSV()
    ui.setupUi(Dialog_HSV)
    Dialog_HSV.show()
    sys.exit(app.exec_())
