# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

captext = None


class Ui_Dialog(object):
    def val(self):
        return captext
    def setupUi(self, Dialog, path):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 153)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 351, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Records/img/Neo.png"))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Goudy Stout")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 100, 121, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(path))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 30, 161, 16))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Records/img/line.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 100, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Records/img/nlogo.png"))
        self.label_5.setObjectName("label_5")

        def send():
            global captext
            txt = self.lineEdit.text()
            print(txt)
            if len(txt)>3:
                captext = txt
                Dialog.close()
        
        
        self.pushButton.clicked.connect(send)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Capta"))
        self.label.setText(_translate("Dialog", "Enter the text in Capta "))
        self.pushButton.setText(_translate("Dialog", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
