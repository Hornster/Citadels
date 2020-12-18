from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton
from enums.enums import ViewTypeGameplaySelection, ViewTypeLocal


class GameModeSelectView(QWidget):
    buttonsMaxWidth = 200
    def __init__(self, parent=None):
        self.__changeViewFunc = 0
        super().__init__(parent=parent)
        self.layout = QGridLayout()
        self.localPlayButton = QPushButton("Local game")
        self.localPlayButton.setMaximumWidth(self.buttonsMaxWidth)
        self.lanPlayButton = QPushButton("LAN game")
        self.lanPlayButton.setMaximumWidth(self.buttonsMaxWidth)
        self.__iniView()

        self.lanPlayButton.clicked.connect(self.__onLanGameButtonClick)
        self.localPlayButton.clicked.connect(self.__onLocalGameButtonClick)

    def __iniView(self):
        self.layout.addWidget(self.localPlayButton, 1,1,1,1)
        self.layout.addWidget(self.lanPlayButton, 2,1,1,1)
        self.setLayout(self.layout)

    # Called upon pressing the local play button. Leads to local play beginning.
    def __onLocalGameButtonClick(self):
        self.__changeViewFunc(ViewTypeLocal.PERK_SELECT_P1)

    # Called upon pressing the local play button. Leads to local play beginning.
    def __onLanGameButtonClick(self):
        self.__changeViewFunc(ViewTypeGameplaySelection.LAN_TYPE_SELECTION)

    #The function should accept one argument for view type.
    def RegisterViewSwitchHandler(self, handler):
        self.__changeViewFunc = handler


