from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QRadioButton, QLabel, QVBoxLayout, QProgressBar, QLineEdit
from data.labels import Labels
from enums.enums import ViewTypeGameplaySelection

#View that allows the player to setup a host on their machine.
#ChangeViewFunc: function argument that accepts ViewTypeGameplaySelection enum.
class LanModeSelection(QWidget):
    def __init__(self, changeViewFunc, parent = None):
        super().__init__(parent=parent)
        self.__changeViewFunc = changeViewFunc;
        self.mainLayout = QGridLayout()

        self.hostButton = QPushButton("Host game")
        self.joinGameButton = QPushButton("Join game")
        self.backButton = QPushButton("Back")

        self.backButton.clicked.connect(self.__onBackButtonClick)
        self.hostButton.clicked.connect(self.__onHostGameButtonClick)
        self.joinGameButton.clicked.connect(self.__onClientGameButtonClick)

        self.mainLayout.addWidget(self.hostButton, 1, 1, 1, 1)
        self.mainLayout.addWidget(self.joinGameButton, 2, 1, 1, 1)
        self.mainLayout.addWidget(self.backButton, 3, 1, 1, 1)

        self.setLayout(self.mainLayout)

    #Called upon pressing the back button. Causes return to gameplay selection menu.
    def __onBackButtonClick(self):
        self.__changeViewFunc(ViewTypeGameplaySelection.GAMEPLAY_TYPE_SELECTION)
    #Called upon pressing the host game button. Leads to host settings view.
    def __onHostGameButtonClick(self):
        self.__changeViewFunc(ViewTypeGameplaySelection.HOST)
    #Called upon pressing the join game button. Leads to connection with server settings view.
    def __onClientGameButtonClick(self):
        self.__changeViewFunc(ViewTypeGameplaySelection.CLIENT)