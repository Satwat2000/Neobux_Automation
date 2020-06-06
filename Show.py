# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'last.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, file_name):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 256)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/My Workspace/Automation/Neobux_gitrepo/Records/img/back1.png"))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 331, 181))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 220, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Goudy Stout")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        text = open(file_name).read()
        self.textEdit.setReadOnly(True)
        self.textEdit.setText(text)

        def Yclicked():
            Dialog.close()
        self.pushButton.clicked.connect(Yclicked)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Close Automation"))
        self.label_2.setText(_translate("Dialog", "Work Report "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    path = r"D:\My Workspace\Automation\Neobux Auto\Records\2020-06-03"
    ui.setupUi(Dialog, path)
    Dialog.show()
    sys.exit(app.exec_())
