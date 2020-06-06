import ip, capip, Show, error
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
class fetch():
    def info(self):
        app = QApplication([])
        Dialog = QDialog()  #-->Make object of Form class
        self.infoui = ip.Ui_Dialog()    #-->Make the form class
        self.infoui.setupUi(Dialog)
        Dialog.show()
        app.exec_()  # --->Mode Dialog
        return(self.infoui.val())

    def capta(self,path):
        app = QApplication([])
        Dialog = QDialog()  #-->Make object of Form class
        self.cap = capip.Ui_Dialog()    #-->Make the form class
        self.cap.setupUi(Dialog, path)
        Dialog.show()
        app.exec_()  # --->Mode Dialog
        return(self.cap.val())
    
    def closeit(self,file_path):
        app = QApplication([])
        Dialog = QDialog()  #-->Make object of Form class
        self.end = Show.Ui_Dialog()    #-->Make the form class
        self.end.setupUi(Dialog,file_path)
        Dialog.show()
        app.exec_()  # --->Mode Dialog

class chromeErr():
    def __init__(self):
        app = QApplication([])
        Dialog = QDialog()
        self.noui = error.Ui_Dialog()
        self.noui.setupUi(Dialog)
        Dialog.show()
        app.exec_()
