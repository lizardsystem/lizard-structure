# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
"""
:mod:`lizard_structure.items` provides item definitions. An item definition is
a formal specification of what kinds of key/value pairs you can expect in a
JSON object (or Python dictionary) for such diverse items such as a layer, a
menu item, a feature, a data source.

Technically, an item definition is nothing but a Python class that returns a
dictionary. It is implemented as a class for the following reasons:

- To make sure you comply to the specification. No undefined keys, no missing
  mandatory keys.

- To allow for default values.

- To make sure we can generate always-correct always-up-to-date documentation.


"""
from __future__ import unicode_literals

DEFAULT_HEADING_LEVEL = 1
EXPLANATIONS = {
    'name': 'Name of the item',
    'description': """Description of the item, perhaps shown when hovering
    above it. HTML tags are allowed so you can add links or definition links.
""",
    }


class BaseItem(object):
    """Base class for the other items.

    Flexible implementation so that we only have to specify the fixed and the
    default values (as dictionaries).

    - Fixed values cannot be set with a keyword argument.

    - Default arguments (``None`` is fine as value, btw) can be set using
      keyword arguments, otherwise they get their default values.

    - Keys with ``None`` values are omitted from the resulting dictionary
      returned by :meth:`to_api`.

    """
    fixed = {}
    defaults = {}

    def __init__(self, **kwargs):
        """Set up the item's internal dictionary.

        Keyword arguments can override default values. Only keys present in
        :attr:`defaults` are allowed as keyword arguments. You cannot add your
        own and you cannot override keys in :attr:`fixed`.

        """
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
        """Return our internal dictionary, but strip it of None values first.
        """
        return dict([(k, v) for (k, v) in self._dict.items()
                     if v is not None])


def generate_docstring(name, bases, attrs):
    """Generate a docstring based on the class's defaults/fixed attributes.

    Use this function as a metaclass by adding ``__metaclass__ =
    generate_docstring`` to every individual subclass of :class:`BaseItem`.
    """
    if not '__doc__' in attrs:
        plural = name.lower()[:-4] + 's'
        attrs['__doc__'] = "Item definition for {}".format(plural)
    docstring = []
    docstring.append('\n\n')
    if 'fixed' in attrs:
        docstring.append('Fixed values:')
        docstring.append('')
        for k, v in attrs['fixed'].items():
            docstring.append(k)
            explanation=EXPLANATIONS.get(k)
            if explanation is None:
                explanation = ''
            explanation += ' (**Fixed value**: {v}).'.format(
                    v=repr(v))
            docstring.append(
            '    {explanation}'.format(explanation=explanation))
            docstring.append('')
    if 'defaults' in attrs:
        docstring.append('Available values:')
        docstring.append('')
        for k, v in attrs['defaults'].items():
            docstring.append(k)
            explanation=EXPLANATIONS.get(k)
            if explanation is None:
                explanation = 'Optional.'
                # TODO: perhaps raise an exception? Force documentation?
            if v is not None:
                explanation += ' (**Default value**: {v}).'.format(
                    v=repr(v))
            docstring.append(
            '    {explanation}'.format(explanation=explanation))
            docstring.append('')

    attrs['__doc__'] += '\n'.join(docstring)
    return type(name, bases, attrs)


class LayerTreeItem(BaseItem):
    __metaclass__ = generate_docstring
    defaults = {'name': None,
                'description': None,
                'url': None,
                }


class HeadingItem(BaseItem):
    """Wrapper/interface for heading objects in a LayerTree/menu."""
    __metaclass__ = generate_docstring
    fixed = {'menu_type': 'heading'}
    defaults = {'name': None,
                'description': None,
                'heading_level': DEFAULT_HEADING_LEVEL,
                'extra_data': None,
                'klass': None,
                }


class LayerItem(BaseItem):
    """Wrapper/interface for layer/acceptable objects in a LayerTree/menu."""
    __metaclass__ = generate_docstring
    fixed = {'menu_type': 'workspace_acceptable'}
    defaults = {'name': None,
                'description': None,
                'wms_url': None,
                'wms_params': None,
                'wms_options': None,
                }
