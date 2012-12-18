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
    menu_type = 'heading'

    def __init__(self,
                 name=None,
                 description=None,
                 # edit_link=None,
                 heading_level=None,
                 extra_data=None,
                 klass=None):
        self.name = name
        self.description = description
        self.heading_level = heading_level or DEFAULT_HEADING_LEVEL
        # self.edit_link = edit_link
        self.extra_data = extra_data
        self.klass = klass

    def to_api(self):
        result = {}
        for attr in ['name',
                     'description',
                     'heading_level',
                     # 'extra_data',
                     # 'klass',
                     'menu_type']:
            value = getattr(self, attr)
            if value is None:
                continue
            result[attr] = value
        return result
