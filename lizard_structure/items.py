# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
"""
:mod:`lizard_structure.items` provides item definitions. An item definition is
a formal specification of what kinds of key/value pairs you can expect in a
JSON object (or Python dictionary) for such diverse items such as a layer, a
menu item, a feature, a data source.

Technically, an item is nothing but a Python class that returns a
dictionary. It is implemented as a class for the following reasons:

- To make sure you comply to the specification. No undefined keys, no missing
  mandatory keys.

- To allow for default values.

- To make sure we can generate always-correct always-up-to-date documentation.


"""
from __future__ import unicode_literals

DEFAULT_HEADING_LEVEL = 1


class HeadingItem(object):
    """Wrapper/interface for heading objects in a Project/menu."""
    fixed = {'menu_type': 'heading'}
    defaults = {'name': None,
                'description': None,
                'heading_level': DEFAULT_HEADING_LEVEL,
                'extra_data': None,
                'klass': None}

    def __init__(self, **kwargs):
        for kwarg in kwargs:
            if kwarg not in self.defaults:
                raise TypeError(
                    "__init__() got an unexpected keyword argument {kwarg}",
                    kwarg=kwarg)
        self._dict = {}
        self._dict.update(self.fixed)
        self._dict.update(self.defaults)
        self._dict.update(kwargs)

    def to_api(self):
        return dict([(k, v) for (k, v) in self._dict.items()
                     if v is not None])
