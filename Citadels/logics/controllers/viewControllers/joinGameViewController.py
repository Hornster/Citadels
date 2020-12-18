from logics.views.stacks.gameplaySelection.joinGameView import JoinGameView


class JoinGameViewController():
    def __init__(self, myView: JoinGameView, menuController):
        self.myView = myView
        self.myView.RegisterViewSwitchHandler(self.ChangeView)
        self.menuController = menuController

    def ChangeView(self, newView):
        self.menuController.ChangeView(newView)