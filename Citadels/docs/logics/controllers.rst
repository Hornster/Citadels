Controllers package
===================
Controllers of the game's behavior.

LanMatchController class
-------------------------
A stub for a Lan Match Controller. Singleton. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
GetInstance              \-                     Returns instance of this singleton.
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
PlayerPerkSelected            `PlayersEnum`_, `OffensiveActionEnum`_, Called upon action selection by given player. Passes retrieved data to **PlayerDataController**.
                              `DefensiveActionEnum`_
TurnFinished                  \-                                      Called when turn has been finished. Initiates turn calculations.
ChangeView                    int                                     Changes view to the one assigned under passed id. See view-related `enums`_.
RegisterViewStateResetHandler Func()                                  Registers argumentless function as handler for the view reset event.
============================= ======================================= ===============================================================================================
