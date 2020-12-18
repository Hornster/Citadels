from data.PlayerData import PlayerData
from enums.enums import PlayersEnum, DefensivePerkEnum, OffensivePerkEnum, OffensiveActionEnum, DefensiveActionEnum


class PlayerDataController():
    instance = 0

    def __init__(self):
        self.player1Data = PlayerData(PlayersEnum.P1)
        self.player2Data = PlayerData(PlayersEnum.P2)
        PlayerDataController.instance = self

    @staticmethod
    def GetInstance():
        return PlayerDataController.instance


    def __setPlayerPerks(self, offensivePerk: OffensivePerkEnum,
                         defensivePerk: DefensivePerkEnum,
                         pData: PlayerData):
        pData.offensivePerkEnum = offensivePerk
        pData.defensivePerkEnum = defensivePerk

    def __setPlayerActions(self, offensiveAction: OffensiveActionEnum,
                         defensiveAction: DefensiveActionEnum,
                         pData: PlayerData):
        pData.offensiveActionEnum = offensiveAction
        pData.defensiveActionEnum = defensiveAction

    def SetPlayerPerks(self, whatPlayer: PlayersEnum,
                       offensivePerk: OffensivePerkEnum,
                       defensivePerk: DefensivePerkEnum):
        if(whatPlayer == PlayersEnum.P1):
            self.__setPlayerPerks(offensivePerk, defensivePerk, self.player1Data)
        else:
            self.__setPlayerPerks(offensivePerk, defensivePerk, self.player2Data)

    def SetPlayerActions(self, whatPlayer: PlayersEnum,
                         offensiveAction: OffensiveActionEnum,
                         defensiveAction: DefensiveActionEnum):
        if(whatPlayer == PlayersEnum.P1):
            self.__setPlayerActions(offensiveAction, defensiveAction, self.player1Data)
        else:
            self.__setPlayerActions(offensiveAction, defensiveAction, self.player2Data)

    def GetPlayerData(self, whatPlayer: PlayersEnum):
        if whatPlayer is PlayersEnum.P1:
            return self.player1Data
        else:
            return self.player2Data

    # Registers provided handler for player damage taking event. Provided function
    # must accept two floats params:
    # first as given player's health bar fill percentage
    # second as the player's opponents health bar fill percentage
    def RegisterOnDamageTakenHandler(self, whatPlayer: PlayersEnum, func):
        if(whatPlayer is PlayersEnum.P1):
            self.player1Data.RegisterOnHealthChanged(func)
        else:
            self.player2Data.RegisterOnHealthChanged(func)

    def ResetPlayers(self):
        self.player2Data.Reset()
        self.player1Data.Reset()
        # Force handlers to update health bars
        self.player1Data.TakeDamage(0)
        self.player2Data.TakeDamage(0)
