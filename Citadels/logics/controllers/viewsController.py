
from data.labels import Labels
from ViewManager import ViewManager

#View that allows the player to select next move.
class ViewsController(object):
    def __init__(self, whatPlayer, parent = None):
        super().__init__(parent=parent)
        
        self.modeSelectionView = ViewManager()