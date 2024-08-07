# swagger_client.AssetAdministrationShellBasicDiscoveryAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_asset_links_by_id**](AssetAdministrationShellBasicDiscoveryAPIApi.md#delete_all_asset_links_by_id) | **DELETE** /lookup/shells/{aasIdentifier} | Deletes all specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content
[**get_all_asset_administration_shell_ids_by_asset_link**](AssetAdministrationShellBasicDiscoveryAPIApi.md#get_all_asset_administration_shell_ids_by_asset_link) | **GET** /lookup/shells | Returns a list of Asset Administration Shell ids linked to specific Asset identifiers
[**get_all_asset_links_by_id**](AssetAdministrationShellBasicDiscoveryAPIApi.md#get_all_asset_links_by_id) | **GET** /lookup/shells/{aasIdentifier} | Returns a list of specific Asset identifiers based on an Asset Administration Shell id to edit discoverable content
[**post_all_asset_links_by_id**](AssetAdministrationShellBasicDiscoveryAPIApi.md#post_all_asset_links_by_id) | **POST** /lookup/shells/{aasIdentifier} | Creates specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content

# **delete_all_asset_links_by_id**
> delete_all_asset_links_by_id(aas_identifier)

Deletes all specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellBasicDiscoveryAPIApi()
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes all specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content
    api_instance.delete_all_asset_links_by_id(aas_identifier)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellBasicDiscoveryAPIApi->delete_all_asset_links_by_id: %s\n" % e)
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

# **get_all_asset_administration_shell_ids_by_asset_link**
> InlineResponse200 get_all_asset_administration_shell_ids_by_asset_link(asset_ids=asset_ids, limit=limit, cursor=cursor)

Returns a list of Asset Administration Shell ids linked to specific Asset identifiers

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellBasicDiscoveryAPIApi()
asset_ids = [
    'asset_ids_example']  # list[str] | A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId) (optional)
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns a list of Asset Administration Shell ids linked to specific Asset identifiers
    api_response = api_instance.get_all_asset_administration_shell_ids_by_asset_link(asset_ids=asset_ids, limit=limit,
                                                                                     cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling AssetAdministrationShellBasicDiscoveryAPIApi->get_all_asset_administration_shell_ids_by_asset_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | [**list[str]**](str.md)| A list of specific Asset identifiers. Each Asset identifier is a base64-url-encoded [SpecificAssetId](https://api.swaggerhub.com/domains/Plattform_i40/Part1-MetaModel-Schemas/V3.0.1#/components/schemas/SpecificAssetId) | [optional] 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_asset_links_by_id**
> list[SpecificAssetId] get_all_asset_links_by_id(aas_identifier)

Returns a list of specific Asset identifiers based on an Asset Administration Shell id to edit discoverable content

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellBasicDiscoveryAPIApi()
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns a list of specific Asset identifiers based on an Asset Administration Shell id to edit discoverable content
    api_response = api_instance.get_all_asset_links_by_id(aas_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellBasicDiscoveryAPIApi->get_all_asset_links_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**list[SpecificAssetId]**](SpecificAssetId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_all_asset_links_by_id**
> list[SpecificAssetId] post_all_asset_links_by_id(body, aas_identifier)

Creates specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.AssetAdministrationShellBasicDiscoveryAPIApi()
body = [aas_python_http_client.SpecificAssetId()]  # list[SpecificAssetId] | A list of specific Asset identifiers
aas_identifier = 'aas_identifier_example'  # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Creates specific Asset identifiers linked to an Asset Administration Shell to edit discoverable content
    api_response = api_instance.post_all_asset_links_by_id(body, aas_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAdministrationShellBasicDiscoveryAPIApi->post_all_asset_links_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SpecificAssetId]**](SpecificAssetId.md)| A list of specific Asset identifiers | 
 **aas_identifier** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**list[SpecificAssetId]**](SpecificAssetId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

