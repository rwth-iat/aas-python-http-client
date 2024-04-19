# swagger_client.AASXFileServerAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_aasxby_package_id**](AASXFileServerAPIApi.md#delete_aasxby_package_id) | **DELETE** /packages/{packageId} | Deletes a specific AASX package from the server
[**get_aasxby_package_id**](AASXFileServerAPIApi.md#get_aasxby_package_id) | **GET** /packages/{packageId} | Returns a specific AASX package from the server
[**get_all_aasx_package_ids**](AASXFileServerAPIApi.md#get_all_aasx_package_ids) | **GET** /packages | Returns a list of available AASX packages at the server
[**post_aasx_package**](AASXFileServerAPIApi.md#post_aasx_package) | **POST** /packages | Stores the AASX package at the server
[**put_aasxby_package_id**](AASXFileServerAPIApi.md#put_aasxby_package_id) | **PUT** /packages/{packageId} | Updates the AASX package at the server

# **delete_aasxby_package_id**
> delete_aasxby_package_id(package_id)

Deletes a specific AASX package from the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AASXFileServerAPIApi()
package_id = 'B' # str | The package Id (UTF8-BASE64-URL-encoded)

try:
    # Deletes a specific AASX package from the server
    api_instance.delete_aasxby_package_id(package_id)
except ApiException as e:
    print("Exception when calling AASXFileServerAPIApi->delete_aasxby_package_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**| The package Id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aasxby_package_id**
> str get_aasxby_package_id(package_id)

Returns a specific AASX package from the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AASXFileServerAPIApi()
package_id = 'B' # str | The package Id (UTF8-BASE64-URL-encoded)

try:
    # Returns a specific AASX package from the server
    api_response = api_instance.get_aasxby_package_id(package_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AASXFileServerAPIApi->get_aasxby_package_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_id** | **str**| The package Id (UTF8-BASE64-URL-encoded) | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/asset-administration-shell-package, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_aasx_package_ids**
> GetPackageDescriptionsResult get_all_aasx_package_ids(aas_id=aas_id, limit=limit, cursor=cursor)

Returns a list of available AASX packages at the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AASXFileServerAPIApi()
aas_id = 'B' # str | The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) (optional)
limit = 56 # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example' # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns a list of available AASX packages at the server
    api_response = api_instance.get_all_aasx_package_ids(aas_id=aas_id, limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AASXFileServerAPIApi->get_all_aasx_package_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_id** | **str**| The Asset Administration Shell’s unique id (UTF8-BASE64-URL-encoded) | [optional] 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 

### Return type

[**GetPackageDescriptionsResult**](GetPackageDescriptionsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_aasx_package**
> PackageDescription post_aasx_package(aas_ids, file, file_name)

Stores the AASX package at the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AASXFileServerAPIApi()
aas_ids = ['aas_ids_example'] # list[str] | 
file = 'file_example' # str | 
file_name = 'file_name_example' # str | 

try:
    # Stores the AASX package at the server
    api_response = api_instance.post_aasx_package(aas_ids, file, file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AASXFileServerAPIApi->post_aasx_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_ids** | [**list[str]**](str.md)|  | 
 **file** | **str**|  | 
 **file_name** | **str**|  | 

### Return type

[**PackageDescription**](PackageDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_aasxby_package_id**
> put_aasxby_package_id(aas_ids, file, file_name, package_id)

Updates the AASX package at the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AASXFileServerAPIApi()
aas_ids = ['aas_ids_example'] # list[str] | 
file = 'file_example' # str | 
file_name = 'file_name_example' # str | 
package_id = 'B' # str | The package Id (UTF8-BASE64-URL-encoded)

try:
    # Updates the AASX package at the server
    api_instance.put_aasxby_package_id(aas_ids, file, file_name, package_id)
except ApiException as e:
    print("Exception when calling AASXFileServerAPIApi->put_aasxby_package_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aas_ids** | [**list[str]**](str.md)|  | 
 **file** | **str**|  | 
 **file_name** | **str**|  | 
 **package_id** | **str**| The package Id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

