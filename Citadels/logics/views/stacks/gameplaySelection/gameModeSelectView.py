from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton
from enums.enums import ViewTypeGameplaySelection

class GameModeSelectView(QWidget):
    buttonsMaxWidth = 200
    def __init__(self, changeViewFunc, parent=None):
        super().__init__(parent=parent)
        self.__changeViewFunc = changeViewFunc

        self.layout = QGridLayout()
        self.localPlayButton = QPushButton("Local game")
        self.localPlayButton.setMaximumWidth(self.buttonsMaxWidth)
        self.lanPlayButton = QPushButton("LAN game")
        self.localPlayButton.setMaximumWidth(self.buttonsMaxWidth)
        self.__iniView()

        self.lanPlayButton.clicked.connect(self.__onLanGameButtonClick)

    def __iniView(self):
        self.layout.addWidget(self.localPlayButton, 1,1,1,1)
        self.layout.addWidget(self.lanPlayButton, 2,1,1,1)
        self.setLayout(self.layout)

    #Called upon pressing the local play button. Leads to local play beginning.
    #def __onBackButtonClick(self):
    #    self.__viewManager.ChangeView(ViewTypeGameplaySelection.GAMEPLAY_TYPE_SELECTION)

    #Called upon pressing the local play button. Leads to local play beginning.
    def __onLanGameButtonClick(self):
        self.__changeViewFunc(ViewTypeGameplaySelection.LAN_TYPE_SELECTION)


