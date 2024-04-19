# swagger_client.SubmodelAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_by_path**](SubmodelAPIApi.md#delete_file_by_path) | **DELETE** /submodel/submodel-elements/{idShortPath}/attachment | Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
[**delete_submodel_element_by_path**](SubmodelAPIApi.md#delete_submodel_element_by_path) | **DELETE** /submodel/submodel-elements/{idShortPath} | Deletes a submodel element at a specified path within the submodel elements hierarchy
[**get_all_submodel_elements**](SubmodelAPIApi.md#get_all_submodel_elements) | **GET** /submodel/submodel-elements | Returns all submodel elements including their hierarchy
[**get_all_submodel_elements_metadata**](SubmodelAPIApi.md#get_all_submodel_elements_metadata) | **GET** /submodel/submodel-elements/$metadata | Returns the metadata attributes of all submodel elements including their hierarchy
[**get_all_submodel_elements_path**](SubmodelAPIApi.md#get_all_submodel_elements_path) | **GET** /submodel/submodel-elements/$path | Returns all submodel elements including their hierarchy in the Path notation
[**get_all_submodel_elements_reference**](SubmodelAPIApi.md#get_all_submodel_elements_reference) | **GET** /submodel/submodel-elements/$reference | Returns the References of all submodel elements
[**get_all_submodel_elements_value_only**](SubmodelAPIApi.md#get_all_submodel_elements_value_only) | **GET** /submodel/submodel-elements/$value | Returns all submodel elements including their hierarchy in the ValueOnly representation
[**get_file_by_path**](SubmodelAPIApi.md#get_file_by_path) | **GET** /submodel/submodel-elements/{idShortPath}/attachment | Downloads file content from a specific submodel element from the Submodel at a specified path
[**get_operation_async_result**](SubmodelAPIApi.md#get_operation_async_result) | **GET** /submodel/submodel-elements/{idShortPath}/operation-results/{handleId} | Returns the Operation result of an asynchronous invoked Operation
[**get_operation_async_result_value_only**](SubmodelAPIApi.md#get_operation_async_result_value_only) | **GET** /submodel/submodel-elements/{idShortPath}/operation-results/{handleId}/$value | Returns the value of the Operation result of an asynchronous invoked Operation
[**get_operation_async_status**](SubmodelAPIApi.md#get_operation_async_status) | **GET** /submodel/submodel-elements/{idShortPath}/operation-status/{handleId} | Returns the Operation status of an asynchronous invoked Operation
[**get_submodel**](SubmodelAPIApi.md#get_submodel) | **GET** /submodel | Returns the Submodel
[**get_submodel_element_by_path**](SubmodelAPIApi.md#get_submodel_element_by_path) | **GET** /submodel/submodel-elements/{idShortPath} | Returns a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_metadata**](SubmodelAPIApi.md#get_submodel_element_by_path_metadata) | **GET** /submodel/submodel-elements/{idShortPath}/$metadata | Returns the matadata attributes of a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_path**](SubmodelAPIApi.md#get_submodel_element_by_path_path) | **GET** /submodel/submodel-elements/{idShortPath}/$path | Returns a specific submodel element from the Submodel at a specified path in the Path notation
[**get_submodel_element_by_path_reference**](SubmodelAPIApi.md#get_submodel_element_by_path_reference) | **GET** /submodel/submodel-elements/{idShortPath}/$reference | Returns the Referene of a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_value_only**](SubmodelAPIApi.md#get_submodel_element_by_path_value_only) | **GET** /submodel/submodel-elements/{idShortPath}/$value | Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
[**get_submodel_metadata**](SubmodelAPIApi.md#get_submodel_metadata) | **GET** /submodel/$metadata | Returns the metadata attributes of a specific Submodel
[**get_submodel_path**](SubmodelAPIApi.md#get_submodel_path) | **GET** /submodel/$path | Returns the Submodel in the Path notation
[**get_submodel_reference**](SubmodelAPIApi.md#get_submodel_reference) | **GET** /submodel/$reference | Returns the Reference of the Submodel
[**get_submodel_value_only**](SubmodelAPIApi.md#get_submodel_value_only) | **GET** /submodel/$value | Returns the Submodel in the ValueOnly representation
[**invoke_operation**](SubmodelAPIApi.md#invoke_operation) | **POST** /submodel/submodel-elements/{idShortPath}/invoke | Synchronously invokes an Operation at a specified path
[**invoke_operation_async**](SubmodelAPIApi.md#invoke_operation_async) | **POST** /submodel/submodel-elements/{idShortPath}/invoke-async | Asynchronously invokes an Operation at a specified path
[**invoke_operation_async_value_only**](SubmodelAPIApi.md#invoke_operation_async_value_only) | **POST** /submodel/submodel-elements/{idShortPath}/invoke-async/$value | Asynchronously invokes an Operation at a specified path
[**invoke_operation_sync_value_only**](SubmodelAPIApi.md#invoke_operation_sync_value_only) | **POST** /submodel/submodel-elements/{idShortPath}/invoke/$value | Synchronously invokes an Operation at a specified path
[**patch_submodel**](SubmodelAPIApi.md#patch_submodel) | **PATCH** /submodel | Updates the Submodel
[**patch_submodel_element_by_path**](SubmodelAPIApi.md#patch_submodel_element_by_path) | **PATCH** /submodel/submodel-elements/{idShortPath} | Updates an existing SubmodelElement
[**patch_submodel_element_by_path_metadata**](SubmodelAPIApi.md#patch_submodel_element_by_path_metadata) | **PATCH** /submodel/submodel-elements/{idShortPath}/$metadata | Updates the metadata attributes an existing SubmodelElement
[**patch_submodel_element_by_path_value_only**](SubmodelAPIApi.md#patch_submodel_element_by_path_value_only) | **PATCH** /submodel/submodel-elements/{idShortPath}/$value | Updates the value of an existing SubmodelElement
[**patch_submodel_metadata**](SubmodelAPIApi.md#patch_submodel_metadata) | **PATCH** /submodel/$metadata | Updates the metadata attributes of the Submodel
[**patch_submodel_value_only**](SubmodelAPIApi.md#patch_submodel_value_only) | **PATCH** /submodel/$value | Updates the values of the Submodel
[**post_submodel_element**](SubmodelAPIApi.md#post_submodel_element) | **POST** /submodel/submodel-elements | Creates a new submodel element
[**post_submodel_element_by_path**](SubmodelAPIApi.md#post_submodel_element_by_path) | **POST** /submodel/submodel-elements/{idShortPath} | Creates a new submodel element at a specified path within submodel elements hierarchy
[**put_file_by_path**](SubmodelAPIApi.md#put_file_by_path) | **PUT** /submodel/submodel-elements/{idShortPath}/attachment | Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
[**put_submodel**](SubmodelAPIApi.md#put_submodel) | **PUT** /submodel | Updates the Submodel
[**put_submodel_element_by_path**](SubmodelAPIApi.md#put_submodel_element_by_path) | **PUT** /submodel/submodel-elements/{idShortPath} | Updates an existing submodel element at a specified path within submodel elements hierarchy

# **delete_file_by_path**
> delete_file_by_path(id_short_path)

Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.delete_file_by_path(id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->delete_file_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_submodel_element_by_path**
> delete_submodel_element_by_path(id_short_path)

Deletes a submodel element at a specified path within the submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Deletes a submodel element at a specified path within the submodel elements hierarchy
    api_instance.delete_submodel_element_by_path(id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->delete_submodel_element_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_elements**
> GetSubmodelElementsResult get_all_submodel_elements(limit=limit, cursor=cursor, level=level, extent=extent)

Returns all submodel elements including their hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements(limit=limit, cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_all_submodel_elements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**GetSubmodelElementsResult**](GetSubmodelElementsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_elements_metadata**
> GetSubmodelElementsMetadataResult get_all_submodel_elements_metadata(limit=limit, cursor=cursor, level=level)

Returns the metadata attributes of all submodel elements including their hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the metadata attributes of all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_metadata(limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_all_submodel_elements_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**GetSubmodelElementsMetadataResult**](GetSubmodelElementsMetadataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_elements_path**
> GetPathItemsResult get_all_submodel_elements_path(limit=limit, cursor=cursor, level=level)

Returns all submodel elements including their hierarchy in the Path notation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns all submodel elements including their hierarchy in the Path notation
    api_response = api_instance.get_all_submodel_elements_path(limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_all_submodel_elements_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**GetPathItemsResult**](GetPathItemsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_elements_reference**
> GetReferencesResult get_all_submodel_elements_reference(limit=limit, cursor=cursor, level=level)

Returns the References of all submodel elements

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the References of all submodel elements
    api_response = api_instance.get_all_submodel_elements_reference(limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_all_submodel_elements_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

[**GetReferencesResult**](GetReferencesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_elements_value_only**
> GetSubmodelElementsValueResult get_all_submodel_elements_value_only(limit=limit, cursor=cursor, level=level, extent=extent)

Returns all submodel elements including their hierarchy in the ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all submodel elements including their hierarchy in the ValueOnly representation
    api_response = api_instance.get_all_submodel_elements_value_only(limit=limit, cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_all_submodel_elements_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**GetSubmodelElementsValueResult**](GetSubmodelElementsValueResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_by_path**
> str get_file_by_path(id_short_path)

Downloads file content from a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Downloads file content from a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_file_by_path(id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_file_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_async_result**
> OperationResult get_operation_async_result(id_short_path, handle_id)

Returns the Operation result of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation result of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_result(id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_operation_async_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **handle_id** | **str**| The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded) | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_async_result_value_only**
> OperationResultValueOnly get_operation_async_result_value_only(id_short_path, handle_id)

Returns the value of the Operation result of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the value of the Operation result of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_result_value_only(id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_operation_async_result_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **handle_id** | **str**| The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded) | 

### Return type

[**OperationResultValueOnly**](OperationResultValueOnly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_async_status**
> BaseOperationResult get_operation_async_status(id_short_path, handle_id)

Returns the Operation status of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation status of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_status(id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_operation_async_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **handle_id** | **str**| The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded) | 

### Return type

[**BaseOperationResult**](BaseOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel**
> Submodel get_submodel(level=level, extent=extent)

Returns the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns the Submodel
    api_response = api_instance.get_submodel(level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**Submodel**](Submodel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_element_by_path**
> SubmodelElement get_submodel_element_by_path(id_short_path, level=level, extent=extent)

Returns a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path(id_short_path, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_element_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**SubmodelElement**](SubmodelElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_element_by_path_metadata**
> SubmodelElementMetadata get_submodel_element_by_path_metadata(id_short_path, cursor=cursor)

Returns the matadata attributes of a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns the matadata attributes of a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_metadata(id_short_path, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_element_by_path_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 

### Return type

[**SubmodelElementMetadata**](SubmodelElementMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_element_by_path_path**
> PathItem get_submodel_element_by_path_path(id_short_path, level=level)

Returns a specific submodel element from the Submodel at a specified path in the Path notation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns a specific submodel element from the Submodel at a specified path in the Path notation
    api_response = api_instance.get_submodel_element_by_path_path(id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_element_by_path_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**PathItem**](PathItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_element_by_path_reference**
> Reference get_submodel_element_by_path_reference(id_short_path, level=level)

Returns the Referene of a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the Referene of a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_reference(id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_element_by_path_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_element_by_path_value_only**
> SubmodelElementValue get_submodel_element_by_path_value_only(id_short_path, level=level, extent=extent)

Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
    api_response = api_instance.get_submodel_element_by_path_value_only(id_short_path, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_element_by_path_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**SubmodelElementValue**](SubmodelElementValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_metadata**
> SubmodelMetadata get_submodel_metadata(level=level)

Returns the metadata attributes of a specific Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the metadata attributes of a specific Submodel
    api_response = api_instance.get_submodel_metadata(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**SubmodelMetadata**](SubmodelMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_path**
> list[PathItem] get_submodel_path(level=level)

Returns the Submodel in the Path notation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the Submodel in the Path notation
    api_response = api_instance.get_submodel_path(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**list[PathItem]**](PathItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_reference**
> Reference get_submodel_reference(level=level)

Returns the Reference of the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the Reference of the Submodel
    api_response = api_instance.get_submodel_reference(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_value_only**
> SubmodelValue get_submodel_value_only(level=level, extent=extent)

Returns the Submodel in the ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns the Submodel in the ValueOnly representation
    api_response = api_instance.get_submodel_value_only(level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->get_submodel_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**SubmodelValue**](SubmodelValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation**
> OperationResult invoke_operation(body, id_short_path)

Synchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.OperationRequest() # OperationRequest | Operation request object
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Synchronously invokes an Operation at a specified path
    api_response = api_instance.invoke_operation(body, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->invoke_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequest**](OperationRequest.md)| Operation request object | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_async**
> invoke_operation_async(body, id_short_path)

Asynchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.OperationRequest() # OperationRequest | Operation request object
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Asynchronously invokes an Operation at a specified path
    api_instance.invoke_operation_async(body, id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->invoke_operation_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequest**](OperationRequest.md)| Operation request object | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_async_value_only**
> invoke_operation_async_value_only(body, id_short_path)

Asynchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.OperationRequestValueOnly() # OperationRequestValueOnly | Operation request object
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Asynchronously invokes an Operation at a specified path
    api_instance.invoke_operation_async_value_only(body, id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->invoke_operation_async_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequestValueOnly**](OperationRequestValueOnly.md)| Operation request object | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_sync_value_only**
> OperationResultValueOnly invoke_operation_sync_value_only(body, id_short_path)

Synchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.OperationRequestValueOnly() # OperationRequestValueOnly | Operation request object
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Synchronously invokes an Operation at a specified path
    api_response = api_instance.invoke_operation_sync_value_only(body, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->invoke_operation_sync_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequestValueOnly**](OperationRequestValueOnly.md)| Operation request object | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

[**OperationResultValueOnly**](OperationResultValueOnly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel**
> patch_submodel(body, level=level)

Updates the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.Submodel() # Submodel | Submodel object
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the Submodel
    api_instance.patch_submodel(body, level=level)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->patch_submodel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Submodel**](Submodel.md)| Submodel object | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_element_by_path**
> patch_submodel_element_by_path(body, id_short_path, level=level)

Updates an existing SubmodelElement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | SubmodelElement object
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates an existing SubmodelElement
    api_instance.patch_submodel_element_by_path(body, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->patch_submodel_element_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| SubmodelElement object | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_element_by_path_metadata**
> patch_submodel_element_by_path_metadata(body, id_short_path, limit=limit, cursor=cursor, level=level)

Updates the metadata attributes an existing SubmodelElement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.GetSubmodelElementsMetadataResult() # GetSubmodelElementsMetadataResult | Metadata attributes of the SubmodelElement
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the metadata attributes an existing SubmodelElement
    api_instance.patch_submodel_element_by_path_metadata(body, id_short_path, limit=limit, cursor=cursor, level=level)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->patch_submodel_element_by_path_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSubmodelElementsMetadataResult**](GetSubmodelElementsMetadataResult.md)| Metadata attributes of the SubmodelElement | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_element_by_path_value_only**
> patch_submodel_element_by_path_value_only(body, id_short_path, limit=limit, cursor=cursor, level=level)

Updates the value of an existing SubmodelElement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.GetSubmodelElementsValueResult() # GetSubmodelElementsValueResult | The SubmodelElement in its ValueOnly representation
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the value of an existing SubmodelElement
    api_instance.patch_submodel_element_by_path_value_only(body, id_short_path, limit=limit, cursor=cursor, level=level)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->patch_submodel_element_by_path_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetSubmodelElementsValueResult**](GetSubmodelElementsValueResult.md)| The SubmodelElement in its ValueOnly representation | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_metadata**
> patch_submodel_metadata(body, level=level)

Updates the metadata attributes of the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.SubmodelMetadata() # SubmodelMetadata | The metadata attributes of the Submodel object
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the metadata attributes of the Submodel
    api_instance.patch_submodel_metadata(body, level=level)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->patch_submodel_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelMetadata**](SubmodelMetadata.md)| The metadata attributes of the Submodel object | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_value_only**
> patch_submodel_value_only(body, level=level)

Updates the values of the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.SubmodelValue() # SubmodelValue | Submodel object in its ValueOnly representation
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the values of the Submodel
    api_instance.patch_submodel_value_only(body, level=level)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->patch_submodel_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelValue**](SubmodelValue.md)| Submodel object in its ValueOnly representation | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submodel_element**
> SubmodelElement post_submodel_element(body)

Creates a new submodel element

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element

try:
    # Creates a new submodel element
    api_response = api_instance.post_submodel_element(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->post_submodel_element: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 

### Return type

[**SubmodelElement**](SubmodelElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submodel_element_by_path**
> SubmodelElement post_submodel_element_by_path(body, id_short_path)

Creates a new submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Creates a new submodel element at a specified path within submodel elements hierarchy
    api_response = api_instance.post_submodel_element_by_path(body, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->post_submodel_element_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

[**SubmodelElement**](SubmodelElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file_by_path**
> put_file_by_path(file_name, file, id_short_path)

Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
file_name = 'file_name_example' # str | 
file = 'file_example' # str | 
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.put_file_by_path(file_name, file, id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->put_file_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **file** | **str**|  | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_submodel**
> put_submodel(body, level=level)

Updates the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.Submodel() # Submodel | Submodel object
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates the Submodel
    api_instance.put_submodel(body, level=level)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->put_submodel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Submodel**](Submodel.md)| Submodel object | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_submodel_element_by_path**
> put_submodel_element_by_path(body, id_short_path, level=level)

Updates an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.put_submodel_element_by_path(body, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling SubmodelAPIApi->put_submodel_element_by_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

