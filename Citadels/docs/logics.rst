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

.. _`logics/controllers`: logics/controllers.rst
.. _`logics/viewControllers`: logics/viewControllers.rst
.. _`logics/views/gameplay`: logics/views

MainWindow class
----------------
Main class of the application. Initializes other classes. Public functions:

======================== ===================== ===============================================================================================
Name                      Args                  Description
======================== ===================== ===============================================================================================
CreateViews              \-                    Initializes views. The order of initialized views must mirror the values of view-related `enums`_ .
======================== ===================== ===============================================================================================

.. _`enums`: enums.rst
