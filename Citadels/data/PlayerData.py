from enums.enums import PlayersEnum, OffensiveActionEnum, OffensivePerkEnum, DefensiveActionEnum, DefensivePerkEnum


class PlayerData():
    __maxHealth = 10.0
    def __init__(self, whatPlayer: PlayersEnum):
        self.whatPlayer = whatPlayer
        self.health = PlayerData.__maxHealth
        self.offensiveAction = OffensiveActionEnum.THOR_HAMMER
        self.defensiveAction = DefensiveActionEnum.LIQUID_METAL_SHIELD
        self.offensivePerkEnum = OffensivePerkEnum.ARTILLERY_EFFORT
        self.defensivePerkEnum = DefensivePerkEnum.FUSION_REACTORS_OVERLOAD
    
    def TakeDamage(self, damageAmount):
        self.health = self.health - damageAmount