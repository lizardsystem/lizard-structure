# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
"""
The basic premise is that lizard-structure only *shows* a data source's
structure. There are no edit actions, so no POST/PUT/DELETE: only GET.

There are several basic ways to deal with naming the views. Especially when
you also want POST/PUT/DELETE, having both ``ObjectList`` and ``ObjectDetail``
makes sense. But we don't need that. What's most interesting are the lists,
these are also often the most effective. You don't want to have to grab
handfuls of URLs before you can render a page. You want the most useful data
right away. So on an :ref:`data source` page, you want a list of projects. On
a :ref:`project` page, a list of layers. And so on.

We deemed it more useful to call the view with the list of projects the data
source view, though. A data source *is* a list of projects, so it makes sense
that way.

But: a project also has information on itself, as has a project, etc.

"""
from __future__ import unicode_literals

# from django.core.urlresolvers import reverse
# from django.utils.translation import ugettext as _
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
import pkginfo


class DataSourceView(GenericAPIView):
    """
    Information about the data source itself and its list of projects.

    Use this to discover the projects you can show in your user interface.
    """

    @property
    def projects(self):
        """Return maptree categories.

        Maptree categories are usable as root objects of lizard pages.
        """
        return []

    @property
    def our_name_and_version(self):
        """Return name version number of our package.
        """
        our_module = self.__module__
        package = our_module.split('.')[0]
        version = pkginfo.installed.Installed(our_module).version
        return '{package} ({version})'.format(package=package,
                                              version=version)

    @property
    def about_ourselves(self):
        """Return metadata about ourselves."""
        return {'generator': self.our_name_and_version}

    def get(self, response, format=None):
        result = {}
        result['about_ourselves'] = self.about_ourselves
        result['projects'] = self.projects
        return Response(result)


class ProjectView(GenericAPIView):
    """
    Information about the project and its list of layers.
    """
    # Representation: some sort of sidebar structure/tree with menuitems or
    # workspaceacceptables.
    pass


class LayerView(GenericAPIView):
    """
    Information about the layer and its list of features.
    """
    # Representations: geojson, WMS, etc.
    pass


class FeatureView(GenericAPIView):
    """
    Information about the feature and most importantly its representations.
    """
    # Representations! flot, png graph, html, csv, etc.
    pass
