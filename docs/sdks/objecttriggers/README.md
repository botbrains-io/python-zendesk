# ObjectTriggers
(*object_triggers*)

## Overview

### Available Operations

* [list_object_triggers](#list_object_triggers) - List Object Triggers
* [create_object_trigger](#create_object_trigger) - Create Object Trigger
* [get_object_trigger](#get_object_trigger) - Show Object Trigger
* [update_object_trigger](#update_object_trigger) - Update Object Trigger
* [delete_object_trigger](#delete_object_trigger) - Delete Object Trigger
* [list_active_object_triggers](#list_active_object_triggers) - List Active Object Triggers
* [list_object_triggers_definitions](#list_object_triggers_definitions) - List Object Trigger Action and Condition Definitions
* [delete_many_object_triggers](#delete_many_object_triggers) - Delete Many Object Triggers
* [search_object_triggers](#search_object_triggers) - Search Object Triggers
* [update_many_object_triggers](#update_many_object_triggers) - Update Many Object Triggers

## list_object_triggers

Lists all triggers for the specified custom object.

#### Allowed For 
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListObjectTriggers" method="get" path="/api/v2/custom_objects/{custom_object_key}/triggers" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.object_triggers.list_object_triggers(custom_object_key="car", active=True, sort_by="position", sort_order="desc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `custom_object_key`                                                                                                                                    | *str*                                                                                                                                                  | :heavy_check_mark:                                                                                                                                     | The key of a custom object                                                                                                                             |
| `active`                                                                                                                                               | *Optional[bool]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                     | Filter by active triggers if true or inactive triggers if false                                                                                        |
| `sort_by`                                                                                                                                              | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position" |
| `sort_order`                                                                                                                                           | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                    |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |

### Response

**[models.ObjectTriggersResponse](../../models/objecttriggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_object_trigger

Creates a new object trigger for a specified object.

#### Allowed For

* Administrators
* Agents in custom roles with the `manage_triggers` permission (Enterprise only)


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateObjectTrigger" method="post" path="/api/v2/custom_objects/{custom_object_key}/triggers" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.object_triggers.create_object_trigger(custom_object_key="car", trigger={
        "actions": [
            {
                "field": "custom_object.order.custom_fields.miles",
                "value": "100",
            },
        ],
        "conditions": {
            "all": [],
            "any": [
                {
                    "field": "custom_object.order.custom_fields.heat",
                    "operator": "not_present",
                },
            ],
        },
        "title": "active test order trigger with any conditions",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                   | *str*                                                                                 | :heavy_check_mark:                                                                    | The key of a custom object                                                            |
| `trigger`                                                                             | [Optional[models.ObjectTriggerObjectInput]](../../models/objecttriggerobjectinput.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ObjectTriggerResponse](../../models/objecttriggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_object_trigger

Returns details of a specific object trigger.
#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="GetObjectTrigger" method="get" path="/api/v2/custom_objects/{custom_object_key}/triggers/{trigger_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.object_triggers.get_object_trigger(custom_object_key="car", trigger_id=198)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `trigger_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the trigger                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObjectTriggerResponse](../../models/objecttriggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_object_trigger

Updates a specified object trigger.

**Note**: Updating a condition or action updates both the conditions and actions arrays,
clearing all existing values of both arrays. Include all your conditions
and actions when updating any condition or action.

#### Allowed For

* Administrators
* Agents in custom roles with the `manage_triggers` permission (Enterprise only)


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateObjectTrigger" method="put" path="/api/v2/custom_objects/{custom_object_key}/triggers/{trigger_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.object_triggers.update_object_trigger(custom_object_key="car", trigger_id=198, trigger={
        "actions": [
            {
                "field": "custom_object.order.custom_fields.miles",
                "value": "100",
            },
        ],
        "conditions": {
            "all": [],
            "any": [
                {
                    "field": "custom_object.order.custom_fields.heat",
                    "operator": "not_present",
                },
            ],
        },
        "title": "active test order trigger with any conditions",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                   | *str*                                                                                 | :heavy_check_mark:                                                                    | The key of a custom object                                                            |
| `trigger_id`                                                                          | *int*                                                                                 | :heavy_check_mark:                                                                    | The ID of the trigger                                                                 |
| `trigger`                                                                             | [Optional[models.ObjectTriggerObjectInput]](../../models/objecttriggerobjectinput.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ObjectTriggerResponse](../../models/objecttriggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_object_trigger

Deletes a specified object trigger.

#### Allowed For

* Administrators
* Agents in custom roles with the `manage_triggers` permission (Enterprise only)


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteObjectTrigger" method="delete" path="/api/v2/custom_objects/{custom_object_key}/triggers/{trigger_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.object_triggers.delete_object_trigger(custom_object_key="car", trigger_id=198)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `trigger_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the trigger                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_object_triggers

Lists all active object triggers.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Administrators
* Agents in custom roles with the `manage_triggers` permission (Enterprise only)


### Example Usage

<!-- UsageSnippet language="python" operationID="ListActiveObjectTriggers" method="get" path="/api/v2/custom_objects/{custom_object_key}/triggers/active" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.object_triggers.list_active_object_triggers(custom_object_key="car", sort_by="position", sort_order="desc", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The key of a custom object                                                                                                                                                                                                                                                                                          |
| `sort_by`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"                                                                                                                                                              |
| `sort_order`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                                                                                                                                                                                 |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListActiveObjectTriggersResponse](../../models/listactiveobjecttriggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_object_triggers_definitions

Lists the conditions and actions of all triggers for the specified custom object.

#### Allowed For 
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListObjectTriggersDefinitions" method="get" path="/api/v2/custom_objects/{custom_object_key}/triggers/definitions" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.object_triggers.list_object_triggers_definitions(custom_object_key="car")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ObjectTriggerDefinitionResponse](../../models/objecttriggerdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_many_object_triggers

Deletes the object triggers corresponding to the provided comma-separated list of ids. 

**Note**: You can only bulk-delete triggers associated with one object at a time, specified by the `custom_object_key` in the request.

#### Allowed For

* Administrators
* Agents in custom roles with the `manage_triggers` permission (Enterprise only)

#### Request Parameters

The DELETE request takes an `ids` object that lists the
object triggers to delete. All of the specified object trigger `ids` must be associated with a single object.

| Name | Description
| ---- | -----------
| ids  | The ids of the triggers to delete

#### Example request

```js
{
  "ids": "25,23,27,22"
}
```


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteManyObjectTriggers" method="delete" path="/api/v2/custom_objects/{custom_object_key}/triggers/destroy_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.object_triggers.delete_many_object_triggers(custom_object_key="car", ids="131,178,938")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | A comma separated list of trigger IDs                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_object_triggers

Returns a list of object triggers that meet your filter or search criteria.

#### Pagination

* Offset pagination only

See [Using Offset Pagination](/api-reference/ticketing/introduction/#using-offset-pagination).

#### Allowed For

* Agents

#### Filter

Use the `filter` query parameter to filter an object trigger search by one or more attributes. For example, the following `filter` argument filters object triggers by the `title` attribute:

```json
{
  "json": {
    "title": "test"
  }
}
```


### Example Usage

<!-- UsageSnippet language="python" operationID="SearchObjectTriggers" method="get" path="/api/v2/custom_objects/{custom_object_key}/triggers/search" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.object_triggers.search_object_triggers(custom_object_key="car", query="important_trigger", filter_={
        "json_": {
            "actions": [
                {},
            ],
            "active": True,
            "category_id": "10026",
            "conditions": {},
            "description": "Close and save a ticket",
            "position": 8,
            "raw_title": "Close and Save",
            "title": "Close and Save",
        },
    }, active=True, sort="position", sort_by="position", sort_order="desc", include="usage_24h")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `custom_object_key`                                                                                                                                    | *str*                                                                                                                                                  | :heavy_check_mark:                                                                                                                                     | The key of a custom object                                                                                                                             |
| `query`                                                                                                                                                | *str*                                                                                                                                                  | :heavy_check_mark:                                                                                                                                     | Query string used to find all triggers with matching title                                                                                             |
| `filter_`                                                                                                                                              | [Optional[models.TriggerSearchFilter]](../../models/triggersearchfilter.md)                                                                            | :heavy_minus_sign:                                                                                                                                     | Trigger attribute filters for the search. See [Filter](#filter)                                                                                        |
| `active`                                                                                                                                               | *Optional[bool]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                     | Filter by active triggers if true or inactive triggers if false                                                                                        |
| `sort`                                                                                                                                                 | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | Cursor-based pagination only. Possible values are "alphabetical", "created_at", "updated_at", or "position".                                           |
| `sort_by`                                                                                                                                              | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position" |
| `sort_order`                                                                                                                                           | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                    |
| `include`                                                                                                                                              | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | A sideload to include in the response. See [Sideloads](#sideloads-2)                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |

### Response

**[models.ObjectTriggersResponse](../../models/objecttriggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many_object_triggers

Updates the position or the active status of multiple object triggers. Any additional properties are ignored.

**Note**: You can only bulk-update triggers associated with one object at a time, specified by the `custom_object_key` in the request.

#### Allowed For

* Administrators
* Agents in custom roles with the `manage_triggers` permission (Enterprise only)

#### Request Parameters

The PUT request expects a `triggers` object that lists the object triggers to update. All of the specified object trigger `ids` must be associated with a single object.

You can specify the following properties for each object trigger you're updating:

| Name        | Mandatory | Description
| --------    | --------- | -----------
| id          | yes       | The ID of the object trigger to update
| position    | no        | The new position of the object trigger
| active      | no        | The active status of the object trigger (true or false)

#### Example Request

```js
{
  "triggers": [
    {"id": 25, "position": 3},
    {"id": 23, "active": true},
    {"id": 27, "position": 9, "active": false},
    {"id": 22, "position": 7}
  ]
}
```


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateManyObjectTriggers" method="put" path="/api/v2/custom_objects/{custom_object_key}/triggers/update_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.object_triggers.update_many_object_triggers(custom_object_key="car", triggers=[
        {
            "id": 25,
            "position": 1,
        },
        {
            "active": False,
            "id": 26,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                     | *str*                                                                                   | :heavy_check_mark:                                                                      | The key of a custom object                                                              |
| `triggers`                                                                              | List[[models.ObjectTriggerBulkUpdateItem](../../models/objecttriggerbulkupdateitem.md)] | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ObjectTriggersResponse](../../models/objecttriggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |