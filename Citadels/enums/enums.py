from enum import IntEnum
class StackTypeLocal(IntEnum):
    PERK_SELECT_P1 = 0
    PERK_SELECT_P2 = 1
    LOCAL_TURN_P1 = 2
    LOCAL_TURN_P2 = 3
    
class StackTypeLan(IntEnum):
    
    LAN_MODE_SELECTION = 4
    HOST_CONNECTION_AWAIT = 5
    CLIENT_CONNECTING = 6
    AWAIT_TURN = 7
    LAN_TURN_P1 = 8
    LAN_TURN_P2 = 9

class GameplayTypeEnum(IntEnum):
    LOCAL = 0
    LAN = 1
