
# Horizon API Mask

Plugin replace IP and protocol in EndpointsTable

* add `api_filter` to INSTALLED_APPS tuple;
* add `api_filter.overrides` to `customization_module` key in HORIZON_CONFIG.
* add `API_MASK_URL' key in DJANGO_CONFIG, default is socket.getfqdn()
* add `API_MASK_PROTOCOL` key in DJANGO_CONFIG, default is `https`