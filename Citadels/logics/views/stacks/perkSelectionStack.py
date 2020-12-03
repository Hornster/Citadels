from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QRadioButton, QLabel, QVBoxLayout
from data.labels import Labels

class PerkSelectionStack(QWidget):
    def __init__(self, whatPlayer, parent = None):
        super().__init__(parent=parent)
        
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
        
        self.mainLayout.addWidget(self.playerNote, 1, 2, 1, 1)
        self.mainLayout.addWidget(self.countersTip, 2, 2, 1, 1)
        self.mainLayout.addWidget(offensiveLayoutWidget, 3, 1, 2, 3)
        self.mainLayout.addWidget(defensiveLayoutWidget, 5, 1, 2, 3)
        

        self.setLayout(self.mainLayout)
        
    #Initializes controls that are used to select offensive perks of the station in the game.
    #Returns fully setup offensive area layout.
    def __CreateOffensivePerkControls(self):
        offensivePerkLayout = QGridLayout()
        #Offensive perks
        #Radio buttons defining the offensive perks group.
        self.artilleryEffortRadioButton = QRadioButton(Labels.ARTILLERY_EFFORT)
        self.siegeFleetEffortRadioButton = QRadioButton(Labels.SIEGE_FLEET_EFFORT)
        self.FighterFleetEffortRadioButton = QRadioButton(Labels.FIGHTER_FLEET_EFFORT)
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
        defensivePerkLayout = QGridLayout()
        #Defensive perks
        #Radio buttons defining the offensive perks group.
        self.fusionReactorsOverloadRadioButton = QRadioButton(Labels.FUSION_REACTORS_OVERLOAD)
        self.magFieldAmplifyRadioButton = QRadioButton(Labels.AMPLIFY_MAG_FIELD)
        self.expTargetingArrayRadioButton = QRadioButton(Labels.EXP_TARGETING_ARRAY)
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