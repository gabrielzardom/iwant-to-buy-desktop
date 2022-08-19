from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QGraphicsScene
from ui_login import Ui_LoginWindow
from arm_mongo import *
from user import *
from cliente import MainWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.database = arm_database()
        self.userload = obj_users()
        self.client_w = None

        self.ui.btnlogin.clicked.connect(self.tryToLogin)

    def tryToLogin(self):
        if self.userload.login(self.database.get_user(self.ui.txtemail.text()), str.encode(self.ui.txtpassword.text())):
            self.client_w = MainWindow(self.userload.get_str_userID())
            self.client_w.show()
            self.hide()
