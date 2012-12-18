Django base views for implementing your API
===========================================

.. automodule:: lizard_structure.views


Data source view
----------------


.. autoclass:: lizard_structure.views.DataSourceView
   :members: get, our_name_and_version

   There is one method you always have to implement:

   .. automethod:: projects

   If you want to return more information about ourselves than the default:

   .. automethod:: about_ourselves

   Normally, you should not have to modify or implement the other methods.



Helper base view
-----------------

.. autoclass:: lizard_structure.views.BaseAPIView
   :members:
