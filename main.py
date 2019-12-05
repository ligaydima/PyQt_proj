import sys

from PyQt5.QtWidgets import QApplication

DB_NAME = "notifications.db"
TABLE_NAME = "notifications"

if __name__ == '__main__':
    from main_class import Main

    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())
