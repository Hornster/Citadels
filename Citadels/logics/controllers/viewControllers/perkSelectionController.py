
from enums.enums import OffensivePerkEnum, DefensivePerkEnum
from logics.views.stacks.perkSelectionView import PerkSelectionView
class PerkSelectionController():
    def __init__(perkSelectionView: PerkSelectionView):
        self.perkSelectionView = perkSelectionView 
        self.selectedPerkHandler #Stores call to match controller. Called to inform about what perks have been chosen.


    def ParsePerks(selectedOffensivePerk: OffensivePerkEnum, selectedDefPerk: DefensivePerkEnum):
        self.selectedPerkHandler(selectedOffensivePerk, selectedDefPerk)

    def RegisterSelectedPerksListener(listener):
        self.selectedPerkHandler = listener


      
