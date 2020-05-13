# behapass_client.LoggerApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_register_user**](LoggerApi.md#delete_register_user) | **DELETE** /logger/user/{user_id}/movements | Removes unfinished registration movements
[**get_button_record**](LoggerApi.md#get_button_record) | **GET** /logger/buttons | Returns all existing button records
[**get_movement_record**](LoggerApi.md#get_movement_record) | **GET** /logger/movements | Returns all recorded movements
[**get_register_user**](LoggerApi.md#get_register_user) | **GET** /logger/user/{user_id}/movements | Returns all recorded movements
[**get_user_data**](LoggerApi.md#get_user_data) | **GET** /logger/user/{user_id} | Returns selected user&#39;s data
[**logger_get**](LoggerApi.md#logger_get) | **GET** /logger/ | Returns all existing records
[**post_logger_record**](LoggerApi.md#post_logger_record) | **POST** /logger/ | Stores received records
[**post_lookup**](LoggerApi.md#post_lookup) | **POST** /logger/lookup | Identifies the user
[**post_register_user**](LoggerApi.md#post_register_user) | **POST** /logger/user/{user_id}/movements | Stores user data permanently once registered
[**post_user_record**](LoggerApi.md#post_user_record) | **POST** /logger/user | Creates a new user ID


# **delete_register_user**
> delete_register_user(user_id)

Removes unfinished registration movements

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
user_id = 'user_id_example' # str | 

try:
    # Removes unfinished registration movements
    api_instance.delete_register_user(user_id)
except ApiException as e:
    print("Exception when calling LoggerApi->delete_register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_button_record**
> ButtonRecord get_button_record(x_fields=x_fields)

Returns all existing button records

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Returns all existing button records
    api_response = api_instance.get_button_record(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->get_button_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ButtonRecord**](ButtonRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movement_record**
> MovementRecord get_movement_record(x_fields=x_fields)

Returns all recorded movements

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Returns all recorded movements
    api_response = api_instance.get_movement_record(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->get_movement_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**MovementRecord**](MovementRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_register_user**
> MovementRecord get_register_user(user_id, x_fields=x_fields)

Returns all recorded movements

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
user_id = 'user_id_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Returns all recorded movements
    api_response = api_instance.get_register_user(user_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->get_register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**MovementRecord**](MovementRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data**
> UserRecord get_user_data(user_id)

Returns selected user's data

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
user_id = 'user_id_example' # str | 

try:
    # Returns selected user's data
    api_response = api_instance.get_user_data(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->get_user_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserRecord**](UserRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logger_get**
> LoggerRecord logger_get(x_fields=x_fields)

Returns all existing records

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Returns all existing records
    api_response = api_instance.logger_get(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->logger_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**LoggerRecord**](LoggerRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_logger_record**
> post_logger_record(payload)

Stores received records

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
payload = behapass_client.LoggerRecord() # LoggerRecord | 

try:
    # Stores received records
    api_instance.post_logger_record(payload)
except ApiException as e:
    print("Exception when calling LoggerApi->post_logger_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**LoggerRecord**](LoggerRecord.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lookup**
> LookupResult post_lookup(payload)

Identifies the user

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
payload = behapass_client.LoggerRecord() # LoggerRecord | 

try:
    # Identifies the user
    api_response = api_instance.post_lookup(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->post_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**LoggerRecord**](LoggerRecord.md)|  | 

### Return type

[**LookupResult**](LookupResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_register_user**
> post_register_user(user_id, payload)

Stores user data permanently once registered

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
user_id = 'user_id_example' # str | 
payload = behapass_client.MovementRecord() # MovementRecord | 

try:
    # Stores user data permanently once registered
    api_instance.post_register_user(user_id, payload)
except ApiException as e:
    print("Exception when calling LoggerApi->post_register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **payload** | [**MovementRecord**](MovementRecord.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_user_record**
> UserRecord post_user_record(payload)

Creates a new user ID

### Example
```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi()
payload = behapass_client.UserData() # UserData | 

try:
    # Creates a new user ID
    api_response = api_instance.post_user_record(payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->post_user_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UserData**](UserData.md)|  | 

### Return type

[**UserRecord**](UserRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

