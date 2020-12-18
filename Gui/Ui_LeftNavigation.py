# -*- coding: utf-8 -*-

"""
Created on 2020/4/18 23:59
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from CustomWidgets.ClistWidgetItem import *


class UiLeftNavigation(QScrollArea):

    style = '''
QLabel{
    background-color:rgba(0,0,0,0);
}
#leftNavigation{
    border:0px;
    border-right:1px solid #e5e5e5;
}
#btn_addSongListItem{
    border-image:url(:/icon/Resource/addsonglistitem.png);
}
#btn_addSongListItem:hover{
    border-image:url(:/icon/Resource/addsonglistitem1.png);
}
QListWidget{
    border:0px;
    outline:0px;
}
#lw_recommand::item:hover,#lw_myMusic::item:hover,#lw_create_music_list::item:hover{
    background-color: #f2f2f2;
}
#lw_recommand::item:selected,#lw_myMusic::item:selected,#lw_create_music_list::item:selected{
    background-color: #eee;
    border-left:3px solid red;
}

    '''
    itemHeight = 40

    # def __init__(self, parent=None):
    #     super(UiLeftNavigation, self).__init__(parent)
    #     self.setupUi()

    def setupUi(self):
        self.setObjectName('leftNavigation')
        self.setWidgetResizable(True)  # 至关重要，没有的话不仅大小不可变。控件不设置大小还无法显示
        self.setFixedWidth(240)
        self.mainWidget = QWidget()
        self.setWidget(self.mainWidget)
        # self.mainWidget.setMinimumSize(200, 300)
        self.vly_mainLayout = QVBoxLayout(self.mainWidget)
        self.vly_mainLayout.setSpacing(0)
        self.vly_mainLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_recommand = QLabel('推荐')
        self.lb_recommand.setStyleSheet('padding-left:5px;')
        self.lb_recommand.setFixedHeight(self.itemHeight)
        self.lw_recommand = QListWidget()
        self.lw_recommand.setObjectName('lw_recommand')
        self.vly_mainLayout.addWidget(self.lb_recommand)
        self.vly_mainLayout.addWidget(self.lw_recommand)

        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/findmusic.png', '发现音乐')
        self.lw_recommand.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_recommand.setItemWidget(item, itemWeight)

        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/fm.png', '私人FM')
        self.lw_recommand.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_recommand.setItemWidget(item, itemWeight)

        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/Livebroadcast.png', 'LOOK直播')
        self.lw_recommand.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_recommand.setItemWidget(item, itemWeight)

        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/video.png', '视频')
        self.lw_recommand.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_recommand.setItemWidget(item, itemWeight)

        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/friend.png', '朋友')
        self.lw_recommand.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_recommand.setItemWidget(item, itemWeight)

        self.lw_recommand.setFixedHeight(self.lw_recommand.count()*self.itemHeight)

        self.lb_myMusic = QLabel('我的音乐')
        self.lb_myMusic.setStyleSheet('padding-left:5px;')
        self.lb_myMusic.setFixedHeight(self.itemHeight)
        self.lw_myMusic = QListWidget()
        self.lw_myMusic.setObjectName('lw_myMusic')
        self.vly_mainLayout.addWidget(self.lb_myMusic)
        self.vly_mainLayout.addWidget(self.lw_myMusic)

        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/localmusic.png', '本地音乐')
        self.lw_myMusic.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_myMusic.setItemWidget(item, itemWeight)
        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/download.png', '下载管理')
        self.lw_myMusic.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_myMusic.setItemWidget(item, itemWeight)
        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/cloudmusic.png', '云盘音乐')
        self.lw_myMusic.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_myMusic.setItemWidget(item, itemWeight)
        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/collect.png', '我的收藏')
        self.lw_myMusic.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_myMusic.setItemWidget(item, itemWeight)

        self.lw_myMusic.setFixedHeight(self.lw_myMusic.count() * self.itemHeight)

        self.hly_create_music_list = QHBoxLayout()
        self.hly_create_music_list.setContentsMargins(0, 0, 5, 0)
        self.hly_create_music_list.setObjectName('hly_create_music_list')
        self.hly_create_music_list.setSpacing(7)
        self.lb_create_music_list = QLabel('创建的歌单')
        self.lb_create_music_list.setStyleSheet('padding-left:5px;')
        self.lb_create_music_list.setObjectName('lb_create_music_list')
        self.lb_create_music_list.setFixedHeight(self.itemHeight)
        self.hly_create_music_list.addWidget(self.lb_create_music_list)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_create_music_list.addItem(spacerItem)
        self.btn_addSongListItem = QPushButton()
        self.btn_addSongListItem.setFixedSize(self.itemHeight - 20, self.itemHeight - 20)
        self.btn_addSongListItem.setObjectName('btn_addSongListItem')
        self.hly_create_music_list.addWidget(self.btn_addSongListItem)
        self.btn_openList = QPushButton()
        self.btn_openList.setObjectName('btn_openList')
        self.btn_openList.setFixedSize(self.itemHeight - 15, self.itemHeight - 15)
        self.btn_openList.setStyleSheet('#btn_openList{border-image:url(:/icon/Resource/down.png);}'
                                        '#btn_openList:hover{border-image:url(:/icon/Resource/down1.png);}')
        self.hly_create_music_list.addWidget(self.btn_openList)
        self.vly_mainLayout.addLayout(self.hly_create_music_list)
        self.lw_create_music_list = QListWidget()
        self.lw_create_music_list.setObjectName('lw_create_music_list')
        self.vly_mainLayout.addWidget(self.lw_create_music_list)

        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/like.png', '我喜欢的音乐')
        self.lw_create_music_list.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_create_music_list.setItemWidget(item, itemWeight)

        item = QListWidgetItem()
        itemWeight = IconListItem(':/icon/Resource/musiclist.png', '纯音乐')
        self.lw_create_music_list.addItem(item)
        size = item.sizeHint()
        item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
        self.lw_create_music_list.setItemWidget(item, itemWeight)

        self.lw_create_music_list.setMinimumHeight(self.lw_create_music_list.count() * self.itemHeight)

        spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vly_mainLayout.addItem(spacerItem)
        self.mainWidget.setLayout(self.vly_mainLayout)
        self.setStyleSheet(self.style)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = UiLeftNavigation()
    w.setupUi()
    w.show()
    sys.exit(app.exec_())


