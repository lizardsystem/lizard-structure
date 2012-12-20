.. _`chapter-restapi`


The Lizard API
##############

This describes the resources that make up the Lizard API v1.


The Lizard Portal REST API
====================================

Get a Portal List
--------------------

::

  GET /api/v1/portals

**Response** ::

  Status: 200 OK

.. code-block:: javascript

  {
    data: [
      {
        "id" : "{portal id}",
        "name": "{portal name}",
        "description": "{portal description}",
        "url": "/api/v1/portals/{portal id}"
      }
    ]
    count: 1
  }

Get a Portal
-------------------

::

  GET /api/v2/portals/:portalid

**Response** ::

  Status: 200 OK

.. code-block:: javascript

  {
    data: {
      "id": "{portal id}"
      "name": "{portal name}"
      "description": "{portal description}",
      "icon": "/api/v1/icons/4"
	  "appScreenUrl": "/api/v1/portals/{portalid}/appScreen/"
      "links": [
         {
           "name": "{link name}",
           "url": "{link url}"
         },
      ],
    }
  }


The Lizard Datasource REST API
===================================
