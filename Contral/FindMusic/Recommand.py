# -*- coding: utf-8 -*-

"""
Created on 2020/5/6 19:21
@author: Acer
@email: 2992493013@qq.com
@description: ‘发现音乐’中tab的个性推荐页面的逻辑实现
"""

from Gui.FindMusicUi.RecommandUi.Ui_Recommand import *


class Recommand(UiRecommand):
    style = '''

    '''

    def __init__(self, parent=None):
        super(Recommand, self).__init__(parent)
        self.setupUi()
        self.initRecommandMusicList()
        self.initLatestMusicList()

    def initRecommandMusicList(self):
        '''推荐歌单初始化工作'''

    def initLatestMusicList(self):
        '''最新音乐的初始化工作'''

        '''槽函数'''
        self.latest_musicList.lMusicList.itemClicked.connect(self.lMusicListClicked)
        self.latest_musicList.rMusicList.itemClicked.connect(self.rMusicListClicked)

    '''********************************最新音乐*************************'''
    def lMusicListClicked(self, item):
        '''左边的list被点击'''
        self.latest_musicList.rMusicList.clearSelection()  # 取消选择右边选中的项
        if item == self.latest_musicList.rMusicList.item(0):
            pass

    def rMusicListClicked(self, item):
        '''又边的list被点击'''
        self.latest_musicList.lMusicList.clearSelection()  # 取消选择右边选中的项
        if item == self.latest_musicList.rMusicList.item(0):
            pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = Recommand()
    w.show()
    sys.exit(app.exec_())
