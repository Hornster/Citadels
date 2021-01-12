Enums package
=============
All enums in this package inherit from **IntEnum**.

Views enums
-----------
These enums are used to switch between given views in the game and are dividing the views into categories. Values should be reflected in the order of 
view initialization in the `MainWindow`_ class, in the **CreateViews** funciton. First view must start with 0 and there cannot be a hole between any two
neighbouring views (i.e. for 13 views, values should range from 0 to 12 with step of 1: 0, 1, 2, ..., 12).

========================================= =========== ===============================================================================================
Name                                      Value range Description
========================================= =========== ===============================================================================================
ViewTypeGameplaySelection                 [0-3]       Available gameplay selection views (menu).
ViewTypeLocal                             [4-7]       Available local game views (hot seat mode, shown during gameplay).
MatchEnds                                 [8-10]      Types of gameplay ends that may occur.
ViewTypeLan                               [11-17]     Available LAN game views (shown during gameplay).
========================================= =========== ===============================================================================================

.. _`MainWindow`: logics.rst

ViewManagerTypeEnum
----------------
Enum that represents all view managers available in game.

Perk choices enums
------------------
Group of enums used to define types of perks. Values: [0-2]

========================================= ===============================================================================================
Name                                      Description
========================================= ===============================================================================================
OffensivePerkEnum                         IDs of offensive perks.
DefensivePerkEnum                         IDs of defensive perks.
========================================= ===============================================================================================

Action choices enums
--------------------
Group of enums used to define types of actions during a match. Values: [0-2]

========================================= ===============================================================================================
Name                                      Description
========================================= ===============================================================================================
OffensiveActionEnum                       IDs of offensive actions.
DefensiveActionEnum                       IDs of defensive actions.
========================================= ===============================================================================================

TurnResultEnum
--------------
Enum that represents possible endings of a match. Values: [0-3].

LAN messages enums
-----------------
These enums define the headers of planned messages that server and client can send during LAN gameplay.

========================================= ===============================================================================================
Name                                      Description
========================================= ===============================================================================================
ServerMsgType                             Types of messages sent by the server to the client.
ClientMsgType                             Types of messages sent by the client to the server.
========================================= ===============================================================================================
