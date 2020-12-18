from ViewManager import ViewManager
from data.labels import Labels
from enums.enums import PlayersEnum, TurnResultEnum, ViewTypeGameplaySelection
from logics.controllers.LanMatchController import LanMatchController
from logics.controllers.LocalMatchController import LocalMatchController
from logics.controllers.MenuController import MenuController
from logics.controllers.viewControllers.AftermatchViewController import AftermatchViewController
from logics.controllers.viewControllers.gameModeSelectViewController import GameModeSelectViewController
from logics.controllers.viewControllers.hostModeIniViewController import HostModeIniViewController
from logics.controllers.viewControllers.joinGameViewController import JoinGameViewController
from logics.controllers.viewControllers.lanModeSelectionViewController import LanModeSelectionViewController
from logics.controllers.viewControllers.perkSelectionController import PerkSelectionController
from logics.controllers.viewControllers.turnController import TurnController
from logics.views.stacks.TurnView import TurnView
from logics.views.stacks.aftermatchView import AftermatchView
from logics.views.stacks.gameplaySelection.gameModeSelectView import GameModeSelectView
from logics.views.stacks.gameplaySelection.hostModeIniView import HostModeIniView
from logics.views.stacks.gameplaySelection.joinGameView import JoinGameView
from logics.views.stacks.gameplaySelection.lanModeSelection import LanModeSelection
from logics.views.stacks.perkSelectionView import PerkSelectionView


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