from data.labels import Labels
from ViewManager import ViewManager
from logics.controllers.LocalMatchController import LocalMatchController


# View that allows the player to select next move.
class ViewsCreator(object):
    localMatchController = LocalMatchController()

    def __init__(self, whatPlayer, parent=None):
        super().__init__(parent=parent)

        self.modeSelectionView = ViewManager()
