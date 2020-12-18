from enums.enums import PlayersEnum, OffensiveActionEnum, OffensivePerkEnum, DefensiveActionEnum, DefensivePerkEnum


class PlayerData():
    maxHealth = 10.0
    def __init__(self, whatPlayer: PlayersEnum):
        self.onHealthChanged = []
        self.whatPlayer = whatPlayer
        self.health = PlayerData.maxHealth
        self.offensiveActionEnum = OffensiveActionEnum.THOR_HAMMER
        self.defensiveActionEnum = DefensiveActionEnum.LIQUID_METAL_SHIELD
        self.offensivePerkEnum = OffensivePerkEnum.ARTILLERY_EFFORT
        self.defensivePerkEnum = DefensivePerkEnum.FUSION_REACTORS_OVERLOAD

    # Causes the player to receive provided damage, then calls event handler if any attached.
    def TakeDamage(self, damageAmount):
        self.health = self.health - damageAmount

        for handler in self.onHealthChanged:
            handler(self.health/PlayerData.maxHealth)

    def Reset(self):
        self.health = PlayerData.maxHealth

        self.offensiveActionEnum = OffensiveActionEnum.THOR_HAMMER
        self.defensiveActionEnum = DefensiveActionEnum.LIQUID_METAL_SHIELD
        self.offensivePerkEnum = OffensivePerkEnum.ARTILLERY_EFFORT
        self.defensivePerkEnum = DefensivePerkEnum.FUSION_REACTORS_OVERLOAD

    # Provided function shall accept one argument in form of float.
    def RegisterOnHealthChanged(self, func):
        self.onHealthChanged.append(func)