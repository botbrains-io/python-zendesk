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

<!-- UsageSnippet language="python" operationID="ListCustomObjectFields" method="get" path="/api/v2/custom_objects/{custom_object_key}/fields" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_fields.list_custom_object_fields(custom_object_key="car", page_size=100, include_standard_fields=True)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The key of a custom object                                                                                                                                                                                                                                                                                          |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `include_standard_fields`                                                                                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Include standard fields if true. Exclude them if false                                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListCustomObjectFieldsResponse](../../models/listcustomobjectfieldsresponse.md)**

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

<!-- UsageSnippet language="python" operationID="CreateCustomObjectField" method="post" path="/api/v2/custom_objects/{custom_object_key}/fields" -->
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

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `custom_object_key`                                                               | *str*                                                                             | :heavy_check_mark:                                                                | The key of a custom object                                                        |
| `custom_object_field`                                                             | [Optional[models.CustomObjectFieldInput]](../../models/customobjectfieldinput.md) | :heavy_minus_sign:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

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

<!-- UsageSnippet language="python" operationID="ShowCustomObjectField" method="get" path="/api/v2/custom_objects/{custom_object_key}/fields/{custom_object_field_key_or_id}" -->
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `custom_object_field_key_or_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The key or id of a custom object field                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

<!-- UsageSnippet language="python" operationID="UpdateCustomObjectField" method="patch" path="/api/v2/custom_objects/{custom_object_key}/fields/{custom_object_field_key_or_id}" -->
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `custom_object_field_key_or_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The key or id of a custom object field                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

<!-- UsageSnippet language="python" operationID="DeleteCustomObjectField" method="delete" path="/api/v2/custom_objects/{custom_object_key}/fields/{custom_object_field_key_or_id}" -->
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `custom_object_field_key_or_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The key or id of a custom object field                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## reorder_custom_object_fields

Sets a preferred order of custom fields for a specific object by providing field ids in the desired order.
#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ReorderCustomObjectFields" method="put" path="/api/v2/custom_objects/{custom_object_key}/fields/reorder" -->
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

<!-- UsageSnippet language="python" operationID="CustomObjectFieldsLimit" method="get" path="/api/v2/custom_objects/{custom_object_key}/limits/field_limit" -->
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomObjectLimitsResponse](../../models/customobjectlimitsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |