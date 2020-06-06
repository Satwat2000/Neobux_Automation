# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from os import path 
from win32com.client import Dispatch

class support():
    def chrome_version(self):
        paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
        version = list(filter(None, [self.get_version_via_com(p) for p in paths]))[0]
        version = version.split('.')
        return(str(version[0]))

    def get_version_via_com(self,filename):
        parser = Dispatch("Scripting.FileSystemObject")
        try:
            version = parser.GetFileVersion(filename)
        except Exception:
            print("Chrome.exe not found")
            return None
        return version


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 207)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 401, 231))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Records/img/bg.png"))
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(260, 170, 81, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        
        self.url = QtWidgets.QLabel(Dialog)
        self.url.setGeometry(QtCore.QRect(160, 62, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.url.setFont(font)
        self.url.setTextFormat(QtCore.Qt.AutoText)
        self.url.setObjectName("url")
        self.path = QtWidgets.QLabel(Dialog)
        self.path.setGeometry(QtCore.QRect(10, 130, 411, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.path.setFont(font)
        self.path.setAlignment(QtCore.Qt.AlignCenter)
        self.path.setWordWrap(False)
        self.path.setIndent(-10)
        self.path.setObjectName("path")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 24, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 54, 55, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(270, 54, 118, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.buttonBox.clicked.connect(lambda:Dialog.close())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        urlLink="<a href=\"https://sites.google.com/a/chromium.org/chromedriver/downloads\">Download Driver</a>"
        self.url.setText(_translate("Dialog", urlLink))
        self.url.setOpenExternalLinks(True)
        self.path.setText(_translate("Dialog", path.dirname(path.abspath(__file__))))
        print(path.dirname(path.abspath(__file__)))
        self.label_2.setText(_translate("Dialog", "Your Chrome Version"))
        find = support()
        self.label_3.setText(_translate("Dialog", find.chrome_version()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
