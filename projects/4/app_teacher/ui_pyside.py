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

        self.layout5 = QGridLayout()
        self.layout5 = QtWidgets.QGridLayout(self)
        self.layout5.addWidget(QLabel("path"), 0, 1)
        self.layout5.addWidget(QLabel("params"), 0, 2)
        self.layout5.addWidget(QLabel("result"), 0, 3)
        self.layout5.addWidget(QLineEdit(""), 1, 1)
        self.layout5.addWidget(QLineEdit(""), 1, 2)
        self.layout5.addWidget(QLineEdit(""), 1, 3)
        self.layout5.addWidget(QPushButton("request"), 2, 2)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        # self.setCentralWidget(widget)

    @QtCore.Slot()
    def magic(self):
        # self.text.setText(random.choice(self.hello))
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(1280, 720)
    widget.show()
    sys.exit(app.exec())
