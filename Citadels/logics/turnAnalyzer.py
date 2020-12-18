
from data.PlayerData import PlayerData
from enums.enums import DefensiveActionEnum, DefensivePerkEnum, OffensiveActionEnum, OffensivePerkEnum, TurnResultEnum

#Calculations for every turn end taking into account players' choices.
class TurnAnalyzer():
    instance = 0
    buffStrength = 0.2 #Used to boost power, in percents.
    debuffStrength = -0.2   #Used to weaken power, in percents. 
    baseDefensePower = 0.8 #base defense power. How much damage is ignored, in percents.
    baseMinorMismatchDefensePower = 0.4    #base defense power when not the right, but still partially working,
                                           #defense tactic is used. In percents.
    baseMajorMismatchDefensePower = 0      #base defense power when unapropriate equippment is used. In percents.
    #multipliers for attack values that base on chosen perk and attack type.
    __attackMultipliersByPerk = {
        OffensiveActionEnum.FIGHTER_FLEET : {
            OffensivePerkEnum.ARTILLERY_EFFORT : debuffStrength,
            OffensivePerkEnum.FIGHTER_FLEET_EFFORT : buffStrength,
            OffensivePerkEnum.SIEGE_FLEET_EFFORT : 0,
            },
        OffensiveActionEnum.SIEGE_FLEET : {
            OffensivePerkEnum.ARTILLERY_EFFORT : 0,
            OffensivePerkEnum.FIGHTER_FLEET_EFFORT : debuffStrength,
            OffensivePerkEnum.SIEGE_FLEET_EFFORT : buffStrength,
            },
        OffensiveActionEnum.THOR_HAMMER : {
            OffensivePerkEnum.ARTILLERY_EFFORT : buffStrength,
            OffensivePerkEnum.FIGHTER_FLEET_EFFORT : 0,
            OffensivePerkEnum.SIEGE_FLEET_EFFORT : debuffStrength,
            },
        }
    #multipliers for defense values that base on chosen perk and defense type.
    __defenseMultipliersByPerk = {
        DefensiveActionEnum.LIQUID_METAL_SHIELD : {
            DefensivePerkEnum.EXPERIMENTAL_TARGETTING_ARRAY : 0,
            DefensivePerkEnum.FUSION_REACTORS_OVERLOAD : debuffStrength,
            DefensivePerkEnum.MAG_FIELD_AMPLIFICATION : buffStrength,
            },
        DefensiveActionEnum.FLAK_BATTERY : {
            DefensivePerkEnum.EXPERIMENTAL_TARGETTING_ARRAY : buffStrength,
            DefensivePerkEnum.FUSION_REACTORS_OVERLOAD : 0,
            DefensivePerkEnum.MAG_FIELD_AMPLIFICATION : debuffStrength,
            },
        DefensiveActionEnum.THOR_FLECHETTE : {
            DefensivePerkEnum.EXPERIMENTAL_TARGETTING_ARRAY : debuffStrength,
            DefensivePerkEnum.FUSION_REACTORS_OVERLOAD : buffStrength,
            DefensivePerkEnum.MAG_FIELD_AMPLIFICATION : 0,
            }
        }
    #How effective is given defense type against given attack types, in percents.
    __defenseEfficiencyByAttackType = {
        DefensiveActionEnum.LIQUID_METAL_SHIELD : {
            OffensiveActionEnum.FIGHTER_FLEET : baseMinorMismatchDefensePower,
            OffensiveActionEnum.SIEGE_FLEET : baseMajorMismatchDefensePower,
            OffensiveActionEnum.THOR_HAMMER : baseDefensePower,
            },
        DefensiveActionEnum.FLAK_BATTERY : {
            OffensiveActionEnum.FIGHTER_FLEET : baseDefensePower,
            OffensiveActionEnum.SIEGE_FLEET : baseMinorMismatchDefensePower,
            OffensiveActionEnum.THOR_HAMMER : baseMajorMismatchDefensePower,
            },
        DefensiveActionEnum.THOR_FLECHETTE : {
            OffensiveActionEnum.FIGHTER_FLEET : baseMajorMismatchDefensePower,
            OffensiveActionEnum.SIEGE_FLEET : baseDefensePower,
            OffensiveActionEnum.THOR_HAMMER : baseMinorMismatchDefensePower,
            }
        }
    def __init__(self):
        self.baseAttackPower = 1.0  # base attack power of the players, for every piece of equipment.
        TurnAnalyzer.instance = self

    @staticmethod
    def GetInstance():
        return TurnAnalyzer.instance

    # Used to calculate the results of current turn. Returns value of type
    # TurnResultEnum, which indicates whether has the round ended (and who won) or is it still going.
    def CalculateTurn(self, p1Data: PlayerData, p2Data: PlayerData):
        p1AttackPower = self.__CalculateAttackPower(p1Data)
        p1DefensePower =  self.__CalculateDefensePower(p2Data, p1Data)

        p2AttackPower =  self.__CalculateAttackPower(p2Data)
        p2DefensePower =  self.__CalculateDefensePower(p1Data, p2Data)

        p1AttackValue =  self.__CalculateAttackValue(p1AttackPower, p2DefensePower)
        p2AttackValue =  self.__CalculateAttackValue(p2AttackPower, p1DefensePower)

        p1Data.TakeDamage(p2AttackValue)
        p2Data.TakeDamage(p1AttackValue)

        return self.__CheckVictoryConditions(p1Data, p2Data)

    # Calculates attack power for provided player.
    def __CalculateAttackPower(self, playerData: PlayerData):
        attackPowerMultiplier = 1 +  self.__attackMultipliersByPerk[playerData.offensiveActionEnum][playerData.offensivePerkEnum]
        attackPower = self.baseAttackPower * attackPowerMultiplier
        return attackPower

    # Calculates defense power for provided defender, basing on attacker's selection.
    def __CalculateDefensePower(self, attacker : PlayerData, defender : PlayerData):
        baseDefEfficiency =  self.__defenseEfficiencyByAttackType[defender.defensiveActionEnum][attacker.offensiveActionEnum]
        defEfficiencyMultiplier =  self.__defenseMultipliersByPerk[defender.defensiveActionEnum][defender.defensivePerkEnum]
        defenseValue = baseDefEfficiency * (1 + defEfficiencyMultiplier)
        return defenseValue

    # Returns attack power reduced by defense power. Defense power tells by how much percent will
    # the attack power be reduced.
    def __CalculateAttackValue(self, attackPower, defensePower):
        return attackPower * (1 - defensePower)

    # Checks if either of the players ran out of hp, and returns conclusion.
    def __CheckVictoryConditions(self, p1Data: PlayerData, p2Data: PlayerData):
        if (p1Data.health <= 0 and p2Data.health <= 0):
            return TurnResultEnum.DRAW
        elif (p1Data.health <= 0):
            return TurnResultEnum.P2_WINS
        elif (p2Data.health <= 0):
            return TurnResultEnum.P1_WINS
        else:
            return TurnResultEnum.CONTINUE