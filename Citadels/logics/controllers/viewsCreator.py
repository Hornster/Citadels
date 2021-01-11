from logics.ViewManager import ViewManager
from enums.enums import PlayersEnum, TurnResultEnum, ViewTypeGameplaySelection
from logics.controllers.LanMatchController import LanMatchController
from logics.controllers.LocalMatchController import LocalMatchController
from logics.controllers.MenuController import MenuController
from logics.viewControllers.AftermatchViewController import AftermatchViewController
from logics.viewControllers.gameModeSelectViewController import GameModeSelectViewController
from logics.viewControllers.hostModeIniViewController import HostModeIniViewController
from logics.viewControllers.joinGameViewController import JoinGameViewController
from logics.viewControllers.lanModeSelectionViewController import LanModeSelectionViewController
from logics.viewControllers.perkSelectionController import PerkSelectionController
from logics.viewControllers.turnController import TurnController
from logics.views.gameplay.TurnView import TurnView
from logics.views.gameplay.aftermatchView import AftermatchView
from logics.views.gameplaySelection.gameModeSelectView import GameModeSelectView
from logics.views.gameplaySelection.hostModeIniView import HostModeIniView
from logics.views.gameplaySelection.joinGameView import JoinGameView
from logics.views.gameplaySelection.lanModeSelection import LanModeSelection
from logics.views.gameplay.perkSelectionView import PerkSelectionView


class ViewsCreator():

    def __init__(self, viewManager: ViewManager):
        self.localMatchController = LocalMatchController(viewManager)
        self.lanMatchController = LanMatchController(viewManager)
        self.menuController = MenuController(viewManager)

    def GetPerksView(self, whatPlayer: PlayersEnum, nextView, isOnline: bool):
        newPerkView = PerkSelectionView(whatPlayer)
        perkSelectionController: PerkSelectionController


        if not isOnline:
            perkSelectionController = PerkSelectionController(whatPlayer, newPerkView,
                                                              self.localMatchController, nextView)
        else:
            perkSelectionController = PerkSelectionController(whatPlayer, newPerkView, self.lanMatchController, nextView)

        return newPerkView

    def GetTurnsView(self, whatPlayer: PlayersEnum, nextView, isOnline: bool):
        newTurnsView = TurnView(whatPlayer)
        turnController: TurnController

        if not isOnline:
            turnController = TurnController(whatPlayer, newTurnsView, self.localMatchController, nextView)
        else:
            turnController = TurnController(whatPlayer, newTurnsView, self.lanMatchController, nextView)

        return newTurnsView

    def GetGameModeSelectView(self):
        newGameModeSelectView = GameModeSelectView()
        gameModeController = GameModeSelectViewController(newGameModeSelectView, self.menuController)

        return newGameModeSelectView

    def GetHostModeIniView(self):
        newHostIniModeView = HostModeIniView()
        hostModeIniViewController = HostModeIniViewController(newHostIniModeView, self.menuController)

        return newHostIniModeView

    def GetJoinGameView(self):
        newJoinGameView = JoinGameView()
        joinGameViewController = JoinGameViewController(newJoinGameView, self.menuController)

        return newJoinGameView

    def GetLanModeSelectionView(self):
        newLanModeSelectionView = LanModeSelection()
        lanModeSelectionViewController = LanModeSelectionViewController(newLanModeSelectionView, self.menuController)

        return newLanModeSelectionView

    #Creates a match end view. Note that TurnResultEnum.CONTINUE is not supported.
    def GetMatchEndView(self, turnResult: TurnResultEnum):
        textToShow = "If you see this, something went terribly wrong."
        if turnResult is TurnResultEnum.P1_WINS:
            textToShow = "Player 1 is victorious!"
        elif turnResult is TurnResultEnum.P2_WINS:
            textToShow = "Player 2 is victorious!"
        elif turnResult is TurnResultEnum.DRAW:
            textToShow = "Draw! No victorious player, only death and pain!" # If continue is added, it should not count.
        else:
            raise NameError("There cannot be a view for CONTINUE turn result!")

        newAftermatchView = AftermatchView(textToShow)
        aftermatchViewController = AftermatchViewController(newAftermatchView, self.menuController, ViewTypeGameplaySelection.GAMEPLAY_TYPE_SELECTION)

        return newAftermatchView