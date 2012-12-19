Lizard-structure: how Lizard fits together
##########################################

Tagline of this app: **structure of Lizard, defined and documented in a REST
interface**.

`Lizard <http://lizard.org>`_ is a framework for showing water-related
information in a web interface. We build most of what's now Lizard in the
`Python <http://python.org>`_ web framework `Django
<http://djangoproject.com>`_. We're now separating the various bits and
pieces more formally with a `REST
<https://en.wikipedia.org/wiki/Representational_state_transfer>`_ web
API.

A REST API means you can tie in easier into Lizard with your own software
instead of buying into Lizard's whole Python and Django stack.

Lizard-structure provides the documentation on the API. It also provides base
view classes for Django to make it very easy to support the API with all the
existing Django Lizard apps. The **main goal** however is documentation.

Here is the table of contents:

.. toctree::
   :maxdepth: 2

   core
   views
   items
   project
