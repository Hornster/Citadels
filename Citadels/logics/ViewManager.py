from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from enums.enums import ViewManagerTypeEnum, ViewTypeLan, PlayersEnum, ViewTypeLocal


class ViewManager(QStackedWidget):
    def __init__(self, mainWindow: QMainWindow):
        super().__init__(mainWindow)

    # Argument viewArrays should be a numpy array of QWidgets
    def AddViews(self, viewArray: []):
        for view in viewArray:
            self.addWidget(view)

    # Initializes the view manager instance to work with lan view.
    # def __IniForLan(self):
        # self.addWidget(AwaitOtherPlayerView("Host connection"))
        # self.addWidget(AwaitOtherPlayerView("Client connection"))
        # self.addWidget(PerkSelectionView("Player 1"))  # P1 perk settings
        # self.addWidget(PerkSelectionView("Player 2"))  # P2 perk settings
        # self.addWidget(AwaitOtherPlayerView("Other Player"))
        # self.addWidget(TurnView("Player 1"))  # P1 turn widget
        # self.addWidget(TurnView("Player 2"))  # P2 turn widget

    def ChangeView(self, newView):
        self.setCurrentIndex(newView)



