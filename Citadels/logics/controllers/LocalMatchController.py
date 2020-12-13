from ViewManager import ViewManager
from enums.enums import PlayersEnum, OffensivePerkEnum, DefensivePerkEnum, DefensiveActionEnum, OffensiveActionEnum
from logics.controllers.playerDataController import PlayerDataController


class LocalMatchController():
    localMatchController = 0

    def __init__(self, viewManager: ViewManager):
        self.viewManager = viewManager
        LocalMatchController.localMatchController = self

    def GetInstance(self):
        return LocalMatchController.localMatchController

    def PlayerPerkSelected(self, whatPlayer: PlayersEnum, offensivePerk: OffensivePerkEnum, defensivePerk: DefensivePerkEnum):
        playerDataController = PlayerDataController.GetInstance()
        playerDataController.SetPlayerPerks(whatPlayer, offensivePerk, defensivePerk)

    def PlayerActionSelected(self, whatPlayer: PlayersEnum, offensiveAction: OffensiveActionEnum, defensiveAction: DefensiveActionEnum):
        playerDataController = PlayerDataController.GetInstance()
        playerDataController.SetPlayerActions(whatPlayer, offensiveAction, defensiveAction)

    def ChangeView(self, newView):
        self.viewManager.ChangeView(newView)
