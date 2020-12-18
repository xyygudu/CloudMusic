# -*- coding: utf-8 -*-

"""
Created on 2020/5/5 15:41
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CircularButton(QPushButton):
    style = '''
#CircularButton{
    background-color:red;
}
        '''

    def __init__(self, parent=None, radius=30, iconPath='../Resource/userimage.jpg'):
        super(CircularButton, self).__init__(parent)
        self.radius = radius
        self.iconPath = iconPath
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.icon = QIcon(iconPath)
        self.setIcon(self.icon)
        self.setFixedSize(2*radius, 2*radius)
        self.setObjectName('CircularButton')
        self.setStyleSheet(self.style)

    def paintEvent(self, a0: QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHints(QPainter.Antialiasing, True)  # 抗锯齿
        rect = self.rect()
        qp.drawPixmap(QRect(1, 1, self.width()-2, self.height()-2), QPixmap(self.iconPath))
        qp.drawRoundedRect(rect, self.radius, self.radius)
        qp.end()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = CircularButton()
    w.show()
    sys.exit(app.exec_())