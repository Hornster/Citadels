from enums.enums import PlayersEnum, OffensiveActionEnum, DefensiveActionEnum
from logics.controllers.playerDataController import PlayerDataController
from logics.views.stacks.TurnView import TurnView

class TurnController():
    def __init__(self, whatPlayer: PlayersEnum, myView: TurnView, matchController, nextView):
        self.nextView = nextView
        self.whatPlayer = whatPlayer
        self.myView = myView
        self.myView.RegisterOnActionConfirmed(self.ParseSelections)
        self.selectedActionHandler = 0 # Stores call to matchController. Passes info about what actions have been selected.
        self.__matchController = matchController

        self.__RegisterHandlers()

    def __RegisterHandlers(self):
        playersDataController = PlayerDataController.GetInstance()
        playersDataController.RegisterOnDamageTakenHandler(self.whatPlayer, self.UpdateMyHealthBar)

        self.__matchController.RegisterViewStateResetHandler(self.__ResetViewState)

        if self.whatPlayer is PlayersEnum.P1:
            playersDataController.RegisterOnDamageTakenHandler(PlayersEnum.P2, self.UpdateEnemyHealthBar)
        else:
            playersDataController.RegisterOnDamageTakenHandler(PlayersEnum.P1, self.UpdateEnemyHealthBar)

    def __ResetViewState(self):
        self.myView.ResetState()

    def ParseSelections(self, offensiveAction:OffensiveActionEnum, defensiveAction:DefensiveActionEnum):
        self.__matchController.PlayerActionSelected(self.whatPlayer, offensiveAction, defensiveAction)
        if(self.whatPlayer is PlayersEnum.P1):
            self.__matchController.ChangeView(self.nextView)
        else:
            self.__matchController.TurnFinished()

    # Registers event handler that will be called upon confirming action
    # selection by the player. Should accept arguments:
    # OffensiveActionEnum
    # DefensiveActionEnum
    def RegisterSelectedActionListener(self, listener):
        self.selectedAcitonHandler = listener

    def UpdateMyHealthBar(self, myFillPercentage):
        self.myView.SetMyHealthBarValue(myFillPercentage)

    def UpdateEnemyHealthBar(self, enemyFillPercentage):
        self.myView.SetEnemyHealthBarValue(enemyFillPercentage)

