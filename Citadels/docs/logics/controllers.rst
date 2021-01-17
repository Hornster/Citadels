Controllers package
===================
Controllers of the game's behavior.

LanMatchController class
-------------------------
A stub for a Lan Match Controller. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
GetInstance              \-                     Returns instance of the class.
ChangeView               int                    Changes view to the one assigned under passed id. See view-related `enums`_.
======================== ====================== ===============================================================================================

.. _`enums`: ../enums.rst

LocalMatchController class
--------------------------
Match controller for locla, hotseat match. Public functions:

============================= ======================================= ===============================================================================================
Name                          Args                                    Description
============================= ======================================= ===============================================================================================
PlayerPerkSelected            `PlayersEnum`_, `OffensivePerkEnum`_,   Called upon perk selection by given player. Passes retrieved data to **PlayerDataController**.
                              `DefensivePerkEnum`_
PlayerActionSelected          `PlayersEnum`_, `OffensiveActionEnum`_, Called upon action selection by given player. Passes retrieved data to **PlayerDataController**.
                              `DefensiveActionEnum`_
TurnFinished                  \-                                      Called when turn has been finished. Initiates turn calculations.
ChangeView                    int                                     Changes view to the one assigned under passed id. See view-related `enums`_.
RegisterViewStateResetHandler Func()                                  Registers argumentless function as handler for the view reset event.
============================= ======================================= ===============================================================================================

.. _`PlayersEnum`: ../enums.rst
.. _`OffensivePerkEnum`: ../enums.rst
.. _`DefensivePerkEnum`: ../enums.rst
.. _`OffensiveActionEnum`: ../enums.rst
.. _`DefensiveActionEnum`: ../enums.rst

MenuController class
--------------------
Controller for the main menu of the game. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
GetInstance              \-                     Returns instance of the class.
ChangeView               int                    Changes view to the one assigned under passed id. See view-related `enums`_.
======================== ====================== ===============================================================================================

PlayerDataController class
--------------------------
Manages players' data. Singleton. Public functions:

============================= ======================================= ===============================================================================================
Name                          Args                                    Description
============================= ======================================= ===============================================================================================
SetPlayerPerks                `PlayersEnum`_, `OffensivePerkEnum`_,   Called upon perk selection by given player. Sets perks of the players in their respective
                              `DefensivePerkEnum`_                    objects.
SetPlayerActions              `PlayersEnum`_, `OffensiveActionEnum`_, Called upon action selection by given player. Sets actions of the players in their respective.
                              `DefensiveActionEnum`_                  objects.
GetPlayerData                 `PlayersEnum`_                          Returns the data of the player assigned to provided via argument ID.
RegisterOnDamageTakenHandler  `PlayersEnum`_, Func(float, float)      Registers a handler for player receiving damage event. The provided function requires 2
                                                                      arguments:
                                                                      - First float for the player's healthbar fill percentage (their ID passed in PlayersEnum arg)
                                                                      - Second float for the other player's healthbar fill percentage
ResetPlayers                  \-                                      Resets the state of the players.
GetInstance                   \-                                      Returns instance of the class.
============================= ======================================= ===============================================================================================


