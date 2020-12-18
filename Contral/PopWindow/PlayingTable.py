# -*- coding: utf-8 -*-

"""
Created on 2020/5/3 21:17
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from Gui.PopWindowUi.Ui_PlayingTable import *


class PlayingTable(UiPlayingTable):
    def __init__(self, parent=None, parentHeight=800):
        super(PlayingTable, self).__init__(parent, parentHeight)
        self.setupUi()




if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = PlayingTable()
    w.show()
    sys.exit(app.exec_())
