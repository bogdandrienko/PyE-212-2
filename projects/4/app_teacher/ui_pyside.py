import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget, QGridLayout,
)
import aiohttp
import asyncio
import json


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Analyse")

        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        # self.button = QtWidgets.QPushButton("File")
        # self.text = QtWidgets.QLabel("Hello World")
        # self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
        #
        # self.button.clicked.connect(self.magic)

        # self.layout1 = QVBoxLayout()
        # self.layout1 = QtWidgets.QVBoxLayout(self)
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]
        #
        # for w in widgets:
        #     self.layout1.addWidget(w())
        # self.layout3 = QtWidgets.QVBoxLayout(self)

        # self.layout1 = QVBoxLayout()
        # self.layout1 = QtWidgets.QVBoxLayout(self)
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDial,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]
        #
        # for w in widgets:
        #     self.layout1.addWidget(w())

        # мы создаём сетку для отображения всех виджетов
        self.layout5 = QGridLayout()
        self.layout5 = QtWidgets.QGridLayout(self)

        # создаём кнопку
        self.button = QPushButton("request")
        self.layout5.addWidget(self.button, 2, 2)
        # присоединяем к кнопке
        self.button.clicked.connect(self.request)

        # наименование api-пути
        self.layout5.addWidget(QLabel("path"), 0, 1)

        # значение api-пути
        self.path_edit = QLineEdit("http://192.168.1.121/api/result/")
        self.layout5.addWidget(self.path_edit, 1, 1)

        self.layout5.addWidget(QLabel("params"), 0, 2)

        self.params_edit = QLineEdit("")
        self.layout5.addWidget(self.params_edit, 1, 2)

        self.result_label = QLabel("result")
        self.layout5.addWidget(self.result_label, 3, 1)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        # self.setCentralWidget(widget)

    @QtCore.Slot()
    def request(self):
        path = self.path_edit.text()
        params = {"value": self.params_edit.text()}

        async def main():
            async with aiohttp.ClientSession() as session:

                if len(params["value"]) > 0:
                    async with session.post(path, data=params) as response:
                        html = await response.text()
                else:
                    async with session.get(path) as response:
                        # print("Status:", response.status)
                        # print("Content-type:", response.headers['content-type'])

                        # html = await response.text()
                        html = await response.text()
                        print(type(html))
                        html = json.loads(html)
                        print(type(html))
                        print("Body:", html)


                        # if type(html["recepts"]) == type(""):
                        #     self.result_label.setText(html["recepts"])
                        # elif type(html["recepts"]) == type([]):
                        #     for i in html["recepts"]:
                        #         str1 += f'{i}\n'
                        #     self.result_label.setText(str1)
                        # else:
                        #     self.result_label.setText("ошибка")
                        if isinstance(html["recepts"], str):
                            # печатает текст отсутствия рецепта
                            self.result_label.setText(html["recepts"])
                        elif isinstance(html["recepts"], list):
                            str1 = ''
                            for i in html["recepts"]:
                                str1 += f'{i}\n'
                            self.result_label.setText(str1)
                        else:
                            self.result_label.setText("ошибка")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(1280, 720)
    widget.show()
    sys.exit(app.exec())
