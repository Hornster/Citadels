from ViewManager import ViewManager


class LanMatchController():

    def __init__(self, viewManager: ViewManager):
        self.viewManager = viewManager
        LanMatchController.lanMatchControllerInstance = self

    def GetInstance(self):
        return self.lanMatchControllerInstance

    def ChangeView(self, newView):
        self.viewManager.ChangeView(newView)