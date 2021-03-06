.. _`chapter-views`:

Django base views for implementing your API
===========================================

.. automodule:: lizard_structure.views


Data source view
----------------

Base view for a :ref:`data source`.

.. autoclass:: lizard_structure.views.DataSourceView
   :members: get, our_name_and_version

   There is one method you always have to implement:

   .. automethod:: layer_trees

   If you want to return more information about ourselves than the default:

   .. automethod:: about_ourselves

   Normally, you should not have to modify or implement the other methods.


TODO: Layer tree view
---------------------

Base view for a :ref:`layer tree`.

.. autoclass:: lizard_structure.views.LayerTreeView
   :members:


TODO: Layer view
----------------

Base view for a :ref:`layer`.

.. autoclass:: lizard_structure.views.LayerView
   :members:


TODO: Feature view
------------------

Base view for a :ref:`feature`.

.. autoclass:: lizard_structure.views.FeatureView
   :members:
