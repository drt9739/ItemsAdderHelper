import sys

import PyQt6
import requests

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QLabel, QWidget
from Scripts.sevenTv import SevenTvApi


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test app')
        self.setFixedSize(QSize(400, 300))
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.label = QLabel()
        self.layout = QVBoxLayout(self.central_widget)
        self.label.setFixedSize(QSize(300, 200))
        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        api = SevenTvApi()
        emote = api.get_emote('https://7tv.app/emotes/62c7468b004dd4ed9b4c16e2')

        image = QPixmap()
        image.loadFromData(emote.get_image())
        self.label.setPixmap(image)


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
