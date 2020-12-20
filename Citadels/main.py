from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QHBoxLayout, QLayout
from ViewManager import ViewManager
from enums.enums import ViewTypeLocal, ViewTypeLan, ViewManagerTypeEnum, ViewTypeGameplaySelection, PlayersEnum, \
    TurnResultEnum
from logics.controllers.LanMatchController import LanMatchController
from logics.controllers.LocalMatchController import LocalMatchController
from logics.controllers.MenuController import MenuController
import sys


from logics.controllers.playerDataController import PlayerDataController
from logics.controllers.viewsCreator import ViewsCreator
from logics.turnAnalyzer import TurnAnalyzer


class MainWindow(QWidget):
    xPos = 400
    yPos = 400
    width = 800
    height = 600

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.playerDataController = PlayerDataController()
        self.turnAnalyzer = TurnAnalyzer()

        self.viewManager = ViewManager(self)
        self.viewsCreator = ViewsCreator(self.viewManager)
        viewsArray = self.CreateViews()
        self.viewManager.AddViews(viewsArray)

        self.localMatchController = LocalMatchController(self.viewManager)
        self.lanMatchController = LanMatchController(self.viewManager)
        self.menuController = MenuController(self.viewManager)

        self.localMatchController.ChangeView(ViewTypeGameplaySelection.GAMEPLAY_TYPE_SELECTION)

        hBox = QHBoxLayout(self)
        hBox.addWidget(self.viewManager)
        # hBox.removeWidget(self.stackManager)
        # self.stackManager.close() - use this to make the controls disappear completely. You will need to create new one later on
        self.setLayout(hBox)
        hBox.addWidget(self.viewManager)
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setWindowTitle("Citadels")

        # Resetting players updates their UI info as well.
        self.playerDataController.ResetPlayers()


    def CreateViews(self):
        viewsArray = []

        # Create menu views
        viewsArray.append(self.viewsCreator.GetGameModeSelectView())
        viewsArray.append(self.viewsCreator.GetLanModeSelectionView())
        viewsArray.append(self.viewsCreator.GetHostModeIniView())
        viewsArray.append(self.viewsCreator.GetJoinGameView())

        # Create local gameplay views
        viewsArray.append(self.viewsCreator.GetPerksView(PlayersEnum.P1,
                                                        ViewTypeLocal.PERK_SELECT_P2, False))
        viewsArray.append(self.viewsCreator.GetPerksView(PlayersEnum.P2,
                                                        ViewTypeLocal.LOCAL_TURN_P1, False))
        viewsArray.append(self.viewsCreator.GetTurnsView(PlayersEnum.P1,
                                                        ViewTypeLocal.LOCAL_TURN_P2, False))
        viewsArray.append(self.viewsCreator.GetTurnsView(PlayersEnum.P2,
                                                        ViewTypeLocal.LOCAL_TURN_P1, False))

        # Match end views
        viewsArray.append(self.viewsCreator.GetMatchEndView(TurnResultEnum.DRAW))
        viewsArray.append(self.viewsCreator.GetMatchEndView(TurnResultEnum.P1_WINS))
        viewsArray.append(self.viewsCreator.GetMatchEndView(TurnResultEnum.P2_WINS))

        return viewsArray

    def GetViewManager(type: ViewManagerTypeEnum):
        return ViewManager(type)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())