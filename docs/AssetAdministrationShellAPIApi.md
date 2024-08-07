# swagger_client.AssetAdministrationShellAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_by_path_aas**](AssetAdministrationShellAPIApi.md#delete_file_by_path_aas) | **DELETE** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
[**delete_submodel_by_id_aas**](AssetAdministrationShellAPIApi.md#delete_submodel_by_id_aas) | **DELETE** /aas/submodels/{submodelIdentifier} | Deletes the submodel from the Asset Administration Shell.
[**delete_submodel_element_by_path_aas**](AssetAdministrationShellAPIApi.md#delete_submodel_element_by_path_aas) | **DELETE** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Deletes a submodel element at a specified path within the submodel elements hierarchy
[**delete_submodel_reference_by_id**](AssetAdministrationShellAPIApi.md#delete_submodel_reference_by_id) | **DELETE** /aas/submodel-refs/{submodelIdentifier} | Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!
[**delete_thumbnail**](AssetAdministrationShellAPIApi.md#delete_thumbnail) | **DELETE** /aas/asset-information/thumbnail | 
[**get_all_submodel_elements_aas**](AssetAdministrationShellAPIApi.md#get_all_submodel_elements_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements | Returns all submodel elements including their hierarchy
[**get_all_submodel_elements_metadata_aas**](AssetAdministrationShellAPIApi.md#get_all_submodel_elements_metadata_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/$metadata | Returns all submodel elements including their hierarchy
[**get_all_submodel_elements_path_aas**](AssetAdministrationShellAPIApi.md#get_all_submodel_elements_path_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/$path | Returns all submodel elements including their hierarchy
[**get_all_submodel_elements_reference_aas**](AssetAdministrationShellAPIApi.md#get_all_submodel_elements_reference_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/$reference | Returns all submodel elements as a list of References
[**get_all_submodel_elements_value_only_aas**](AssetAdministrationShellAPIApi.md#get_all_submodel_elements_value_only_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/$value | Returns all submodel elements including their hierarchy in the ValueOnly representation
[**get_all_submodel_references**](AssetAdministrationShellAPIApi.md#get_all_submodel_references) | **GET** /aas/submodel-refs | Returns all submodel references
[**get_asset_administration_shell**](AssetAdministrationShellAPIApi.md#get_asset_administration_shell) | **GET** /aas | Returns a specific Asset Administration Shell
[**get_asset_administration_shell_reference**](AssetAdministrationShellAPIApi.md#get_asset_administration_shell_reference) | **GET** /aas/$reference | Returns a specific Asset Administration Shell as a Reference
[**get_asset_information**](AssetAdministrationShellAPIApi.md#get_asset_information) | **GET** /aas/asset-information | Returns the Asset Information
[**get_file_by_path_aas**](AssetAdministrationShellAPIApi.md#get_file_by_path_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Downloads file content from a specific submodel element from the Submodel at a specified path
[**get_operation_async_result_aas**](AssetAdministrationShellAPIApi.md#get_operation_async_result_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-results/{handleId} | Returns the Operation result of an asynchronous invoked Operation
[**get_operation_async_result_value_only_aas**](AssetAdministrationShellAPIApi.md#get_operation_async_result_value_only_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-results/{handleId}/$value | Returns the value of the Operation result of an asynchronous invoked Operation
[**get_operation_async_status_aas**](AssetAdministrationShellAPIApi.md#get_operation_async_status_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-status/{handleId} | Returns the Operation status of an asynchronous invoked Operation
[**get_submodel_aas**](AssetAdministrationShellAPIApi.md#get_submodel_aas) | **GET** /aas/submodels/{submodelIdentifier} | Returns the Submodel
[**get_submodel_element_by_path_aas**](AssetAdministrationShellAPIApi.md#get_submodel_element_by_path_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Returns a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_metadata_aas**](AssetAdministrationShellAPIApi.md#get_submodel_element_by_path_metadata_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$metadata | Returns the metadata attributes if a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_path_aas**](AssetAdministrationShellAPIApi.md#get_submodel_element_by_path_path_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$path | Returns a specific submodel element from the Submodel at a specified path in the Path notation
[**get_submodel_element_by_path_reference_aas**](AssetAdministrationShellAPIApi.md#get_submodel_element_by_path_reference_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$reference | Returns the Reference of a specific submodel element from the Submodel at a specified path in the ValueOnly representation
[**get_submodel_element_by_path_value_only_aas**](AssetAdministrationShellAPIApi.md#get_submodel_element_by_path_value_only_aas) | **GET** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$value | Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
[**get_submodel_metadata_aas**](AssetAdministrationShellAPIApi.md#get_submodel_metadata_aas) | **GET** /aas/submodels/{submodelIdentifier}/$metadata | Returns the Submodel&#x27;s metadata elements
[**get_submodel_metadata_reference_aas**](AssetAdministrationShellAPIApi.md#get_submodel_metadata_reference_aas) | **GET** /aas/submodels/{submodelIdentifier}/$reference | Returns the Submodel as a Reference
[**get_submodel_path_aas**](AssetAdministrationShellAPIApi.md#get_submodel_path_aas) | **GET** /aas/submodels/{submodelIdentifier}/$path | Returns the Submodel&#x27;s metadata elements
[**get_submodel_value_only_aas**](AssetAdministrationShellAPIApi.md#get_submodel_value_only_aas) | **GET** /aas/submodels/{submodelIdentifier}/$value | Returns the Submodel&#x27;s ValueOnly representation
[**get_thumbnail**](AssetAdministrationShellAPIApi.md#get_thumbnail) | **GET** /aas/asset-information/thumbnail | 
[**invoke_operation_async_aas**](AssetAdministrationShellAPIApi.md#invoke_operation_async_aas) | **POST** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke-async | Synchronously invokes an Operation at a specified path
[**invoke_operation_async_value_only_aas**](AssetAdministrationShellAPIApi.md#invoke_operation_async_value_only_aas) | **POST** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke-asnyc/$value | Asynchronously invokes an Operation at a specified path
[**invoke_operation_sync_aas**](AssetAdministrationShellAPIApi.md#invoke_operation_sync_aas) | **POST** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke | Synchronously invokes an Operation at a specified path
[**invoke_operation_sync_value_only_aas**](AssetAdministrationShellAPIApi.md#invoke_operation_sync_value_only_aas) | **POST** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke/$value | Synchronously invokes an Operation at a specified path
[**patch_submodel_aas**](AssetAdministrationShellAPIApi.md#patch_submodel_aas) | **PATCH** /aas/submodels/{submodelIdentifier} | Updates the Submodel
[**patch_submodel_element_value_by_path_aas**](AssetAdministrationShellAPIApi.md#patch_submodel_element_value_by_path_aas) | **PATCH** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Updates an existing submodel element value at a specified path within submodel elements hierarchy
[**patch_submodel_element_value_by_path_metadata_aas**](AssetAdministrationShellAPIApi.md#patch_submodel_element_value_by_path_metadata_aas) | **PATCH** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$metadata | Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy
[**patch_submodel_element_value_by_path_value_only_aas**](AssetAdministrationShellAPIApi.md#patch_submodel_element_value_by_path_value_only_aas) | **PATCH** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$value | Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy
[**patch_submodel_metadata_aas**](AssetAdministrationShellAPIApi.md#patch_submodel_metadata_aas) | **PATCH** /aas/submodels/{submodelIdentifier}/$metadata | Updates the metadata attributes of the Submodel
[**patch_submodel_value_only_aas**](AssetAdministrationShellAPIApi.md#patch_submodel_value_only_aas) | **PATCH** /aas/submodels/{submodelIdentifier}/$value | Updates teh values of the Submodel
[**post_submodel_element_aas**](AssetAdministrationShellAPIApi.md#post_submodel_element_aas) | **POST** /aas/submodels/{submodelIdentifier}/submodel-elements | Creates a new submodel element
[**post_submodel_element_by_path_aas**](AssetAdministrationShellAPIApi.md#post_submodel_element_by_path_aas) | **POST** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Creates a new submodel element at a specified path within submodel elements hierarchy
[**post_submodel_reference**](AssetAdministrationShellAPIApi.md#post_submodel_reference) | **POST** /aas/submodel-refs | Creates a submodel reference at the Asset Administration Shell
[**put_asset_administration_shell**](AssetAdministrationShellAPIApi.md#put_asset_administration_shell) | **PUT** /aas | Updates an existing Asset Administration Shell
[**put_asset_information**](AssetAdministrationShellAPIApi.md#put_asset_information) | **PUT** /aas/asset-information | Updates the Asset Information
[**put_file_by_path_aas**](AssetAdministrationShellAPIApi.md#put_file_by_path_aas) | **PUT** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
[**put_submodel_aas**](AssetAdministrationShellAPIApi.md#put_submodel_aas) | **PUT** /aas/submodels/{submodelIdentifier} | Updates the Submodel
[**put_submodel_element_by_path_aas**](AssetAdministrationShellAPIApi.md#put_submodel_element_by_path_aas) | **PUT** /aas/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Updates an existing submodel element at a specified path within submodel elements hierarchy
[**put_thumbnail**](AssetAdministrationShellAPIApi.md#put_thumbnail) | **PUT** /aas/asset-information/thumbnail | 

# **delete_file_by_path_aas**
> delete_file_by_path_aas(submodel_identifier, id_short_path)

Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.delete_file_by_path_aas(submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->delete_file_by_path_aas: %s\n" % e)
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

# **delete_submodel_by_id_aas**
> delete_submodel_by_id_aas(submodel_identifier)

Deletes the submodel from the Asset Administration Shell.

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes the submodel from the Asset Administration Shell.
    api_instance.delete_submodel_by_id_aas(submodel_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->delete_submodel_by_id_aas: %s\n" % e)
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

# **delete_submodel_element_by_path_aas**
> delete_submodel_element_by_path_aas(submodel_identifier, id_short_path)

Deletes a submodel element at a specified path within the submodel elements hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Deletes a submodel element at a specified path within the submodel elements hierarchy
    api_instance.delete_submodel_element_by_path_aas(submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->delete_submodel_element_by_path_aas: %s\n" % e)
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

# **delete_submodel_reference_by_id**
> delete_submodel_reference_by_id(submodel_identifier)

Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!
    api_instance.delete_submodel_reference_by_id(submodel_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->delete_submodel_reference_by_id: %s\n" % e)
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

# **delete_thumbnail**
> delete_thumbnail()



### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()

try:
    api_instance.delete_thumbnail()
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->delete_thumbnail: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_elements_aas**
> GetSubmodelElementsResult get_all_submodel_elements_aas(submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)

Returns all submodel elements including their hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue'  # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_aas(submodel_identifier, limit=limit, cursor=cursor,
                                                              level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_all_submodel_elements_aas: %s\n" % e)
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

# **get_all_submodel_elements_metadata_aas**
> GetSubmodelElementsMetadataResult get_all_submodel_elements_metadata_aas(submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns all submodel elements including their hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_metadata_aas(submodel_identifier, limit=limit, cursor=cursor,
                                                                       level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_all_submodel_elements_metadata_aas: %s\n" % e)
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

# **get_all_submodel_elements_path_aas**
> GetPathItemsResult get_all_submodel_elements_path_aas(submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns all submodel elements including their hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_path_aas(submodel_identifier, limit=limit, cursor=cursor,
                                                                   level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_all_submodel_elements_path_aas: %s\n" % e)
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

# **get_all_submodel_elements_reference_aas**
> GetReferencesResult get_all_submodel_elements_reference_aas(submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns all submodel elements as a list of References

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'core'  # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns all submodel elements as a list of References
    api_response = api_instance.get_all_submodel_elements_reference_aas(submodel_identifier, limit=limit, cursor=cursor,
                                                                        level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_all_submodel_elements_reference_aas: %s\n" % e)
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

# **get_all_submodel_elements_value_only_aas**
> GetSubmodelElementsValueResult get_all_submodel_elements_value_only_aas(submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)

Returns all submodel elements including their hierarchy in the ValueOnly representation

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue'  # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all submodel elements including their hierarchy in the ValueOnly representation
    api_response = api_instance.get_all_submodel_elements_value_only_aas(submodel_identifier, limit=limit,
                                                                         cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_all_submodel_elements_value_only_aas: %s\n" % e)
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

# **get_all_submodel_references**
> GetReferencesResult get_all_submodel_references(limit=limit, cursor=cursor)

Returns all submodel references

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns all submodel references
    api_response = api_instance.get_all_submodel_references(limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_all_submodel_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 

### Return type

[**GetReferencesResult**](GetReferencesResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_administration_shell**
> AssetAdministrationShell get_asset_administration_shell()

Returns a specific Asset Administration Shell

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()

try:
    # Returns a specific Asset Administration Shell
    api_response = api_instance.get_asset_administration_shell()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_asset_administration_shell: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssetAdministrationShell**](AssetAdministrationShell.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_administration_shell_reference**
> Reference get_asset_administration_shell_reference()

Returns a specific Asset Administration Shell as a Reference

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()

try:
    # Returns a specific Asset Administration Shell as a Reference
    api_response = api_instance.get_asset_administration_shell_reference()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_asset_administration_shell_reference: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_information**
> AssetInformation get_asset_information()

Returns the Asset Information

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()

try:
    # Returns the Asset Information
    api_response = api_instance.get_asset_information()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_asset_information: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssetInformation**](AssetInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_by_path_aas**
> str get_file_by_path_aas(submodel_identifier, id_short_path)

Downloads file content from a specific submodel element from the Submodel at a specified path

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Downloads file content from a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_file_by_path_aas(submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_file_by_path_aas: %s\n" % e)
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

# **get_operation_async_result_aas**
> OperationResult get_operation_async_result_aas(submodel_identifier, aas_identifier, id_short_path, handle_id)

Returns the Operation result of an asynchronous invoked Operation

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example'  # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation result of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_result_aas(submodel_identifier, aas_identifier, id_short_path,
                                                               handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_operation_async_result_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_operation_async_result_value_only_aas**
> OperationResultValueOnly get_operation_async_result_value_only_aas(submodel_identifier, aas_identifier, id_short_path, handle_id)

Returns the value of the Operation result of an asynchronous invoked Operation

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example'  # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the value of the Operation result of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_result_value_only_aas(submodel_identifier, aas_identifier,
                                                                          id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_operation_async_result_value_only_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_operation_async_status_aas**
> BaseOperationResult get_operation_async_status_aas(submodel_identifier, aas_identifier, id_short_path, handle_id)

Returns the Operation status of an asynchronous invoked Operation

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example'  # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation status of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_status_aas(submodel_identifier, aas_identifier, id_short_path,
                                                               handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_operation_async_status_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_aas**
> Submodel get_submodel_aas(submodel_identifier, level=level, extent=extent)

Returns the Submodel

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue'  # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns the Submodel
    api_response = api_instance.get_submodel_aas(submodel_identifier, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_aas: %s\n" % e)
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

# **get_submodel_element_by_path_aas**
> SubmodelElement get_submodel_element_by_path_aas(submodel_identifier, id_short_path, level=level, extent=extent)

Returns a specific submodel element from the Submodel at a specified path

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue'  # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_aas(submodel_identifier, id_short_path, level=level,
                                                                 extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_element_by_path_aas: %s\n" % e)
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

# **get_submodel_element_by_path_metadata_aas**
> SubmodelElementMetadata get_submodel_element_by_path_metadata_aas(submodel_identifier, id_short_path, level=level)

Returns the metadata attributes if a specific submodel element from the Submodel at a specified path

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the metadata attributes if a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_metadata_aas(submodel_identifier, id_short_path,
                                                                          level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_element_by_path_metadata_aas: %s\n" % e)
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

# **get_submodel_element_by_path_path_aas**
> PathItem get_submodel_element_by_path_path_aas(submodel_identifier, id_short_path, level=level)

Returns a specific submodel element from the Submodel at a specified path in the Path notation

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns a specific submodel element from the Submodel at a specified path in the Path notation
    api_response = api_instance.get_submodel_element_by_path_path_aas(submodel_identifier, id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_element_by_path_path_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_reference_aas**
> Reference get_submodel_element_by_path_reference_aas(submodel_identifier, id_short_path, level=level)

Returns the Reference of a specific submodel element from the Submodel at a specified path in the ValueOnly representation

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
level = 'core'  # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the Reference of a specific submodel element from the Submodel at a specified path in the ValueOnly representation
    api_response = api_instance.get_submodel_element_by_path_reference_aas(submodel_identifier, id_short_path,
                                                                           level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_element_by_path_reference_aas: %s\n" % e)
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

# **get_submodel_element_by_path_value_only_aas**
> SubmodelElementValue get_submodel_element_by_path_value_only_aas(submodel_identifier, id_short_path, level=level)

Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
    api_response = api_instance.get_submodel_element_by_path_value_only_aas(submodel_identifier, id_short_path,
                                                                            level=level)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellAPIApi->get_submodel_element_by_path_value_only_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**SubmodelElementValue**](SubmodelElementValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_metadata_aas**
> SubmodelMetadata get_submodel_metadata_aas(submodel_identifier, level=level)

Returns the Submodel's metadata elements

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the Submodel's metadata elements
    api_response = api_instance.get_submodel_metadata_aas(submodel_identifier, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_metadata_aas: %s\n" % e)
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

# **get_submodel_metadata_reference_aas**
> Reference get_submodel_metadata_reference_aas(submodel_identifier, level=level)

Returns the Submodel as a Reference

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core'  # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the Submodel as a Reference
    api_response = api_instance.get_submodel_metadata_reference_aas(submodel_identifier, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_metadata_reference_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to core]

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_path_aas**
> list[PathItem] get_submodel_path_aas(submodel_identifier, level=level)

Returns the Submodel's metadata elements

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the Submodel's metadata elements
    api_response = api_instance.get_submodel_path_aas(submodel_identifier, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_path_aas: %s\n" % e)
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

# **get_submodel_value_only_aas**
> SubmodelValue get_submodel_value_only_aas(submodel_identifier, level=level, extent=extent)

Returns the Submodel's ValueOnly representation

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue'  # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns the Submodel's ValueOnly representation
    api_response = api_instance.get_submodel_value_only_aas(submodel_identifier, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_submodel_value_only_aas: %s\n" % e)
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

# **get_thumbnail**
> str get_thumbnail()



### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()

try:
    api_response = api_instance.get_thumbnail()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->get_thumbnail: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_async_aas**
> invoke_operation_async_aas(body, submodel_identifier, id_short_path)

Synchronously invokes an Operation at a specified path

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.OperationRequest()  # OperationRequest | Operation request object
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Synchronously invokes an Operation at a specified path
    api_instance.invoke_operation_async_aas(body, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->invoke_operation_async_aas: %s\n" % e)
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

# **invoke_operation_async_value_only_aas**
> invoke_operation_async_value_only_aas(body, submodel_identifier, id_short_path)

Asynchronously invokes an Operation at a specified path

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.OperationRequestValueOnly()  # OperationRequestValueOnly | Operation request object
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Asynchronously invokes an Operation at a specified path
    api_instance.invoke_operation_async_value_only_aas(body, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->invoke_operation_async_value_only_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequestValueOnly**](OperationRequestValueOnly.md)| Operation request object | 
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

# **invoke_operation_sync_aas**
> OperationResult invoke_operation_sync_aas(body, submodel_identifier, id_short_path)

Synchronously invokes an Operation at a specified path

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.OperationRequest()  # OperationRequest | Operation request object
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Synchronously invokes an Operation at a specified path
    api_response = api_instance.invoke_operation_sync_aas(body, submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->invoke_operation_sync_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequest**](OperationRequest.md)| Operation request object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_sync_value_only_aas**
> OperationResultValueOnly invoke_operation_sync_value_only_aas(body, submodel_identifier, id_short_path)

Synchronously invokes an Operation at a specified path

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.OperationRequestValueOnly()  # OperationRequestValueOnly | Operation request object
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Synchronously invokes an Operation at a specified path
    api_response = api_instance.invoke_operation_sync_value_only_aas(body, submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->invoke_operation_sync_value_only_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequestValueOnly**](OperationRequestValueOnly.md)| Operation request object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **id_short_path** | **str**| IdShort path to the submodel element (dot-separated) | 

### Return type

[**OperationResultValueOnly**](OperationResultValueOnly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_submodel_aas**
> patch_submodel_aas(body, submodel_identifier, level=level)

Updates the Submodel

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.Submodel()  # Submodel | Submodel object
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core'  # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the Submodel
    api_instance.patch_submodel_aas(body, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->patch_submodel_aas: %s\n" % e)
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

# **patch_submodel_element_value_by_path_aas**
> patch_submodel_element_value_by_path_aas(body, submodel_identifier, id_short_path, level=level)

Updates an existing submodel element value at a specified path within submodel elements hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.SubmodelElement()  # SubmodelElement | The updated value of the submodel element
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates an existing submodel element value at a specified path within submodel elements hierarchy
    api_instance.patch_submodel_element_value_by_path_aas(body, submodel_identifier, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->patch_submodel_element_value_by_path_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| The updated value of the submodel element | 
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

# **patch_submodel_element_value_by_path_metadata_aas**
> patch_submodel_element_value_by_path_metadata_aas(body, submodel_identifier, id_short_path, level=level)

Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.SubmodelElementMetadata()  # SubmodelElementMetadata | The updated metadata attributes of the submodel element
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy
    api_instance.patch_submodel_element_value_by_path_metadata_aas(body, submodel_identifier, id_short_path,
                                                                   level=level)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellAPIApi->patch_submodel_element_value_by_path_metadata_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElementMetadata**](SubmodelElementMetadata.md)| The updated metadata attributes of the submodel element | 
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

# **patch_submodel_element_value_by_path_value_only_aas**
> patch_submodel_element_value_by_path_value_only_aas(body, submodel_identifier, id_short_path, level=level)

Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.SubmodelElementValue()  # SubmodelElementValue | The updated value of the submodel element
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy
    api_instance.patch_submodel_element_value_by_path_value_only_aas(body, submodel_identifier, id_short_path,
                                                                     level=level)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellAPIApi->patch_submodel_element_value_by_path_value_only_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElementValue**](SubmodelElementValue.md)| The updated value of the submodel element | 
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

# **patch_submodel_metadata_aas**
> patch_submodel_metadata_aas(body, submodel_identifier, level=level)

Updates the metadata attributes of the Submodel

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.SubmodelMetadata()  # SubmodelMetadata | Submodel object
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core'  # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the metadata attributes of the Submodel
    api_instance.patch_submodel_metadata_aas(body, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->patch_submodel_metadata_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelMetadata**](SubmodelMetadata.md)| Submodel object | 
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

# **patch_submodel_value_only_aas**
> patch_submodel_value_only_aas(body, submodel_identifier, level=level)

Updates teh values of the Submodel

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.SubmodelValue()  # SubmodelValue | Submodel object in the ValueOnly representation
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core'  # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates teh values of the Submodel
    api_instance.patch_submodel_value_only_aas(body, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->patch_submodel_value_only_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelValue**](SubmodelValue.md)| Submodel object in the ValueOnly representation | 
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

# **post_submodel_element_aas**
> SubmodelElement post_submodel_element_aas(body, submodel_identifier)

Creates a new submodel element

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.SubmodelElement()  # SubmodelElement | Requested submodel element
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Creates a new submodel element
    api_response = api_instance.post_submodel_element_aas(body, submodel_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->post_submodel_element_aas: %s\n" % e)
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

# **post_submodel_element_by_path_aas**
> SubmodelElement post_submodel_element_by_path_aas(body, submodel_identifier, id_short_path)

Creates a new submodel element at a specified path within submodel elements hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.SubmodelElement()  # SubmodelElement | Requested submodel element
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Creates a new submodel element at a specified path within submodel elements hierarchy
    api_response = api_instance.post_submodel_element_by_path_aas(body, submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->post_submodel_element_by_path_aas: %s\n" % e)
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

# **post_submodel_reference**
> Reference post_submodel_reference(body)

Creates a submodel reference at the Asset Administration Shell

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.Reference()  # Reference | Reference to the Submodel

try:
    # Creates a submodel reference at the Asset Administration Shell
    api_response = api_instance.post_submodel_reference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->post_submodel_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Reference**](Reference.md)| Reference to the Submodel | 

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_administration_shell**
> put_asset_administration_shell(body)

Updates an existing Asset Administration Shell

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.AssetAdministrationShell()  # AssetAdministrationShell | Asset Administration Shell object

try:
    # Updates an existing Asset Administration Shell
    api_instance.put_asset_administration_shell(body)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->put_asset_administration_shell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetAdministrationShell**](AssetAdministrationShell.md)| Asset Administration Shell object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_information**
> put_asset_information(body)

Updates the Asset Information

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.AssetInformation()  # AssetInformation | Asset Information object

try:
    # Updates the Asset Information
    api_instance.put_asset_information(body)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->put_asset_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetInformation**](AssetInformation.md)| Asset Information object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file_by_path_aas**
> put_file_by_path_aas(file_name, file, submodel_identifier, id_short_path)

Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
file_name = 'file_name_example'  # str | 
file = 'file_example'  # str | 
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.put_file_by_path_aas(file_name, file, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->put_file_by_path_aas: %s\n" % e)
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

# **put_submodel_aas**
> put_submodel_aas(body, submodel_identifier, level=level)

Updates the Submodel

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.Submodel()  # Submodel | Submodel object
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep'  # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates the Submodel
    api_instance.put_submodel_aas(body, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->put_submodel_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Submodel**](Submodel.md)| Submodel object | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_submodel_element_by_path_aas**
> put_submodel_element_by_path_aas(body, submodel_identifier, id_short_path)

Updates an existing submodel element at a specified path within submodel elements hierarchy

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
body = aas_python_http_client.SubmodelElement()  # SubmodelElement | Requested submodel element
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example'  # str | IdShort path to the submodel element (dot-separated)

try:
    # Updates an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.put_submodel_element_by_path_aas(body, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->put_submodel_element_by_path_aas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
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

# **put_thumbnail**
> put_thumbnail(file_name, file)



### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellAPIApi()
file_name = 'file_name_example'  # str | 
file = 'file_example'  # str | 

try:
    api_instance.put_thumbnail(file_name, file)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellAPIApi->put_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

