from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QHBoxLayout, QLayout
from ViewManager import ViewManager
from enums.enums import ViewTypeLocal, ViewTypeLan, ViewManagerTypeEnum, ViewTypeGameplaySelection
from logics.controllers.LanMatchController import LanMatchController
from logics.controllers.LocalMatchController import LocalMatchController
from logics.controllers.MenuController import MenuController
import sys

# https://www.tutorialspoint.com/pyqt/pyqt_qstackedwidget.htm
# https://realpython.com/python-sockets/
# https://python101.readthedocs.io/pl/latest/pyqt/kalkulator/index.html


class MainWindow(QWidget):
    xPos = 400
    yPos = 400
    width = 800
    height = 600

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.viewManager = ViewManager(self, ViewManagerTypeEnum.MODE_SELECTION)

        self.localMatchController = LocalMatchController(self.viewManager)
        self.lanMatchController = LanMatchController(self.viewManager)
        self.menuController = MenuController(self.viewManager)

        self.localMatchController.ChangeView(ViewTypeGameplaySelection.GAMEPLAY_TYPE_SELECTION)

        hBox = QHBoxLayout(self)
        hBox.addWidget(self.viewManager)
        # hBox.removeWidget(self.stackManager)
        # self.stackManager.close() - use this to make the controls disappear completely. You will need to create new one later on
        self.setLayout(hBox)
        hBox.addWidget(self.viewManager)
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setWindowTitle("Citadels")
        # Set stacks manager as central widget.

    def GetViewManager(type: ViewManagerTypeEnum):
        return ViewManager(type)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())