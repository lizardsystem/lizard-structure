.. _`chapter-restapi`


The Lizard Portal API
#####################

This describes the resources that make up the Lizard API v1.

Portal
=======

Get a Portal List
-------------------

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

  GET /api/v1/portals/:portalid

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


Application Screen
====================

Get a list of Application Screens
----------------------------------

::

  GET /api/v1/portals/:portalid/appscreens/

**Response** ::

  Status: 200 OK

.. code-block:: javascript

  {
    "data": [
      {
        "id": "{app id}",
		"name": "{app name}",
		"description": "{app description}",
		"url": "/api/v1/portal/{app id}",
		"icon": "/api/v1/icon/{icon id}",
		"actionType": "lizard.app.xxxxx"
	  },
      {
	    "id": '{app id2}",
		"name": "{app name2}",
		"description": "{app description}",
		"url": "/api/v1/portal/{app id2}",
		"icon": "/api/v1/icon/{icon id}",
		"actionType": "linkTo"
	  }
    ],
	"count": 1
   }

Get a Application Screen
---------------------------

::

  GET /api/v1/portals/:portalid/appscreens/:appscreenid

**Response** ::

  Status: 200 OK

.. code-block:: javascript

  {
    "data": {
      "id": "{app id}",
	  "name": "{app name}",
	  "description": "{app description}",
	  "url": "/api/v1/portal/{app id}",
	  "icon": "/api/v1/icon/{icon id}",
	  "actionType": "lizard.app.xxxxx"
     }
   }

Applications
===============

Get a list of Applications
----------------------------

.. note::

  This seems to be the same as the Application Screen.

::

  GET /api/v1/apps

**Response** ::

  Status: 200 OK

.. code-block:: javascript


  {
    "data": [
      {
        "id": "{app id}",
        "name": "{app name}",
        "description": "{app description}",
        "url": "/api/v1/apps/{app id}",
        "icon": "/api/v1/icons/{icon id}",
        "actionType": "{lizard.app.xxxxx}",
      },
    ],
    "count": 1
  }



The Lizard Datasource REST API
###################################
