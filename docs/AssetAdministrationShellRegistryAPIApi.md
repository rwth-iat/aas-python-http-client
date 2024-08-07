# swagger_client.AssetAdministrationShellRegistryAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset_administration_shell_descriptor_by_id**](AssetAdministrationShellRegistryAPIApi.md#delete_asset_administration_shell_descriptor_by_id) | **DELETE** /shell-descriptors/{aasIdentifier} | Deletes an Asset Administration Shell Descriptor, i.e. de-registers an AAS
[**delete_submodel_descriptor_by_id_through_superpath**](AssetAdministrationShellRegistryAPIApi.md#delete_submodel_descriptor_by_id_through_superpath) | **DELETE** /shell-descriptors/{aasIdentifier}/submodel-descriptors/{submodelIdentifier} | Deletes a Submodel Descriptor, i.e. de-registers a submodel
[**get_all_asset_administration_shell_descriptors**](AssetAdministrationShellRegistryAPIApi.md#get_all_asset_administration_shell_descriptors) | **GET** /shell-descriptors | Returns all Asset Administration Shell Descriptors
[**get_all_submodel_descriptors_through_superpath**](AssetAdministrationShellRegistryAPIApi.md#get_all_submodel_descriptors_through_superpath) | **GET** /shell-descriptors/{aasIdentifier}/submodel-descriptors | Returns all Submodel Descriptors
[**get_asset_administration_shell_descriptor_by_id**](AssetAdministrationShellRegistryAPIApi.md#get_asset_administration_shell_descriptor_by_id) | **GET** /shell-descriptors/{aasIdentifier} | Returns a specific Asset Administration Shell Descriptor
[**get_submodel_descriptor_by_id_through_superpath**](AssetAdministrationShellRegistryAPIApi.md#get_submodel_descriptor_by_id_through_superpath) | **GET** /shell-descriptors/{aasIdentifier}/submodel-descriptors/{submodelIdentifier} | Returns a specific Submodel Descriptor
[**post_asset_administration_shell_descriptor**](AssetAdministrationShellRegistryAPIApi.md#post_asset_administration_shell_descriptor) | **POST** /shell-descriptors | Creates a new Asset Administration Shell Descriptor, i.e. registers an AAS
[**post_submodel_descriptor_through_superpath**](AssetAdministrationShellRegistryAPIApi.md#post_submodel_descriptor_through_superpath) | **POST** /shell-descriptors/{aasIdentifier}/submodel-descriptors | Creates a new Submodel Descriptor, i.e. registers a submodel
[**put_asset_administration_shell_descriptor_by_id**](AssetAdministrationShellRegistryAPIApi.md#put_asset_administration_shell_descriptor_by_id) | **PUT** /shell-descriptors/{aasIdentifier} | Updates an existing Asset Administration Shell Descriptor
[**put_submodel_descriptor_by_id_through_superpath**](AssetAdministrationShellRegistryAPIApi.md#put_submodel_descriptor_by_id_through_superpath) | **PUT** /shell-descriptors/{aasIdentifier}/submodel-descriptors/{submodelIdentifier} | Updates an existing Submodel Descriptor

# **delete_asset_administration_shell_descriptor_by_id**
> delete_asset_administration_shell_descriptor_by_id(aas_identifier)

Deletes an Asset Administration Shell Descriptor, i.e. de-registers an AAS

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
aas_identifier = 'B'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes an Asset Administration Shell Descriptor, i.e. de-registers an AAS
    api_instance.delete_asset_administration_shell_descriptor_by_id(aas_identifier)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->delete_asset_administration_shell_descriptor_by_id: %s\n" % e)
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

# **delete_submodel_descriptor_by_id_through_superpath**
> delete_submodel_descriptor_by_id_through_superpath(aas_identifier, submodel_identifier)

Deletes a Submodel Descriptor, i.e. de-registers a submodel

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes a Submodel Descriptor, i.e. de-registers a submodel
    api_instance.delete_submodel_descriptor_by_id_through_superpath(aas_identifier, submodel_identifier)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->delete_submodel_descriptor_by_id_through_superpath: %s\n" % e)
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

# **get_all_asset_administration_shell_descriptors**
> GetAssetAdministrationShellDescriptorsResult get_all_asset_administration_shell_descriptors(limit=limit, cursor=cursor, asset_kind=asset_kind, asset_type=asset_type)

Returns all Asset Administration Shell Descriptors

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)
asset_kind = aas_python_http_client.AssetKind()  # AssetKind | The Asset's kind (Instance or Type) (optional)
asset_type = 'asset_type_example'  # str | The Asset's type (UTF8-BASE64-URL-encoded) (optional)

try:
    # Returns all Asset Administration Shell Descriptors
    api_response = api_instance.get_all_asset_administration_shell_descriptors(limit=limit, cursor=cursor,
                                                                               asset_kind=asset_kind,
                                                                               asset_type=asset_type)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->get_all_asset_administration_shell_descriptors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 
 **asset_kind** | [**AssetKind**](.md)| The Asset&#x27;s kind (Instance or Type) | [optional] 
 **asset_type** | **str**| The Asset&#x27;s type (UTF8-BASE64-URL-encoded) | [optional] 

### Return type

[**GetAssetAdministrationShellDescriptorsResult**](GetAssetAdministrationShellDescriptorsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submodel_descriptors_through_superpath**
> GetSubmodelDescriptorsResult get_all_submodel_descriptors_through_superpath(aas_identifier, limit=limit, cursor=cursor)

Returns all Submodel Descriptors

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns all Submodel Descriptors
    api_response = api_instance.get_all_submodel_descriptors_through_superpath(aas_identifier, limit=limit,
                                                                               cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->get_all_submodel_descriptors_through_superpath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
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

# **get_asset_administration_shell_descriptor_by_id**
> AssetAdministrationShellDescriptor get_asset_administration_shell_descriptor_by_id(aas_identifier)

Returns a specific Asset Administration Shell Descriptor

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
aas_identifier = 'B'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns a specific Asset Administration Shell Descriptor
    api_response = api_instance.get_asset_administration_shell_descriptor_by_id(aas_identifier)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->get_asset_administration_shell_descriptor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**AssetAdministrationShellDescriptor**](AssetAdministrationShellDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submodel_descriptor_by_id_through_superpath**
> SubmodelDescriptor get_submodel_descriptor_by_id_through_superpath(aas_identifier, submodel_identifier)

Returns a specific Submodel Descriptor

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns a specific Submodel Descriptor
    api_response = api_instance.get_submodel_descriptor_by_id_through_superpath(aas_identifier, submodel_identifier)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->get_submodel_descriptor_by_id_through_superpath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 
 **submodel_identifier** | **str**| The Submodel’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**SubmodelDescriptor**](SubmodelDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset_administration_shell_descriptor**
> AssetAdministrationShellDescriptor post_asset_administration_shell_descriptor(body)

Creates a new Asset Administration Shell Descriptor, i.e. registers an AAS

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
body = aas_python_http_client.AssetAdministrationShellDescriptor()  # AssetAdministrationShellDescriptor | Asset Administration Shell Descriptor object

try:
    # Creates a new Asset Administration Shell Descriptor, i.e. registers an AAS
    api_response = api_instance.post_asset_administration_shell_descriptor(body)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->post_asset_administration_shell_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetAdministrationShellDescriptor**](AssetAdministrationShellDescriptor.md)| Asset Administration Shell Descriptor object | 

### Return type

[**AssetAdministrationShellDescriptor**](AssetAdministrationShellDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_submodel_descriptor_through_superpath**
> SubmodelDescriptor post_submodel_descriptor_through_superpath(body, aas_identifier)

Creates a new Submodel Descriptor, i.e. registers a submodel

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
body = aas_python_http_client.SubmodelDescriptor()  # SubmodelDescriptor | Submodel Descriptor object
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Creates a new Submodel Descriptor, i.e. registers a submodel
    api_response = api_instance.post_submodel_descriptor_through_superpath(body, aas_identifier)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->post_submodel_descriptor_through_superpath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelDescriptor**](SubmodelDescriptor.md)| Submodel Descriptor object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**SubmodelDescriptor**](SubmodelDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_administration_shell_descriptor_by_id**
> put_asset_administration_shell_descriptor_by_id(body, aas_identifier)

Updates an existing Asset Administration Shell Descriptor

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
body = aas_python_http_client.AssetAdministrationShellDescriptor()  # AssetAdministrationShellDescriptor | Asset Administration Shell Descriptor object
aas_identifier = 'B'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Updates an existing Asset Administration Shell Descriptor
    api_instance.put_asset_administration_shell_descriptor_by_id(body, aas_identifier)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->put_asset_administration_shell_descriptor_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssetAdministrationShellDescriptor**](AssetAdministrationShellDescriptor.md)| Asset Administration Shell Descriptor object | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_submodel_descriptor_by_id_through_superpath**
> put_submodel_descriptor_by_id_through_superpath(body, aas_identifier, submodel_identifier)

Updates an existing Submodel Descriptor

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellRegistryAPIApi()
body = aas_python_http_client.SubmodelDescriptor()  # SubmodelDescriptor | Submodel Descriptor object
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)
submodel_identifier = 'submodel_identifier_example'  # str | The Submodel’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Updates an existing Submodel Descriptor
    api_instance.put_submodel_descriptor_by_id_through_superpath(body, aas_identifier, submodel_identifier)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellRegistryAPIApi->put_submodel_descriptor_by_id_through_superpath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubmodelDescriptor**](SubmodelDescriptor.md)| Submodel Descriptor object | 
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

