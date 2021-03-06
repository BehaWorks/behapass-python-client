# behapass-client
BehaPass API description

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1
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
import behapass_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import behapass_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import behapass_client
from behapass_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = behapass_client.LoggerApi(behapass_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Removes unfinished registration movements
    api_instance.delete_register_user(user_id)
except ApiException as e:
    print("Exception when calling LoggerApi->delete_register_user: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LoggerApi* | [**delete_register_user**](docs/LoggerApi.md#delete_register_user) | **DELETE** /logger/user/{user_id}/movements | Removes unfinished registration movements
*LoggerApi* | [**get_button_record**](docs/LoggerApi.md#get_button_record) | **GET** /logger/buttons | Returns all existing button records
*LoggerApi* | [**get_movement_record**](docs/LoggerApi.md#get_movement_record) | **GET** /logger/movements | Returns all recorded movements
*LoggerApi* | [**get_register_user**](docs/LoggerApi.md#get_register_user) | **GET** /logger/user/{user_id}/movements | Returns all recorded movements
*LoggerApi* | [**get_user_data**](docs/LoggerApi.md#get_user_data) | **GET** /logger/user/{user_id} | Returns selected user&#39;s data
*LoggerApi* | [**logger_get**](docs/LoggerApi.md#logger_get) | **GET** /logger/ | Returns all existing records
*LoggerApi* | [**post_logger_record**](docs/LoggerApi.md#post_logger_record) | **POST** /logger/ | Stores received records
*LoggerApi* | [**post_lookup**](docs/LoggerApi.md#post_lookup) | **POST** /logger/lookup | Identifies the user
*LoggerApi* | [**post_register_user**](docs/LoggerApi.md#post_register_user) | **POST** /logger/user/{user_id}/movements | Stores user data permanently once registered
*LoggerApi* | [**post_user_record**](docs/LoggerApi.md#post_user_record) | **POST** /logger/user | Creates a new user ID


## Documentation For Models

 - [BadRequestResponse](docs/BadRequestResponse.md)
 - [ButtonRecord](docs/ButtonRecord.md)
 - [LoggerRecord](docs/LoggerRecord.md)
 - [LookupResult](docs/LookupResult.md)
 - [MovementRecord](docs/MovementRecord.md)
 - [PartialRegistrationResponse](docs/PartialRegistrationResponse.md)
 - [UserData](docs/UserData.md)
 - [UserRecord](docs/UserRecord.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



