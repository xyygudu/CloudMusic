# -*- coding: utf-8 -*-

"""
Created on 2020/5/6 19:06
@author: Acer
@email: 2992493013@qq.com
@description: 本页面是‘发现音乐’中tab的个性推荐页面
"""

from CustomWidgets.CImageListWidget import *
from CustomWidgets.CBanner import *
from Gui.FindMusicUi.RecommandUi.Ui_LatestMusic import *


class UiRecommand(QWidget):
    style = '''

    '''
    def setupUi(self):
        self.setObjectName('recommand')
        self.main_hLayout = QHBoxLayout(self)  # 水平布局两边放两个spacerItem，中间放控件
        self.main_hLayout.setContentsMargins(0, 0, 0, 0)
        spacerItem = QSpacerItem(100, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.main_hLayout.addItem(spacerItem)
        self.vly_content = QVBoxLayout()
        self.vly_content.setContentsMargins(0, 0, 0, 0)
        self.main_hLayout.addLayout(self.vly_content)
        spacerItem = QSpacerItem(100, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.main_hLayout.addItem(spacerItem)

        self.vly_banner = QVBoxLayout()  # 放轮播图的布局
        self.vly_banner.setContentsMargins(0, 0, 0, 0)
        self.vly_content.addLayout(self.vly_banner)
        self.vly_recom_musicList = QVBoxLayout()  # 放推荐歌单
        self.vly_recom_musicList.setContentsMargins(0, 0, 0, 0)
        self.vly_content.addLayout(self.vly_recom_musicList)
        self.vly_specialSent = QVBoxLayout()  # 放独家放送
        self.vly_content.addLayout(self.vly_specialSent)
        self.vly_latestMusic = QVBoxLayout()  # 放最新音乐
        self.vly_content.addLayout(self.vly_latestMusic)
        self.vly_recom_mv = QVBoxLayout()  # 放推荐MV
        self.vly_content.addLayout(self.vly_recom_mv)
        self.vly_look = QVBoxLayout()  # 放看看
        self.vly_content.addLayout(self.vly_look)

        self.banner = CBanner()
        self.vly_banner.addWidget(self.banner)
        self.recom_musicList = CImageListWidget(self, '推荐歌单', 2, 5, 1)
        # self.recom_musicList.hideTitle()  # 隐藏标题
        self.vly_recom_musicList.addWidget(self.recom_musicList)
        self.specialSend = CImageListWidget(self, '独家放送', 1, 3, 1.5)
        self.vly_specialSent.addWidget(self.specialSend)
        self.latest_musicList = UiLatestMusicList(self)
        self.vly_latestMusic.addWidget(self.latest_musicList)
        self.recom_mv = CImageListWidget(self, '推荐MV', 1, 3, 1.5)
        self.vly_recom_mv.addWidget(self.recom_mv)
        self.look = CImageListWidget(self, '看看', 1, 4, 0.75)
        self.vly_look.addWidget(self.look)

        self.setStyleSheet(self.style)
