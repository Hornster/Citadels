from ViewManager import ViewManager


class LanMatchController():
    lanMatchControllerInstance = 0

    def __init__(self, viewManager: ViewManager):
        self.viewManager = viewManager
        lanMatchControllerInstance = self

    def GetInstance(self):
        return self.lanMatchControllerInstance

    def ChangeView(self, newView):
        self.viewManager.ChangeView(newView)