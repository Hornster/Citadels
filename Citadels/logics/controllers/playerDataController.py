from data.PlayerData import PlayerData
from enums.enums import PlayersEnum, DefensivePerkEnum, OffensivePerkEnum, OffensiveActionEnum, DefensiveActionEnum


class PlayerDataController():

    def __init__(self):
        self.player1Data = PlayerData(PlayersEnum.P1)
        self.player2Data = PlayerData(PlayersEnum.P2)
        PlayerDataController.instance = self

    def GetInstance(self):
        return PlayerDataController.instance

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
