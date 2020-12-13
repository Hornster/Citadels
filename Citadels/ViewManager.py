from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from logics.views.stacks.gameplaySelection.gameModeSelectView import GameModeSelectView
from logics.views.stacks.gameplaySelection.lanModeSelection import LanModeSelection
from logics.views.stacks.gameplaySelection.hostModeIniView import HostModeIniView
from logics.views.stacks.gameplaySelection.joinGameView import JoinGameView
from logics.views.stacks.awaitOtherPlayerView import AwaitOtherPlayerView
from logics.views.stacks.perkSelectionView import PerkSelectionView
from logics.views.stacks.TurnView import TurnView
from enums.enums import ViewManagerTypeEnum, ViewTypeLan

class ViewManager(QStackedWidget):
    def __init__(self, mainWindow: QMainWindow, type: ViewManagerTypeEnum):
        super().__init__(mainWindow)
        #The order of added stacks to the manager has to mirror values in ViewTypeEnum.
        #if type == ViewManagerTypeEnum.LOCAL:
        #    self.__IniForLocal()
        #elif type == ViewManagerTypeEnum.LAN:
        #    self.__IniForLan()
        #elif type == ViewManagerTypeEnum.MODE_SELECTION:
        #    self.__IniForGametypeSelection()
        self.__IniForGametypeSelection()
        self.__IniForLocal()
        self.__IniForLan()
        
    def __IniForLocal(self):
        self.addWidget(PerkSelectionView("Player 1")) #P1 perk settings
        self.addWidget(PerkSelectionView("Player 2")) #P2 perk settings
        self.addWidget(TurnView("Player 1")) #P1 turn widget
        self.addWidget(TurnView("Player 2")) #P2 turn widget

    # Initializes the view manager instance to work with lan view.
    def __IniForLan(self):
        self.addWidget(AwaitOtherPlayerView("Host connection"))
        self.addWidget(AwaitOtherPlayerView("Client connection"))
        self.addWidget(PerkSelectionView("Player 1"))  # P1 perk settings
        self.addWidget(PerkSelectionView("Player 2"))  # P2 perk settings
        self.addWidget(AwaitOtherPlayerView("Other Player"))
        self.addWidget(TurnView("Player 1"))  # P1 turn widget
        self.addWidget(TurnView("Player 2"))  # P2 turn widget

    def __IniForGametypeSelection(self):
        self.addWidget(GameModeSelectView(self.ChangeView))
        self.addWidget(LanModeSelection(self.ChangeView))
        self.addWidget(HostModeIniView(self.ChangeView))
        self.addWidget(JoinGameView(self.ChangeView))

    def ChangeView(self, newView):
        self.setCurrentIndex(newView)



