# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.

from django.test import TestCase
from lizard_structure import items


class HeadingItemTest(TestCase):

    def test_basic_case(self):
        heading = items.HeadingItem(name='Test heading')
        self.assertEquals(heading.to_api()['name'], 'Test heading')

    def test_no_unspecified_keys_in_dict(self):
        # We should be as empty as possible.
        heading = items.HeadingItem(name='Test heading')
        self.assertFalse('description' in heading.to_api())

    def test_default_values(self):
        heading = items.HeadingItem(name='Test heading')
        self.assertEquals(heading.to_api()['heading_level'], 1)

    def test_overwritten_default_values(self):
        heading = items.HeadingItem(name='Test heading',
                                    heading_level=42)
        self.assertEquals(heading.to_api()['heading_level'], 42)

    def test_fixed_values(self):
        heading = items.HeadingItem(name='Test heading')
        self.assertEquals(heading.to_api()['menu_type'], 'heading')

    def test_unmodifiable_fixed_values(self):
        self.assertRaises(TypeError, items.HeadingItem, menu_type='reinout')

    def test_fail_on_unknown_arguments(self):
        self.assertRaises(TypeError, items.HeadingItem, reinout='great')
        # TypeError: __init__() got an unexpected keyword argument 'reinout'

    def test_has_generated_docstring(self):
        self.assertTrue(items.HeadingItem.__doc__)
