# CustomObjectFields
(*custom_object_fields*)

## Overview

### Available Operations

* [list_custom_object_fields](#list_custom_object_fields) - List Custom Object Fields
* [create_custom_object_field](#create_custom_object_field) - Create Custom Object Field
* [show_custom_object_field](#show_custom_object_field) - Show Custom Object Field
* [update_custom_object_field](#update_custom_object_field) - Update Custom Object Field
* [delete_custom_object_field](#delete_custom_object_field) - Delete Custom Object Field
* [reorder_custom_object_fields](#reorder_custom_object_fields) - Reorder Custom Fields of an Object
* [custom_object_fields_limit](#custom_object_fields_limit) - Custom Object Fields Limit

## list_custom_object_fields

Lists all undeleted custom fields for the specified object.

#### Allowed For
* Agents

#### Pagination
* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_fields.list_custom_object_fields(custom_object_key="car", include_standard_fields=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          | car                                                                 |
| `include_standard_fields`                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include standard fields if true. Exclude them if false              | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomObjectFieldsResponse](../../models/customobjectfieldsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_custom_object_field

Creates any of the following custom field types:

* text (default when no "type" is specified)
* textarea
* checkbox
* date
* integer
* decimal
* regexp
* dropdown
* lookup
* multiselect

See [About custom field types](https://support.zendesk.com/hc/en-us/articles/203661866) in Zendesk help.

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_fields.create_custom_object_field(custom_object_key="car", custom_object_field={
        "key": "color",
        "title": "Color",
        "type": "text",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The key of a custom object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | car                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `custom_object_field`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[models.CustomObjectFieldInput]](../../models/customobjectfieldinput.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | {<br/>"active": true,<br/>"created_at": "2022-09-07T23:21:59Z",<br/>"description": "Make",<br/>"id": 4398096842879,<br/>"key": "make",<br/>"position": 0,<br/>"properties": {<br/>"autoincrement_enabled": true,<br/>"autoincrement_next_sequence": 1,<br/>"autoincrement_padding": 5,<br/>"autoincrement_prefix": "Order # ",<br/>"is_unique": false<br/>},<br/>"raw_description": "Make",<br/>"raw_title": "Make",<br/>"regexp_for_validation": null,<br/>"system": false,<br/>"title": "Make",<br/>"type": "text",<br/>"updated_at": "2022-09-07T23:22:00Z",<br/>"url": "https://company.zendesk.com/api/v2/custom_objects/car/fields/4398096842879.json"<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Response

**[models.CustomObjectFieldResponse](../../models/customobjectfieldresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_custom_object_field

Returns a custom field for a specific object using a provided key or id of the field.
#### Allowed For
* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_fields.show_custom_object_field(custom_object_key="car", custom_object_field_key_or_id="make")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          | car                                                                 |
| `custom_object_field_key_or_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The key or id of a custom object field                              | make                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomObjectFieldResponse](../../models/customobjectfieldresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_custom_object_field

Updates individual custom object fields. The updating rules are as follows:
* Takes a `custom_object_field` object that specifies the properties to update
* The `key` property cannot be updated
* If updating a standard field, only the `title`, `description`, and `properties` attributes can be updated.
* The `properties` parameter is comprised of four parts and can't be changed if any records exist for the object.
    * `autoincrement_enabled`: A Boolean that enables and disables autonumbering. Must be false if is_unique is true.
    * `autoincrement_prefix`: A string value that is used as a prefix to the autogenerated numbers. It can't exceed 30 characters.
    * `autoincrement_padding`: An integer specifying the starting number of digits in the autogenerated numbers. This value may be between 0-9. However, if you create records in excess of of these digits, additional digits are added as necessary.
    * `autoincrement_next_sequence`: An integer that will be used as the next number in the autonumbering sequence. It can't be negative or less than the current autonumbering value.
    * `is_unique`: A Boolean that enforces uniqueness for manually entered record names. When true, custom object record names must be unique. Must be false if autoincrement_enabled is true.
#### Allowed For
* Admins

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_fields.update_custom_object_field(custom_object_key="car", custom_object_field_key_or_id="make")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          | car                                                                 |
| `custom_object_field_key_or_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The key or id of a custom object field                              | make                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomObjectFieldResponse](../../models/customobjectfieldresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_custom_object_field

Deletes a field with the specified key. Note: You can't delete standard fields.
#### Allowed For
* Admins

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.custom_object_fields.delete_custom_object_field(custom_object_key="car", custom_object_field_key_or_id="make")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          | car                                                                 |
| `custom_object_field_key_or_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The key or id of a custom object field                              | make                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## reorder_custom_object_fields

Sets a preferred order of custom fields for a specific object by providing field ids in the desired order.
#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_fields.reorder_custom_object_fields(custom_object_key="car")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          | car                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## custom_object_fields_limit

List the current count and the limit for a custom object's fields
#### Allowed For
* Agents

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_fields.custom_object_fields_limit(custom_object_key="car")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          | car                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomObjectLimitsResponse](../../models/customobjectlimitsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |