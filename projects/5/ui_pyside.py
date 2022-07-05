import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import (
    QCheckBox,
    QLabel,
    QLineEdit,
    QPushButton,
)
import json
import requests
import aiohttp
import asyncio
import threading
import multiprocessing


class MyUserInterfaceClass(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        self.label_path = QLabel("path")
        self.layout.addWidget(self.label_path, 0, 0)
        self.line_edit_path = QLineEdit("http://127.0.0.1:8000/api/create_user/")
        self.layout.addWidget(self.line_edit_path, 0, 1)

        self.label_username = QLabel("username")
        self.layout.addWidget(self.label_username, 1, 0)
        self.line_edit_username = QLineEdit("username")
        self.layout.addWidget(self.line_edit_username, 1, 1)

        self.label_password1 = QLabel("password1")
        self.layout.addWidget(self.label_password1, 2, 0)
        self.line_edit_password1 = QLineEdit("password1")
        self.layout.addWidget(self.line_edit_password1, 2, 1)

        self.label_password2 = QLabel("password2")
        self.layout.addWidget(self.label_password2, 3, 0)
        self.line_edit_password2 = QLineEdit("password2")
        self.layout.addWidget(self.line_edit_password2, 3, 1)

        self.check_box_is_equal = QCheckBox("")
        self.layout.addWidget(self.check_box_is_equal, 2, 2)
        self.label_is_equal = QLabel("")
        self.layout.addWidget(self.label_is_equal, 3, 2)

        self.result_label = QLabel("result")
        self.layout.addWidget(self.result_label, 4, 0)
        self.button = QPushButton("request")
        self.layout.addWidget(self.button, 4, 1)
        # self.button.clicked.connect(self.sync_request)
        self.button.clicked.connect(self.async_request)

        self.setWindowTitle("Create user in Django")
        self.resize(640, 480)
        self.show()

    @QtCore.Slot()
    def sync_request(self):
        url = self.line_edit_path.text()
        username = self.line_edit_username.text()
        password1 = self.line_edit_password1.text()
        password2 = self.line_edit_password2.text()
        if password1 != password2:
            self.check_box_is_equal.setChecked(False)
            self.label_is_equal.setText("пароли не совпадают!")
        else:
            self.check_box_is_equal.setChecked(True)
            self.label_is_equal.setText("")
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/51.0.2704.103 Safari/537.36"}
            response = requests.post(
                url=url,
                data={"username": username, "password": password1},
                headers=headers
            )
            json_data = json.loads(response.content)
            self.result_label.setText(json_data["result"])

    @QtCore.Slot()
    def async_request(self):
        url = self.line_edit_path.text()
        username = self.line_edit_username.text()
        password1 = self.line_edit_password1.text()
        password2 = self.line_edit_password2.text()
        if password1 != password2:
            self.check_box_is_equal.setChecked(False)
            self.label_is_equal.setText("пароли не совпадают!")
        else:
            self.check_box_is_equal.setChecked(True)
            self.label_is_equal.setText("")
            headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/51.0.2704.103 Safari/537.36"}

            async def async_function():
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                            url=url, data={"username": username, "password": password1}, headers=headers
                    ) as response:
                        json_data = await response.json()
                        self.result_label.setText(json_data["result"])

            asyncio.get_event_loop().run_until_complete(async_function())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    ui = MyUserInterfaceClass()
    sys.exit(app.exec())
