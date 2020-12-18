from logics.views.stacks.gameplaySelection.gameModeSelectView import GameModeSelectView


class GameModeSelectViewController():
    def __init__(self, myView: GameModeSelectView, menuController):
        self.myView = myView
        self.myView.RegisterViewSwitchHandler(self.ChangeView)
        self.menuController = menuController

    def ChangeView(self, newView):
        self.menuController.ChangeView(newView)