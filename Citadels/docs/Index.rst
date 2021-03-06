Citadels Docs
=============

Foreword
-------
Documentation files are grouped accordingly to packages in the project. Given file describes all classes that the package assigned to it contains. __init__.py files are ommitted since these are empty.
List of packages can be found below:

=================================== =========================================================
Name                                Description
=================================== =========================================================
`data`_                             Label constants and data structures.
`enums`_                            Enums used in the project
`logics`_                           Controllers and views packages. Main, TurnAnalyzer 
                                    and ViewManager classes.
`logics/controllers`_               Gameplay controllers - the actual game calculations.
`logics/viewControllers`_           Views controllers - initialization of views, data passing to controllers.
`logics/views/gameplay`_            Views used during match.
`logics/views/gameplaySelection`_   Views used in selection of gameplay type.
=================================== =========================================================

.. _`data`: data.rst
.. _`enums`: enums.rst
.. _`logics`: logics.rst
.. _`logics/controllers`: logics/controllers.rst
.. _`logics/viewControllers`: logics/viewControllers.rst
.. _`logics/views/gameplay`: logics/views/gameplay.rst
.. _`logics/views/gameplaySelection`: logics/views/gameplaySelection.rst
