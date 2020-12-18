# -*- coding: utf-8 -*-

"""
Created on 2020/5/4 22:20
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from Gui.PopWindowUi.Ui_MyOperation import *


class MyOperation(UiMyOperation):
    def __init__(self, parent=None):
        super(MyOperation, self).__init__(parent)
        self.setupUi()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = MyOperation()
    w.show()
    sys.exit(app.exec_())
