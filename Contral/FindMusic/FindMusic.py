# -*- coding: utf-8 -*-

"""
Created on 2020/5/4 15:42
@author: Acer
@email: 2992493013@qq.com
@description: 
"""

from Gui.FindMusicUi.Ui_FindMusic import *


class FindMusic(UiFindMusic):
    def __init__(self, parent=None):
        super(FindMusic, self).__init__(parent)
        self.setupUi()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = FindMusic()
    w.show()
    sys.exit(app.exec_())

