# -*- coding: utf-8 -*-

"""
Created on 2020/6/19 21:27
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CCircularLabel(QLabel):
    style = '''


    '''
    clicked = pyqtSignal()  # Label点击信号

    def __init__(self, parent=None, width=30, borderW=0):
        super(CCircularLabel, self).__init__(parent)
        self.width = width
        self.borderW = borderW
        self.setFixedSize(width, width)
        self.setObjectName('lb_circularImage')
        # self.setScaledContents(True)
        # 这个变量的作用是可以随时改变图片，如果不用变量，
        # paintEvent重写后CCircularLabel就无法使用setPixmap
        # 因为setPixmap最重也是调用paintEven实现的，
        # 如果paintEvent中drawPixmap固定为特定图片的化，setPixmap就失效
        self.pixmap = QPixmap(":/pic/Resource/userimage.jpg")
        self.mask = MaskWeight(self, self.rect())

        self.qss = '''
#lb_circularImage{
    border:2px solid #228fff;
    border-radius:'''+str(int(width/2))+'''px;
}
        '''

        self.setStyleSheet(self.qss)

    def paintEvent(self, a0: QPaintEvent):
        '''
        重写了paintEvent,setPixmap失效，因为setPixmap实质上也是调用paintEvent
        而paintEvent要绘制的图片始终是self.pixmap，所以要更换图片只需要改变self.pixmap的值
        然后update()即可,即调用下面写的changePixmap即可
        :param a0:
        :return:
        '''
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHints(QPainter.Antialiasing, True)  # 抗锯齿

        qpath = QPainterPath()
        qpath.addEllipse(self.borderW, self.borderW, self.width - 2*self.borderW, self.width - 2*self.borderW)  # 从(0,0)开始画椭圆，宽高都是width-4，-4的目的就是为了好用qss设置2像素边框
        qp.setClipPath(qpath)

        # 设置label默认图像
        qp.drawPixmap(QRect(self.borderW, self.borderW, self.width - 2*self.borderW, self.width - 2*self.borderW), self.pixmap)
        qp.end()
        # QWidget.paintEvent(self, a0)

    def setPixmap(self, pixmap):
        '''setPixMap失效，所以只能调用这个函数'''
        self.pixmap = pixmap
        self.update()

    def mousePressEvent(self, ev: QMouseEvent):
        if ev.button() == Qt.LeftButton:
            self.clicked.emit()

    def enterEvent(self, a0: QEvent):
        self.showMask()

    def leaveEvent(self, a0: QEvent):
        self.closeMask()

    def showMask(self):
        self.mask.show()

    def closeMask(self):
        self.mask.close()


class MaskWeight(QWidget):

    def __init__(self, parent=None, rect=None):
        super().__init__(parent)
        self.setObjectName('mask')
        self.maskRect = rect
        # self.maskRect=QRect(0,0,1,1)
        self.setFixedSize(0, 0)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_StyledBackground)
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        # self.setWindowOpacity(0.5)  # 设置窗口透明度
        qss = '''
#mask{
    background:rgba(0,0,0,80);
    border-radius:'''+str(int(rect.width()/2))+'''px;
}
        '''
        self.setStyleSheet(qss)

    def show(self):
        """重写show，设置遮罩大小与parent一致
        """
        if self.parent() is None:
            return

        if self.maskRect is not None:
            self.setFixedSize(self.maskRect.width(),self.maskRect.height())
            self.setGeometry(self.maskRect.left(), self.maskRect.top(), self.maskRect.width(),self.maskRect.height())
            # print(self.maskRect.left(), self.maskRect.right(), self.maskRect.width(),self.maskRect.height())
        else:
            parent_rect = self.parent().geometry()
            self.setFixedSize(parent_rect.width(), parent_rect.height())
            self.setGeometry(0, 0, parent_rect.width(), parent_rect.height())
            # print(parent_rect.width(), parent_rect.height())

        super().show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = CCircularLabel()
    w.show()
    sys.exit(app.exec_())
