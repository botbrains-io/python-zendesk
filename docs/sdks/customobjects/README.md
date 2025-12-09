# CustomObjects

## Overview

### Available Operations

* [list_custom_objects](#list_custom_objects) - List Custom Objects
* [create_custom_object](#create_custom_object) - Create Custom Object
* [show_custom_object](#show_custom_object) - Show Custom Object
* [update_custom_object](#update_custom_object) - Update Custom Object
* [delete_custom_object](#delete_custom_object) - Delete Custom Object
* [custom_objects_limit](#custom_objects_limit) - Custom Objects Limit

## list_custom_objects

Lists all undeleted custom objects for the account
#### Allowed For
* Agents

### Example Usage

<!-- UsageSnippet language="python" operationID="ListCustomObjects" method="get" path="/api/v2/custom_objects" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_objects.list_custom_objects()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomObjectsResponse](../../models/customobjectsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_custom_object

Creates an object describing all the properties required to create a custom object record
#### Allowed For
* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateCustomObject" method="post" path="/api/v2/custom_objects" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_objects.create_custom_object(request={
        "custom_object": {
            "key": "apartment",
            "title": "Apartment",
            "title_pluralized": "Apartments",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CustomObjectsCreateRequest](../../models/customobjectscreaterequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.CustomObjectResponse](../../models/customobjectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_custom_object

Returns an object with the specified key
#### Allowed For
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowCustomObject" method="get" path="/api/v2/custom_objects/{custom_object_key}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_objects.show_custom_object(custom_object_key="car")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomObjectResponse](../../models/customobjectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_custom_object

Updates an individual custom object. The updating rules are as follows:
* Takes a `custom_object` object that specifies the properties to update
* The `key` property cannot be updated
#### Allowed For
* Admins

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateCustomObject" method="patch" path="/api/v2/custom_objects/{custom_object_key}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_objects.update_custom_object(custom_object_key="car")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomObjectResponse](../../models/customobjectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_custom_object

Permanently deletes the custom object with the specified key
#### Allowed For
* Admins

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteCustomObject" method="delete" path="/api/v2/custom_objects/{custom_object_key}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.custom_objects.delete_custom_object(custom_object_key="car")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## custom_objects_limit

List the current count and the limit for custom objects
#### Allowed For
* Admins

### Example Usage

<!-- UsageSnippet language="python" operationID="CustomObjectsLimit" method="get" path="/api/v2/custom_objects/limits/object_limit" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_objects.custom_objects_limit()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomObjectLimitsResponse](../../models/customobjectlimitsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |