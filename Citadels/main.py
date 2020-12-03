

from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QShortcut, QMainWindow, QHBoxLayout, QLayout
from StackManager import StackManager
from enums.enums import StackTypeLocal, StackTypeLan, GameplayTypeEnum
import sys

#https://www.tutorialspoint.com/pyqt/pyqt_qstackedwidget.htm
#https://realpython.com/python-sockets/
#https://python101.readthedocs.io/pl/latest/pyqt/kalkulator/index.html

class MainWindow(QWidget):
    xPos = 400
    yPos = 400
    width = 800
    height = 600
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.stackManager = StackManager(self, GameplayTypeEnum.LOCAL)

        self.stackManager.ChangeStack(StackTypeLocal.LOCAL_TURN_P1)
        hBox = QHBoxLayout(self)
        hBox.addWidget(self.stackManager)
        #hBox.removeWidget(self.stackManager)
        #self.stackManager.close() - use this to make the controls disappear completely. You will need to create new one later on
        self.setLayout(hBox)
        hBox.addWidget(self.stackManager)
        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setWindowTitle("Citadels")
        #Set stacks manager as central widget.
    def GetStackManager(type: GameplayTypeEnum):
        return StackManager(type)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())