from ViewManager import ViewManager
from enums.enums import ViewTypeLocal

class LocalMatchController():
    def __init__(self, viewManager: ViewManager):
        self.viewManager = viewManager
    def __Begin(self):
        self.viewManager.ChangeView()
    #def __PreparePerks(self):

