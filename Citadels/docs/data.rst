Data package
============

Constants and data storing structures.

Labels class
------------
Stores all labels used in the game, in static form.

PlayerData class
----------------
Stores current state of the player during the game. Arguments of members are provided from left to right. Members:

======================== ===================== ===============================================================================================
Name                      Args                  Description
======================== ===================== ===============================================================================================
TakeDamage               float                 Registers damaged dealt to the player passed in the argument. calls **onHealthChanged** event.
Reset                    \-                     Resets the state of the player.
RegisterOnHealthChanged  func(float)           Registers handler of health change event. Handler needs to have one argument of **float** type.
======================== ===================== ===============================================================================================

PlayerNames class
----------------
Knows player names, used to translate player specifying enums to these names. Static class. Arguments of members are provided from left to right. Members:

======================== ===================== ===============================================================================================
Name                      Args                  Description
======================== ===================== ===============================================================================================
GetPlayerName            `PlayersEnum`_        Returns name of a player specified by provided enum value.
======================== ===================== ===============================================================================================
.. _`PlayersEnum` Citadels/Citadels/enums
