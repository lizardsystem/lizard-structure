Changelog of lizard-structure
===================================================


0.2 (unreleased)
----------------

- Added "item definitions" to properly document and specify items such as menu
  headers and projects. Their end result is a dictionary that will be returned
  as json by the API.

- Added lots of documentation, including documentation generated from the
  docstrings. The docstring documentation is carefully managed so that the
  documentation as a whole remains clear and logical to read.

- Renamed "application" to "data source" as "application" looks too much like
  "Django application". Inside Lizard, the icons in lizard-ui's interface are
  also called "application icons", so we don't use this overloaded term here.

- Using version from ``setup.py`` in the sphinx documentation.


0.1 (2012-12-05)
----------------

- Documented the four core Lizard concepts. [reinout]

- Set up documentation generation at https://lizard-structure.readthedocs.org/
  . [reinout]

- Set up testing on travis:
  https://travis-ci.org/lizardsystem/lizard-structure . [reinout]

- Removed lizard-ui dependency. [reinout]

- Initial project structure created with nensskel 1.30.dev0. [reinout]
