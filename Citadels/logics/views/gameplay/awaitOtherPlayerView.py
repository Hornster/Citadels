
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QStackedWidget
from PyQt5.QtWidgets import QGridLayout, QPushButton, QRadioButton, QLabel, QVBoxLayout, QProgressBar
from data.labels import Labels

#View that allows the player to select next move.
class AwaitOtherPlayerView(QWidget):
    def __init__(self, whatPlayer, parent = None):
        super().__init__(parent=parent)
        
        self.mainLayout = QVBoxLayout()

        self.awaitingInfo = QLabel("Awaiting " + whatPlayer + "...")

        self.mainLayout.addWidget(self.awaitingInfo)

        self.setLayout(self.mainLayout)