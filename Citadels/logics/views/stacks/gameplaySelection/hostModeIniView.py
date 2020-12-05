

from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QRadioButton, QLabel, QVBoxLayout, QProgressBar, QLineEdit
from data.labels import Labels
from enums.enums import ViewTypeGameplaySelection

#View that allows the player to setup a host on their machine.
class HostModeIniView(QWidget):
    def __init__(self, changeViewFunc, parent = None):
        super().__init__(parent=parent)
        self.__changeViewFunc = changeViewFunc;
        self.mainLayout = QGridLayout()

        self.backButton = QPushButton("Back")
        self.hostButton = QPushButton("Host!")
        self.portInputLabel = QLabel("Port:")
        self.portInputLabel.adjustSize()
        self.portInputBox = QLineEdit()

        self.backButton.clicked.connect(self.__onBackButtonClick)

        self.mainLayout.addWidget(self.portInputLabel, 1, 1, 1, 1)
        self.mainLayout.addWidget(self.portInputBox, 1, 2, 1, 1)
        self.mainLayout.addWidget(self.hostButton, 3, 2, 1, 1)
        self.mainLayout.addWidget(self.backButton, 4, 2, 1, 1)

        self.setLayout(self.mainLayout)
    def __onBackButtonClick(self):
        self.__changeViewFunc(ViewTypeGameplaySelection.LAN_TYPE_SELECTION)