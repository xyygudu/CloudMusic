# -*- coding: utf-8 -*-

"""
Created on 2020/5/11 10:09
@author: Acer
@email: 2992493013@qq.com
@description: 网易云轮播图
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CommanHelper.LinkLIst import *


class Indicator(QWidget):
    '''轮播图下面的索引'''
    entered = pyqtSignal()
    def __init__(self, parent=None):
        super(Indicator, self).__init__(parent)
        self.selected = False
        self.frontColor = QColor(220, 0, 0)
        self.backColor = QColor(200, 200, 200)
        self.setFixedSize(20, 4)

    def select(self, isSelected):
        self.selected = isSelected
        self.update()

    def enterEvent(self, a0: QEvent):
        self.select(True)
        self.entered.emit()

    def leaveEvent(self, a0: QEvent):
        self.select(False)

    def paintEvent(self, a0: QPaintEvent):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        if self.selected:
            painter.setBrush(QBrush(self.frontColor))
        else:
            painter.setBrush(QBrush(self.backColor))
        painter.drawRect(self.rect())
        painter.end()


class ClickQLabel(QLabel):
    style = '''
#clickQLabel{
    border:1px solid #f00;
}
    '''
    clicked = pyqtSignal()  # 点击信号
    def __init__(self, parent=None):
        super(ClickQLabel, self).__init__(parent)
        self.setObjectName('clickQLabel')
        # self.setStyleSheet(self.style)
        self.setScaledContents(True)

    def mousePressEvent(self, ev: QMouseEvent):
        self.clicked.emit()

    def enterEvent(self, a0: QEvent):
        # 改变鼠标手势
        self.setCursor(Qt.PointingHandCursor)

IMAGE_SCALE = 2.7  # 图片宽高比
CENTER_IMAGE_HEIGHT = 250
CENTER_IMAGE_WIDTH = int(CENTER_IMAGE_HEIGHT * IMAGE_SCALE)
SIDE_IMAGE_HEIGHT = CENTER_IMAGE_HEIGHT - 15
SIDE_IMAGE_WIDTH = int(SIDE_IMAGE_HEIGHT * IMAGE_SCALE)


class CBanner(QWidget):
    style = '''

    '''
    #
    def __init__(self, parent=None, imageList=['../Resource/1.png','../Resource/2.png','../Resource/3.png','../Resource/4.png', '../Resource/5.png'], msc=3000):
        super(CBanner, self).__init__(parent)
        self.imageList = imageList
        self.circularImageLabelList = DoubleCircularLinkedList()  # 用双循环链表存图片
        self.circularIndexList = DoubleCircularLinkedList()  # 用双循环链表存放底部索引
        self.indexList = []
        self.imageLabelList = []
        self.timer = QTimer()  # 定时启动动画
        self.timer.timeout.connect(self.restartAnimation)
        self.timer.start(msc)
        self.setupUi()
        self.bannerWidth = self.bannerWidget.width()
        self.bannerHeight = self.bannerWidget.height()  # 固定为250
        # self.initBanner()
        # 创建并启动动画组
        self.animation_group = QParallelAnimationGroup(self)  # 动画组
        # self.createAnimation()
        # self.animation_group.start()


    def setupUi(self):
        self.resize(900, 295)
        self.setFixedHeight(CENTER_IMAGE_HEIGHT + 45)  # 45是几个布局的margin
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 15, 0, 15)
        self.bannerWidget = QWidget()
        self.bannerWidget.setFixedHeight(250)
        self.main_layout.addWidget(self.bannerWidget)
        self.hLayout = QHBoxLayout()
        self.hLayout.setContentsMargins(0, 0, 0, 0)
        spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hLayout.addItem(spacerItem)
        self.indexLayout = QHBoxLayout()  # 放轮播图下面的index
        self.indexLayout.setContentsMargins(0, 15, 0, 0)
        self.indexLayout.setSpacing(8)
        self.hLayout.addLayout(self.indexLayout)
        spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hLayout.addItem(spacerItem)
        self.main_layout.addLayout(self.hLayout)

        self.setStyleSheet(self.style)

        for i in range(len(self.imageList)):
            indicator = Indicator()
            self.indexList.append(indicator)
            self.indexLayout.addWidget(indicator)
            # 创建QLabel
            imagelabel = ClickQLabel(self.bannerWidget)
            self.imageLabelList.append(imagelabel)
            self.circularImageLabelList.append(imagelabel)
            self.circularIndexList.append(indicator)
        self.currentIndex = self.circularImageLabelList.getHead()  # 得到头节点
        self.currentBottomIndex = self.circularIndexList.getHead()  # 得到底部索引的头

        self.initBannerImages(self.imageList)

    def initBanner(self):
        '''设置每个Qlabel的位置'''
        if len(self.imageList) == 3:
            self.currentIndex.prev.item.setGeometry(0, 15, int(SIDE_IMAGE_WIDTH), SIDE_IMAGE_HEIGHT)  # 左
            self.currentIndex.item.setGeometry(int((self.bannerWidth-CENTER_IMAGE_WIDTH)/2), 0, CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT)
            self.currentBottomIndex.item.select(True)
            self.currentIndex.item.raise_()  # 在最上层显示
            self.currentIndex.next.item.setGeometry(self.bannerWidth-SIDE_IMAGE_WIDTH, 15, SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
        elif len(self.imageList) > 3:
            self.currentIndex.item.setGeometry(int((self.bannerWidth - CENTER_IMAGE_WIDTH) / 2), 0, CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT)
            self.currentBottomIndex.item.select(True)
            self.currentIndex.item.raise_()  # 最上层显示
            self.currentIndex.prev.item.setGeometry(0, 15, int(SIDE_IMAGE_WIDTH), SIDE_IMAGE_HEIGHT)
            self.currentIndex.next.item.setGeometry(self.bannerWidth - SIDE_IMAGE_WIDTH, 15, SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
            current = self.currentIndex.next.next
            while current != self.currentIndex.prev:
                current.item.setGeometry(int((self.bannerWidth-CENTER_IMAGE_WIDTH)/2), 15, SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT)
                current = current.next
        else:
            print('CustomWidget.CBanner:轮播图图片数量不能小于3')

    def initBannerImages(self, imageList):
        for i in range(len(imageList)):
            self.imageLabelList[i].setPixmap(QPixmap(imageList[i]))

    def resizeEvent(self, a0: QResizeEvent):
        self.bannerWidth = self.bannerWidget.width()
        self.bannerHeight = self.bannerWidget.height()
        self.initBanner()

    def createAnimation(self):
        self.animation_group.clear()  # 这句很重要，因为要清理之前添加的动画
        if len(self.imageList) == 3:
            newIndex = self.currentIndex
            current = self.currentIndex
            # print('CBanner.CBanner:中间的item', current.item)
            # print('CBanner.CBanner:动画前',current.item.geometry())
            while True:
                animation = QPropertyAnimation(current.item, b"geometry", self)
                animation.setStartValue(current.item.geometry())
                if current == self.currentIndex:  # 中间的移到左边
                    animation.setEndValue(QRect(0, 15, int(SIDE_IMAGE_WIDTH), SIDE_IMAGE_HEIGHT))
                elif current == self.currentIndex.prev:  # 左边的移到右边
                    animation.setEndValue(QRect(self.bannerWidth - SIDE_IMAGE_WIDTH, 15, SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT))
                elif current == self.currentIndex.next:  # 右边的移到中间
                    animation.setEndValue(QRect(int((self.bannerWidth - CENTER_IMAGE_WIDTH) / 2), 0, CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT))
                    # animation.finished.connect(self.test)
                    newIndex = current
                    self.currentBottomIndex = self.currentBottomIndex.next
                    self.select(self.currentBottomIndex)
                else:
                    print('CustomWidget.CBanner:创建动画函数有问题')
                animation.setDuration(100)  # 动画时长
                self.animation_group.addAnimation(animation)
                current = current.next
                if current == self.currentIndex:
                    break
            self.currentIndex = newIndex
            self.currentIndex.item.raise_()  # 在最上层显示
        elif len(self.imageList) > 3:
            newIndex = self.currentIndex
            current = self.currentIndex
            while True:
                animation = QPropertyAnimation(current.item, b"geometry", self)
                animation.setStartValue(current.item.geometry())
                if current == self.currentIndex:  # 中间的移到左边
                    animation.setEndValue(QRect(0, 15, int(SIDE_IMAGE_WIDTH), SIDE_IMAGE_HEIGHT))
                elif current == self.currentIndex.prev:  # 左边的移到中间
                    animation.setEndValue(QRect(int((self.bannerWidth - CENTER_IMAGE_WIDTH) / 2), 15, SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT))
                elif current == self.currentIndex.next:  # 右边的移到中间
                    animation.setEndValue(QRect(int((self.bannerWidth - CENTER_IMAGE_WIDTH) / 2), 0, CENTER_IMAGE_WIDTH, CENTER_IMAGE_HEIGHT))
                    newIndex = current
                    self.currentBottomIndex = self.currentBottomIndex.next
                    self.select(self.currentBottomIndex)
                elif current == self.currentIndex.next.next:  # 中间的移到右边
                    animation.setEndValue(
                        QRect(self.bannerWidth - SIDE_IMAGE_WIDTH, 15, SIDE_IMAGE_WIDTH, SIDE_IMAGE_HEIGHT))
                else:
                    animation.setEndValue(current.item.geometry())
                animation.setDuration(100)  # 动画时长
                self.animation_group.addAnimation(animation)
                current = current.next
                if current == self.currentIndex:
                    break
            self.currentIndex = newIndex  # 动画完成后更新当前索引
            self.currentIndex.item.raise_()  # 在最上层显示

    def select(self, index):
        '''除了当前索引被选中，其他都非选中'''
        cur = self.currentBottomIndex
        while True:
            if cur == index:
                cur.item.select(True)
            else:
                cur.item.select(False)
            cur = cur.next
            if cur == self.currentBottomIndex:
                break

    def restartAnimation(self):
        self.createAnimation()
        self.animation_group.start()

    def enterEvent(self, a0: QEvent):
        self.timer.stop()

    def leaveEvent(self, a0: QEvent):
        self.timer.start()

    # def test(self):
    #     print('CBanner.CBanner:动画后', self.currentIndex.prev.item.geometry())



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = CBanner()
    w.show()
    sys.exit(app.exec_())
