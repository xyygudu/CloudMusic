# -*- coding: utf-8 -*-

"""
Created on 2020/5/2 23:06
@author: Acer
@email: 2992493013@qq.com
@description: 放整个发现音乐点击页面，需要包括tabwidget的6个tab页面，而且也设置了每个tab总体页面的最大宽度，不需要单独再每个控件中设置最大宽度
"""

from Contral.FindMusic.Recommand import *


class UiFindMusic(QWidget):

    style = '''
QTabWidget::pane {
    border-top: 1px solid #E5E5E5;
    background-color:#FFFFFF;
}

QTabWidget QTabBar::tab {
    border-bottom: 2px solid rgba(0,0,0,0);
    min-width: 70px; /*不要太大就可以使得border宽度和字体一样宽*/
    margin-left:25px; /*用来隔开每个tab*/
    margin-right-25px;
    padding-top: 14px;
    padding-bottom:14px;
    font-size: 17px;
    color:#444;
    background-color:#fafafa;
}

QTabBar::tab:hover{
    color:rgb(198, 47, 47);
}

QTabBar::tab:selected {
    color:rgb(198, 47, 47);
    background-color:#fafafa;
    border-bottom: 2px solid rgb(198, 47, 47);
    /*border-bottom: 2px solid #2080F7;*/
    /*font-weight:bold;*/
}

QTabWidget::tab-bar {
    border-top: 2px solid #E5E5E5;
    border-bottom: 2px solid #E5E5E5;
    border-left:1px solid #E5E5E5;
    alignment: center;
    font-size: 17px;
    background-color:#fafafa;
}


QScrollArea{
    border:0px;
}

#Main_widget{
    font-family:Microsoft YaHei;
    background-color:#fafafa;
}

    '''
    MAX_WIDTN = 1300  # 最大化窗口时，每个tab页面里面的内容最大宽度

    def setupUi(self):
        self.setObjectName("Main_widget")
        # self.resize(1079, 743)  # 初始化不要设置size，免得放入QScrollArea中出现滚动条，不设置size，放入水平布局后自然会设置成合适的大小
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.tabW_findMusic = QTabWidget(self)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        self.tabW_findMusic.setFont(font)
        self.tabW_findMusic.setMinimumSize(QSize(200, 0))
        self.tabW_findMusic.setMaximumSize(QSize(2000, 16777215))
        self.tabW_findMusic.setObjectName("tabW_findMusic")
        self.tab_personal_recom = QWidget()
        self.tab_personal_recom.setObjectName("tab_personal_recom")
        self.tab1_vly_layout = QVBoxLayout(self.tab_personal_recom)
        self.tab1_vly_layout.setContentsMargins(0, 0, 0, 0)
        self.tab1_vly_layout.setSpacing(0)
        self.tab1_vly_layout.setObjectName("tab1_vly_layout")
        self.scrollArea_pers_recom = QScrollArea(self.tab_personal_recom)
        self.scrollArea_pers_recom.setWidgetResizable(True)
        self.scrollArea_pers_recom.setObjectName("scrollArea_pers_recom")
        self.area_pers_recom = QWidget()
        self.area_pers_recom.setGeometry(QRect(0, 0, 965, 713))
        self.area_pers_recom.setObjectName("area_pers_recom")
        self.hly_pers_recom = QHBoxLayout(self.area_pers_recom)  # 这个是个性推荐总布局，里面只放一个大控件（其他类写的控件：RecommandUi）
        self.hly_pers_recom.setContentsMargins(0, 0, 0, 0)
        self.hly_pers_recom.setSpacing(0)
        self.hly_pers_recom.setObjectName("hly_pers_recom")
        self.recommand = Recommand()
        self.recommand.setMaximumWidth(UiFindMusic.MAX_WIDTN)
        self.recommand.setMinimumWidth(self.width())
        self.hly_pers_recom.addWidget(self.recommand)

        self.scrollArea_pers_recom.setWidget(self.area_pers_recom)
        self.tab1_vly_layout.addWidget(self.scrollArea_pers_recom)
        self.tabW_findMusic.addTab(self.tab_personal_recom, "")
        self.tab_song_sheet = QWidget()
        self.tab_song_sheet.setObjectName("tab_song_sheet")
        self.tabW_findMusic.addTab(self.tab_song_sheet, "")
        self.tab_anchor_station = QWidget()
        self.tab_anchor_station.setObjectName("tab_anchor_station")
        self.tabW_findMusic.addTab(self.tab_anchor_station, "")
        self.tab_rank = QWidget()
        self.tab_rank.setObjectName("tab_rank")
        self.tabW_findMusic.addTab(self.tab_rank, "")
        self.tab_singer = QWidget()
        self.tab_singer.setObjectName("tab_singer")
        self.tabW_findMusic.addTab(self.tab_singer, "")
        self.tab_lastest_music = QWidget()
        self.tab_lastest_music.setObjectName("tab_lastest_music")
        self.tabW_findMusic.addTab(self.tab_lastest_music, "")
        self.horizontalLayout.addWidget(self.tabW_findMusic)
        spacerItem1 = QSpacerItem(50, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.setStyleSheet(self.style)
        self.retranslateUi()
        self.tabW_findMusic.setCurrentIndex(0)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.tabW_findMusic.setTabText(self.tabW_findMusic.indexOf(self.tab_personal_recom), _translate("Form", "个性推荐"))
        self.tabW_findMusic.setTabText(self.tabW_findMusic.indexOf(self.tab_song_sheet), _translate("Form", "歌单"))
        self.tabW_findMusic.setTabText(self.tabW_findMusic.indexOf(self.tab_anchor_station), _translate("Form", "主播电台"))
        self.tabW_findMusic.setTabText(self.tabW_findMusic.indexOf(self.tab_rank), _translate("Form", "排行榜"))
        self.tabW_findMusic.setTabText(self.tabW_findMusic.indexOf(self.tab_singer), _translate("Form", "歌手"))
        self.tabW_findMusic.setTabText(self.tabW_findMusic.indexOf(self.tab_lastest_music), _translate("Form", "最新音乐"))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = UiFindMusic()
    w.setupUi()
    w.show()
    sys.exit(app.exec_())