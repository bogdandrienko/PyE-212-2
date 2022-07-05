import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QGridLayout, QLineEdit, QLabel, QCheckBox, QSlider)
import cv2


# Прочитать изображение в оперативную память (место где лежит)
# Показываем статистику по изображению
# Получить от пользователя данные для изменения изображения
# Изменяем изображение в памяти
# Сохраняем (перезаписываем данные в памяти)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()

        label_path = QLabel("укажите путь к изображению")
        self.line_edit_path = QLineEdit("temp/image.jpg")
        self.is_file_have = QCheckBox("наличие файла")
        btn_check = QPushButton("check")
        btn_check.clicked.connect(self.read_image)

        label_width = QLabel("ширина")
        self.line_edit_width = QLineEdit("0")
        label_height = QLabel("высота")
        self.line_edit_height = QLineEdit("0")

        self.slider_quality = QSlider()
        self.slider_quality.setMinimum(1)
        self.slider_quality.setMaximum(100)
        self.slider_quality.setValue(95)

        self.grid.addWidget(label_path, 0, 0)

        self.grid.addWidget(self.line_edit_path, 1, 0)
        self.grid.addWidget(self.is_file_have, 1, 1)
        self.grid.addWidget(btn_check, 1, 2)

        self.grid.addWidget(label_width, 3, 0)
        self.grid.addWidget(label_height, 3, 1)

        self.grid.addWidget(self.line_edit_width, 4, 0)
        self.grid.addWidget(self.line_edit_height, 4, 1)
        self.grid.addWidget(self.slider_quality, 4, 2)

        btn_start = QPushButton("start")
        self.grid.addWidget(btn_start, 5, 0)
        btn_start.clicked.connect(self.computing_image)

        self.setLayout(self.grid)

        self.img = None

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Фотошоп 0.1')
        self.show()

    def read_image(self):
        try:
            path = self.line_edit_path.text()
            self.img = cv2.imread(path, cv2.IMREAD_COLOR)  # cv2.IMREAD_GRAYSCALE
            h, w, c = self.img.shape
            self.line_edit_width.setText(str(w))
            self.line_edit_height.setText(str(h))
            self.is_file_have.setChecked(True)
        except Exception as error:
            print(error)
            self.is_file_have.setChecked(False)

    def computing_image(self):

        new_width = int(self.line_edit_width.text())
        new_height = int(self.line_edit_height.text())
        quality = int(self.slider_quality.value())

        img = self.img
        resized = cv2.resize(img, (new_width // 2, new_height // 2), interpolation=cv2.INTER_AREA)
        image_gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        cv2.imshow('image', img)
        cv2.imshow('resized', resized)
        cv2.imshow('image_gray', image_gray)
        cv2.waitKey(1)
        cv2.imwrite('temp/image_gray.jpg', image_gray, [cv2.IMWRITE_JPEG_QUALITY, quality])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
