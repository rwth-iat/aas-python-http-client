# swagger_client.SubmodelRegistryAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_submodel_descriptor_by_id**](SubmodelRegistryAPIApi.md#delete_submodel_descriptor_by_id) | **DELETE** /submodel-descriptors/{submodelIdentifier} | Deletes a Submodel Descriptor, i.e. de-registers a submodel
[**get_all_submodel_descriptors**](SubmodelRegistryAPIApi.md#get_all_submodel_descriptors) | **GET** /submodel-descriptors | Returns all Submodel Descriptors
[**get_submodel_descriptor_by_id**](SubmodelRegistryAPIApi.md#get_submodel_descriptor_by_id) | **GET** /submodel-descriptors/{submodelIdentifier} | Returns a specific Submodel Descriptor
[**post_submodel_descriptor**](SubmodelRegistryAPIApi.md#post_submodel_descriptor) | **POST** /submodel-descriptors | Creates a new Submodel Descriptor, i.e. registers a submodel
[**put_submodel_descriptor_by_id**](SubmodelRegistryAPIApi.md#put_submodel_descriptor_by_id) | **PUT** /submodel-descriptors/{submodelIdentifier} | Updates an existing Submodel Descriptor

# **delete_submodel_descriptor_by_id**
> delete_submodel_descriptor_by_id(submodel_identifier)

Deletes a Submodel Descriptor, i.e. de-registers a submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRegistryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes a Submodel Descriptor, i.e. de-registers a submodel
    api_instance.delete_submodel_descriptor_by_id(submodel_identifier)
except ApiException as e:
    print("Exception when calling SubmodelRegistryAPIApi->delete_submodel_descriptor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_descriptors**
> GetSubmodelDescriptorsResult get_all_submodel_descriptors(limit=limit, cursor=cursor)

Returns all Submodel Descriptors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRegistryAPIApi()
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns all Submodel Descriptors
    api_response = api_instance.get_all_submodel_descriptors(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRegistryAPIApi->get_all_submodel_descriptors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 

### Return type

[**GetSubmodelDescriptorsResult**](GetSubmodelDescriptorsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_descriptor_by_id**
> SubmodelDescriptor get_submodel_descriptor_by_id(submodel_identifier)

Returns a specific Submodel Descriptor

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRegistryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns a specific Submodel Descriptor
    api_response = api_instance.get_submodel_descriptor_by_id(submodel_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRegistryAPIApi->get_submodel_descriptor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**SubmodelDescriptor**](SubmodelDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submodel_descriptor**
> SubmodelDescriptor post_submodel_descriptor(body)

Creates a new Submodel Descriptor, i.e. registers a submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRegistryAPIApi()
body = swagger_client.SubmodelDescriptor() # SubmodelDescriptor | Submodel Descriptor object

try:
    # Creates a new Submodel Descriptor, i.e. registers a submodel
    api_response = api_instance.post_submodel_descriptor(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRegistryAPIApi->post_submodel_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelDescriptor**](SubmodelDescriptor.md)| Submodel Descriptor object | 

### Return type

[**SubmodelDescriptor**](SubmodelDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_submodel_descriptor_by_id**
> put_submodel_descriptor_by_id(body, submodel_identifier)

Updates an existing Submodel Descriptor

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRegistryAPIApi()
body = swagger_client.SubmodelDescriptor() # SubmodelDescriptor | Submodel Descriptor object
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Updates an existing Submodel Descriptor
    api_instance.put_submodel_descriptor_by_id(body, submodel_identifier)
except ApiException as e:
    print("Exception when calling SubmodelRegistryAPIApi->put_submodel_descriptor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelDescriptor**](SubmodelDescriptor.md)| Submodel Descriptor object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

