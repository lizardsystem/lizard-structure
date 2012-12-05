Introducing the four core Lizard concepts
#########################################

There are four core concepts in Lizard's structure:

Application

    Lizard can connect to a lot of data sources; an application provides such
    a connection. So :ref:`application` more or less equals "data source".

Project

    Within an :ref:`application`, there will be one or more basic groups of
    data. Every group of data is what we call a :ref:`project`.

Layer

    Every :ref:`project` has multiple layers in some sort of
    structure. A :ref:`layer` is most often a map layer, but it doesn't have
    to be.

Feature

    A :ref:`layer` consists of features. A map layer might show water
    level measurement points: every one of those is a :ref:`feature`.

.. note::

   There are four levels. No more. That's Lizard's structure! You could call
   it **Lizard's world view**. Most of what we encountered in the Lizard
   websites of the last couple of years fits this structure. And if you need
   something extra special, you can just create a regular Lizard Django
   application and you'll have all the freedom to do weird things that you can
   wish for.


.. _application:

Application
===========

Lizard is organized around applications. The main Lizard characteristic is
that it can show data from many different sources. (With "show" we can mean
quite elaborate web interfaces, btw.) For every data source, there is a
separate application. One to read FEWS data from a database. Another to read
it from a JDBC coupling. One to link to geoserver WMS layers. Another to show
river dike calculations.

So in the end, if a Lizard website connects to you via the lizard-structure
API, Lizard connects with you as an application.

You, as an application, are the starting point for Lizard to talk to
you. You'll give lizard a list of projects which it can display in its
interface, for instance.


.. _project:

Project
=======

A project is a large-scale grouping of the data available in an
:ref:`application`. Do not have too many of these. As an example: if your
application provides water level measurements, a good project level might be
the water board or municipality or whatever you have as top-level customer. So
every municipality becomes a :ref:`project`.

The goal you need to keep in mind here is that a :ref:`project` often
translates into a separate page in the Lizard web interface. If that is what
you want: fine. If not: you need to re-think what you're calling a project.


.. _layer:

Layer
=====

A layer is best understood as simply a map layer. One of the map layers you
place over a google or openstreetmap base map. It doesn't really matter
whether it is a WMS layer or geojson or even a simple non-map list of items:
for the concept you simply need to think "map layer" and you've got the
correct mental picture.


.. _feature:

Feature
=======

If a :ref:`layer` is basically a map layer, a :ref:`feature` is an item on
that map layer. A river, a dike segment, a water level measurement. A feature
is the lowest useful level of information.

The best way to think about a feature is of something that you can click on on
a map. You click it and you get a graph of the data. Or a table with more
information. Or a PDF.

And in case the :ref:`layer` wasn't a map layer but just a list of features,
it still holds true that a feature is something with a table, graph or PDF. In
this case it simply is one of the items in that list.
