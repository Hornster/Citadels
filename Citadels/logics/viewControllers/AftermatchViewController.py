from logics.views.gameplay.aftermatchView import AftermatchView


class AftermatchViewController():
    def __init__(self, aftermatchView: AftermatchView, menuController, nextView):
        self.nextView = nextView
        self.menuController = menuController
        self.aftermatchView = aftermatchView
        self.aftermatchView.RegisterOnMatchEndConfirmHandler(self.ExitMatch)

    def ExitMatch(self):
        self.menuController.ChangeView(self.nextView)
