Helper functions and base classes
=================================

Both :mod:`lizard_structure.items` and :mod:`lizard_structure.views` have
helper functions and base classes. We document them here to keep the view
and the item definitions documentation clean.


Helper base view
-----------------

.. autoclass:: lizard_structure.views.BaseAPIView
   :members:


Base class for building item definitions
----------------------------------------

.. autoclass:: lizard_structure.items.BaseItem
   :members:


Helper function for generating item definition documentation
------------------------------------------------------------

.. autofunction:: lizard_structure.items.generate_docstring
