# -*- coding: utf-8 -*-

"""
Created on 2020/5/6 12:54
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CImageInfo(QWidget):
    clicked = pyqtSignal()
    style = '''
#lb_info{
    color:#404040;
}
    '''
    def __init__(self, parent=None, text='请添加图片描述', imagePath='../Resource/userimage.jpg', aspectRatio=1):
        super(CImageInfo, self).__init__(parent)
        self.text = text
        self.imagePath = imagePath
        self.aspectRatio = aspectRatio  # 显示图片的QLable图片宽高比
        self.setupUi()

    def setupUi(self):
        self.vly = QVBoxLayout(self)
        self.vly.setContentsMargins(0, 0, 0, 0)
        self.vly.setSpacing(10)
        self.lb_image = QLabel('')
        self.lb_image.setObjectName('lb_image')
        self.lb_image.setScaledContents(True)  # 显示完整的图片
        # self.lb_image.setMinimumSize(150, 150)  # 不能设置最大size，免得窗口过大时，本控件不能占满整个父控件(这句可以不要，因为在布局中会自然分配大小)
        self.lb_image.setPixmap(QPixmap(self.imagePath))
        self.lb_info = QLabel(self.text)
        self.lb_info.setObjectName('lb_info')
        # self.lb_info.setMinimumWidth(150)
        self.lb_info.setFixedHeight(50)
        self.lb_info.setWordWrap(True)
        self.vly.addWidget(self.lb_image)
        self.vly.addWidget(self.lb_info)

        self.setStyleSheet(self.style)

    def setText(self, text):
        self.lb_info.setText(text)

    def mousePressEvent(self, a0: QMouseEvent):
        if a0.buttons() == Qt.LeftButton:
            self.clicked.emit()  # 点击信号发送出去

    def enterEvent(self, a0: QEvent):
        self.setCursor(Qt.PointingHandCursor)

    def resizeEvent(self, a0: QResizeEvent):
        width = self.lb_image.width()
        height = int(width / self.aspectRatio)
        # 当主窗口宽度变化时，本控件宽度也会改变，要使lb_image的宽高相同，就只设置lb_iamge的高度固定，
        # 如果宽度固定了，那下次执行resizeEvent时，lb_image的宽度就不会变化，无法做到控件随主窗口变大变小
        self.lb_image.setFixedHeight(height)
        self.lb_info.resize(width, 50)




class CImageListWidget(QWidget):
    style = '''
#btn_more{
    background-color:rgba(0,0,0,0);
    color:#404040;
}
#btn_more:hover{
    color:#707070;
}
    '''
    def __init__(self, parent=None,titleName='推荐歌单',row=2, col=5, aspectRatio=1):
        super(CImageListWidget, self).__init__(parent)
        self.titleName = titleName
        self.col = col  # 每一行有多少列
        self.row = row
        self.aspectRatio = aspectRatio  # 显示图片的QLable图片宽高比
        self.setupUi()

    def setupUi(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.hly_title = QHBoxLayout()
        self.hly_title.setContentsMargins(0, 0, 0, 0)
        self.lb_title = QLabel(self.titleName)
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

        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 15, 0, 15)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.imageInfo_list = []
        for i in range(self.row):  # 默认两行
            for j in range(self.col):
                self.vly = QVBoxLayout()
                self.vly.setContentsMargins(0, 0, 0, 0)
                imageInfo = CImageInfo(self, '请添加图片描述请添加图片描述请添加图片', aspectRatio=self.aspectRatio)
                self.vly.addWidget(imageInfo)
                self.gridLayout.addLayout(self.vly, i, j)
                self.imageInfo_list.append(imageInfo)
        self.main_layout.addLayout(self.gridLayout)
        spacerItem = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.main_layout.addItem(spacerItem)

        self.setStyleSheet(self.style)

    def hideTitle(self):
        self.lb_title.hide()
        self.btn_more.hide()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = CImageListWidget()
    # w.hideTitle()
    w.show()
    sys.exit(app.exec_())

