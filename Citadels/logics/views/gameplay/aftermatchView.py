from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout


class AftermatchView(QWidget):
    def __init__(self, textToShow, parent = None):
        super().__init__(parent=parent)

        self.onMatchConfirmHandler = 0

        self.shownText = QLabel(textToShow)
        self.nextButton = QPushButton("End match")

        self.nextButton.clicked.connect(self.OnMatchEndConfirm)

        self.myLayout = QVBoxLayout()
        self.myLayout.addWidget(self.shownText)
        self.myLayout.addWidget(self.nextButton)

        self.setLayout(self.myLayout)

    def OnMatchEndConfirm(self):
        self.onMatchConfirmHandler()

    def RegisterOnMatchEndConfirmHandler(self, handler):
        self.onMatchConfirmHandler = handler

