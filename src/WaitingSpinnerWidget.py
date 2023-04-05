import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Overlay(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)

        self.label = QLabel('0000', self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
    
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 180)))
        
        self.label.move(int(self.width()/2 -10), int(self.height()/2 -5))

        painter.setPen(QPen(Qt.NoPen))
        for i in range(14):
            if (self.counter / 5) % 14 == i:
                painter.setBrush(QBrush(QColor(127 + (self.counter % 5)*32, 0, 127)))
            else:
                painter.setBrush(QBrush(QColor(127, 127, 127)))

            painter.drawEllipse(
                int(self.width()/2 + 50 * math.cos(2 * math.pi * i / 14.0) - 5),
                int(self.height()/2 + 50 * math.sin(2 * math.pi * i / 14.0) -10),
                10, 10)
        painter.end()

    # 50 millisecond 간격으로 이벤트가 발생하는 타이머 설정
    def showEvent(self, event):
        self.timer = self.startTimer(50)
        self.counter = 1
    
    # 타이머 콜백
    def timerEvent(self, event):
        self.counter += 1
        clock = 0.05
        clock = self.counter*clock
        clock = '%0.2f' % clock
        self.update()
        self.label.setText(str(clock))

