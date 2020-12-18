# -*- coding: utf-8 -*-

"""
Created on 2020/4/20 18:57
@author: Acer
@email: 2992493013@qq.com
@description: 正在播放
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class SingerHoverMask(QLabel):
    '''鼠标进入正在播放的音乐界面的歌手图像上时，显示最大化遮罩'''
    style = '''
#label{
    border-image:url(:/icon/Resource/max.png);
    background:rgba(0,0,0,102);
}
    '''
    def __init__(self, parent=None, rect = None):
        super(SingerHoverMask, self).__init__(parent)
        self.setObjectName('label')
        self.maskRect = rect
        self.setFixedSize(0, 0)

        self.setAttribute(Qt.WA_StyledBackground)
        self.setScaledContents(True)
        self.setStyleSheet(self.style)

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
        super().show()


class HoverButton(QPushButton):
    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.singerMask = SingerHoverMask(self)

    def enterEvent(self, a0: QEvent):
        '''鼠标移入btn_singerImage显示最大化图片'''
        self.singerMask.show()

    def leaveEvent(self, a0: QEvent):
        self.singerMask.close()


class UiPlayingWidget(QWidget):
    style = '''
#playing_widget{
    border-top:1px solid #ddd;
    border-right:1px solid #ddd;
}
#btn_addToLoveList{
    border-image:url(:/icon/Resource/love.png);
}
#btn_addToLoveList:hover{
    border-image:url(:/icon/Resource/love1.png);
}
#btn_share{
    border-image:url(:/icon/Resource/send.png);
}
#btn_share:hover{
    border-image:url(:/icon/Resource/send1.png);
}

    '''


    def setupUi(self):
        self.setAttribute(Qt.WA_StyledBackground)
        self.setMinimumSize(QSize(240, 60))
        self.setMaximumSize(QSize(240, 60))
        self.setStyleSheet(self.style)
        self.setObjectName("playing_widget")
        self.horizontalLayout_2 = QHBoxLayout(self)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_singerImage = HoverButton(self)
        qss = 'border-image:url(:/pic/Resource/singer.png);'
        self.btn_singerImage.setStyleSheet(qss)
        self.btn_singerImage.setMinimumSize(QSize(40, 40))
        self.btn_singerImage.setMaximumSize(QSize(40, 40))
        self.btn_singerImage.setText("")
        self.btn_singerImage.setObjectName("btn_singerImage")
        self.horizontalLayout_2.addWidget(self.btn_singerImage)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lb_songName = QLabel('曾经的你')
        self.lb_songName.setObjectName("lb_songName")
        self.verticalLayout_3.addWidget(self.lb_songName)
        self.lb_singer = QLabel('许巍')
        self.lb_singer.setObjectName("lb_singer")
        self.verticalLayout_3.addWidget(self.lb_singer)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_addToLoveList = QPushButton(self)
        self.btn_addToLoveList.setMinimumSize(QSize(20, 0))
        self.btn_addToLoveList.setMaximumSize(QSize(20, 19))
        self.btn_addToLoveList.setText("")
        self.btn_addToLoveList.setObjectName("btn_addToLoveList")
        self.verticalLayout_4.addWidget(self.btn_addToLoveList)
        self.btn_share = QPushButton(self)
        self.btn_share.setMinimumSize(QSize(20, 19))
        self.btn_share.setMaximumSize(QSize(20, 20))
        self.btn_share.setText("")
        self.btn_share.setObjectName("btn_share")
        self.verticalLayout_4.addWidget(self.btn_share)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = UiPlayingWidget()
    w.show()
    sys.exit(app.exec_())