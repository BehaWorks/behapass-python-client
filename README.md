# swagger-client
Logger API description

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoggerApi(swagger_client.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_button_record(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoggerApi->get_button_record: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LoggerApi* | [**get_button_record**](docs/LoggerApi.md#get_button_record) | **GET** /logger/buttons | 
*LoggerApi* | [**get_logger_record**](docs/LoggerApi.md#get_logger_record) | **GET** /logger/ | 
*LoggerApi* | [**get_movement_record**](docs/LoggerApi.md#get_movement_record) | **GET** /logger/movements | 
*LoggerApi* | [**post_logger_record**](docs/LoggerApi.md#post_logger_record) | **POST** /logger/ | 


## Documentation For Models

 - [ButtonRecord](docs/ButtonRecord.md)
 - [LoggerRecord](docs/LoggerRecord.md)
 - [MovementRecord](docs/MovementRecord.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


