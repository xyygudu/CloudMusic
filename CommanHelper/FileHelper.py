from PyQt5.QtCore import QFile


class FlieHelper:
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

    # @staticmethod
    # def setStyle(style):
    #     qss = QFile(style)
    #     qss.open(QFile.ReadOnly)
    #     qss_style = qss.readAll()
    #     qss.close()
    #     return qss_style


