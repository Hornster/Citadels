from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QRadioButton, QLabel, QVBoxLayout
from data.labels import Labels
from enums.enums import OffensivePerkEnum, DefensivePerkEnum

class PerkSelectionView(QWidget):
    def __init__(self, whatPlayer, parent = None):
        super().__init__(parent=parent)
        
        #Selected perks information will be stored here.
        self.selectedDefPerk
        self.selectedOffensivePerk

        self.mainLayout = QGridLayout()

        offensivePerkLayout = self.__CreateOffensivePerkControls()
        defensivePerkLayout = self.__CreateDefensivePerkControls()

        offensiveLayoutWidget = QWidget()
        defensiveLayoutWidget = QWidget()
        offensiveLayoutWidget.setLayout(offensivePerkLayout)
        defensiveLayoutWidget.setLayout(defensivePerkLayout)
        
        self.__whatPlayer = whatPlayer
        self.playerNote = QLabel(whatPlayer)
        self.countersTip = QLabel(Labels.COUNTERS_TIP)
        
        self.nextButton = QPushButton("Ready!")
        self.nextButton.click.connect(self.__OnPerksApproved)
        
        self.mainLayout.addWidget(self.playerNote, 1, 2, 1, 1)
        self.mainLayout.addWidget(self.countersTip, 2, 2, 1, 1)
        self.mainLayout.addWidget(offensiveLayoutWidget, 3, 1, 2, 3)
        self.mainLayout.addWidget(defensiveLayoutWidget, 5, 1, 2, 3)
        

        self.setLayout(self.mainLayout)

        self.__perkSelectionListener #Will be called like a function when player confirms selection of perks.
        
    #Initializes controls that are used to select offensive perks of the station in the game.
    #Returns fully setup offensive area layout.
    def __CreateOffensivePerkControls(self):
        self.selectedOffensivePerk = OffensivePerkEnum.ARTILLERY_EFFORT

        offensivePerkLayout = QGridLayout()
        #Offensive perks
        #Radio buttons defining the offensive perks group.
        self.artilleryEffortRadioButton = QRadioButton(Labels.ARTILLERY_EFFORT)
        self.siegeFleetEffortRadioButton = QRadioButton(Labels.SIEGE_FLEET_EFFORT)
        self.FighterFleetEffortRadioButton = QRadioButton(Labels.FIGHTER_FLEET_EFFORT)

        self.artilleryEffortRadioButton.click.connect(self.__OnArtilleryEffortBtnClick)
        self.siegeFleetEffortRadioButton.click.connect(self.__OnSiegeEffortBtnClick)
        self.FighterFleetEffortRadioButton.click.connect(self.__OnFighterEffortBtnClick)

        self.artilleryEffortRadioButton.click()
        #descriptions for above radiobuttons
        self.artilleryEffortLabel = QLabel(Labels.ARTILLERY_EFFORT_DETAILS)
        self.siegeFleetEffortLabel = QLabel(Labels.SIEGE_FLEET_EFFORT_DETAILS)
        self.fighterFleetEffortLabel = QLabel(Labels.FIGHTER_FLEET_EFFORT_DETAILS)

        self.offensivePerksTip = QLabel("Select offensive perk.")

        offensivePerkLayout.addWidget(self.offensivePerksTip, 1, 1, 1, 1)

        offensivePerkLayout.addWidget(self.artilleryEffortRadioButton, 2, 1, 1, 1)
        offensivePerkLayout.addWidget(self.siegeFleetEffortRadioButton, 3, 1, 1, 1)
        offensivePerkLayout.addWidget(self.FighterFleetEffortRadioButton, 4, 1, 1, 1)

        offensivePerkLayout.addWidget(self.artilleryEffortLabel, 2, 2, 1, 1)
        offensivePerkLayout.addWidget(self.siegeFleetEffortLabel, 3, 2, 1, 1)
        offensivePerkLayout.addWidget(self.fighterFleetEffortLabel, 4, 2, 1, 1)

        return offensivePerkLayout
    
    #Initializes controls that are used to select defensive perks of the station in the game.
    def __CreateDefensivePerkControls(self):
        self.selectedDefPerk = DefensivePerkEnum.FUSION_REACTORS_OVERLOAD

        defensivePerkLayout = QGridLayout()
        #Defensive perks
        #Radio buttons defining the offensive perks group.
        self.fusionReactorsOverloadRadioButton = QRadioButton(Labels.FUSION_REACTORS_OVERLOAD)
        self.magFieldAmplifyRadioButton = QRadioButton(Labels.AMPLIFY_MAG_FIELD)
        self.expTargetingArrayRadioButton = QRadioButton(Labels.EXP_TARGETING_ARRAY)

        self.fusionReactorsOverloadRadioButton.click.connect(self.__OnFusionReactorsBtnClick)
        self.magFieldAmplifyRadioButton.click.connect(self.__OnMagFieldAmplifyBtnClick)
        self.expTargetingArrayRadioButton.click.connect(self.__OnExpTargetingArrayBtnClick)

        self.fusionReactorsOverloadRadioButton.click()
        #descriptions for above radiobuttons
        self.fusionReactorsOverloadLabel = QLabel(Labels.FUSION_REACTORS_OVERLOAD_DETAILS)
        self.magFieldAmplifyLabel = QLabel(Labels.AMPLIFY_MAG_FIELD_DETAILS)
        self.expTargetingArrayLabel = QLabel(Labels.EXP_TARGETING_ARRAY_DETAILS)
        
        self.defensivePerksTip = QLabel("Select defensive perk.")

        defensivePerkLayout.addWidget(self.defensivePerksTip, 1, 1, 1, 1)

        defensivePerkLayout.addWidget(self.fusionReactorsOverloadRadioButton, 2, 1, 1, 1)
        defensivePerkLayout.addWidget(self.magFieldAmplifyRadioButton, 3, 1, 1, 1)
        defensivePerkLayout.addWidget(self.expTargetingArrayRadioButton, 4, 1, 1, 1)

        defensivePerkLayout.addWidget(self.fusionReactorsOverloadLabel, 2, 2, 1, 1)
        defensivePerkLayout.addWidget(self.magFieldAmplifyLabel, 3, 2, 1, 1)
        defensivePerkLayout.addWidget(self.expTargetingArrayLabel, 4, 2, 1, 1)

        return defensivePerkLayout

    def __OnArtilleryEffortBtnClick():
        self.selectedOffensivePerk = OffensivePerkEnum.ARTILLERY_EFFORT
    def __OnSiegeEffortBtnClick():
        self.selectedOffensivePerk = OffensivePerkEnum.SIEGE_FLEET_EFFORT
    def __OnFighterEffortBtnClick():
        self.selectedOffensivePerk = OffensivePerkEnum.FIGHTER_FLEET_EFFORT

    def __OnFusionReactorsBtnClick():
        self.selectedDefPerk = DefensivePerkEnum.FUSION_REACTORS_OVERLOAD
    def __OnMagFieldAmplifyBtnClick():
        self.selectedDefPerk = DefensivePerkEnum.MAG_FIELD_AMPLIFICATION
    def __OnExpTargetingArrayBtnClick():
        self.selectedDefPerk = DefensivePerkEnum.EXPERIMENTAL_TARGETTING_ARRAY

    #Upon approving selection, will pass the data down to logic so it can be remembered and used.
    def __OnPerksApproved():
        self.__perkSelectionListener(self.selectedOffensivePerk, self.selectedDefPerk)
    #Used to register a single listener for the perk selection confirmation event.
    #The event handler must accept two values as params:
    #OffensivePerkEnum
    #DefensivePerkEnum
    def RegisterPerkSelectionListener(listener):
        self.__perkSelectionListener = listener