# Triggers
(*triggers*)

## Overview

### Available Operations

* [list_triggers](#list_triggers) - List Ticket Triggers
* [create_trigger](#create_trigger) - Create Trigger
* [get_trigger](#get_trigger) - Show Ticket Trigger
* [update_trigger](#update_trigger) - Update Ticket Trigger
* [delete_trigger](#delete_trigger) - Delete Ticket Trigger
* [list_trigger_revisions](#list_trigger_revisions) - List Ticket Trigger Revisions
* [trigger_revision](#trigger_revision) - Show Ticket Trigger Revision
* [list_active_triggers](#list_active_triggers) - List Active Ticket Triggers
* [list_trigger_action_condition_definitions](#list_trigger_action_condition_definitions) - List Ticket Trigger Action and Condition Definitions
* [delete_many_triggers](#delete_many_triggers) - Bulk Delete Ticket Triggers
* [reorder_triggers](#reorder_triggers) - Reorder Ticket Triggers
* [search_triggers](#search_triggers) - Search Ticket Triggers
* [update_many_triggers](#update_many_triggers) - Update Many Ticket Triggers

## list_triggers

Lists all ticket triggers for the current account.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Agents

#### Sideloads

The following sideloads are supported. The usage sideloads are only supported on the Support Professional or Suite Growth plan or above.

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each trigger, if present
| permissions      | The permissions for each trigger
| usage_1h         | The number of times each trigger has been used in the past hour
| usage_24h        | The number of times each trigger has been used in the past day
| usage_7d         | The number of times each trigger has been used in the past week
| usage_30d        | The number of times each trigger has been used in the past thirty days


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.triggers.list_triggers(page_size=100, active=True, sort="position", sort_by="position", sort_order="desc", category_id="10026")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `active`                                                                                                                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter by active triggers if true or inactive triggers if false                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Cursor-based pagination only. Possible values are "alphabetical", "created_at", "updated_at", or "position".                                                                                                                                                                                                        |
| `sort_by`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"                                                                                                                                                              |
| `sort_order`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                                                                                                                                                                                 |
| `category_id`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter triggers by category ID                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListTriggersResponse](../../models/listtriggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_trigger

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

    res = z_client.triggers.create_trigger(trigger={
        "actions": [
            {
                "field": "group_id",
                "value": "20455932",
            },
        ],
        "category_id": "10026",
        "conditions": {
            "all": [
                {
                    "field": "status",
                    "operator": "is",
                    "value": "open",
                },
                {
                    "field": "priority",
                    "operator": "less_than",
                    "value": "high",
                },
            ],
        },
        "title": "Roger Wilco",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger`                                                           | [Optional[models.Trigger]](../../models/trigger.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TriggerResponse](../../models/triggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_trigger

#### Allowed For

* Agents

The Via Type value is a number instead of a text string. See [Via types reference](/documentation/ticketing/reference-guides/via-types/) for the keys.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.triggers.get_trigger(trigger_id=198)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the trigger                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TriggerResponse](../../models/triggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_trigger

#### Allowed For

* Agents

#### Note

Updating a condition or action updates both the conditions and actions arrays,
clearing all existing values of both arrays. Include all your conditions
and actions when updating any condition or action.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.triggers.update_trigger(trigger_id=198, trigger={
        "actions": [
            {
                "field": "group_id",
                "value": "20455932",
            },
        ],
        "category_id": "10026",
        "conditions": {
            "all": [
                {
                    "field": "status",
                    "operator": "is",
                    "value": "open",
                },
                {
                    "field": "priority",
                    "operator": "less_than",
                    "value": "high",
                },
            ],
        },
        "title": "Roger Wilco",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the trigger                                               |
| `trigger`                                                           | [Optional[models.Trigger]](../../models/trigger.md)                 | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TriggerResponse](../../models/triggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_trigger

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

    z_client.triggers.delete_trigger(trigger_id=198)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the trigger                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_trigger_revisions

List the revisions associated with a ticket trigger. Ticket trigger revision history is only available on Enterprise plans.

#### Allowed For

 * Agents

#### Sideloads

The following sideloads are supported:

| Name  | Will sideload
| ----- | -------------
| users | The user that authored each revision

#### Pagination

This endpoint uses cursor-based pagination. The records are ordered in
descending order by the `created_at` timestamp, then by `id` on duplicate
`created_at` values.

The `cursor` parameter is a non-human-readable argument you can use to move
forward or backward in time.

Each JSON response will contain the following attributes to help you get
more results:

- `after_url` requests more recent results
- `before_url` requests older results
- `after_cursor` is the cursor to build the request yourself
- `before_cursor` is the cursor to build the request yourself

The properties are null if no more records are available.

You can request a maximum of 1000 records using the `limit` parameter. If
no `limit` parameter is supplied, it will default to 1,000.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.triggers.list_trigger_revisions(trigger_id=198)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the trigger                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TriggerRevisionsResponse](../../models/triggerrevisionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## trigger_revision

Fetches a revision associated with a ticket trigger. Ticket trigger revision history is only available on Enterprise plans.

#### Allowed For

 * Agents

#### Sideloads

The following sideloads are supported:

| Name  | Will sideload
| ----- | -------------
| users | The user that authored each revision


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.triggers.trigger_revision(trigger_id=198, trigger_revision_id=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the trigger                                               |
| `trigger_revision_id`                                               | *int*                                                               | :heavy_check_mark:                                                  | The ID of the revision for a particular trigger                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TriggerRevisionResponse](../../models/triggerrevisionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_triggers

Lists all active ticket triggers.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.
#### Allowed For

* Agents

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each ticket trigger, if present
| permissions      | The permissions for each trigger
| usage_1h         | The number of times each ticket trigger has been used in the past hour
| usage_24h        | The number of times each ticket trigger has been used in the past day
| usage_7d         | The number of times each ticket trigger has been used in the past week
| usage_30d        | The number of times each ticket trigger has been used in the past thirty days


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.triggers.list_active_triggers(sort="position", sort_by="position", sort_order="desc", category_id="10026")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sort`                                                                                                                                                 | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | Cursor-based pagination only. Possible values are "alphabetical", "created_at", "updated_at", or "position".                                           |
| `sort_by`                                                                                                                                              | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position" |
| `sort_order`                                                                                                                                           | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                    |
| `category_id`                                                                                                                                          | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | Filter triggers by category ID                                                                                                                         |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |

### Response

**[models.TriggersResponse](../../models/triggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_trigger_action_condition_definitions

Returns the definitions of the actions a ticket trigger can perform and the
definitions of the conditions under which a ticket trigger can execute. The
definition of the action includes a title ("Status"), a type ("list"), and
possible values. The definition of the condition includes the same fields
as well as the possible operators.

For a list of supported actions, see the [Actions reference](/documentation/ticketing/reference-guides/actions-reference)
For a list of supported conditions, see the [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)

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

    res = z_client.triggers.list_trigger_action_condition_definitions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TriggerDefinitionResponse](../../models/triggerdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_many_triggers

Deletes the ticket triggers corresponding to the provided comma-separated list of IDs.

#### Allowed For

* Agents

#### Request Parameters

The DELETE request takes one parameter, an `ids` object that lists the
ticket triggers to delete.

| Name | Description
| ---- | -----------
| ids  | The IDs of the triggers to delete

#### Example request

```js
{
  "ids": "25,23,27,22"
}
```


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.triggers.delete_many_triggers(ids="131,178,938")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | A comma separated list of trigger IDs                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## reorder_triggers

Alters the firing order of ticket triggers in the account. See
[Reordering and sorting triggers](https://support.zendesk.com/hc/en-us/articles/115015696088)
in the Zendesk Help Center. The firing order is set in a `trigger_ids` array in the request body.

You must include every ticket trigger id in your account to reorder the ticket triggers. If not, the endpoint will return 404 Forbidden.

Reordering ticket triggers via the API is not permitted if you have more than one ticket trigger category. If there is more than one
ticket trigger category, the endpoint will return a `LimitOneCategory` error.

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

    res = z_client.triggers.reorder_triggers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TriggerResponse](../../models/triggerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_triggers

#### Pagination

* Offset pagination only

See [Using Offset Pagination](/api-reference/ticketing/introduction/#using-offset-pagination).

#### Allowed For

* Agents

#### Sideloads

The following sideloads are supported. For more information, see [Side-loading](/documentation/ticketing/using-the-zendesk-api/side_loading/).

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each ticket trigger, if present
| permissions      | The permissions for each ticket trigger
| usage_1h         | The number of times each ticket trigger has been used in the past hour
| usage_24h        | The number of times each ticket trigger has been used in the past day
| usage_7d         | The number of times each ticket trigger has been used in the past week
| usage_30d        | The number of times each ticket trigger has been used in the past thirty days

#### Filter

Use the `filter` query parameter to filter a ticket trigger search by one or more attributes. For example, the following `filter` argument filters ticket triggers by the `description` attribute:

```json
{
  "json": {
    "description": "Close a ticket"
  }
}
```


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.triggers.search_triggers(query="important_trigger", filter_={
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
| `query`                                                                                                                                                | *str*                                                                                                                                                  | :heavy_check_mark:                                                                                                                                     | Query string used to find all triggers with matching title                                                                                             |
| `filter_`                                                                                                                                              | [Optional[models.TriggerSearchFilter]](../../models/triggersearchfilter.md)                                                                            | :heavy_minus_sign:                                                                                                                                     | Trigger attribute filters for the search. See [Filter](#filter)                                                                                        |
| `active`                                                                                                                                               | *Optional[bool]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                     | Filter by active triggers if true or inactive triggers if false                                                                                        |
| `sort`                                                                                                                                                 | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | Cursor-based pagination only. Possible values are "alphabetical", "created_at", "updated_at", or "position".                                           |
| `sort_by`                                                                                                                                              | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | Offset pagination only. Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position" |
| `sort_order`                                                                                                                                           | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                    |
| `include`                                                                                                                                              | *Optional[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                     | A sideload to include in the response. See [Sideloads](#sideloads-2)                                                                                   |
| `retries`                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                       | :heavy_minus_sign:                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                    |

### Response

**[models.TriggersResponse](../../models/triggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many_triggers

Updates the position or the active status of multiple ticket triggers. Any additional properties are ignored.

#### Allowed For

* Agents

#### Request Parameters

The PUT request expects a `triggers` object that lists the ticket triggers to update.

Each ticket trigger may have the following properties:

| Name        | Mandatory | Description
| --------    | --------- | -----------
| id          | yes       | The ID of the ticket trigger to update
| position    | no        | The new position of the ticket trigger
| active      | no        | The active status of the ticket trigger (true or false)
| category_id | no        | The ID of the new category the ticket trigger is to be moved to

#### Example Request

```js
{
  "triggers": [
    {"id": 25, "position": 3},
    {"id": 23, "position": 5},
    {"id": 27, "position": 9},
    {"id": 22, "position": 7}
  ]
}
```


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.triggers.update_many_triggers(triggers=[
        {
            "id": 25,
            "position": 5,
        },
        {
            "active": False,
            "id": 26,
        },
        {
            "category_id": "10027",
            "id": 27,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `triggers`                                                                  | List[[models.TriggerBulkUpdateItem](../../models/triggerbulkupdateitem.md)] | :heavy_minus_sign:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.TriggersResponse](../../models/triggersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |