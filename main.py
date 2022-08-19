import sys
from PySide2.QtWidgets import QApplication
from login import LoginWindow
from cliente import MainWindow

from arm_mongo import *
from user import *

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = LoginWindow()
    w.show()

    sys.exit(app.exec_())
