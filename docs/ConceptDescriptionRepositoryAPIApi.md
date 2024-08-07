# swagger_client.ConceptDescriptionRepositoryAPIApi

All URIs are relative to *{protocol}://{host_name}:{port}/api/{version_prefix}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_concept_description_by_id**](ConceptDescriptionRepositoryAPIApi.md#delete_concept_description_by_id) | **DELETE** /concept-descriptions/{cdIdentifier} | Deletes a Concept Description
[**get_all_concept_descriptions**](ConceptDescriptionRepositoryAPIApi.md#get_all_concept_descriptions) | **GET** /concept-descriptions | Returns all Concept Descriptions
[**get_concept_description_by_id**](ConceptDescriptionRepositoryAPIApi.md#get_concept_description_by_id) | **GET** /concept-descriptions/{cdIdentifier} | Returns a specific Concept Description
[**post_concept_description**](ConceptDescriptionRepositoryAPIApi.md#post_concept_description) | **POST** /concept-descriptions | Creates a new Concept Description
[**put_concept_description_by_id**](ConceptDescriptionRepositoryAPIApi.md#put_concept_description_by_id) | **PUT** /concept-descriptions/{cdIdentifier} | Updates an existing Concept Description

# **delete_concept_description_by_id**
> delete_concept_description_by_id(cd_identifier)

Deletes a Concept Description

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.ConceptDescriptionRepositoryAPIApi()
cd_identifier = 'B'  # str | The Concept Description’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Deletes a Concept Description
    api_instance.delete_concept_description_by_id(cd_identifier)
except ApiException as e:
    print("Exception when calling ConceptDescriptionRepositoryAPIApi->delete_concept_description_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cd_identifier** | **str**| The Concept Description’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_concept_descriptions**
> GetConceptDescriptionsResult get_all_concept_descriptions(id_short=id_short, is_case_of=is_case_of, data_specification_ref=data_specification_ref, limit=limit, cursor=cursor)

Returns all Concept Descriptions

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.ConceptDescriptionRepositoryAPIApi()
id_short = 'id_short_example'  # str | The Concept Description’s IdShort (optional)
is_case_of = 'B'  # str | IsCaseOf reference (UTF8-BASE64-URL-encoded) (optional)
data_specification_ref = 'B'  # str | DataSpecification reference (UTF8-BASE64-URL-encoded) (optional)
limit = 56  # int | The maximum number of elements in the response array (optional)
cursor = 'cursor_example'  # str | A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue (optional)

try:
    # Returns all Concept Descriptions
    api_response = api_instance.get_all_concept_descriptions(id_short=id_short, is_case_of=is_case_of,
                                                             data_specification_ref=data_specification_ref, limit=limit,
                                                             cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptDescriptionRepositoryAPIApi->get_all_concept_descriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_short** | **str**| The Concept Description’s IdShort | [optional] 
 **is_case_of** | **str**| IsCaseOf reference (UTF8-BASE64-URL-encoded) | [optional] 
 **data_specification_ref** | **str**| DataSpecification reference (UTF8-BASE64-URL-encoded) | [optional] 
 **limit** | **int**| The maximum number of elements in the response array | [optional] 
 **cursor** | **str**| A server-generated identifier retrieved from pagingMetadata that specifies from which position the result listing should continue | [optional] 

### Return type

[**GetConceptDescriptionsResult**](GetConceptDescriptionsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concept_description_by_id**
> ConceptDescription get_concept_description_by_id(cd_identifier)

Returns a specific Concept Description

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.ConceptDescriptionRepositoryAPIApi()
cd_identifier = 'B'  # str | The Concept Description’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Returns a specific Concept Description
    api_response = api_instance.get_concept_description_by_id(cd_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptDescriptionRepositoryAPIApi->get_concept_description_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cd_identifier** | **str**| The Concept Description’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

[**ConceptDescription**](ConceptDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_concept_description**
> ConceptDescription post_concept_description(body)

Creates a new Concept Description

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.ConceptDescriptionRepositoryAPIApi()
body = aas_python_http_client.ConceptDescription()  # ConceptDescription | Concept Description object

try:
    # Creates a new Concept Description
    api_response = api_instance.post_concept_description(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptDescriptionRepositoryAPIApi->post_concept_description: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConceptDescription**](ConceptDescription.md)| Concept Description object | 

### Return type

[**ConceptDescription**](ConceptDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_concept_description_by_id**
> put_concept_description_by_id(body, cd_identifier)

Updates an existing Concept Description

### Example

```python
from __future__ import print_function
import time
import aas_python_http_client
from aas_python_http_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = aas_python_http_client.ConceptDescriptionRepositoryAPIApi()
body = aas_python_http_client.ConceptDescription()  # ConceptDescription | Concept Description object
cd_identifier = 'B'  # str | The Concept Description’s unique id (UTF8-BASE64-URL-encoded)

try:
    # Updates an existing Concept Description
    api_instance.put_concept_description_by_id(body, cd_identifier)
except ApiException as e:
    print("Exception when calling ConceptDescriptionRepositoryAPIApi->put_concept_description_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConceptDescription**](ConceptDescription.md)| Concept Description object | 
 **cd_identifier** | **str**| The Concept Description’s unique id (UTF8-BASE64-URL-encoded) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

