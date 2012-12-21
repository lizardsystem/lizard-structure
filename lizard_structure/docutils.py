# (c) Nelen & Schuurmans.  LGPL licensed, see LICENSE.rst.
"""
:mod:`lizard_structure.docutils` provides the docutil metaclass to
automatically document the items.

"""

EXPLANATIONS = {
    'name': 'Name of the item',
    'description': """Description of the item, perhaps shown when hovering
    above it. HTML tags are allowed so you can add links or definition links.
"""}


def attrs_docstring(attr_name, attr, docstring):
    """Generate part of a docstring based on the attribute name."""

    values = {'fixed': 'Fixed values:',
              'defaults': 'Available values'}
    explanation_option = {'fixed': '',
                          'defaults': 'Optional.'}
    explanation_repr = {'fixed': ' (**Fixed value**: {v})',
                        'defaults': ' (**Default value**: {v}).'}

    docstring.append(values[attr_name])
    docstring.append('')
    for k, v in attr.items():
        docstring.append(k)
        explanation = EXPLANATIONS.get(k)
        if explanation is None:
            explanation = explanation_option[attr_name]
        explanation += explanation_repr[attr_name].format(v=repr(v))
        docstring.append(
            '    {explanation}'.format(explanation=explanation))
        docstring.append('')


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

    for item in ('fixed', 'defaults'):
        if item in attrs:
            attrs_docstring(item, attrs[item], docstring)

    attrs['__doc__'] += '\n'.join(docstring)
    return type(name, bases, attrs)
