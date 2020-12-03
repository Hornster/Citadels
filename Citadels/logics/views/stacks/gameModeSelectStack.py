from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton


class GameModeSelectStack(QWidget):
    buttonsMaxWidth = 200
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.layout = QGridLayout()
        self.localPlayButton = QPushButton("Local game")
        self.localPlayButton.setMaximumWidth(self.buttonsMaxWidth)
        self.lanPlayButton = QPushButton("LAN game")
        self.localPlayButton.setMaximumWidth(self.buttonsMaxWidth)
        self.__iniStack()

    def __iniStack(self):
        self.layout.addWidget(self.localPlayButton, 0,1,1,1)
        self.layout.addWidget(self.lanPlayButton, 1,1,1,1)
        self.setLayout(self.layout)

    #Returns the main widget of the stack.
    def GetWidget(self) -> QWidget:
        return self.__myWidget


