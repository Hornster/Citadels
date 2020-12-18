from logics.views.stacks.gameplaySelection.hostModeIniView import HostModeIniView


class HostModeIniViewController():
    def __init__(self, myView: HostModeIniView, menuController):
        self.myView = myView
        self.myView.RegisterViewSwitchHandler(self.ChangeView)
        self.menuController = menuController

    def ChangeView(self, newView):
        self.menuController.ChangeView(newView)
