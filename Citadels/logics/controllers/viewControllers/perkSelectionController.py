
from enums.enums import OffensivePerkEnum, DefensivePerkEnum
from logics.controllers.viewControllers.PerkViewControllerBase import PerkViewControllerBase
from logics.views.stacks.perkSelectionView import PerkSelectionView
from logics.controllers.LocalMatchController import LocalMatchController


class PerkSelectionController(PerkViewControllerBase):
    def __init__(self, perkSelectionView: PerkSelectionView, matchController, nextView):
        super.__init__()
        self.perkSelectionView = perkSelectionView
        self.RegisterSelectedPerksListener(self.ParsePerks)
        self.selectedPerkHandler #Stores call to match controller. Called to inform about what perks have been chosen.
        self.__matchController = matchController


    def ParsePerks(self, selectedOffensivePerk: OffensivePerkEnum, selectedDefPerk: DefensivePerkEnum):
        self.__matchController(selectedOffensivePerk, selectedDefPerk)

