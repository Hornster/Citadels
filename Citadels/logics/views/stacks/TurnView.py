
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QRadioButton, QLabel, QVBoxLayout, QProgressBar
from data.labels import Labels
from enums.enums import OffensiveActionEnum, DefensiveActionEnum

#View that allows the player to select next move.
class TurnView(QWidget):
    def __init__(self, whatPlayer, parent = None):
        super().__init__(parent=parent)

        self.selectedOffensiveAction = OffensiveActionEnum.THOR_HAMMER
        self.selectedDefAction = DefensiveActionEnum.LIQUID_METAL_SHIELD
        self.mainLayout = QGridLayout()

        offensiveLayout = self.__CreateOffensiveControls()
        defensiveLayout = self.__CreateDefensiveControls()
        citadelStateLayout = self.__CreateHealthState()

        offensiveLayoutWidget = QWidget()
        defensiveLayoutWidget = QWidget()
        citadelStateWidget = QWidget()

        offensiveLayoutWidget.setLayout(offensiveLayout)
        defensiveLayoutWidget.setLayout(defensiveLayout)
        citadelStateWidget.setLayout(citadelStateLayout)
        
        self.__whatPlayer = whatPlayer
        self.playerNote = QLabel(whatPlayer)

        self.countersTip = QLabel(Labels.COUNTERS_TIP)
        
        self.mainLayout.addWidget(self.playerNote, 1, 1, 1, 1)
        self.mainLayout.addWidget(self.countersTip, 2, 1, 1, 1)
        self.mainLayout.addWidget(citadelStateWidget, 3, 1, 1, 2)
        self.mainLayout.addWidget(offensiveLayoutWidget, 4, 1, 2, 3)
        self.mainLayout.addWidget(defensiveLayoutWidget, 4, 2, 2, 3)
        
        self.nextButton = QPushButton("Ready!")

        self.setLayout(self.mainLayout)

        self.__actionSelectionListener = 0  # Will be called (as function) upon confirming of selection by the player.
        
    #Initializes controls that are used to select offensive perks of the station in the game.
    #Returns fully setup offensive area layout.
    def __CreateOffensiveControls(self):
        offensiveLayout = QGridLayout()
        self.offensiveTip = QLabel("Select your next attack.")
        #Offensive s
        #Radio buttons defining the offensive s group.
        self.artilleryRadioButton = QRadioButton(Labels.ARTILLERY)
        self.siegeFleetRadioButton = QRadioButton(Labels.SIEGE_FLEET)
        self.FighterFleetRadioButton = QRadioButton(Labels.FIGHTER_FLEET)

        self.artilleryRadioButton.clicked.connect(self.__OnThorHammerBtnClick)
        self.siegeFleetRadioButton.clicked.connect(self.__OnSiegeFleetBtnClick)
        self.FighterFleetRadioButton.clicked.connect(self.__OnFighterFleetBtnClick)

        self.artilleryRadioButton.click()

        offensiveLayout.addWidget(self.offensiveTip, 1, 1, 1, 1)

        offensiveLayout.addWidget(self.artilleryRadioButton, 2, 1, 1, 1)
        offensiveLayout.addWidget(self.siegeFleetRadioButton, 3, 1, 1, 1)
        offensiveLayout.addWidget(self.FighterFleetRadioButton, 4, 1, 1, 1)

        return offensiveLayout
    
    #Initializes controls that are used to select defensive s of the station in the game.
    def __CreateDefensiveControls(self):
        defensiveLayout = QGridLayout()
        self.defensivesTip = QLabel("Select your next defensive action.")
        #Defensive s
        #Radio buttons defining the offensive s group.
        self.thorFlechetteRadioButton = QRadioButton(Labels.THOR_FLECHETTE)
        self.liquidMetalShieldRadioButton = QRadioButton(Labels.LIQUID_METAL_SHIELD)
        self.flakBatteryRadioButton = QRadioButton(Labels.FLAK_BATTERY)

        self.thorFlechetteRadioButton.clicked.connect(self.__OnThorFlechetteBtnClick)
        self.liquidMetalShieldRadioButton.clicked.connect(self.__OnLiquidMetalShieldBtnClick)
        self.flakBatteryRadioButton.clicked.connect(self.__OnFlakBatteryBtnClick)

        self.thorFlechetteRadioButton.click()

        #descriptions for above radiobuttons
        defensiveLayout.addWidget(self.defensivesTip, 1, 1, 1, 1)

        defensiveLayout.addWidget(self.thorFlechetteRadioButton, 2, 1, 1, 1)
        defensiveLayout.addWidget(self.liquidMetalShieldRadioButton, 3, 1, 1, 1)
        defensiveLayout.addWidget(self.flakBatteryRadioButton, 4, 1, 1, 1)

        return defensiveLayout
    #Creates set of controls that show current health of the player and their opponent.
    def __CreateHealthState(self):
        self.myHealthBar = QProgressBar()
        self.myHealthBarDesc = QLabel("Your Citadel Hull Integrity:")

        self.enemyHealthBar=QProgressBar()
        self.enemyHealthBarDesc = QLabel("Enemy Citadel Hull Integrity")
        
        layout = QGridLayout()
        layout.addWidget(self.myHealthBarDesc, 1, 1, 1, 1)
        layout.addWidget(self.myHealthBar, 2, 1, 1, 1)

        layout.addWidget(self.enemyHealthBarDesc, 1, 2, 1, 1)
        layout.addWidget(self.enemyHealthBar, 2, 2, 1, 1)

        return layout

    def __OnThorHammerBtnClick(self):
        self.selectedOffensiveAction = OffensiveActionEnum.THOR_HAMMER
    def __OnSiegeFleetBtnClick(self):
        self.selectedOffensiveAction = OffensiveActionEnum.SIEGE_FLEET
    def __OnFighterFleetBtnClick(self):
        self.selectedOffensiveAction = OffensiveActionEnum.FIGHTER_FLEET

    def __OnLiquidMetalShieldBtnClick(self):
        self.selectedDefAction = DefensiveActionEnum.LIQUID_METAL_SHIELD
    def __OnThorFlechetteBtnClick(self):
        self.selectedDefAction = DefensiveActionEnum.THOR_FLECHETTE
    def __OnFlakBatteryBtnClick(self):
        self.selectedDefAction = DefensiveActionEnum.FLAK_BATTERY

    def __OnSelectionApproved(self):
        self.__actionSelectionListener(self.selectedOffensiveAction, self.selectedDefAction)

    # Registers handler for the selection confirmation event.
    # Provided handler must have arguments:
    # OffensiveActionEnum
    # DefensiveActionEnum
    def RegisterOnActionConfirmed(self, handler):
        self.__actionSelectionListener = handler