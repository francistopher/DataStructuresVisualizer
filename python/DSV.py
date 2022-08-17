import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QFont
from IntroText import IntroText

class DSV(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: black;")
        self.introText = IntroText("Designed By Christopher Francisco", self)

        self.showFullScreen()
        self.__width = self.frameGeometry().width()
        self.__height = self.frameGeometry().height()
        
        self.__configureIntroText()

    def __configureIntroText(self):
        self.introText.setTextColor("white")
        self.introText.setBackgroundColor("red")
        self.introText.reSize(self.__getWidth(0.5), self.__getHeight(0.1))
        self.introText.reLocate(self.__getWidth(0.25), self.__getHeight((1.0 - 0.1) * 0.5))
        self.introText.setFontSize(self.__getHeight((1.0 - 0.1) * 0.05))

    def __getWidth(self, factor):
        return factor * self.__width

    def __getHeight(self, factor):
        return factor * self.__height

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    dsv = DSV()
    sys.exit(app.exec())
