
# -*- coding: utf-8 -*-

"""
Created on 2020/4/19 19:19
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from Gui.Ui_LeftNavigation import *


class LeftNavigation(UiLeftNavigation):
    def __init__(self, parent=None):
        super(LeftNavigation, self).__init__(parent)
        self.setupUi()

        self.lw_recommand.itemClicked.connect(self.recommandListItemChanged)
        self.lw_myMusic.itemClicked.connect(self.myMusicListItemChanged)
        self.lw_create_music_list.itemClicked.connect(self.creatMusicListItemChanged)
        self.btn_addSongListItem.clicked.connect(self.btnAddSongListItem)
        self.btn_openList.clicked.connect(self.btnOpenOrFoldMusicList)

    def recommandListItemChanged(self, item):
        # 清空其他列表选中的选项(如果后期加入我的收藏，则这里也要添加代码)
        self.lw_myMusic.clearSelection()
        self.lw_create_music_list.clearSelection()

    def myMusicListItemChanged(self, item):
        # 清空其他列表选中的选项(如果后期加入我的收藏，则这里也要添加代码)
        self.lw_recommand.clearSelection()
        self.lw_create_music_list.clearSelection()

    def creatMusicListItemChanged(self, item):
        # 清空其他列表选中的选项(如果后期加入我的收藏，则这里也要添加代码)
        self.lw_recommand.clearSelection()
        self.lw_myMusic.clearSelection()

    def btnAddSongListItem(self):
        '''点击创建新歌单槽函数'''


    def btnOpenOrFoldMusicList(self):
        '''展开或者折叠创建的歌单的槽函数'''
        if self.lw_create_music_list.isHidden() == False:  # 关闭
            self.btn_openList.setStyleSheet('#btn_openList{border-image:url(:/icon/Resource/right.png);}'
                                            '#btn_openList:hover{border-image:url(:/icon/Resource/right1.png);}')
            self.lw_create_music_list.setHidden(True)
        else:
            self.btn_openList.setStyleSheet('#btn_openList{border-image:url(:/icon/Resource/down.png);}'
                                            '#btn_openList:hover{border-image:url(:/icon/Resource/down1.png);}')
            self.lw_create_music_list.setHidden(False)



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = LeftNavigation()
    w.show()
    sys.exit(app.exec_())