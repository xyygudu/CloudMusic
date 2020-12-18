
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class CSearchEdit(QWidget):

    style = '''
#cSearchWeight{
    border:0px solid #eee;
    border-radius:15px;
    background-color:#a82828;
}

#lineEdit{
    border:0;
    color:#ccc;
    padding-left:10px;
    background-color:rgba(255,255,255,0); /*完全透明*/
    font-family:Microsoft YaHei;
    font-size:16px;
}

#searchBtn{
    border:0;
    background-color:rgba(255,255,255,0); /*完全透明*/
    border-image:url(:/icon/Resource/search.png)
    
}

#searchBtn:hover{
    border:0;
    border-image:url(:/icon/Resource/searchhover.png)   
}
    '''

    searchSignal = pyqtSignal(str)  # 将输入框的数据发送处出去

    def __init__(self, placeHolderText = '请输入学生学号', width = 200, heigh = 30, parent=None):
        super(CSearchEdit, self).__init__(parent)

        # 先创建一个QLineEdit
        self.lineEdit = QLineEdit()
        self.lineEdit.setObjectName('lineEdit')
        self.lineEdit.setPlaceholderText(placeHolderText)
        self.lineEdit.setMinimumSize(150, heigh)

        # 创建一个搜索按钮
        self.searchBtn = QPushButton()
        self.searchBtn.setObjectName('searchBtn')
        self.searchBtn.setFixedSize(int(heigh*3/5), int(heigh*3/5))  # 正方形搜索按钮

        # 创建水平布局，将上面两个控件添加进来
        self.hLayout = QHBoxLayout()
        self.hLayout.setContentsMargins(0, 0, 10, 0)
        self.hLayout.addWidget(self.lineEdit)
        self.hLayout.addWidget(self.searchBtn)

        self.setObjectName('cSearchWeight')
        self.setAttribute(Qt.WA_StyledBackground)  # 很重要, 没有这句QSS对QWeight的有些代码会无效
        self.setLayout(self.hLayout)
        self.setFixedSize(width, heigh)
        self.setStyleSheet(self.style)

        '''绑定槽函数'''
        self.searchBtn.clicked.connect(self.btnSearch)

    def btnSearch(self):
        self.searchSignal.emit(self.lineEdit.text())  # 将输入框的数据发送出去



if __name__ == '__main__':
    '''测试自定义搜索框'''
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = CSearchEdit()
    w.show()
    sys.exit(app.exec_())