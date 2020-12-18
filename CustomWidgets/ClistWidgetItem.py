# -*- coding: utf-8 -*-

"""
Created on 2020/4/19 0:12
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class IconListItem(QWidget):
    '''带有icon的ListWidgetItem'''
    style = '''
QLabel{
    color:#555;
}
    '''
    def __init__(self,iconPath='', text='自定义文字', iconSize=20, parent=None):
        super(IconListItem, self).__init__(parent)
        '''ui'''
        self.icon = QLabel('')
        self.icon.setFixedSize(iconSize, iconSize)
        self.icon.setPixmap(QPixmap(iconPath))
        self.icon.setScaledContents(True)
        self.text = QLabel(text)
        self.text.setObjectName('text')
        self.text.setAlignment(Qt.AlignVCenter)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        # font.setBold(True)
        # font.setWeight(75)
        self.text.setFont(font)
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.icon)
        self.h_layout.addWidget(self.text)
        self.h_layout.setContentsMargins(20, 0, 20, 0)
        self.setLayout(self.h_layout)
        self.setStyleSheet(self.style)
        # self.resize(240, 35)

    def setMargin(self, margin):
        self.h_layout.setContentsMargins(margin, 0, margin, 0)

    def setSpacing(self, spacing):
        self.h_layout.setSpacing(spacing)


class SimpleMusicListItem(QWidget):
    style = '''
    #lb_author{
        color:#555;
    }
    QLabel{
        background-color:rgba(0,0,0,0);
    }
        '''

    def __init__(self, parent=None):
        super(SimpleMusicListItem, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.main_hly = QHBoxLayout(self)
        self.main_hly.setContentsMargins(0, 8, 0, 8)
        self.lb_order = QLabel('01')
        self.lb_order.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.lb_order.setObjectName('lb_order')
        self.lb_order.setFixedWidth(50)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.lb_order.setFont(font)
        self.main_hly.addWidget(self.lb_order)

        self.lb_image = QLabel('')
        self.lb_image.setScaledContents(True)
        self.lb_image.setPixmap(QPixmap('../Resource/userimage.jpg'))
        self.lb_image.setObjectName('lb_image')
        self.main_hly.addWidget(self.lb_image)

        self.vly_info = QVBoxLayout()
        self.vly_info.setContentsMargins(0, 0, 0, 0)
        self.vly_info.setSpacing(0)
        self.lb_musicName = QLabel('歌曲名称')
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.lb_musicName.setFont(font)
        self.vly_info.addWidget(self.lb_musicName)
        # spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.vly_info.addItem(spacerItem)
        self.hly_author = QHBoxLayout()
        self.hly_author.setContentsMargins(0, 0, 0, 0)
        self.hly_author.setSpacing(7)
        self.lb_sound_quality = QLabel("")
        self.lb_sound_quality.setFixedSize(22, 14)
        self.lb_sound_quality.setPixmap(QPixmap('../Resource/standard-sound.png'))
        self.lb_sound_quality.setScaledContents(True)
        self.hly_author.addWidget(self.lb_sound_quality)
        self.lb_author = QLabel('歌曲作者')
        self.lb_author.setObjectName('lb_author')
        # self.lb_author.setFixedHeight(20)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(9)
        self.lb_author.setFont(font)
        self.hly_author.addWidget(self.lb_author)
        self.vly_info.addLayout(self.hly_author)
        self.main_hly.addLayout(self.vly_info)

        spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.main_hly.addItem(spacerItem)

        self.setStyleSheet(self.style)
        # self.setFixedSize(400, 60)

    def resizeEvent(self, a0: QResizeEvent):
        imageHeight = self.lb_image.height()
        self.lb_image.setFixedWidth(imageHeight)

    def setItemInfo(self, infoList):
        '''
        为这个item添加信息，包括序号，歌曲图片，歌名，标签图片，歌手
        :param infoList:
        :return:
        '''
        self.lb_order.setText(infoList[0])
        self.lb_image.setPixmap(QPixmap(infoList[1]))
        self.lb_musicName.setText(infoList[2])
        self.lb_sound_quality.setPixmap(QPixmap(infoList[3]))
        self.lb_author.setText(infoList[4])




if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = SimpleMusicListItem()
    w.show()
    sys.exit(app.exec_())