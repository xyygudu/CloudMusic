# -*- coding: utf-8 -*-

"""
Created on 2020/6/17 20:54
@author: Acer
@email: 2992493013@qq.com
@description: 自定义button
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CButton(QPushButton):

    # 按钮形状
    RECTANGlE = 0
    CICULAR = 1

    def __init__(self, text='', parent=None):
        super(CButton, self).__init__(parent)
        self.entered = False
        self.setText(text)

    def setShape(self, shape=RECTANGlE):
        if shape == CButton.CICULAR:
            pass
        elif shape ==CButton.RECTANGlE:
            pass

    def hover(self, iconPath=None):
        if iconPath is not None:
            if self.entered:
                # iconPath需要重新修改
                icon = QIcon(iconPath)
                self.setIcon(icon)
            else:
                icon = QIcon(iconPath)
                self.setIcon(icon)

    def enterEvent(self, a0: QEvent):
        self.entered = True

    def leaveEvent(self, a0: QEvent):
        self.entered = False
