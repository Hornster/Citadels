from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QRadioButton, QLabel, QVBoxLayout, QProgressBar, QLineEdit
from data.labels import Labels
from enums.enums import ViewTypeGameplaySelection

#View that allows the player to setup a host on their machine.
class JoinGameView(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.__changeViewFunc = 0;
        self.mainLayout = QGridLayout()

        self.backButton = QPushButton("Back")
        self.joinButton = QPushButton("Join!")

        self.backButton.clicked.connect(self.__onBackButtonClick)
        
        self.serverAddressInputBox = QLineEdit(self)
        self.portInputBox = QLineEdit(self)

        self.serverAddressLabel = QLabel("Server Address:")
        self.portInputLabel = QLabel("Port:")
        
        self.mainLayout.addWidget(self.serverAddressLabel, 1, 1, 1, 1)
        self.mainLayout.addWidget(self.serverAddressInputBox, 1, 2, 1, 1)
        self.mainLayout.addWidget(self.portInputLabel, 2, 1, 1, 1)
        self.mainLayout.addWidget(self.portInputBox, 2, 2, 1, 1)
        self.mainLayout.addWidget(self.backButton, 3, 2, 1, 1)

        self.setLayout(self.mainLayout)

    def __onBackButtonClick(self):
        self.__changeViewFunc(ViewTypeGameplaySelection.LAN_TYPE_SELECTION)

    # The function should accept one argument for view type.
    def RegisterViewSwitchHandler(self, handler):
        self.__changeViewFunc = handler