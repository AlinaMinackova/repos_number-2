import random
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QBrush, QPen,QPainter, QPolygon
from PyQt5.QtCore import QPoint, Qt


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.flag = False
        self.pushButton.clicked.connect(self.run)
        self.setWindowTitle('круги')

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.begin(self)
            self.drawEllipse(painter)
            painter.end()

    def drawEllipse(self, painter):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        size = random.randint(50, 100)
        col = QColor()
        painter.setPen(col)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(x, y, size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())