import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QGridLayout, QLineEdit, QLabel, QCheckBox, QSlider)
from PyQt5.QtGui import QFont
import cv2

# Прочитать изображение в оперативную память (место где лежит)
# Показываем статистику по изображению
# Получить от пользователя данные для изменения изображения
# Изменяем изображение в памяти
# Сохраняем (перезаписываем данные в памяти)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        grid = QGridLayout()

        label_path = QLabel("укажите путь к изображению")
        self.line_edit_path = QLineEdit("temp/image.jpg")
        is_file_have = QCheckBox("наличие файла")
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

        grid.addWidget(label_path, 0, 0)

        grid.addWidget(self.line_edit_path, 1, 0)
        grid.addWidget(is_file_have, 1, 1)
        grid.addWidget(btn_check, 1, 2)

        grid.addWidget(label_width, 3, 0)
        grid.addWidget(label_height, 3, 1)

        grid.addWidget(self.line_edit_width, 4, 0)
        grid.addWidget(self.line_edit_height, 4, 1)
        grid.addWidget(self.slider_quality, 4, 2)

        self.setLayout(grid)

        # QToolTip.setFont(QFont('SansSerif', 10))
        #
        # self.setToolTip('This is a <b>QWidget</b> widget')
        #
        # btn = QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())
        # btn.move(50, 50)
        # btn.clicked.connect(self.print_hi)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Фотошоп 0.1')
        self.show()

    def read_image(self):
        print()
        path = self.line_edit_path.text()
        # img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img = cv2.imread(path, cv2.IMREAD_COLOR)

        h, w, c = img.shape
        print('width:  ', w)
        print('height: ', h)
        print('channel:', c)

        self.line_edit_width.setText(str(w))
        self.line_edit_height.setText(str(h))

        new_width = int(self.line_edit_width.text())
        new_height = int(self.line_edit_height.text())
        quality = int(self.slider_quality.value())
        print('quality:', quality)

        resized = cv2.resize(img, (new_width//2, new_height//2), interpolation=cv2.INTER_AREA)

        cv2.imshow('image', img)
        cv2.imshow('resized', resized)

        cv2.waitKey(1)
        cv2.imwrite('temp/image_gray.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, quality])

        print("hi!")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
