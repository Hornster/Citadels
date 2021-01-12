Logics package
==============
Contains processing logic of the game.

Child packages:
---------------

========================================= ===============================================================================================
Name                                      Description
========================================= ===============================================================================================
`controllers`_                            Gameplay controllers - the actual game calculations.
`viewControllers`_                        Views controllers - initialization of views, data passing to controllers.
`views`_                                  Views used in the game.
========================================= ===============================================================================================

.. _`controllers`: logics/controllers.rst
.. _`viewControllers`: logics/viewControllers.rst
.. _`views`: logics/views

MainWindow class
----------------
Main class of the application. Initializes other classes. Public functions:

======================== ====================== ===============================================================================================
Name                      Args                  Description
======================== ====================== ===============================================================================================
CreateViews              \-                     Initializes views. The order of initialized views must mirror the values of view-related `enums`_ .
GetViewManager           `ViewManagerTypeEnum`_ Returns a view manager accordingly to provided enum value.
======================== ====================== ===============================================================================================

.. _`enums`: enums.rst
.. _`ViewManagerTypeEnum`: enums.rst

TurnAnalyzer class
------------------
Analyzes turns results. Singleton. Use **GetInstance** to retrieve it.

======================== ============================ ===============================================================================================
Name                      Args                        Description
======================== ============================ ===============================================================================================
GetInstance              \-                           Returns instance of this singleton.
CalculateTurn            `PlayerData`_, `PlayerData`_ Calculates results of the last turn using provided players data. Returns `TurnResultEnum`_ that 
                                                      indicates how the turn ended.
======================== ============================ ===============================================================================================

.. _`PlayerData`: data.rst
.. _`TurnResultEnum`: enums.rst

ViewCreator class
-----------------
Creates views for controllers.

======================== ============================ ===============================================================================================
Name                      Args                        Description
======================== ============================ ===============================================================================================
GetPerksView             `PlayersEnum`_, int, bool    Returns a new perk selection view for player of given ID(Players enum).
GetTurnsView             `PlayersEnum`_, int, bool    Returns a new turn view for player of given ID(Players enum).
GetGameModeSelectView    \-                           Returns new game mode selection view.
GetHostModeIniView       \-                           Returns new LAN host mode selection view.
GetJoinGameView          \-                           Returns new LAN game joining view.
GetLanModeSelectionView  \-                           Returns new LAN mode selection view.
GetMatchEndView          `TurnResultEnum`_            Returns a new match end view, dependant on passed argument.
======================== ============================ ===============================================================================================


.. _`PlayersEnum`: enums.rst

ViewManager class
-----------------
Used to switch through available views. Inherits from `QStackedWidget`_.

======================== ============================ ===============================================================================================
Name                      Args                        Description
======================== ============================ ===============================================================================================
AddViews                 QWidget[]                    Adds provided views to the manager.
ChangeView               int                          Changes currently shown view to the one under provided in the argument id. See views ids in `enums`_.
======================== ============================ ===============================================================================================

.. _`QStackedWidget`: https://www.tutorialspoint.com/pyqt/pyqt_qstackedwidget.htm
