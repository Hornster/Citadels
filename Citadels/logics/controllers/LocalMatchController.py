from logics.ViewManager import ViewManager
from enums.enums import PlayersEnum, OffensivePerkEnum, DefensivePerkEnum, DefensiveActionEnum, OffensiveActionEnum, \
    ViewTypeLocal, TurnResultEnum, MatchEnds
from logics.controllers.playerDataController import PlayerDataController
from logics.turnAnalyzer import TurnAnalyzer


class LocalMatchController():
    localMatchController = 0

    def __init__(self, viewManager: ViewManager):
        self.resetViewStateHandlers = [] # stores handlers to views that would like to reset their state.
        self.viewManager = viewManager
        LocalMatchController.localMatchController = self

    def PlayerPerkSelected(self, whatPlayer: PlayersEnum, offensivePerk: OffensivePerkEnum, defensivePerk: DefensivePerkEnum):
        playerDataController = PlayerDataController.GetInstance()
        playerDataController.SetPlayerPerks(whatPlayer, offensivePerk, defensivePerk)

    def PlayerActionSelected(self, whatPlayer: PlayersEnum, offensiveAction: OffensiveActionEnum, defensiveAction: DefensiveActionEnum):
        playerDataController = PlayerDataController.GetInstance()
        playerDataController.SetPlayerActions(whatPlayer, offensiveAction, defensiveAction)

    def TurnFinished(self):
        self.PerformTurnCalculations()

    def ChangeView(self, newView):
        self.viewManager.ChangeView(newView)

    def PerformTurnCalculations(self):
        playerDataController = PlayerDataController.GetInstance()
        turnAnalyzer = TurnAnalyzer.GetInstance()

        player1Data = playerDataController.GetPlayerData(PlayersEnum.P1)
        player2Data = playerDataController.GetPlayerData(PlayersEnum.P2)

        roundResult = turnAnalyzer.CalculateTurn(player1Data, player2Data)

        if roundResult is TurnResultEnum.CONTINUE:
            self.ChangeView(ViewTypeLocal.LOCAL_TURN_P1)
        else:
            if roundResult is TurnResultEnum.DRAW:
                self.ChangeView(MatchEnds.MATCH_END_DRAW)
            elif roundResult is TurnResultEnum.P1_WINS:
                self.ChangeView(MatchEnds.MATCH_END_P1_VICTORY)
            else:
                self.ChangeView(MatchEnds.MATCH_END_P2_VICTORY)

            self.__ResetGameState(playerDataController)

    # Register a resetting function that will be called when game resets
    # it's state. Handler function should have no arguments.
    def RegisterViewStateResetHandler(self, handler):
        self.resetViewStateHandlers.append(handler)

    def __ResetGameState(self, playerDataController: PlayerDataController):
        playerDataController.ResetPlayers()

        for viewHandler in self.resetViewStateHandlers:
            viewHandler()
