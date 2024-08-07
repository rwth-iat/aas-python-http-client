# swagger_client.SerializationAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_serialization_by_ids**](SerializationAPIApi.md#generate_serialization_by_ids) | **GET** /serialization | Returns an appropriate serialization based on the specified format (see SerializationFormat)

# **generate_serialization_by_ids**
> str generate_serialization_by_ids(aas_ids=aas_ids, submodel_ids=submodel_ids, include_concept_descriptions=include_concept_descriptions)

Returns an appropriate serialization based on the specified format (see SerializationFormat)

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.SerializationAPIApi()
aas_ids = [
    'aas_ids_example']  # list[str] | The Asset Administration Shells' unique ids (UTF8-BASE64-URL-encoded) (optional)
submodel_ids = ['submodel_ids_example']  # list[str] | The Submodels' unique ids (UTF8-BASE64-URL-encoded) (optional)
include_concept_descriptions = true  # bool | Include Concept Descriptions? (optional) (default to true)

try:
    # Returns an appropriate serialization based on the specified format (see SerializationFormat)
    api_response = api_instance.generate_serialization_by_ids(aas_ids=aas_ids, submodel_ids=submodel_ids,
                                                              include_concept_descriptions=include_concept_descriptions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SerializationAPIApi->generate_serialization_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_ids** | [**list[str]**](str.md)| The Asset Administration Shells&#x27; unique ids (UTF8-BASE64-URL-encoded) | [optional] 
 **submodel_ids** | [**list[str]**](str.md)| The Submodels&#x27; unique ids (UTF8-BASE64-URL-encoded) | [optional] 
 **include_concept_descriptions** | **bool**| Include Concept Descriptions? | [optional] [default to true]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/asset-administration-shell-package+xml, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

