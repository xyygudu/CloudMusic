# -*- coding: utf-8 -*-

"""
Created on 2020/4/20 19:18
@author: Acer
@email: 2992493013@qq.com
@description: 
"""
from Gui.Ui_Playing import *

class PlayingWidget(UiPlayingWidget):

    def __init__(self, parent=None):
        super(PlayingWidget, self).__init__(parent)
        self.setupUi()
        self.initPlaying()

    def initPlaying(self):
        '''槽函数'''


