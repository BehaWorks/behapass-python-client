# swagger_client.LoggerApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_button_record**](LoggerApi.md#get_button_record) | **GET** /logger/buttons | 
[**get_logger_record**](LoggerApi.md#get_logger_record) | **GET** /logger/ | 
[**get_movement_record**](LoggerApi.md#get_movement_record) | **GET** /logger/movements | 
[**post_logger_record**](LoggerApi.md#post_logger_record) | **POST** /logger/ | 
[**post_lookup**](LoggerApi.md#post_lookup) | **POST** /logger/lookup | 


# **get_button_record**
> ButtonRecord get_button_record(x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoggerApi()
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
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

# **get_logger_record**
> LoggerRecord get_logger_record(x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoggerApi()
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_logger_record(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->get_logger_record: %s\n" % e)
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

# **get_movement_record**
> MovementRecord get_movement_record(x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoggerApi()
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
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

# **post_logger_record**
> post_logger_record(payload)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoggerApi()
payload = swagger_client.LoggerRecord() # LoggerRecord | 

try:
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
> LookupResult post_lookup(payload, x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoggerApi()
payload = swagger_client.LoggerRecord() # LoggerRecord | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.post_lookup(payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->post_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**LoggerRecord**](LoggerRecord.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**LookupResult**](LookupResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

