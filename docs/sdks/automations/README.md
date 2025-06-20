# Automations
(*automations*)

## Overview

### Available Operations

* [list_automations](#list_automations) - List Automations
* [create_automation](#create_automation) - Create Automation
* [show_automation](#show_automation) - Show Automation
* [update_automation](#update_automation) - Update Automation
* [delete_automation](#delete_automation) - Delete Automation
* [list_active_automations](#list_active_automations) - List Active Automations
* [bulk_delete_automations](#bulk_delete_automations) - Bulk Delete Automations
* [search_automations](#search_automations) - Search Automations
* [update_many_automations](#update_many_automations) - Update Many Automations

## list_automations

Lists all automations for the current account.

#### Allowed For

* Agents

#### Available Parameters

You can pass in any combination of the following optional filters:

| Name       | Type    | Comment
| ---------- | ------- | -------
| active     | boolean | Only active automations if true, inactive automations if false
| sort_by    | string  | Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"
| sort_order | string  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Sideloads

The following sideloads are supported. The usage sideloads are only supported on the Support Professional or Suite Growth plan or above.

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each automation, if present
| permissions      | The permissions for each automation
| usage_1h         | The number of times each automation has been used in the past hour
| usage_24h        | The number of times each automation has been used in the past day
| usage_7d         | The number of times each automation has been used in the past week
| usage_30d        | The number of times each automation has been used in the past thirty days

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.automations.list_automations(page_size=100)

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
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListAutomationsResponse](../../models/listautomationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_automation

Creates an automation.

New automations must be unique and have at least one condition that is true only once or an action that nullifies at least one of the conditions. Active automations can have overlapping conditions but can't be identical.

The request must include the following conditions in the `all` array:

- At least one time-based condition
- At least one condition that checks one of the following fields: `status`, `type`, `group_id`, `assignee_id`, or `requester_id`.

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

    res = z_client.automations.create_automation()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AutomationResponse](../../models/automationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_automation

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

    res = z_client.automations.show_automation(automation_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `automation_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | The ID of the automation                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AutomationResponse](../../models/automationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_automation

Updates an automation.

Updated automations must be unique and have at least one condition that is true only once or an action that nullifies at least one of the conditions. Active automations can have overlapping conditions but can't be identical.

The request must include the following conditions in the `all` array:
- At least one time-based condition
- At least one condition that checks one of the following fields: 'status', 'type', 'group_id', 'assignee_id', or 'requester_id'

**Note**: Updating a condition or action updates both the `conditions` and `actions` arrays, clearing all existing values of both arrays. Include all your conditions and actions when updating any condition or action.
**Note**: You might be restricted from updating some default automations.

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

    res = z_client.automations.update_automation(automation_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `automation_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | The ID of the automation                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AutomationResponse](../../models/automationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_automation

**Note**: You might be restricted from deleting some default automations.

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

    z_client.automations.delete_automation(automation_id=25)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `automation_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | The ID of the automation                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_automations

Lists all active automations.

#### Allowed For

* Agents

#### Available Parameters

You can pass in any combination of the following optional filters:

| Name       | Type   | Comment
| ---------- | ------ | -------
| sort_by    | string | Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", or "usage_7d". Defaults to "position"
| sort_order | string | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each automation, if present
| permissions      | The permissions for each automation
| usage_1h         | The number of times each automation has been used in the past hour
| usage_24h        | The number of times each automation has been used in the past day
| usage_7d         | The number of times each automation has been used in the past week
| usage_30d        | The number of times each automation has been used in the past thirty days


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.automations.list_active_automations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AutomationsResponse](../../models/automationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## bulk_delete_automations

Deletes the automations corresponding to the provided comma-separated list of IDs.

**Note**: You might be restricted from deleting some default automations. If included in a bulk deletion, the unrestricted automations will be deleted.

#### Allowed For

* Agents

#### Request Parameters

The DELETE request takes one parameter, an `ids` object that lists the automations to delete.

| Name | Description
| ---- | -----------
| ids  | The IDs of the automations to delete

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

    z_client.automations.bulk_delete_automations()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | List[*int*]                                                         | :heavy_minus_sign:                                                  | The IDs of the automations to delete                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_automations

#### Pagination

* Offset pagination only

See [Using Offset Pagination](/api-reference/ticketing/introduction/#using-offset-pagination).

#### Allowed For

* Agents

#### Sideloads

The following sideloads are supported. For more information, see [Side-loading](/documentation/ticketing/using-the-zendesk-api/side_loading/).

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each automation, if present
| permissions      | The permissions for each automation
| usage_1h         | The number of times each automation has been used in the past hour
| usage_24h        | The number of times each automation has been used in the past day
| usage_7d         | The number of times each automation has been used in the past week
| usage_30d        | The number of times each automation has been used in the past thirty days


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.automations.search_automations(query="close", active=True, sort_by="position", sort_order="desc", include="usage_24h")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                 | *str*                                                                                                                                   | :heavy_check_mark:                                                                                                                      | Query string used to find all automations with matching title                                                                           |
| `active`                                                                                                                                | *Optional[bool]*                                                                                                                        | :heavy_minus_sign:                                                                                                                      | Filter by active automations if true or inactive automations if false                                                                   |
| `sort_by`                                                                                                                               | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | Possible values are "alphabetical", "created_at", "updated_at", and "position". If unspecified, the automations are sorted by relevance |
| `sort_order`                                                                                                                            | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                     |
| `include`                                                                                                                               | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | A sideload to include in the response. See [Sideloads](#sideloads-2)                                                                    |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[models.AutomationsResponse](../../models/automationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many_automations

**Note**: You might be restricted from updating some default automations. If included in a bulk update, the unrestricted automations will be updated.

#### Allowed For

* Agents

#### Request Parameters

The PUT request expects an `automations` object that lists the automations to update.

Each automation may have the following properties:

| Name     | Mandatory | Description
| -------- | --------- | -----------
| id       | yes       | The ID of the automation to update
| position | no        | The new position of the automation
| active   | no        | The active status of the automation (true or false)

#### Example Request

```js
{
  "automations": [
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

    res = z_client.automations.update_many_automations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AutomationsResponse](../../models/automationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |