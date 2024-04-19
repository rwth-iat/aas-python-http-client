# swagger_client.DescriptionAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_description**](DescriptionAPIApi.md#get_description) | **GET** /description | Returns the self-describing information of a network resource (ServiceDescription)

# **get_description**
> ServiceDescription get_description()

Returns the self-describing information of a network resource (ServiceDescription)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DescriptionAPIApi()

try:
    # Returns the self-describing information of a network resource (ServiceDescription)
    api_response = api_instance.get_description()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DescriptionAPIApi->get_description: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceDescription**](ServiceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

