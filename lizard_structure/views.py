# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
"""
:mod:`lizard_structure.views` provides base views for each of the core
concepts defined in :ref:`chapter-core`. The basic premise is that
lizard-structure only *shows* a data source's structure. There are no edit
actions, so no POST/PUT/DELETE: only GET.

Every view has a doctring that can mostly be used as-is by the subclasses that
implement the actual functionality. The docstring is rendered by Django REST
framework in the html API interface, so the view's docstring is the most
important information your API user is going to see. The base views' docstring
must be really clear and concise!

You normally do not have to implement any ``.get()`` method on a view, that is
all taken care of. Every view tells you which properties you have to fill in
to get the base view working with your data.

.. note::

   Properties look like attributes on a class, but they're methods with a
   ``@property`` decorator. You can also just add an attribute if you
   want. See :func:`python:property`.

"""
from __future__ import unicode_literals
import inspect

# from django.core.urlresolvers import reverse
# from django.utils.translation import ugettext as _
from django.contrib.admindocs.utils import trim_docstring
from django.utils.safestring import mark_safe
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import docutils
import pkginfo


class BaseAPIView(GenericAPIView):
    """Base view that provides custom docstring rendering.

    You should not have to subclass from :class:`BaseAPIView` yourself, it is
    only used as a base for the other ones. The custom docstring handling
    happens by overwriting the :meth:`get_description` expected by Django Rest
    framework.
    """

    def get_description(self, html=False):
        """Return the view's docstring as a description.

        This method is a customization of Django REST framework's. There are
        two changes:

        - Our parent's docstring is used if we don't have one ourselves. This
          makes it easy to use a base class with proper documentation on which
          items to expect. The documentation is propagated to every API that
          uses the base class.

        - The docstring is parsed with restructuredtext syntax instead of
          markdown (markdown is preferred by Django REST framework).

        """
        description = self.__doc__
        if description is None:
            # Trick to get our parent's docstring as a fallback if we don't
            # have one ourselves. From
            # http://stackoverflow.com/a/13937525/27401 .
            try:
                description = next(
                    cls.__doc__ for cls in inspect.getmro(type(self))
                    if cls.__doc__ is not None)
            except StopIteration:
                pass

        description = trim_docstring(description)
        if html:
            parts = docutils.core.publish_parts(description,
                                                writer_name='html')
            return mark_safe(parts['fragment'])
        return description


class DataSourceView(BaseAPIView):
    """
    Information about the data source itself and its list of projects.

    Use this to discover the projects you can show in your user interface. The
    result is a dictionary with the following items:

    about_ourselves
        Metadata about ourselves, like the software version that generated
        it. Do not depend on the actual items in here, just display them when
        desired as background information.

    projects
        The list of available projects. A project is a collection of
        layers you can show on a map or in an overview.

    """

    @property
    def projects(self):
        """Return list of projects.

        Overwrite this property in your subclass and return a list of **TODO**
        ProjectInfo dictionaries you create from whatever constitutes a
        project in your own models. To give you an idea, here are some example
        projects:

        - Categories in lizard-wms/lizard-maptree.

        - FEWS connections in lizard-fewsjdbc.

        """
        return []

    @property
    def our_name_and_version(self):
        """Return name version number of our package.

        The default should be OK in most cases.
        """
        our_module = self.__module__
        package = our_module.split('.')[0]
        version = pkginfo.installed.Installed(our_module).version
        return '{package} ({version})'.format(package=package,
                                              version=version)

    @property
    def about_ourselves(self):
        """Return metadata about ourselves.

        By default, return our name and version as the generator of the data
        source.
        """
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
