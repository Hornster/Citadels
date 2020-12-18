from logics.views.stacks.gameplaySelection.lanModeSelection import LanModeSelection


class LanModeSelectionViewController():
    def __init__(self, myView: LanModeSelection, menuController):
        self.myView = myView
        self.myView.RegisterViewSwitchHandler(self.ChangeView)
        self.menuController = menuController


    def ChangeView(self, newView):
        self.menuController.ChangeView(newView)