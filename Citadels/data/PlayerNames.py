from enums.enums import PlayersEnum


class PlayerNames():
    player1Name = "Player 1"
    player2Name = "Player 2"

    @staticmethod
    def GetPlayerName(whatPlayer: PlayersEnum):
        if(whatPlayer is PlayersEnum.P1):
            return PlayerNames.player1Name
        else:
            return PlayerNames.player2Name