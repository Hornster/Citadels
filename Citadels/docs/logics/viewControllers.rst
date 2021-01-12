ViewControllers package
=======================

Controllers for the views - mainly conversion of data format between views and controllers.


AftermatchViewController class
------------------------------
View controller for `AftermatchView`_. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
ExitMatch                \-                     Changes the view to game mode selection view.
======================== ====================== ===============================================================================================

.. _`AftermatchView`: views/gameplay.rst


GameModeSelectViewController class
----------------------------------
View controller for `GameModeSelectView`_. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
ChangeView                int                     Changes the view to provided ID (see `enums`_).
======================== ====================== ===============================================================================================

.. _`enums`: ../enums.rst
.. _`GameModeSelectView`: views/gameplaySelection.rst


HostModeIniViewController class
-------------------------------
View controller for `HostModeInitializationView`_. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
ChangeView                int                     Changes the view to provided ID (see `enums`_).
======================== ====================== ===============================================================================================

.. _`HostModeInitializationView`: views/gameplaySelection.rst


JoinGameViewController class
-------------------------------
View controller for `JoinGameView`_. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
ChangeView                int                     Changes the view to provided ID (see `enums`_).
======================== ====================== ===============================================================================================

.. _`JoinGameView`: views/gameplaySelection.rst


LanModeSelectionViewController class
-------------------------------
View controller for `LanModeSelectionView`_. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
ChangeView                int                     Changes the view to provided ID (see `enums`_).
======================== ====================== ===============================================================================================

.. _`LanModeSelectionView`: views/gameplaySelection.rst


PerkSelectionController class
-------------------------------
View controller for `PerkSelectionView`_. Public functions:

======================== ========================================== ===============================================================================================
Name                     Args                                       Description
======================== ========================================== ===============================================================================================
ParsePerks               `OffensivePerkEnum`_, `DefensivePerkEnum`_ Passes selected perks further and changes the view to the one set during view ini.
======================== ========================================== ===============================================================================================

.. _`PerkSelectionView`: views/gameplay.rst
.. _`OffensivePerkEnum`: ../enums.rst
.. _`DefensivePerkEnum`: ../enums.rst


TurnController class
-------------------------------
View controller for `TurnView`_. Public functions:

============================== ==================================================== ===============================================================================
Name                           Args                                                 Description
============================== ==================================================== ===============================================================================
ParseSelections                `OffensivePerkEnum`_, `DefensivePerkEnum`_           Passes selected perks further and changes the view to the one set
                                                                                    during view ini or turn result.
RegisterSelectedActionListener Func(`OffensiveActionEnum`_, `DefensiveActionEnum`_) Register an action confirmation event handler, called when player finishes 
                                                                                    their turn. Accepts function with two action enums.
UpdateMyHealthBar              float                                                Updates the player's healthbar fill of assigned view to provided percentage.
UpdateEnemyHealthBar           float                                                Updates the enemy's healthbar fill of assigned view to provided percentage.
============================== ==================================================== ===============================================================================

.. _`TurnView`: views/gameplay.rst
.. _`OffensiveActionEnum`: ../enums.rst
.. _`DefensiveActionEnum`: ../enums.rst
