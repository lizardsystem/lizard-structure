.. _`chapter-core`:

Introducing the four core Lizard concepts
#########################################

.. note::

   Warning, this is work in progress. Even though there currently are four
   levels, there's a big chance that something is missing. It is very likely
   that a "FilterFolder" or "FilterLayer" or something like that will be
   added.

There are four core concepts in Lizard's structure:

Data source

    Lizard can connect to many kinds of data. A :ref:`data source` provides
    such a connection.

Layer tree

    Within an :ref:`data source`, there will be one or more basic groups of
    data. Every group of data is what we call a :ref:`layer tree`.

Layer

    Every :ref:`layer tree` has multiple layers in some sort of
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


.. _`data source`:

Data source
===========

A main Lizard characteristic is that it can show data from many different
sources. (With "show" we can mean quite elaborate web interfaces, btw.) For
every data source, there is a separate Lizard Django application
(currently). One to read FEWS data from a database. Another to read it from a
JDBC coupling. One to link to geoserver WMS layers. Another to show river dike
calculations.

So in the end, if a Lizard website connects to you via the lizard-structure
API, Lizard connects with you as a data source.

You, as a data surce, are the starting point for Lizard to talk to you. You'll
give lizard a list of layer trees which it can display in its interface, for
instance.


.. _`layer tree`:

Layer tree
==========

A layer tree is a large-scale grouping of the data available in an :ref:`data
source`. Do not have too many of these. As an example: if your data source
provides water level measurements, a good layer tree level might be the water
board or municipality or whatever you have as top-level customer. So every
municipality becomes a :ref:`layer tree`.

The goal you need to keep in mind here is that a :ref:`layer tree` often
translates into a separate page in the Lizard web interface. If that is what
you want: fine. If not: you need to re-think what you're calling a layer tree.


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
