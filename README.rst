
|License badge|

==========================
Horizon Dashboard API Mask
==========================

Plugin replace IP and protocol in EndpointsTable

Usefull if you have OpenStack API behind proxies.

Reuired
-------

* Python 2.6 +
* Horizon Icehouse +

Installation
------------

.. code-block:: bash

	pip install horizon-api-mask

Required Configuration
----------------------

* add `api_filter` to INSTALLED_APPS tuple;
* add `api_filter.overrides` to `customization_module` key in HORIZON_CONFIG.

Optional Configuration
----------------------

* add `API_MASK_URL` key in DJANGO_CONFIG, default is socket.getfqdn()
* add `API_MASK_PROTOCOL` key in DJANGO_CONFIG, default is `https`

.. |License badge| image:: http://img.shields.io/badge/license-Apache%202.0-green.svg?style=flat