# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
use = None
pas = None

class Ui_Dialog(object):
    def val(self):
        return(use,pas)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 209)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 351, 221))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("D:/My Workspace/Automation/Neobux_gitrepo/Records/img/Neo.png"))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 141, 31))
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
        self.label_4.setPixmap(QtGui.QPixmap("D:/My Workspace/Automation/Neobux_gitrepo/Records/img/line.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 160, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("D:/My Workspace/Automation/Neobux_gitrepo/Records/img/nlogo.png"))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(110, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 110, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")

        def send():
            global use
            global pas
            user = self.lineEdit.text()
            passw = self.lineEdit_2.text()
            print(user)
            print(passw)
            if (len(user)>2 and len(passw)>5):
                use = user
                pas = passw
                Dialog.close()
        
        
        self.pushButton.clicked.connect(send)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Fill in your Details"))
        self.pushButton.setText(_translate("Dialog", "Continue"))
        self.label_2.setText(_translate("Dialog", "Username :"))
        self.label_6.setText(_translate("Dialog", "Password :"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Id"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "**********"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
    print(use,pas)
