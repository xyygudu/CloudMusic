# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PlayingTable.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class UiPlayingTable(QWidget):

    style = '''
/*set style for vertical QScrollBar*/
QScrollBar:vertical{
    width:9px;
    border:0px solid rgba(64,99,250,50%);
    margin:0px,0px,0px,0px;
    padding-top:9px;
    padding-bottom:9px;
}
QScrollBar::handle:vertical{
    width:10px;
    background:#eee;
    border-radius:4px;
    min-height:20;
}
QScrollBar::handle:vertical:hover{
    background:#ddd;
    border:0px rgba(0,0,0,25%);
    border-radius:4px;
}
QScrollBar::sub-line:vertical{
    height:0px;
    background-color:rgba(255,255,255,255);
    subcontrol-position:top;
}
QScrollBar::sub-line:vertical:hover{
    height:0px;
    background:rgba(0,0,0,25%);
    subcontrol-position:top;
}
QScrollBar::add-line:vertical{
    height:0px;
    background-color:rgba(255,255,255,255);
    subcontrol-position:bottom;
}
QScrollBar::add-line:vertical:hover{
    height:0px;
    background:rgba(0,0,0,25%);
    subcontrol-position:bottom;
}
QScrollBar::add-page:vertical{
    background:rgb(255,255,255);
}
QScrollBar::sub-page:vertical{
    background:rgb(255,255,255);
}
QScrollBar::up-arrow:vertical{
    border-width:0px;
    max-height:16px;
    min-width:17px;
}
QScrollBar::down-arrow:vertical{
    border-style:outset;
    border-width:0px;
}


#Custom_Widget {
    background: #f0f0f0;
    border-radius:5px;
}


/*参考网址https://www.cnblogs.com/bclshuai/p/11933912.html*/
QTabWidget::pane {
    margin-top:10px;/*让tab-bar上去一点*/
    border-top: 1px solid #E5E5E5;
    background-color:#FFFFFF;
}

QTabWidget QTabBar::tab {
    border: 1px solid #c5c5c5;
    border-bottom-color: #FFFFFF; /* same as the pane color */
    /*border-radius: 4px;*/
    min-width: 100px;
    padding: 7px;
    font-size: 15px;
    background-color:#fff;
}

QTabBar::tab:hover{
    background-color:#dadada;
}

QTabBar::tab:selected {
    color:#fff;
    background-color:#7c7d85;
    border: 1px solid #7c7d85;
    /*border-bottom: 2px solid #2080F7;*/
    /*font-weight:bold;*/
}

QTabWidget::tab-bar {
    border-top: 2px solid #E5E5E5;
    border-bottom: 2px solid #E5E5E5;
    border-left:1px solid #E5E5E5;
    alignment: center;
    font-size: 14px;
    background-color:#FFFFFF;
}



QTableWidget::item:selected{
    background-color:#ddd;
}


#music_table,#pre_music_table{
    border-top:1px solid #e5e5e5;
}

QPushButton{
    color:#606060;
}
QPushButton:hover{
    color:#202020;
}

    '''
    def __init__(self, parent=None, parentHeight=800):
        super(UiPlayingTable, self).__init__(parent)
        self.parentHeight = parentHeight

    def setupUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)  # 这样就不会在任务栏上显示
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        self.setObjectName("widget")
        self.resize(540, int(0.7*self.parentHeight))
        self.vly_mainLayout = QHBoxLayout()
        self.vly_mainLayout.setContentsMargins(0, 10, 0, 0)
        self.vly_mainLayout.setObjectName("vly_mainLayout")
        self.music_tabWidget = QTabWidget(self)
        self.music_tabWidget.setObjectName("music_tabWidget")
        self.currentListWidget = QWidget()
        self.currentListWidget.setObjectName("currentListWidget")
        self.cur_vly_layout = QVBoxLayout(self.currentListWidget)
        self.cur_vly_layout.setContentsMargins(0, 0, 0, 0)
        self.cur_vly_layout.setSpacing(0)
        self.cur_vly_layout.setObjectName("cur_vly_layout")
        self.cur_hly_layout = QHBoxLayout()
        self.cur_hly_layout.setContentsMargins(35, 3, 35, 3)
        self.cur_hly_layout.setSpacing(10)
        self.cur_hly_layout.setObjectName("cur_hly_layout")
        self.label = QLabel(self.currentListWidget)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setObjectName("label")
        self.cur_hly_layout.addWidget(self.label)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.cur_hly_layout.addItem(spacerItem)
        self.btn_addToCollection = QPushButton(self.currentListWidget)
        self.btn_addToCollection.setIcon(QIcon(':/icon/Resource/bookmark1.png'))
        self.btn_addToCollection.setMinimumSize(QSize(0, 30))
        self.btn_addToCollection.setLayoutDirection(Qt.LeftToRight)
        self.btn_addToCollection.setObjectName("btn_addToCollection")
        self.cur_hly_layout.addWidget(self.btn_addToCollection)
        self.line = QFrame(self.currentListWidget)
        self.line.setMaximumSize(QSize(16777215, 20))
        self.line.setFrameShape(QFrame.NoFrame)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.cur_hly_layout.addWidget(self.line)
        self.btn_clearList = QPushButton(self.currentListWidget)
        self.btn_clearList.setIcon(QIcon(':/icon/Resource/delete1.png'))
        self.btn_clearList.setMinimumSize(QSize(0, 30))
        self.btn_clearList.setObjectName("btn_clearList")
        self.cur_hly_layout.addWidget(self.btn_clearList)
        self.cur_vly_layout.addLayout(self.cur_hly_layout)
        self.music_table = QTableWidget(self.currentListWidget)
        self.music_table.setFocusPolicy(Qt.NoFocus)
        self.music_table.setAutoFillBackground(True)
        self.music_table.setLayoutDirection(Qt.LeftToRight)
        self.music_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.music_table.setAlternatingRowColors(True)
        self.music_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.music_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.music_table.setShowGrid(False)
        self.music_table.setGridStyle(Qt.NoPen)
        self.music_table.setRowCount(30)
        self.music_table.setObjectName("music_table")
        self.music_table.setColumnCount(4)

        # self.music_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 去掉水平滚动条

        item = QTableWidgetItem()
        self.music_table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.music_table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.music_table.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.music_table.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.music_table.setItem(0, 0, item)
        item = QTableWidgetItem()
        self.music_table.setItem(0, 1, item)
        item = QTableWidgetItem()
        self.music_table.setItem(0, 2, item)
        item = QTableWidgetItem()
        self.music_table.setItem(0, 3, item)
        self.music_table.horizontalHeader().setVisible(False)
        # self.music_table.horizontalHeader().setDefaultSectionSize(150)
        # self.music_table.horizontalHeader().setMinimumSectionSize(50)
        self.music_table.horizontalHeader().setStretchLastSection(True)
        # 使行列头自适应宽度，所有列平均分来填充空白部分
        # self.music_table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.music_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 列宽自动分配
        self.music_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)  # 列宽可以调整
        self.music_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)  # 列宽可以调整
        self.music_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)  # 列宽可以调整
        self.music_table.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)  # 垂直滚动条按项移动

        headerView = self.music_table.horizontalHeader()
        headerView.resizeSection(0, 30)  # 设置第一列宽
        headerView.resizeSection(1, 220)  # 设置第一列宽
        headerView.resizeSection(2, 130)  # 设置第二列宽

        self.music_table.verticalHeader().setVisible(False)
        self.music_table.verticalHeader().setDefaultSectionSize(30)
        self.music_table.verticalHeader().setMinimumSectionSize(30)
        self.music_table.verticalHeader().setSortIndicatorShown(False)
        self.cur_vly_layout.addWidget(self.music_table)
        self.music_tabWidget.addTab(self.currentListWidget, "")

        '''*********************播放历史页面**********************'''
        self.prelistWidget = QWidget()
        self.prelistWidget.setObjectName("prelistWidget")
        self.music_tabWidget.addTab(self.prelistWidget, "")
        self.vly_mainLayout.addWidget(self.music_tabWidget)

        self.pre_vly_layout = QVBoxLayout(self.prelistWidget)
        self.pre_vly_layout.setContentsMargins(0, 0, 0, 0)
        self.pre_vly_layout.setSpacing(0)
        self.pre_vly_layout.setObjectName("pre_vly_layout")
        self.pre_hly_layout = QHBoxLayout()
        self.pre_hly_layout.setContentsMargins(35, 3, 35, 3)
        self.pre_hly_layout.setSpacing(10)
        self.pre_hly_layout.setObjectName("pre_hly_layout")
        self.prelabel = QLabel(self.prelistWidget)
        self.prelabel.setMinimumSize(QSize(0, 30))
        self.prelabel.setMaximumSize(QSize(16777215, 30))
        self.prelabel.setObjectName("prelabel")
        self.pre_hly_layout.addWidget(self.prelabel)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.pre_hly_layout.addItem(spacerItem)

        self.btn_preClearList = QPushButton(self.prelistWidget)
        self.btn_preClearList.setIcon(QIcon(':/icon/Resource/delete1.png'))
        self.btn_preClearList.setMinimumSize(QSize(0, 30))
        self.btn_preClearList.setObjectName("btn_preClearList")
        self.pre_hly_layout.addWidget(self.btn_preClearList)
        self.pre_vly_layout.addLayout(self.pre_hly_layout)
        self.pre_music_table = QTableWidget(self.prelistWidget)
        self.pre_music_table.setFocusPolicy(Qt.NoFocus)
        self.pre_music_table.setAutoFillBackground(True)
        self.pre_music_table.setLayoutDirection(Qt.LeftToRight)
        self.pre_music_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pre_music_table.setAlternatingRowColors(True)
        self.pre_music_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pre_music_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pre_music_table.setShowGrid(False)
        self.pre_music_table.setGridStyle(Qt.NoPen)
        self.pre_music_table.setRowCount(30)
        self.pre_music_table.setObjectName("pre_music_table")
        self.pre_music_table.setColumnCount(4)
        # self.pre_music_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 去掉水平滚
        item = QTableWidgetItem()
        self.pre_music_table.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.pre_music_table.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.pre_music_table.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.pre_music_table.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.pre_music_table.setItem(0, 0, item)
        item = QTableWidgetItem()
        self.pre_music_table.setItem(0, 1, item)
        item = QTableWidgetItem()
        self.pre_music_table.setItem(0, 2, item)
        item = QTableWidgetItem()
        self.pre_music_table.setItem(0, 3, item)
        self.pre_music_table.horizontalHeader().setVisible(False)
        # self.pre_music_table.horizontalHeader().setDefaultSectionSize(150)
        # self.pre_music_table.horizontalHeader().setMinimumSectionSize(50)
        self.pre_music_table.horizontalHeader().setStretchLastSection(True)
        # 使行列头自适应宽度，所有列平均分来填充空白部分
        # self.pre_music_table.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.pre_music_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pre_music_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.pre_music_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive)
        self.pre_music_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.pre_music_table.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)  # 垂直滚
        headerView = self.pre_music_table.horizontalHeader()
        headerView.resizeSection(0, 30)  # 设置第一列宽
        headerView.resizeSection(1, 220)  # 设置第一列宽
        headerView.resizeSection(2, 130)  # 设置第二列宽
        self.pre_music_table.verticalHeader().setVisible(False)
        self.pre_music_table.verticalHeader().setDefaultSectionSize(30)
        self.pre_music_table.verticalHeader().setMinimumSectionSize(30)
        self.pre_music_table.verticalHeader().setSortIndicatorShown(False)
        self.pre_vly_layout.addWidget(self.pre_music_table)

        self.setStyleSheet(self.style)
        self.retranslateUi()
        self.music_tabWidget.setCurrentIndex(0)

        self.layout = QVBoxLayout(self)
        # self.layout.setContentsMargins(0, 0, 0, 0)
        # 重点： 这个widget作为背景和圆角阴影
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        self.layout.addWidget(self.widget)
        self.widget.setLayout(self.vly_mainLayout)  # 对整个weight设置布局

        # 绘制窗口阴影，似乎没成功，很可能是重写了paintEvent的原因(把paintEvent注释了，然后再添加了一个weight用来装整个ui)
        # 实例阴影shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        # 设置阴影距离
        self.shadow.setOffset(-1, -1)
        # 设置阴影圆角
        self.shadow.setBlurRadius(5)
        # 设置阴影颜色
        self.shadow.setColor(Qt.gray)
        self.setGraphicsEffect(self.shadow)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("widget", "Form"))
        self.label.setText(_translate("widget", "共9首"))
        self.prelabel.setText(_translate("widget", "共9首"))
        self.btn_addToCollection.setText(_translate("widget", "收藏全部"))
        self.btn_clearList.setText(_translate("widget", "清空"))
        self.btn_preClearList.setText(_translate("widget", "清空"))
        item = self.music_table.horizontalHeaderItem(0)
        item.setText(_translate("widget", "占位"))
        item = self.music_table.horizontalHeaderItem(1)
        item.setText(_translate("widget", "歌曲名称"))
        item = self.music_table.horizontalHeaderItem(2)
        item.setText(_translate("widget", "歌手"))
        item = self.music_table.horizontalHeaderItem(3)
        item.setText(_translate("widget", "时长"))
        __sortingEnabled = self.music_table.isSortingEnabled()
        self.music_table.setSortingEnabled(False)
        item = self.music_table.item(0, 1)
        item.setText(_translate("widget", "曾经的你"))
        item = self.music_table.item(0, 2)
        item.setText(_translate("widget", "许巍"))
        item = self.music_table.item(0, 3)
        item.setText(_translate("widget", "03.35"))
        self.music_table.setSortingEnabled(__sortingEnabled)

        '''***************播放历史*************'''
        item = self.pre_music_table.horizontalHeaderItem(0)
        item.setText(_translate("widget", "占位"))
        item = self.pre_music_table.horizontalHeaderItem(1)
        item.setText(_translate("widget", "歌曲名称"))
        item = self.pre_music_table.horizontalHeaderItem(2)
        item.setText(_translate("widget", "歌手"))
        item = self.pre_music_table.horizontalHeaderItem(3)
        item.setText(_translate("widget", "时长"))
        __sortingEnabled = self.pre_music_table.isSortingEnabled()
        self.pre_music_table.setSortingEnabled(False)
        item = self.pre_music_table.item(0, 1)
        item.setText(_translate("widget", "曾经的你"))
        item = self.pre_music_table.item(0, 2)
        item.setText(_translate("widget", "许巍"))
        item = self.pre_music_table.item(0, 3)
        item.setText(_translate("widget", "03.35"))
        self.pre_music_table.setSortingEnabled(__sortingEnabled)
        self.music_tabWidget.setTabText(self.music_tabWidget.indexOf(self.currentListWidget), _translate("widget", "播放列表"))
        self.music_tabWidget.setTabText(self.music_tabWidget.indexOf(self.prelistWidget), _translate("widget", "历史记录"))





if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = UiPlayingTable()
    w.setupUi()
    w.show()
    sys.exit(app.exec_())
