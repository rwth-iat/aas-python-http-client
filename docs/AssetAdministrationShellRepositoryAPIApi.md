# swagger_client.AssetAdministrationShellRepositoryAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset_administration_shell_by_id**](AssetAdministrationShellRepositoryAPIApi.md#delete_asset_administration_shell_by_id) | **DELETE** /shells/{aasIdentifier} | Deletes an Asset Administration Shell
[**delete_file_by_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#delete_file_by_path_aas_repository) | **DELETE** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
[**delete_submodel_by_id_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#delete_submodel_by_id_aas_repository) | **DELETE** /shells/{aasIdentifier}/submodels/{submodelIdentifier} | Deletes the submodel from the Asset Administration Shell and the Repository.
[**delete_submodel_element_by_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#delete_submodel_element_by_path_aas_repository) | **DELETE** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Deletes a submodel element at a specified path within the submodel elements hierarchy
[**delete_submodel_reference_by_id_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#delete_submodel_reference_by_id_aas_repository) | **DELETE** /shells/{aasIdentifier}/submodel-refs/{submodelIdentifier} | Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!
[**delete_thumbnail_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#delete_thumbnail_aas_repository) | **DELETE** /shells/{aasIdentifier}/asset-information/thumbnail | 
[**get_all_asset_administration_shells**](AssetAdministrationShellRepositoryAPIApi.md#get_all_asset_administration_shells) | **GET** /shells | Returns all Asset Administration Shells
[**get_all_asset_administration_shells_reference**](AssetAdministrationShellRepositoryAPIApi.md#get_all_asset_administration_shells_reference) | **GET** /shells/$reference | Returns References to all Asset Administration Shells
[**get_all_submodel_elements_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_all_submodel_elements_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements | Returns all submodel elements including their hierarchy
[**get_all_submodel_elements_metadata_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_all_submodel_elements_metadata_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/$metadata | Returns all submodel elements including their hierarchy
[**get_all_submodel_elements_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_all_submodel_elements_path_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/$path | Returns all submodel elements including their hierarchy
[**get_all_submodel_elements_reference_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_all_submodel_elements_reference_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/$reference | Returns all submodel elements as a list of References
[**get_all_submodel_elements_value_only_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_all_submodel_elements_value_only_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/$value | Returns all submodel elements including their hierarchy in the ValueOnly representation
[**get_all_submodel_references_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_all_submodel_references_aas_repository) | **GET** /shells/{aasIdentifier}/submodel-refs | Returns all submodel references
[**get_asset_administration_shell_by_id**](AssetAdministrationShellRepositoryAPIApi.md#get_asset_administration_shell_by_id) | **GET** /shells/{aasIdentifier} | Returns a specific Asset Administration Shell
[**get_asset_administration_shell_by_id_reference_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_asset_administration_shell_by_id_reference_aas_repository) | **GET** /shells/{aasIdentifier}/$reference | Returns a specific Asset Administration Shell as a Reference
[**get_asset_information_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_asset_information_aas_repository) | **GET** /shells/{aasIdentifier}/asset-information | Returns the Asset Information
[**get_file_by_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_file_by_path_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Downloads file content from a specific submodel element from the Submodel at a specified path
[**get_operation_async_result_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_operation_async_result_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-results/{handleId} | Returns the Operation result of an asynchronous invoked Operation
[**get_operation_async_result_value_only_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_operation_async_result_value_only_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-results/{handleId}/$value | Returns the ValueOnly notation of the Operation result of an asynchronous invoked Operation
[**get_operation_async_status_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_operation_async_status_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/operation-status/{handleId} | Returns the Operation status of an asynchronous invoked Operation
[**get_submodel_by_id_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_by_id_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier} | Returns the Submodel
[**get_submodel_by_id_metadata_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_by_id_metadata_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/$metadata | Returns the Submodel&#x27;s metadata elements
[**get_submodel_by_id_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_by_id_path_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/$path | Returns the Submodel&#x27;s metadata elements
[**get_submodel_by_id_reference_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_by_id_reference_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/$reference | Returns the Submodel as a Reference
[**get_submodel_by_id_value_only_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_by_id_value_only_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/$value | Returns the Submodel&#x27;s ValueOnly representation
[**get_submodel_element_by_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_element_by_path_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Returns a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_metadata_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_element_by_path_metadata_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$metadata | Returns the metadata attributes if a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_element_by_path_path_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$path | Returns a specific submodel element from the Submodel at a specified path in the Path notation
[**get_submodel_element_by_path_reference_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_element_by_path_reference_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$reference | Returns the Reference of a specific submodel element from the Submodel at a specified path
[**get_submodel_element_by_path_value_only_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_submodel_element_by_path_value_only_aas_repository) | **GET** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$value | Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
[**get_thumbnail_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#get_thumbnail_aas_repository) | **GET** /shells/{aasIdentifier}/asset-information/thumbnail | 
[**invoke_operation_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#invoke_operation_aas_repository) | **POST** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke | Synchronously invokes an Operation at a specified path
[**invoke_operation_async_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#invoke_operation_async_aas_repository) | **POST** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke-async | Asynchronously invokes an Operation at a specified path
[**invoke_operation_async_value_only_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#invoke_operation_async_value_only_aas_repository) | **POST** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke-async/$value | Asynchronously invokes an Operation at a specified path
[**invoke_operation_value_only_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#invoke_operation_value_only_aas_repository) | **POST** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/invoke/$value | Synchronously invokes an Operation at a specified path
[**patch_submodel_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#patch_submodel_aas_repository) | **PATCH** /shells/{aasIdentifier}/submodels/{submodelIdentifier} | Updates the Submodel
[**patch_submodel_by_id_metadata_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#patch_submodel_by_id_metadata_aas_repository) | **PATCH** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/$metadata | Updates the metadata attributes of the Submodel
[**patch_submodel_by_id_value_only_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#patch_submodel_by_id_value_only_aas_repository) | **PATCH** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/$value | Updates teh values of the Submodel
[**patch_submodel_element_value_by_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#patch_submodel_element_value_by_path_aas_repository) | **PATCH** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Updates an existing submodel element value at a specified path within submodel elements hierarchy
[**patch_submodel_element_value_by_path_metadata**](AssetAdministrationShellRepositoryAPIApi.md#patch_submodel_element_value_by_path_metadata) | **PATCH** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$metadata | Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy
[**patch_submodel_element_value_by_path_value_only**](AssetAdministrationShellRepositoryAPIApi.md#patch_submodel_element_value_by_path_value_only) | **PATCH** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/$value | Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy
[**post_asset_administration_shell**](AssetAdministrationShellRepositoryAPIApi.md#post_asset_administration_shell) | **POST** /shells | Creates a new Asset Administration Shell
[**post_submodel_element_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#post_submodel_element_aas_repository) | **POST** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements | Creates a new submodel element
[**post_submodel_element_by_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#post_submodel_element_by_path_aas_repository) | **POST** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Creates a new submodel element at a specified path within submodel elements hierarchy
[**post_submodel_reference_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#post_submodel_reference_aas_repository) | **POST** /shells/{aasIdentifier}/submodel-refs | Creates a submodel reference at the Asset Administration Shell
[**put_asset_administration_shell_by_id**](AssetAdministrationShellRepositoryAPIApi.md#put_asset_administration_shell_by_id) | **PUT** /shells/{aasIdentifier} | Updates an existing Asset Administration Shell
[**put_asset_information_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#put_asset_information_aas_repository) | **PUT** /shells/{aasIdentifier}/asset-information | Updates the Asset Information
[**put_file_by_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#put_file_by_path_aas_repository) | **PUT** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath}/attachment | Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
[**put_submodel_by_id_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#put_submodel_by_id_aas_repository) | **PUT** /shells/{aasIdentifier}/submodels/{submodelIdentifier} | Updates the Submodel
[**put_submodel_element_by_path_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#put_submodel_element_by_path_aas_repository) | **PUT** /shells/{aasIdentifier}/submodels/{submodelIdentifier}/submodel-elements/{idShortPath} | Updates an existing submodel element at a specified path within submodel elements hierarchy
[**put_thumbnail_aas_repository**](AssetAdministrationShellRepositoryAPIApi.md#put_thumbnail_aas_repository) | **PUT** /shells/{aasIdentifier}/asset-information/thumbnail | 

# **delete_asset_administration_shell_by_id**
> delete_asset_administration_shell_by_id(aas_identifier)

Deletes an Asset Administration Shell

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes an Asset Administration Shell
    api_instance.delete_asset_administration_shell_by_id(aas_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->delete_asset_administration_shell_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_by_path_aas_repository**
> delete_file_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path)

Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Deletes file content of an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.delete_file_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->delete_file_by_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **delete_submodel_by_id_aas_repository**
> delete_submodel_by_id_aas_repository(aas_identifier, submodel_identifier)

Deletes the submodel from the Asset Administration Shell and the Repository.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes the submodel from the Asset Administration Shell and the Repository.
    api_instance.delete_submodel_by_id_aas_repository(aas_identifier, submodel_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->delete_submodel_by_id_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_submodel_element_by_path_aas_repository**
> delete_submodel_element_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path)

Deletes a submodel element at a specified path within the submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Deletes a submodel element at a specified path within the submodel elements hierarchy
    api_instance.delete_submodel_element_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->delete_submodel_element_by_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **delete_submodel_reference_by_id_aas_repository**
> delete_submodel_reference_by_id_aas_repository(aas_identifier, submodel_identifier)

Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes the submodel reference from the Asset Administration Shell. Does not delete the submodel itself!
    api_instance.delete_submodel_reference_by_id_aas_repository(aas_identifier, submodel_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->delete_submodel_reference_by_id_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_thumbnail_aas_repository**
> delete_thumbnail_aas_repository(aas_identifier)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    api_instance.delete_thumbnail_aas_repository(aas_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->delete_thumbnail_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_asset_administration_shells**
> GetAssetAdministrationShellsResult get_all_asset_administration_shells(asset_ids=asset_ids, id_short=id_short, limit=limit, cursor=cursor)

Returns all Asset Administration Shells

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
asset_ids = ['asset_ids_example'] # list[str] | A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId) (optional)
id_short = 'id_short_example' # str | The Asset Administration Shell’s IdShort (optional)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns all Asset Administration Shells
    api_response = api_instance.get_all_asset_administration_shells(asset_ids=asset_ids, id_short=id_short, limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_all_asset_administration_shells: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | [**list[str]**](str.md)| A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId) | [optional] 
 **id_short** | **str**| The Asset Administration Shell’s IdShort | [optional] 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 

### Return type

[**GetAssetAdministrationShellsResult**](GetAssetAdministrationShellsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_asset_administration_shells_reference**
> GetReferencesResult get_all_asset_administration_shells_reference(asset_ids=asset_ids, id_short=id_short, limit=limit, cursor=cursor)

Returns References to all Asset Administration Shells

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
asset_ids = ['asset_ids_example'] # list[str] | A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId) (optional)
id_short = 'id_short_example' # str | The Asset Administration Shell’s IdShort (optional)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns References to all Asset Administration Shells
    api_response = api_instance.get_all_asset_administration_shells_reference(asset_ids=asset_ids, id_short=id_short, limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_all_asset_administration_shells_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | [**list[str]**](str.md)| A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId) | [optional] 
 **id_short** | **str**| The Asset Administration Shell’s IdShort | [optional] 
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

# **get_all_submodel_elements_aas_repository**
> GetSubmodelElementsResult get_all_submodel_elements_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)

Returns all submodel elements including their hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_all_submodel_elements_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_all_submodel_elements_metadata_aas_repository**
> GetSubmodelElementsMetadataResult get_all_submodel_elements_metadata_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns all submodel elements including their hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_metadata_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_all_submodel_elements_metadata_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_all_submodel_elements_path_aas_repository**
> GetPathItemsResult get_all_submodel_elements_path_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)

Returns all submodel elements including their hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns all submodel elements including their hierarchy
    api_response = api_instance.get_all_submodel_elements_path_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_all_submodel_elements_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]
 **extent** | **str**| Determines to which extent the resource is being serialized | [optional] [default to withoutBlobValue]

### Return type

[**GetPathItemsResult**](GetPathItemsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_elements_reference_aas_repository**
> GetReferencesResult get_all_submodel_elements_reference_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns all submodel elements as a list of References

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns all submodel elements as a list of References
    api_response = api_instance.get_all_submodel_elements_reference_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_all_submodel_elements_reference_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_all_submodel_elements_value_only_aas_repository**
> GetSubmodelElementsValueResult get_all_submodel_elements_value_only_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level)

Returns all submodel elements including their hierarchy in the ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns all submodel elements including their hierarchy in the ValueOnly representation
    api_response = api_instance.get_all_submodel_elements_value_only_aas_repository(aas_identifier, submodel_identifier, limit=limit, cursor=cursor, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_all_submodel_elements_value_only_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **level** | **str**| Determines the structural depth of the respective resource content | [optional] [default to deep]

### Return type

[**GetSubmodelElementsValueResult**](GetSubmodelElementsValueResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_references_aas_repository**
> GetReferencesResult get_all_submodel_references_aas_repository(aas_identifier, limit=limit, cursor=cursor)

Returns all submodel references

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns all submodel references
    api_response = api_instance.get_all_submodel_references_aas_repository(aas_identifier, limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_all_submodel_references_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_asset_administration_shell_by_id**
> AssetAdministrationShell get_asset_administration_shell_by_id(aas_identifier)

Returns a specific Asset Administration Shell

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns a specific Asset Administration Shell
    api_response = api_instance.get_asset_administration_shell_by_id(aas_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_asset_administration_shell_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**AssetAdministrationShell**](AssetAdministrationShell.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_administration_shell_by_id_reference_aas_repository**
> Reference get_asset_administration_shell_by_id_reference_aas_repository(aas_identifier)

Returns a specific Asset Administration Shell as a Reference

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns a specific Asset Administration Shell as a Reference
    api_response = api_instance.get_asset_administration_shell_by_id_reference_aas_repository(aas_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_asset_administration_shell_by_id_reference_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_information_aas_repository**
> AssetInformation get_asset_information_aas_repository(aas_identifier)

Returns the Asset Information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns the Asset Information
    api_response = api_instance.get_asset_information_aas_repository(aas_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_asset_information_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**AssetInformation**](AssetInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_by_path_aas_repository**
> str get_file_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path)

Downloads file content from a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Downloads file content from a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_file_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_file_by_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_operation_async_result_aas_repository**
> OperationResult get_operation_async_result_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id)

Returns the Operation result of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation result of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_result_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_operation_async_result_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_operation_async_result_value_only_aas_repository**
> OperationResultValueOnly get_operation_async_result_value_only_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id)

Returns the ValueOnly notation of the Operation result of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the ValueOnly notation of the Operation result of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_result_value_only_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_operation_async_result_value_only_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_operation_async_status_aas_repository**
> BaseOperationResult get_operation_async_status_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id)

Returns the Operation status of an asynchronous invoked Operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
handle_id = 'handle_id_example' # str | The returned handle id of an operation’s asynchronous invocation used to request the current state of the operation’s execution (UTF8-BASE64-URL-encoded)

try:
    # Returns the Operation status of an asynchronous invoked Operation
    api_response = api_instance.get_operation_async_status_aas_repository(aas_identifier, submodel_identifier, id_short_path, handle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_operation_async_status_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_by_id_aas_repository**
> Submodel get_submodel_by_id_aas_repository(aas_identifier, submodel_identifier, level=level, extent=extent)

Returns the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns the Submodel
    api_response = api_instance.get_submodel_by_id_aas_repository(aas_identifier, submodel_identifier, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_by_id_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_by_id_metadata_aas_repository**
> SubmodelMetadata get_submodel_by_id_metadata_aas_repository(aas_identifier, submodel_identifier, level=level)

Returns the Submodel's metadata elements

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the Submodel's metadata elements
    api_response = api_instance.get_submodel_by_id_metadata_aas_repository(aas_identifier, submodel_identifier, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_by_id_metadata_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_by_id_path_aas_repository**
> list[PathItem] get_submodel_by_id_path_aas_repository(aas_identifier, submodel_identifier, level=level)

Returns the Submodel's metadata elements

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the Submodel's metadata elements
    api_response = api_instance.get_submodel_by_id_path_aas_repository(aas_identifier, submodel_identifier, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_by_id_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_by_id_reference_aas_repository**
> Reference get_submodel_by_id_reference_aas_repository(aas_identifier, submodel_identifier)

Returns the Submodel as a Reference

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns the Submodel as a Reference
    api_response = api_instance.get_submodel_by_id_reference_aas_repository(aas_identifier, submodel_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_by_id_reference_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_by_id_value_only_aas_repository**
> SubmodelValue get_submodel_by_id_value_only_aas_repository(aas_identifier, submodel_identifier, level=level, extent=extent)

Returns the Submodel's ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns the Submodel's ValueOnly representation
    api_response = api_instance.get_submodel_by_id_value_only_aas_repository(aas_identifier, submodel_identifier, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_by_id_value_only_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_aas_repository**
> SubmodelElement get_submodel_element_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level, extent=extent)

Returns a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_element_by_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_metadata_aas_repository**
> SubmodelElementMetadata get_submodel_element_by_path_metadata_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level)

Returns the metadata attributes if a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns the metadata attributes if a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_metadata_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_element_by_path_metadata_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_path_aas_repository**
> PathItem get_submodel_element_by_path_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level)

Returns a specific submodel element from the Submodel at a specified path in the Path notation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Returns a specific submodel element from the Submodel at a specified path in the Path notation
    api_response = api_instance.get_submodel_element_by_path_path_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_element_by_path_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_reference_aas_repository**
> Reference get_submodel_element_by_path_reference_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level)

Returns the Reference of a specific submodel element from the Submodel at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Returns the Reference of a specific submodel element from the Submodel at a specified path
    api_response = api_instance.get_submodel_element_by_path_reference_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_element_by_path_reference_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_submodel_element_by_path_value_only_aas_repository**
> SubmodelElementValue get_submodel_element_by_path_value_only_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level, extent=extent)

Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)
extent = 'withoutBlobValue' # str | Determines to which extent the resource is being serialized (optional) (default to withoutBlobValue)

try:
    # Returns a specific submodel element from the Submodel at a specified path in the ValueOnly representation
    api_response = api_instance.get_submodel_element_by_path_value_only_aas_repository(aas_identifier, submodel_identifier, id_short_path, level=level, extent=extent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_submodel_element_by_path_value_only_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_thumbnail_aas_repository**
> str get_thumbnail_aas_repository(aas_identifier)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    api_response = api_instance.get_thumbnail_aas_repository(aas_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->get_thumbnail_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoke_operation_aas_repository**
> OperationResult invoke_operation_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)

Synchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.OperationRequest() # OperationRequest | Operation request object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Synchronously invokes an Operation at a specified path
    api_response = api_instance.invoke_operation_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->invoke_operation_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequest**](OperationRequest.md)| Operation request object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **invoke_operation_async_aas_repository**
> invoke_operation_async_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)

Asynchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.OperationRequest() # OperationRequest | Operation request object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Asynchronously invokes an Operation at a specified path
    api_instance.invoke_operation_async_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->invoke_operation_async_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequest**](OperationRequest.md)| Operation request object | 
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

# **invoke_operation_async_value_only_aas_repository**
> invoke_operation_async_value_only_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)

Asynchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.OperationRequestValueOnly() # OperationRequestValueOnly | Operation request object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Asynchronously invokes an Operation at a specified path
    api_instance.invoke_operation_async_value_only_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->invoke_operation_async_value_only_aas_repository: %s\n" % e)
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

# **invoke_operation_value_only_aas_repository**
> OperationResultValueOnly invoke_operation_value_only_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)

Synchronously invokes an Operation at a specified path

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.OperationRequestValueOnly() # OperationRequestValueOnly | Operation request object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Synchronously invokes an Operation at a specified path
    api_response = api_instance.invoke_operation_value_only_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->invoke_operation_value_only_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OperationRequestValueOnly**](OperationRequestValueOnly.md)| Operation request object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **patch_submodel_aas_repository**
> patch_submodel_aas_repository(body, aas_identifier, submodel_identifier, level=level)

Updates the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.Submodel() # Submodel | Submodel object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the Submodel
    api_instance.patch_submodel_aas_repository(body, aas_identifier, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->patch_submodel_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Submodel**](Submodel.md)| Submodel object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **patch_submodel_by_id_metadata_aas_repository**
> patch_submodel_by_id_metadata_aas_repository(body, aas_identifier, submodel_identifier, level=level)

Updates the metadata attributes of the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.SubmodelMetadata() # SubmodelMetadata | Submodel object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates the metadata attributes of the Submodel
    api_instance.patch_submodel_by_id_metadata_aas_repository(body, aas_identifier, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->patch_submodel_by_id_metadata_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelMetadata**](SubmodelMetadata.md)| Submodel object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **patch_submodel_by_id_value_only_aas_repository**
> patch_submodel_by_id_value_only_aas_repository(body, aas_identifier, submodel_identifier, level=level)

Updates teh values of the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.SubmodelValue() # SubmodelValue | Submodel object in the ValueOnly representation
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
level = 'core' # str | Determines the structural depth of the respective resource content (optional) (default to core)

try:
    # Updates teh values of the Submodel
    api_instance.patch_submodel_by_id_value_only_aas_repository(body, aas_identifier, submodel_identifier, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->patch_submodel_by_id_value_only_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelValue**](SubmodelValue.md)| Submodel object in the ValueOnly representation | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **patch_submodel_element_value_by_path_aas_repository**
> patch_submodel_element_value_by_path_aas_repository(body, aas_identifier, submodel_identifier, id_short_path, level=level)

Updates an existing submodel element value at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | The updated value of the submodel element
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates an existing submodel element value at a specified path within submodel elements hierarchy
    api_instance.patch_submodel_element_value_by_path_aas_repository(body, aas_identifier, submodel_identifier, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->patch_submodel_element_value_by_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| The updated value of the submodel element | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **patch_submodel_element_value_by_path_metadata**
> patch_submodel_element_value_by_path_metadata(body, aas_identifier, submodel_identifier, id_short_path, level=level)

Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.SubmodelElementMetadata() # SubmodelElementMetadata | The updated metadata attributes of the submodel element
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates the metadata attributes of an existing submodel element value at a specified path within submodel elements hierarchy
    api_instance.patch_submodel_element_value_by_path_metadata(body, aas_identifier, submodel_identifier, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->patch_submodel_element_value_by_path_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElementMetadata**](SubmodelElementMetadata.md)| The updated metadata attributes of the submodel element | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **patch_submodel_element_value_by_path_value_only**
> patch_submodel_element_value_by_path_value_only(body, aas_identifier, submodel_identifier, id_short_path, level=level)

Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.SubmodelElementValue() # SubmodelElementValue | The updated value of the submodel element
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)
level = 'deep' # str | Determines the structural depth of the respective resource content (optional) (default to deep)

try:
    # Updates the value of an existing submodel element value at a specified path within submodel elements hierarchy
    api_instance.patch_submodel_element_value_by_path_value_only(body, aas_identifier, submodel_identifier, id_short_path, level=level)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->patch_submodel_element_value_by_path_value_only: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElementValue**](SubmodelElementValue.md)| The updated value of the submodel element | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **post_asset_administration_shell**
> AssetAdministrationShell post_asset_administration_shell(body)

Creates a new Asset Administration Shell

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.AssetAdministrationShell() # AssetAdministrationShell | Asset Administration Shell object

try:
    # Creates a new Asset Administration Shell
    api_response = api_instance.post_asset_administration_shell(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->post_asset_administration_shell: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetAdministrationShell**](AssetAdministrationShell.md)| Asset Administration Shell object | 

### Return type

[**AssetAdministrationShell**](AssetAdministrationShell.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submodel_element_aas_repository**
> SubmodelElement post_submodel_element_aas_repository(body, aas_identifier, submodel_identifier)

Creates a new submodel element

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Creates a new submodel element
    api_response = api_instance.post_submodel_element_aas_repository(body, aas_identifier, submodel_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->post_submodel_element_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**SubmodelElement**](SubmodelElement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submodel_element_by_path_aas_repository**
> SubmodelElement post_submodel_element_by_path_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)

Creates a new submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Creates a new submodel element at a specified path within submodel elements hierarchy
    api_response = api_instance.post_submodel_element_by_path_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->post_submodel_element_by_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **post_submodel_reference_aas_repository**
> Reference post_submodel_reference_aas_repository(body, aas_identifier)

Creates a submodel reference at the Asset Administration Shell

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.Reference() # Reference | Reference to the Submodel
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Creates a submodel reference at the Asset Administration Shell
    api_response = api_instance.post_submodel_reference_aas_repository(body, aas_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->post_submodel_reference_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Reference**](Reference.md)| Reference to the Submodel | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**Reference**](Reference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_administration_shell_by_id**
> put_asset_administration_shell_by_id(body, aas_identifier)

Updates an existing Asset Administration Shell

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.AssetAdministrationShell() # AssetAdministrationShell | Asset Administration Shell object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Updates an existing Asset Administration Shell
    api_instance.put_asset_administration_shell_by_id(body, aas_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->put_asset_administration_shell_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetAdministrationShell**](AssetAdministrationShell.md)| Asset Administration Shell object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_information_aas_repository**
> put_asset_information_aas_repository(body, aas_identifier)

Updates the Asset Information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.AssetInformation() # AssetInformation | Asset Information object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Updates the Asset Information
    api_instance.put_asset_information_aas_repository(body, aas_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->put_asset_information_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetInformation**](AssetInformation.md)| Asset Information object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file_by_path_aas_repository**
> put_file_by_path_aas_repository(file_name, file, aas_identifier, submodel_identifier, id_short_path)

Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
file_name = 'file_name_example' # str | 
file = 'file_example' # str | 
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Uploads file content to an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.put_file_by_path_aas_repository(file_name, file, aas_identifier, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->put_file_by_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **file** | **str**|  | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **put_submodel_by_id_aas_repository**
> put_submodel_by_id_aas_repository(body, aas_identifier, submodel_identifier)

Updates the Submodel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.Submodel() # Submodel | Submodel object
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Updates the Submodel
    api_instance.put_submodel_by_id_aas_repository(body, aas_identifier, submodel_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->put_submodel_by_id_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Submodel**](Submodel.md)| Submodel object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_submodel_element_by_path_aas_repository**
> put_submodel_element_by_path_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)

Updates an existing submodel element at a specified path within submodel elements hierarchy

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
body = swagger_client.SubmodelElement() # SubmodelElement | Requested submodel element
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example' # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)
id_short_path = 'id_short_path_example' # str | IdShort path to the submodel element (dot-separated)

try:
    # Updates an existing submodel element at a specified path within submodel elements hierarchy
    api_instance.put_submodel_element_by_path_aas_repository(body, aas_identifier, submodel_identifier, id_short_path)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->put_submodel_element_by_path_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelElement**](SubmodelElement.md)| Requested submodel element | 
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

# **put_thumbnail_aas_repository**
> put_thumbnail_aas_repository(file_name, file, aas_identifier)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetAdministrationShellRepositoryAPIApi()
file_name = 'file_name_example' # str | 
file = 'file_example' # str | 
aas_identifier = 'aas_identifier_example' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    api_instance.put_thumbnail_aas_repository(file_name, file, aas_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellRepositoryAPIApi->put_thumbnail_aas_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**|  | 
 **file** | **str**|  | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

