Gameplay Package
================
Views that concern the match. Turns, perks selection, etc.

AftermatchView class
--------------------

View that shows the result of an match. Public functions:

================================ ==================================================== ===============================================================================
Name                             Args                                                 Description
================================ ==================================================== ===============================================================================
OnMatchEndConfirm                \-                                                   Called when the match has been concluded and the player left it. (As in, 
                                                                                      clicked "Leave" button to get back to menu)
                                                                                      during view ini or turn result.
RegisterOnMatchEndConfirmHandler Func()                                               Registers an event handler called by **OnMatchEndConfirm**.
================================ ==================================================== ===============================================================================


AwaitOtherPlayerView class
--------------------------
Stub of a view that was planned to be used in LAN mode. It would be shown when given player made their decision but the other hasn't done so yet.


PerkSelectionView
-----------------
View that allows the player to select their perks. Public functions:

================================ ==================================================== ===============================================================================
Name                             Args                                                 Description
================================ ==================================================== ===============================================================================
ResetState                       \-                                                   Resets the state of the view to first radio buttons being selected in their
                                                                                      groups.
RegisterPerkSelectionListener    Func(`OffensivePerkEnum`_, `DefensivePerkEnum`_)     
================================ ==================================================== ===============================================================================

.. _`OffensivePerkEnum`: ../../enums.rst
.. _`DefensivePerkEnum`: ../../enums.rst


TurnView class
--------------
View that shows UI for turns during matches between players. Public functions:

================================ ==================================================== ===============================================================================
Name                             Args                                                 Description
================================ ==================================================== ===============================================================================
CalculateFillValue               float                                                Checks how much of the bar shall be filled using provided percentage value, then
                                                                                      returns it.
RegisterOnActionConfirmed        Func(`OffensiveActionEnum`_, `DefensiveActionEnum`_) Registers handler called when the player confirms his selection of moves for
                                                                                      current turn.
SetMyHealthBarValue              float                                                Sets the health bar of current player to provided fill percentage.
SetEnemyHealthBarValue           float                                                Sets the health bar of current player's enemy to provided fill percentage.
ResetState                       \-                                                   Resets the view.
================================ ==================================================== ===============================================================================

.. _`OffensiveActionEnum`: ../../enums.rst
.. _`DefensiveActionEnum`: ../../enums.rst
