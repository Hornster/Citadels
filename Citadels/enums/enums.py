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
