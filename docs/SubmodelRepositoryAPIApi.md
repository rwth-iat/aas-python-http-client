# swagger_client.SubmodelRepositoryAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_by_path_submodel_repo**](SubmodelRepositoryAPIApi.md#delete_file_by_path_submodel_repo) | **DELETE** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
[**delete_submodel_by_id**](SubmodelRepositoryAPIApi.md#delete_submodel_by_id) | **DELETE** /submodels/{submodelIdentifier} | Deletes a Submodel
[**delete_submodel_element_by_path_submodel_repo**](SubmodelRepositoryAPIApi.md#delete_submodel_element_by_path_submodel_repo) | **DELETE** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Deletes a submodel element at a specified path within the submodel elements hierarchy
[**get_all_submodel_elements_metadata_submodel_repository**](SubmodelRepositoryAPIApi.md#get_all_submodel_elements_metadata_submodel_repository) | **GET** /submodels/{submodelIdentifier}/submodel-elements/$metadata | Returns the metadata attributes of all submodel elements including their hierarchy
[**get_all_submodel_elements_path_submodel_repo**](SubmodelRepositoryAPIApi.md#get_all_submodel_elements_path_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/$path | Returns all submodel elements including their hierarchy in the Path notation
[**get_all_submodel_elements_reference_submodel_repo**](SubmodelRepositoryAPIApi.md#get_all_submodel_elements_reference_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/$reference | Returns the References of all submodel elements
[**get_all_submodel_elements_submodel_repository**](SubmodelRepositoryAPIApi.md#get_all_submodel_elements_submodel_repository) | **GET** /submodels/{submodelIdentifier}/submodel-elements | Returns all submodel elements including their hierarchy
[**get_all_submodel_elements_value_only_submodel_repo**](SubmodelRepositoryAPIApi.md#get_all_submodel_elements_value_only_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/$value | Returns all submodel elements including their hierarchy in the ValueOnly representation
[**get_all_submodels**](SubmodelRepositoryAPIApi.md#get_all_submodels) | **GET** /submodels | Returns all Submodels
[**get_all_submodels_metadata**](SubmodelRepositoryAPIApi.md#get_all_submodels_metadata) | **GET** /submodels/$metadata | Returns the metadata attributes of all Submodels
[**get_all_submodels_path**](SubmodelRepositoryAPIApi.md#get_all_submodels_path) | **GET** /submodels/$path | Returns all Submodels in the Path notation
[**get_all_submodels_reference**](SubmodelRepositoryAPIApi.md#get_all_submodels_reference) | **GET** /submodels/$reference | Returns the References for all Submodels
[**get_all_submodels_value_only**](SubmodelRepositoryAPIApi.md#get_all_submodels_value_only) | **GET** /submodels/$value | Returns all Submodels in their ValueOnly representation
[**get_file_by_path_submodel_repo**](SubmodelRepositoryAPIApi.md#get_file_by_path_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Downloads file content from a specific submodel element from the Submodel at a specified path
[**get_operation_async_result_submodel_repo**](SubmodelRepositoryAPIApi.md#get_operation_async_result_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-results/{handleId} | Returns the Operation result of an asynchronous invoked Operation
[**get_operation_async_result_value_only_submodel_repo**](SubmodelRepositoryAPIApi.md#get_operation_async_result_value_only_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-results/{handleId}/$value | Returns the Operation result of an asynchronous invoked Operation
[**get_operation_async_status_submodel_repo**](SubmodelRepositoryAPIApi.md#get_operation_async_status_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-status/{handleId} | Returns the Operation status of an asynchronous invoked Operation
[**get_submodel_by_id**](SubmodelRepositoryAPIApi.md#get_submodel_by_id) | **GET** /submodels/{submodelIdentifier} | Returns a specific Submodel
[**get_submodel_by_id_metadata**](SubmodelRepositoryAPIApi.md#get_submodel_by_id_metadata) | **GET** /submodels/{submodelIdentifier}/$metadata | Returns the metadata attributes of a specific Submodel
[**get_submodel_by_id_path**](SubmodelRepositoryAPIApi.md#get_submodel_by_id_path) | **GET** /submodels/{submodelIdentifier}/$path | Returns a specific Submodel in the Path notation
[**get_submodel_by_id_reference**](SubmodelRepositoryAPIApi.md#get_submodel_by_id_reference) | **GET** /submodels/{submodelIdentifier}/$reference | Returns the Reference of a specific Submodel
[**get_submodel_by_id_value_only**](SubmodelRepositoryAPIApi.md#get_submodel_by_id_value_only) | **GET** /submodels/{submodelIdentifier}/$value | Returns a specific Submodel in the ValueOnly representation
[**get_submodel_element_by_path_metadata_submodel_repo**](SubmodelRepositoryAPIApi.md#get_submodel_element_by_path_metadata_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$metadata | Returns the matadata attributes of a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_path_submodel_repo**](SubmodelRepositoryAPIApi.md#get_submodel_element_by_path_path_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$path | Returns a specific submodel element from the Submodel at a specified path in the Path notation
[**get_submodel_element_by_path_reference_submodel_repo**](SubmodelRepositoryAPIApi.md#get_submodel_element_by_path_reference_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$reference | Returns the Referene of a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_submodel_repo**](SubmodelRepositoryAPIApi.md#get_submodel_element_by_path_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Returns a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_value_only_submodel_repo**](SubmodelRepositoryAPIApi.md#get_submodel_element_by_path_value_only_submodel_repo) | **GET** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$value | Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
[**invoke_operation_async_submodel_repo**](SubmodelRepositoryAPIApi.md#invoke_operation_async_submodel_repo) | **POST** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke-async | Asynchronously invokes an Operation at a specified path
[**invoke_operation_async_value_only_submodel_repo**](SubmodelRepositoryAPIApi.md#invoke_operation_async_value_only_submodel_repo) | **POST** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke-async/$value | Asynchronously invokes an Operation at a specified path
[**invoke_operation_submodel_repo**](SubmodelRepositoryAPIApi.md#invoke_operation_submodel_repo) | **POST** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke | Synchronously invokes an Operation at a specified path
[**invoke_operation_value_only_submodel_repo**](SubmodelRepositoryAPIApi.md#invoke_operation_value_only_submodel_repo) | **POST** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke/$value | Synchronously invokes an Operation at a specified path
[**patch_submodel_by_id**](SubmodelRepositoryAPIApi.md#patch_submodel_by_id) | **PATCH** /submodels/{submodelIdentifier} | Updates an existing Submodel
[**patch_submodel_by_id_metadata**](SubmodelRepositoryAPIApi.md#patch_submodel_by_id_metadata) | **PATCH** /submodels/{submodelIdentifier}/$metadata | Updates the metadata attributes of an existing Submodel
[**patch_submodel_by_id_value_only**](SubmodelRepositoryAPIApi.md#patch_submodel_by_id_value_only) | **PATCH** /submodels/{submodelIdentifier}/$value | Updates the values of an existing Submodel
[**patch_submodel_element_by_path_metadata_submodel_repo**](SubmodelRepositoryAPIApi.md#patch_submodel_element_by_path_metadata_submodel_repo) | **PATCH** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$metadata | Updates the metadata attributes an existing SubmodelElement
[**patch_submodel_element_by_path_submodel_repo**](SubmodelRepositoryAPIApi.md#patch_submodel_element_by_path_submodel_repo) | **PATCH** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Updates an existing SubmodelElement
[**patch_submodel_element_by_path_value_only_submodel_repo**](SubmodelRepositoryAPIApi.md#patch_submodel_element_by_path_value_only_submodel_repo) | **PATCH** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$value | Updates the value of an existing SubmodelElement
[**post_submodel**](SubmodelRepositoryAPIApi.md#post_submodel) | **POST** /submodels | Creates a new Submodel
[**post_submodel_element_by_path_submodel_repo**](SubmodelRepositoryAPIApi.md#post_submodel_element_by_path_submodel_repo) | **POST** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Creates a new submodel element at a specified path within submodel elements hierarchy
[**post_submodel_element_submodel_repository**](SubmodelRepositoryAPIApi.md#post_submodel_element_submodel_repository) | **POST** /submodels/{submodelIdentifier}/submodel-elements | Creates a new submodel element
[**put_file_by_path_submodel_repo**](SubmodelRepositoryAPIApi.md#put_file_by_path_submodel_repo) | **PUT** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
[**put_submodel_by_id**](SubmodelRepositoryAPIApi.md#put_submodel_by_id) | **PUT** /submodels/{submodelIdentifier} | Updates an existing Submodel
[**put_submodel_element_by_path_submodel_repo**](SubmodelRepositoryAPIApi.md#put_submodel_element_by_path_submodel_repo) | **PUT** /submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Updates an existing submodel element at a specified path within submodel elements hierarchy

# **delete_file_by_path_submodel_repo**
> delete_file_by_path_submodel_repo(submodel_identifier, id_short_path)

Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.delete_file_by_path_submodel_repo(submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->delete_file_by_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_submodel_by_id**
> delete_submodel_by_id(submodel_identifier)

Deletes a Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes a Submodel
    api_instance.delete_submodel_by_id(submodel_identifier)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->delete_submodel_by_id: %s\n" % e)
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

# **delete_submodel_element_by_path_submodel_repo**
> delete_submodel_element_by_path_submodel_repo(submodel_identifier, id_short_path)

Deletes a submodel element at a specified path within the submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Deletes a submodel element at a specified path within the submodel elements hierarchy
    api_instance.delete_submodel_element_by_path_submodel_repo(submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->delete_submodel_element_by_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_elements_metadata_submodel_repository**
> GetSubmodelElementsMetadataResult get_all_submodel_elements_metadata_submodel_repository(submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns the metadata attributes of all submodel elements including their hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the metadata attributes of all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_metadata_submodel_repository(submodel_identifier, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodel_elements_metadata_submodel_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_all_submodel_elements_path_submodel_repo**
> GetPathItemsResult get_all_submodel_elements_path_submodel_repo(submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns all submodel elements including their hierarchy in the Path notation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns all submodel elements including their hierarchy in the Path notation
    api_response = api_instance.get_all_submodel_elements_path_submodel_repo(submodel_identifier, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodel_elements_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_all_submodel_elements_reference_submodel_repo**
> GetReferencesResult get_all_submodel_elements_reference_submodel_repo(submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns the References of all submodel elements

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the References of all submodel elements
    api_response = api_instance.get_all_submodel_elements_reference_submodel_repo(submodel_identifier, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodel_elements_reference_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_all_submodel_elements_submodel_repository**
> GetSubmodelElementsResult get_all_submodel_elements_submodel_repository(submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)

Returns all submodel elements including their hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_submodel_repository(submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodel_elements_submodel_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_all_submodel_elements_value_only_submodel_repo**
> GetSubmodelElementsValueResult get_all_submodel_elements_value_only_submodel_repo(submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)

Returns all submodel elements including their hierarchy in the ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all submodel elements including their hierarchy in the ValueOnly representation
    api_response = api_instance.get_all_submodel_elements_value_only_submodel_repo(submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodel_elements_value_only_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_all_submodels**
> GetSubmodelsResult get_all_submodels(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level, extent=extent)

Returns all Submodels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
semantic_id = 'semantic_id_example' # str | The value of the semantic id reference (BASE64-URL-encoded) (optional)
id_short = 'id_short_example' # str | The Asset Administration Shell’s IdShort (optional)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all Submodels
    api_response = api_instance.get_all_submodels(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semantic_id** | **str**| The value of the semantic id reference (BASE64-URL-encoded) | [optional] 
 **id_short** | **str**| The Asset Administration Shell’s IdShort | [optional] 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**GetSubmodelsResult**](GetSubmodelsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodels_metadata**
> GetSubmodelsMetadataResult get_all_submodels_metadata(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level)

Returns the metadata attributes of all Submodels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
semantic_id = 'semantic_id_example' # str | The value of the semantic id reference (BASE64-URL-encoded) (optional)
id_short = 'id_short_example' # str | The Asset Administration Shell’s IdShort (optional)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the metadata attributes of all Submodels
    api_response = api_instance.get_all_submodels_metadata(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodels_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semantic_id** | **str**| The value of the semantic id reference (BASE64-URL-encoded) | [optional] 
 **id_short** | **str**| The Asset Administration Shell’s IdShort | [optional] 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**GetSubmodelsMetadataResult**](GetSubmodelsMetadataResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodels_path**
> GetPathItemsResult get_all_submodels_path(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level)

Returns all Submodels in the Path notation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
semantic_id = 'semantic_id_example' # str | The value of the semantic id reference (BASE64-URL-encoded) (optional)
id_short = 'id_short_example' # str | The Asset Administration Shell’s IdShort (optional)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns all Submodels in the Path notation
    api_response = api_instance.get_all_submodels_path(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodels_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semantic_id** | **str**| The value of the semantic id reference (BASE64-URL-encoded) | [optional] 
 **id_short** | **str**| The Asset Administration Shell’s IdShort | [optional] 
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

# **get_all_submodels_reference**
> GetReferencesResult get_all_submodels_reference(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level)

Returns the References for all Submodels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
semantic_id = 'semantic_id_example' # str | The value of the semantic id reference (BASE64-URL-encoded) (optional)
id_short = 'id_short_example' # str | The Asset Administration Shell’s IdShort (optional)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the References for all Submodels
    api_response = api_instance.get_all_submodels_reference(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodels_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semantic_id** | **str**| The value of the semantic id reference (BASE64-URL-encoded) | [optional] 
 **id_short** | **str**| The Asset Administration Shell’s IdShort | [optional] 
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

# **get_all_submodels_value_only**
> GetSubmodelsValueResult get_all_submodels_value_only(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level, extent=extent)

Returns all Submodels in their ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
semantic_id = 'semantic_id_example' # str | The value of the semantic id reference (BASE64-URL-encoded) (optional)
id_short = 'id_short_example' # str | The Asset Administration Shell’s IdShort (optional)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all Submodels in their ValueOnly representation
    api_response = api_instance.get_all_submodels_value_only(semantic_id=semantic_id, id_short=id_short, limit=limit, cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_all_submodels_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **semantic_id** | **str**| The value of the semantic id reference (BASE64-URL-encoded) | [optional] 
 **id_short** | **str**| The Asset Administration Shell’s IdShort | [optional] 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**GetSubmodelsValueResult**](GetSubmodelsValueResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_by_path_submodel_repo**
> str get_file_by_path_submodel_repo(submodel_identifier, id_short_path)

Downloads file content from a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Downloads file content from a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_file_by_path_submodel_repo(submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_file_by_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_async_result_submodel_repo**
> OperationResult get_operation_async_result_submodel_repo(submodel_identifier, id_short_path, handle_id)

Returns the Operation result of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation result of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_result_submodel_repo(submodel_identifier, id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_operation_async_result_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_operation_async_result_value_only_submodel_repo**
> OperationResultValueOnly get_operation_async_result_value_only_submodel_repo(submodel_identifier, id_short_path, handle_id)

Returns the Operation result of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation result of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_result_value_only_submodel_repo(submodel_identifier, id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_operation_async_result_value_only_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_operation_async_status_submodel_repo**
> OperationResult get_operation_async_status_submodel_repo(submodel_identifier, id_short_path, handle_id)

Returns the Operation status of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation status of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_status_submodel_repo(submodel_identifier, id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_operation_async_status_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_by_id**
> Submodel get_submodel_by_id(submodel_identifier, level=level, extent=extent)

Returns a specific Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific Submodel
    api_response = api_instance.get_submodel_by_id(submodel_identifier, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_by_id_metadata**
> SubmodelMetadata get_submodel_by_id_metadata(submodel_identifier, level=level)

Returns the metadata attributes of a specific Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the metadata attributes of a specific Submodel
    api_response = api_instance.get_submodel_by_id_metadata(submodel_identifier, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_by_id_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**SubmodelMetadata**](SubmodelMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_by_id_path**
> list[PathItem] get_submodel_by_id_path(submodel_identifier, level=level)

Returns a specific Submodel in the Path notation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns a specific Submodel in the Path notation
    api_response = api_instance.get_submodel_by_id_path(submodel_identifier, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_by_id_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**list[PathItem]**](PathItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_by_id_reference**
> Reference get_submodel_by_id_reference(submodel_identifier)

Returns the Reference of a specific Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns the Reference of a specific Submodel
    api_response = api_instance.get_submodel_by_id_reference(submodel_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_by_id_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_by_id_value_only**
> SubmodelValue get_submodel_by_id_value_only(submodel_identifier, level=level, extent=extent)

Returns a specific Submodel in the ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific Submodel in the ValueOnly representation
    api_response = api_instance.get_submodel_by_id_value_only(submodel_identifier, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_by_id_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_metadata_submodel_repo**
> SubmodelElementMetadata get_submodel_element_by_path_metadata_submodel_repo(submodel_identifier, id_short_path, level=level)

Returns the matadata attributes of a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the matadata attributes of a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_metadata_submodel_repo(submodel_identifier, id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_element_by_path_metadata_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**SubmodelElementMetadata**](SubmodelElementMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_element_by_path_path_submodel_repo**
> list[PathItem] get_submodel_element_by_path_path_submodel_repo(submodel_identifier, id_short_path, level=level)

Returns a specific submodel element from the Submodel at a specified path in the Path notation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns a specific submodel element from the Submodel at a specified path in the Path notation
    api_response = api_instance.get_submodel_element_by_path_path_submodel_repo(submodel_identifier, id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_element_by_path_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**list[PathItem]**](PathItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_element_by_path_reference_submodel_repo**
> Reference get_submodel_element_by_path_reference_submodel_repo(submodel_identifier, id_short_path, level=level)

Returns the Referene of a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the Referene of a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_reference_submodel_repo(submodel_identifier, id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_element_by_path_reference_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_submodel_repo**
> SubmodelElement get_submodel_element_by_path_submodel_repo(submodel_identifier, id_short_path, level=level, extent=extent)

Returns a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_submodel_repo(submodel_identifier, id_short_path, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_element_by_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_value_only_submodel_repo**
> SubmodelElementValue get_submodel_element_by_path_value_only_submodel_repo(submodel_identifier, id_short_path, level=level, extent=extent)

Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
    api_response = api_instance.get_submodel_element_by_path_value_only_submodel_repo(submodel_identifier, id_short_path, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->get_submodel_element_by_path_value_only_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **invoke_operation_async_submodel_repo**
> invoke_operation_async_submodel_repo(body, submodel_identifier, id_short_path)

Asynchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.OperationRequest() # OperationRequest | Operation request object
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Asynchronously invokes an Operation at a specified path
    api_instance.invoke_operation_async_submodel_repo(body, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->invoke_operation_async_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequest**](OperationRequest.md)| Operation request object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_async_value_only_submodel_repo**
> invoke_operation_async_value_only_submodel_repo(body, aas_identifier, submodel_identifier, id_short_path)

Asynchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.OperationRequestValueOnly() # OperationRequestValueOnly | Operation request object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Asynchronously invokes an Operation at a specified path
    api_instance.invoke_operation_async_value_only_submodel_repo(body, aas_identifier, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->invoke_operation_async_value_only_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequestValueOnly**](OperationRequestValueOnly.md)| Operation request object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_submodel_repo**
> OperationResult invoke_operation_submodel_repo(body, submodel_identifier, id_short_path, _async=_async)

Synchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.OperationRequest() # OperationRequest | Operation request object
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
_async = false # bool | Determines whether an operation invocation is performed asynchronously or synchronously (optional) (default to false)

try:
    # Synchronously invokes an Operation at a specified path
    api_response = api_instance.invoke_operation_submodel_repo(body, submodel_identifier, id_short_path, _async=_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->invoke_operation_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequest**](OperationRequest.md)| Operation request object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **_async** | **bool**| Determines whether an operation invocation is performed asynchronously or synchronously | [optional] [default to false]

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_value_only_submodel_repo**
> OperationResultValueOnly invoke_operation_value_only_submodel_repo(body, aas_identifier, submodel_identifier, id_short_path, _async=_async)

Synchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.OperationRequestValueOnly() # OperationRequestValueOnly | Operation request object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
_async = false # bool | Determines whether an operation invocation is performed asynchronously or synchronously (optional) (default to false)

try:
    # Synchronously invokes an Operation at a specified path
    api_response = api_instance.invoke_operation_value_only_submodel_repo(body, aas_identifier, submodel_identifier, id_short_path, _async=_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->invoke_operation_value_only_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequestValueOnly**](OperationRequestValueOnly.md)| Operation request object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **_async** | **bool**| Determines whether an operation invocation is performed asynchronously or synchronously | [optional] [default to false]

### Return type

[**OperationResultValueOnly**](OperationResultValueOnly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_by_id**
> patch_submodel_by_id(body, submodel_identifier, level=level)

Updates an existing Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.Submodel() # Submodel | Submodel object
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates an existing Submodel
    api_instance.patch_submodel_by_id(body, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->patch_submodel_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Submodel**](Submodel.md)| Submodel object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_by_id_metadata**
> patch_submodel_by_id_metadata(body, submodel_identifier, level=level)

Updates the metadata attributes of an existing Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.SubmodelMetadata() # SubmodelMetadata | The metadata attributes of the Submodel object
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the metadata attributes of an existing Submodel
    api_instance.patch_submodel_by_id_metadata(body, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->patch_submodel_by_id_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelMetadata**](SubmodelMetadata.md)| The metadata attributes of the Submodel object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_by_id_value_only**
> patch_submodel_by_id_value_only(body, submodel_identifier, level=level)

Updates the values of an existing Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.SubmodelValue() # SubmodelValue | Submodel object in its ValueOnly representation
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the values of an existing Submodel
    api_instance.patch_submodel_by_id_value_only(body, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->patch_submodel_by_id_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelValue**](SubmodelValue.md)| Submodel object in its ValueOnly representation | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_element_by_path_metadata_submodel_repo**
> patch_submodel_element_by_path_metadata_submodel_repo(body, submodel_identifier, id_short_path, level=level)

Updates the metadata attributes an existing SubmodelElement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.SubmodelElementMetadata() # SubmodelElementMetadata | Metadata attributes of the SubmodelElement
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the metadata attributes an existing SubmodelElement
    api_instance.patch_submodel_element_by_path_metadata_submodel_repo(body, submodel_identifier, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->patch_submodel_element_by_path_metadata_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElementMetadata**](SubmodelElementMetadata.md)| Metadata attributes of the SubmodelElement | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **patch_submodel_element_by_path_submodel_repo**
> patch_submodel_element_by_path_submodel_repo(body, submodel_identifier, id_short_path, level=level)

Updates an existing SubmodelElement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | SubmodelElement object
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates an existing SubmodelElement
    api_instance.patch_submodel_element_by_path_submodel_repo(body, submodel_identifier, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->patch_submodel_element_by_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| SubmodelElement object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **patch_submodel_element_by_path_value_only_submodel_repo**
> patch_submodel_element_by_path_value_only_submodel_repo(body, submodel_identifier, id_short_path, level=level)

Updates the value of an existing SubmodelElement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.SubmodelElementValue() # SubmodelElementValue | The SubmodelElement in its ValueOnly representation
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the value of an existing SubmodelElement
    api_instance.patch_submodel_element_by_path_value_only_submodel_repo(body, submodel_identifier, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->patch_submodel_element_by_path_value_only_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElementValue**](SubmodelElementValue.md)| The SubmodelElement in its ValueOnly representation | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **post_submodel**
> Submodel post_submodel(body)

Creates a new Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.Submodel() # Submodel | Submodel object

try:
    # Creates a new Submodel
    api_response = api_instance.post_submodel(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->post_submodel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Submodel**](Submodel.md)| Submodel object | 

### Return type

[**Submodel**](Submodel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submodel_element_by_path_submodel_repo**
> SubmodelElement post_submodel_element_by_path_submodel_repo(body, submodel_identifier, id_short_path)

Creates a new submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Creates a new submodel element at a specified path within submodel elements hierarchy
    api_response = api_instance.post_submodel_element_by_path_submodel_repo(body, submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->post_submodel_element_by_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

[**SubmodelElement**](SubmodelElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submodel_element_submodel_repository**
> SubmodelElement post_submodel_element_submodel_repository(body, submodel_identifier)

Creates a new submodel element

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Creates a new submodel element
    api_response = api_instance.post_submodel_element_submodel_repository(body, submodel_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->post_submodel_element_submodel_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**SubmodelElement**](SubmodelElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file_by_path_submodel_repo**
> put_file_by_path_submodel_repo(file_name, file, submodel_identifier, id_short_path)

Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
file_name = 'file_name_example' # str | 
file = 'file_example' # str | 
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.put_file_by_path_submodel_repo(file_name, file, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->put_file_by_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **file** | **str**|  | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_submodel_by_id**
> put_submodel_by_id(body, submodel_identifier)

Updates an existing Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.Submodel() # Submodel | Submodel object
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Updates an existing Submodel
    api_instance.put_submodel_by_id(body, submodel_identifier)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->put_submodel_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Submodel**](Submodel.md)| Submodel object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_submodel_element_by_path_submodel_repo**
> put_submodel_element_by_path_submodel_repo(body, submodel_identifier, id_short_path, level=level)

Updates an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubmodelRepositoryAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.put_submodel_element_by_path_submodel_repo(body, submodel_identifier, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling SubmodelRepositoryAPIApi->put_submodel_element_by_path_submodel_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

