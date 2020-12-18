
from enums.enums import OffensivePerkEnum, DefensivePerkEnum, PlayersEnum
from logics.controllers.viewControllers.PerkViewControllerBase import PerkViewControllerBase
from logics.views.stacks.perkSelectionView import PerkSelectionView
from logics.controllers.LocalMatchController import LocalMatchController


class PerkSelectionController():
    def __init__(self, whatPlayer: PlayersEnum,  perkSelectionView: PerkSelectionView, matchController, nextView):
        self.nextView = nextView
        self.whatPlayer = whatPlayer
        self.perkSelectionView = perkSelectionView
        self.perkSelectionView.RegisterPerkSelectionListener(self.ParsePerks)
        self.__matchController = matchController
        self.__matchController.RegisterViewStateResetHandler(self.__ResetViewState)


    def ParsePerks(self, selectedOffensivePerk: OffensivePerkEnum, selectedDefPerk: DefensivePerkEnum):
        self.__matchController.PlayerPerkSelected(self.whatPlayer, selectedOffensivePerk, selectedDefPerk)
        self.__matchController.ChangeView(self.nextView)

    def __ResetViewState(self):
        self.perkSelectionView.ResetState()