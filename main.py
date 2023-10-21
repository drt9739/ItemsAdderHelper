import sys

import PyQt6
import requests

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from Scripts.sevenTv import SevenTvApi


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test app')
        self.setFixedSize(QSize(400, 300))
        self.label = QLabel()
        self.label.setFixedSize(QSize(300, 200))

        api = SevenTvApi()
        emote = api.get_emote('https://7tv.app/emotes/60b0c36388e8246a4b120d7e')
        image = QImage()

        image.loadFromData(emote.get_image())
        pixmap = QPixmap(QPixmap(image))
        self.label.setPixmap(pixmap)


def main():
    """
    Тут будет код запускающий программу
    :return:
    """
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    app.exec()
