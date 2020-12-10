from enum import IntEnum


class ViewTypeLocal(IntEnum):
    PERK_SELECT_P1 = 0
    PERK_SELECT_P2 = 1
    LOCAL_TURN_P1 = 2
    LOCAL_TURN_P2 = 3


class ViewTypeLan(IntEnum):
    LAN_MODE_SELECTION = 4
    HOST_CONNECTION_AWAIT = 5
    CLIENT_CONNECTING = 6
    AWAIT_TURN = 7
    LAN_TURN_P1 = 8
    LAN_TURN_P2 = 9


class ViewTypeGameplaySelection(IntEnum):
    GAMEPLAY_TYPE_SELECTION = 0 #View allowing for selection between local and lan gameplay.
    LAN_TYPE_SELECTION = 1  #View allowing to select between host and client.
    HOST = 2    #View for host settings.
    CLIENT = 3  #View for client settings.


class ViewManagerTypeEnum(IntEnum):
    LOCAL = 0
    LAN = 1
    MODE_SELECTION = 2


#Offensive perk choice enum
class OffensivePerkEnum(IntEnum):
    ARTILLERY_EFFORT = 0
    SIEGE_FLEET_EFFORT = 1
    FIGHTER_FLEET_EFFORT = 2


#Defensive perk choice enum
class DefensivePerkEnum(IntEnum):
    FUSION_REACTORS_OVERLOAD = 0
    MAG_FIELD_AMPLIFICATION = 1
    EXPERIMENTAL_TARGETTING_ARRAY = 2


#Offensive action choice enum
class OffensiveActionEnum(IntEnum):
    THOR_HAMMER = 0
    FIGHTER_FLEET = 1
    SIEGE_FLEET = 2


#Defensive action choice enum
class DefensiveActionEnum(IntEnum):
    LIQUID_METAL_SHIELD = 0
    FLAK_BATTERY = 1
    THOR_FLECHETTE = 2


#Possible states of a round.
class TurnResultEnum(IntEnum):
    CONTINUE = 0
    P1_WINS = 1
    P2_WINS = 2
    DRAW = 3