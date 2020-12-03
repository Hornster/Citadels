from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from logics.views.stacks.gameModeSelectStack import GameModeSelectStack
from logics.views.stacks.perkSelectionStack import PerkSelectionStack
from logics.views.stacks.local.TurnStack import TurnStack
from enums.enums import GameplayTypeEnum

class StackManager(QStackedWidget):
    def __init__(self, mainWindow: QMainWindow, type: GameplayTypeEnum):
        super().__init__(mainWindow)
        #The order of added stacks to the manager has to mirror values in StackTypeEnum.
        if type == GameplayTypeEnum.LOCAL:
            self.__IniForLocal()
        
    def __IniForLocal(self):
        self.addWidget(PerkSelectionStack("Player 1")) #P1 perk settings
        self.addWidget(PerkSelectionStack("Player 2")) #P2 perk settings
        self.addWidget(TurnStack("Player 1")) #P1 turn widget
        self.addWidget(TurnStack("Player 2")) #P2 turn widget


    def ChangeStack(self, newStack):
        self.setCurrentIndex(newStack)



