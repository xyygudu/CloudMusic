# -*- coding: utf-8 -*-

"""
Created on 2020/5/4 21:48
@author: Acer
@email: 2992493013@qq.com
@description: 登录成功后点击登录按钮位置，出现的界面
"""

from CustomWidgets.ClistWidgetItem import *


class UiMyOperation(QWidget):

    style = '''
QPushButton{
    background-color:rgba(0,0,0,0);
}

QListWidget{
    border:0px;
    outline:0px;
}

#Custom_Widget {
    background: #fafafa;
    border-radius:5px;
}
#widget{
    background-color:#fafafa;
}
#lw_myOperation::item:hover{
    background-color: #f6f6f6;
}
#lw_myOperation::item:selected{
    background-color: #eee;
}
#btn_userImage{
    color:#303030;
}
#btn_userImage:hover{
    color:#707070;
}

#btn_attendance{
    border:1px solid #ddd;
    border-radius:4px;
    background-color:#e5493d;
    color:white;
}
#btn_attendance:hover{
    background-color:#c2483e;
}
    '''
    itemHeight = 45

    def setupUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)  # 这样就不会在任务栏上显示
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口透明
        self.setObjectName("widget")
        self.resize(300, 460)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hly_top = QHBoxLayout()
        self.hly_top.setContentsMargins(20, 20, 20, -1)
        self.hly_top.setObjectName("hly_top")
        self.btn_userImage = QPushButton(self)
        self.btn_userImage.setMinimumSize(QSize(0, 50))
        self.btn_userImage.setMaximumSize(QSize(150, 50))
        self.btn_userImage.setIconSize(QSize(50, 50))
        self.btn_userImage.setIcon(QIcon(':/pic/Resource/userimage.jpg'))
        self.btn_userImage.setObjectName("btn_userImage")
        self.hly_top.addWidget(self.btn_userImage)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hly_top.addItem(spacerItem)
        self.btn_attendance = QPushButton(self)
        self.btn_attendance.setIconSize(QSize(20, 18))
        self.btn_attendance.setIcon(QIcon(':/icon/Resource/money.png'))
        self.btn_attendance.setMinimumSize(QSize(80, 30))
        self.btn_attendance.setMaximumSize(QSize(80, 30))
        self.btn_attendance.setObjectName("btn_attendance")
        self.hly_top.addWidget(self.btn_attendance)
        self.verticalLayout.addLayout(self.hly_top)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 20, 0, 20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_dynamic = QPushButton(self)
        self.btn_dynamic.setMinimumSize(QSize(0, 50))
        self.btn_dynamic.setMaximumSize(QSize(200, 50))
        self.btn_dynamic.setObjectName("btn_dynamic")
        self.horizontalLayout.addWidget(self.btn_dynamic)
        self.line = QFrame(self)
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setStyleSheet("border:1px solid  rgb(207, 207, 207);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.btn_care = QPushButton(self)
        self.btn_care.setMinimumSize(QSize(0, 50))
        self.btn_care.setMaximumSize(QSize(16777215, 50))
        self.btn_care.setObjectName("btn_care")
        self.horizontalLayout.addWidget(self.btn_care)
        self.line_2 = QFrame(self)
        self.line_2.setMaximumSize(QSize(1, 16777215))
        self.line_2.setStyleSheet("border:1px solid  rgb(207, 207, 207);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.btn_fans = QPushButton(self)
        self.btn_fans.setMinimumSize(QSize(0, 50))
        self.btn_fans.setMaximumSize(QSize(16777215, 50))
        self.btn_fans.setObjectName("btn_fans")
        self.horizontalLayout.addWidget(self.btn_fans)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QFrame(self)
        self.line_3.setMaximumSize(QSize(600, 1))
        self.line_3.setStyleSheet("border:10px solid  rgb(200, 207, 207);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.lw_myOperation = QListWidget(self)
        # self.lw_myOperation.setMinimumSize(QSize(0, 270))
        # self.lw_myOperation.setMaximumSize(QSize(16777215, 270))
        self.lw_myOperation.setObjectName("lw_myOperation")
        self.verticalLayout.addWidget(self.lw_myOperation)

        self.retranslateUi()
        self.setStyleSheet(self.style)
        name_list = ['会员中心', '我的等级', '网易商城', '个人信息设置', '社交账号绑定', '退出登录']
        icon_list = ['vip.png', 'grade.png', 'shoppingcart.png', 'myinfo.png', 'phone.png', 'exitsignin.png']
        for i in range(6):
            item = QListWidgetItem()
            itemWeight = IconListItem(':/icon/Resource/'+icon_list[i], name_list[i], 30)
            itemWeight.setMargin(20)
            itemWeight.setSpacing(15)
            self.lw_myOperation.addItem(item)
            size = item.sizeHint()
            item.setSizeHint(QSize(size.width(), self.itemHeight))  # 设置item大小
            self.lw_myOperation.setItemWidget(item, itemWeight)
        self.lw_myOperation.setFixedHeight(self.lw_myOperation.count()*self.itemHeight)


        self.layout = QVBoxLayout(self)
        # self.layout.setContentsMargins(0, 0, 0, 0)
        # 重点： 这个widget作为背景和圆角阴影
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        self.layout.addWidget(self.widget)
        self.widget.setLayout(self.verticalLayout)  # 对整个weight设置布局

        # 绘制窗口阴影，似乎没成功，很可能是重写了paintEvent的原因(把paintEvent注释了，然后再添加了一个weight用来装整个ui)
        # 实例阴影shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        # 设置阴影距离
        self.shadow.setOffset(0, 0)
        # 设置阴影圆角
        self.shadow.setBlurRadius(5)
        # 设置阴影颜色
        self.shadow.setColor(Qt.black)
        self.setGraphicsEffect(self.shadow)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.btn_userImage.setText(_translate("Form", "我的昵称"))
        self.btn_attendance.setText(_translate("Form", "签到"))
        self.btn_dynamic.setText(_translate("Form", "0\n"
"动态"))
        self.btn_care.setText(_translate("Form", "0\n"
"关注"))
        self.btn_fans.setText(_translate("Form", "0\n"
"粉丝"))



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = UiMyOperation()
    w.setupUi()
    w.show()
    sys.exit(app.exec_())
