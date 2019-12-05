import os

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QLabel

from form import Form, show_info
from interactor import Interactor
from main import DB_NAME, TABLE_NAME
from main_ui import Ui_MainWindow


def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_notif)
        self.pushButton.clicked.connect(self.show_notif)
        self.params = {
            "Пропущенные": "show_missed",
            "Предстоящие по времени": "show_by_time",
            "Предстоящие по приоритету": "show_by_prior"
        }
        self.comboBox.addItems(list(self.params.keys()))
        self.inter = Interactor(DB_NAME, TABLE_NAME)
        self.delete_missed_btn.clicked.connect(self.delete_missed)

    def add_notif(self):
        self.next = Form()
        self.next.show()

    def delete_missed(self):
        self.inter.delete_req(f"""DELETE FROM {TABLE_NAME} WHERE DATETIME(date_time) < DATETIME('now')""")
        show_info("Пропущенные напоминания удалены")

    def show_notif(self):
        func = self.params.get(self.comboBox.currentText())
        if func == "show_missed":
            self.show_missed()
        if func == "show_by_time":
            self.show_by_time()
        if func == "show_by_prior":
            self.show_by_prior()

    def clear_layout(self, layout):
        for i in range(layout.count()):
            layout_item = layout.itemAt(i)
            if layout_item and layout_item.__class__.__name__ == "QHBoxLayout":
                deleteItemsOfLayout(layout_item.layout())
                layout.removeItem(layout_item)
            elif not layout_item:
                self.clear_layout(layout.layout())

    def convert_to_layout(self, item):
        res = QHBoxLayout()
        lbl1 = QLabel()
        lbl1.setText(" ".join(
            ["Название: " + item[0], "   Приоритет: " + str(item[1]), "   Дата и время: " + item[2] + "   Картинка"]))
        res.addWidget(lbl1)
        lbl2 = QLabel()
        if item[3] != self.inter.alt_img:
            name = item[3]
            os.chdir("media")
            pixmap = QPixmap(name)
            pixmap = pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
            os.chdir("..")
            lbl2.setPixmap(pixmap)
            lbl2.resize(100, 100)
            res.addWidget(lbl2)
        else:
            lbl1.setText(lbl1.text() + " " + self.inter.alt_img)
        return res

    def add_notifs_to_layout(self, arr):
        self.clear_layout(self.notifications_layout)
        if len(list(arr)) == 0:
            show_info("Напоминаний не найдено")
        for i in arr:
            self.notifications_layout.addLayout(self.convert_to_layout(i))

    def show_missed(self):
        res = self.inter.get("""SELECT * FROM {} WHERE DATETIME(date_time) < DATETIME('now')""".format(TABLE_NAME))
        self.add_notifs_to_layout(res)

    def show_by_time(self):
        res = self.inter.get(
            """SELECT * FROM {} WHERE DATETIME(date_time) > DATETIME('now') ORDER BY date_time""".format(TABLE_NAME))
        self.add_notifs_to_layout(res)

    def show_by_prior(self):
        res = self.inter.get(
            """SELECT * FROM {} WHERE DATETIME(date_time) > DATETIME('now') ORDER BY prior""".format(TABLE_NAME))
        self.add_notifs_to_layout(res)
