from enums.enums import PlayersEnum, OffensiveActionEnum, DefensiveActionEnum
from logics.views.stacks.TurnView import TurnView

class TurnController():
    def __init__(self, whatPlayer: PlayersEnum, myView: TurnView):
        self.whichPlayer = whatPlayer
        self.myView = myView
        self.selectedActionHandler = 0 # Stores call to matchController. Passes info about what actions have been selected.

    def ParseSelections(self, offensiveAction:OffensiveActionEnum, defensiveAction:DefensiveActionEnum):
        self.selectedActionHandler(offensiveAction, defensiveAction)

    # Registers event handler that will be called upon confirming action
    # selection by the player. Should accept arguments:
    # OffensiveActionEnum
    # DefensiveActionEnum
    def RegisterSelectedActionListener(self, listener):
        self.selectedAcitonHandler = listener
