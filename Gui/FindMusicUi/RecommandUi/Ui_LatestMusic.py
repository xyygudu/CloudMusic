# -*- coding: utf-8 -*-

"""
Created on 2020/5/7 14:40
@author: Acer
@email: 2992493013@qq.com
@description: 显示最新的10首音乐，由两个qlistwidget组成
"""

from CustomWidgets.ClistWidgetItem import SimpleMusicListItem
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class UiLatestMusicList(QWidget):

    style = '''
QListWidget{
    border:1px solid #e5e5e5;
    background-color:rgba(0,0,0,0);
    outline:0px;
}

#lMusicList::item:hover,#rMusicList::item:hover{
    background-color: #f2f2f2;
}
#lMusicList::item:selected,#rMusicList::item:selected{
    background-color: #eee;
    border-left:3px solid red;
}


#btn_more{
    background-color:rgba(0,0,0,0);
    color:#404040;
}
#btn_more:hover{
    color:#707070;
}
    '''

    itemHeight = 70

    def __init__(self, parent=None):
        super(UiLatestMusicList, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        '''title部分'''
        # self.setMaximumWidth(1300)  # 已经再Ui_FindMusic中设置好了最大宽度，便于保证此类的通用性
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.hly_title = QHBoxLayout()
        self.hly_title.setContentsMargins(0, 0, 0, 0)
        self.lb_title = QLabel('最新音乐')
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.lb_title.setFont(font)
        self.lb_title.setObjectName("lb_title")
        self.lb_title.setFixedHeight(50)
        self.btn_more = QPushButton('更多》')
        self.btn_more.setObjectName('btn_more')
        self.hly_title.addWidget(self.lb_title)
        spacerItem = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_title.addItem(spacerItem)
        self.hly_title.addWidget(self.btn_more)
        self.main_layout.addLayout(self.hly_title)

        self.line = QFrame(self)
        self.line.setMinimumSize(QSize(0, 1))
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet("border:1px solid #e5e5e5;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_layout.addWidget(self.line)

        '''body部分'''
        self.hly_body = QHBoxLayout()
        self.hly_body.setContentsMargins(0, 15, 0, 15)
        # self.hly_body.setSpacing(0)
        self.lMusicList = QListWidget()
        self.lMusicList.setObjectName('lMusicList')
        self.rMusicList = QListWidget()
        self.rMusicList.setObjectName('rMusicList')
        self.hly_body.addWidget(self.lMusicList)
        self.hly_body.addWidget(self.rMusicList)
        self.main_layout.addLayout(self.hly_body)

        self.main_layout.addLayout(self.hly_title)
        spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout.addItem(spacerItem)

        for i in range(5):  # 为左右两个list添加5个item
            item = QListWidgetItem()
            itemWeight = SimpleMusicListItem()
            self.lMusicList.addItem(item)
            size = item.sizeHint()
            item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
            self.lMusicList.setItemWidget(item, itemWeight)

            item = QListWidgetItem()
            itemWeight = SimpleMusicListItem()
            self.rMusicList.addItem(item)
            size = item.sizeHint()
            item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
            self.rMusicList.setItemWidget(item, itemWeight)
        self.lMusicList.setFixedHeight(self.itemHeight * 5+2)  # +2是因为有边框
        self.rMusicList.setFixedHeight(self.itemHeight * 5+2)

        self.setStyleSheet(self.style)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = UiLatestMusicList()
    w.show()
    sys.exit(app.exec_())