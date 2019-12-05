from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from form_ui import Ui_Form
from interactor import Interactor
from main import DB_NAME, TABLE_NAME


def show_info(s):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(s)
    msg.setWindowTitle("Info")
    msg.exec_()


class Form(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.img_name = ""
        self.choose_img_btn.clicked.connect(self.choose_img)
        self.enter_time.setCalendarPopup(True)
        self.enter_time.setDisplayFormat("yyyy-MM-dd hh:mm")
        self.inter = Interactor(DB_NAME, TABLE_NAME)

    def choose_img(self):
        self.img_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', "Картинка(*.png)")[0]

    def accept(self):
        title = self.enter_title.text()
        prior = int(self.enter_prior.text())
        datetime = self.enter_time.text()
        if self.inter.exists(title, prior, datetime, self.img_name):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("This notification already exists")
            msg.setWindowTitle("Info")
            msg.exec_()
            return
        self.inter.insert(title, prior, datetime, self.img_name)
        show_info("Напоминание создано успешно")
        self.close()

    def reject(self):
        self.close()
