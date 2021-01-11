from logics.ViewManager import ViewManager

class MenuController():
    menuControllerInstance = 0
    def __init__(self, viewManager: ViewManager):
        self.viewManager = viewManager
        menuControllerInstance = self
        
    def GetInstance(self):
        return self.menuControllerInstance
    def ChangeView(self, newView):
        self.viewManager.ChangeView(newView)