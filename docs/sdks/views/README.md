# Views

## Overview

### Available Operations

* [list_views](#list_views) - List Views
* [create_view](#create_view) - Create View
* [show_view](#show_view) - Show View
* [update_view](#update_view) - Update View
* [delete_view](#delete_view) - Delete View
* [get_view_count](#get_view_count) - Count Tickets in View
* [execute_view](#execute_view) - Execute View
* [export_view](#export_view) - Export View
* [list_tickets_from_view](#list_tickets_from_view) - List Tickets From a View
* [list_active_views](#list_active_views) - List Active Views
* [list_compact_views](#list_compact_views) - List Views - Compact
* [count_views](#count_views) - Count Views
* [get_view_counts](#get_view_counts) - Count Tickets in Views
* [bulk_delete_views](#bulk_delete_views) - Bulk Delete Views
* [preview_views](#preview_views) - Preview Views
* [preview_count](#preview_count) - Preview Ticket Count
* [search_views](#search_views) - Search Views
* [list_views_by_id](#list_views_by_id) - List Views By ID
* [update_many_views](#update_many_views) - Update Many Views

## list_views

Lists shared and personal views available to the current user.

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each view, if present
| permissions      | The permissions for each view

#### Pagination

- Cursor pagination (recommended, but only sorts by `created_at`)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListViews" method="get" path="/api/v2/views" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.list_views(page_size=100)

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
| `access`                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Only views with given access. May be "personal", "shared", or "account"                                                                                                                                                                                                                                             |
| `active`                                                                                                                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Only active views if true, inactive views if false                                                                                                                                                                                                                                                                  |
| `group_id`                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Only views belonging to given group                                                                                                                                                                                                                                                                                 |
| `sort_by`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Possible values are "alphabetical", "created_at", or "updated_at". Defaults to "position"                                                                                                                                                                                                                           |
| `sort_order`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListViewsResponse](../../models/listviewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_view

#### Allowed For

* Agents

#### JSON Format

The JSON format consists of one property, a `view` object that lists the values to set when the view is created.

**Note**: The request must include at least one condition in the `all` array that checks one of the following fields: `status`, `type`, `group_id`, `assignee_id`, or `requester_id`.

| Name        | Description
| ----------- | -----------
| title       | Required. The title of the view
| all         | Required. An array of one or more conditions. A ticket must meet all of them to be included in the view. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
| any         | An array of one or more conditions. A ticket must meet any of them to be included in the view. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
| description | The description of the view
| active      | Allowed values are true or false. Determines if the view is displayed or not
| output      | An object that specifies the columns to display. Example: `"output": {"columns": ["status", "description", "priority"]}`. See [View columns](#view-columns)
| restriction | An object that describes who can access the view. To give all agents access to the view, omit this property

The `restriction` object has the following properties.

| Name | Comment
| ---- | -------
| type | Allowed values are "Group" or "User"
| id   | The numeric ID of a single group or user
| ids  | The numeric IDs of a single or more groups. Recommended for "Group" `type`

If `type` is "Group", the `ids` property is the preferred method of specifying the group id or ids.

#### Example Request Body

```js
{
  "view": {
    "title": "Kelly's tickets",
    "raw_title": "{{dc.tickets_assigned_to_kelly}}",
    "description": "Tickets that are assigned to Kelly",
    "active": true,
    "position": 3,
    "restriction": {
      "type": "User",
      "id": "213977756"
    },
    "all": [
      {
        "field": "status",
        "operator": "less_than",
        "value": "solved"
      },
      {
        "field": "group_id",
        "operator": "is",
        "value": "24000932"
      },
      {
        "field": "custom_fields_360011872073",
        "operator": "is",
        "value": "Canada"
      },
      ...
    ],
    "output": {
      "columns": ["status", "requester", "assignee"],
      "group_by": "assignee",
      "group_order": "desc",
      "sort_by": "status",
      "sort_order": "desc"
    }
  }
}
```

#### View columns

The `output` request parameter lets you specify what columns to include in the view in the agent interface. Example: `"output": {"columns": ["status", "description", "priority"]}`. The following table lists possible columns for views in the agent UI and the corresponding values in the `columns` array.

For custom fields, specify the id of the custom field in the `columns` array.

You can specify a total of 10 columns to a view.

| View column title in UI     | Value                |
|---------------------------- | -------------------- |
| Assigned                    | `assigned`           |
| Assignee                    | `assignee`           |
| Due Date                    | `due_date`           |
| Group                       | `group`              |
| ID                          | `nice_id`            |
| Updated                     | `updated`            |
| Assignee updated            | `updated_assignee`   |
| Requester updated           | `updated_requester`  |
| Updater                     | `updated_by_type`    |
| Organization                | `organization`       |
| Priority                    | `priority`           |
| Requested                   | `created`            |
| Requester                   | `requester`          |
| Requester language          | `locale_id`          |
| Satisfaction                | `satisfaction_score` |
| Solved                      | `solved`             |
| Status category             | `status`             |
| Subject                     | `description`        |
| Submitter                   | `submitter`          |
| Ticket form                 | `ticket_form`        |
| Type                        | `type`               |
| Brand                       | `brand`              |
| Ticket status               | `custom_status_id`   |

#### View sorting

You can group and sort items in the view by adding items to the `output` parameter:

| Attribute                   | Description
|-----------------------------| -----------
| `group_by`, `sort_by`       | Sort or group the tickets by a column in the [View columns](#view-columns) table. The `description`, `submitter` and `custom_status_id` columns are not supported
| `group_order`, `sort_order` | Either "asc" or "desc"


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateView" method="post" path="/api/v2/views" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.create_view()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewResponse](../../models/viewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_view

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowView" method="get" path="/api/v2/views/{view_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.show_view(view_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `view_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the view                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewResponse](../../models/viewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_view

#### Allowed For

* Agents

#### JSON Format

 The PUT request takes one property, a `view` object that lists the values to update. All properties are optional.

**Note**: Updating a condition updates the containing array, clearing the other conditions. Include all your conditions when updating any condition.

| Name        | Description
| ----------- | -----------
| title       | The title of the view
| all         | An array of one or more conditions. A ticket must meet all the conditions to be included in the view. The PUT request replaces all existing conditions. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
| any         | An array of one or more conditions. A ticket must meet any of them to be included in the view. At least one `all` condition must be defined with the `any` conditions. The PUT request replaces all existing `any` conditions. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)
| active      | Allowed values are true or false. Determines if the view is displayed or not
| output      | An object that specifies the columns to display. Example: `"output": {"columns": ["status", "description," "priority"]}`. See [View columns](#view-columns)
| restriction | An object that describes who can access the view. To give all agents access to the view, omit this property

The `restriction` object has the following properties.

| Name | Comment
| ---- | -------
| type | Allowed values are "Group" or "User"
| id   | The numeric ID of a single group or user
| ids  | The numeric IDs of a single or more groups. Recommended for "Group" `type`

If `type` is "Group", the `ids` property is the preferred method of specifying the group id or ids.

You can also update how items are sorted and grouped. See [View sorting](#view-sorting) in Create View.

#### Example Request Body

```js
{
  "view": {
    "title": "Code red tickets",
    "restriction": {
      "type": "Group",
      "ids": [10052, 10057, 10062, 10002]
    },
    "all": [
      {
        "field": "priority",
        "operator": "is",
        "value": "urgent"
      }
    ],
    "output": {
      "columns": ["status", "requester", "assignee", "updated"]
    }
  }
}
```


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateView" method="put" path="/api/v2/views/{view_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.update_view(view_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `view_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the view                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewResponse](../../models/viewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_view

#### Allowed For
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteView" method="delete" path="/api/v2/views/{view_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.views.delete_view(view_id=25)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `view_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the view                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_view_count

Returns the ticket count for a single view.

This endpoint is rate limited to 5 requests per minute, per view, per agent.

#### View Counts

The view count endpoints, Count Tickets in View (this endpoint) and [Count Tickets in Views](#count-tickets-in-views), let you estimate how many tickets remain in a view without having to retrieve the entire view. They're designed to help estimate view size. From a business perspective, accuracy becomes less relevant as view size increases.

To ensure quality of service, these counts are cached more heavily as the number of tickets in a view grows. For a view with thousands of tickets, you can expect the count to be cached for 60-90 minutes. As a result, the count may not reflect the actual number of tickets in your view.

View counts are represented as JSON objects with the following attributes:

| Name            | Type        | Comment
| --------------- | ------------| -------
| view_id         | integer     | The id of the view
| url             | string      | The API url of the count
| value           | integer     | The cached number of tickets in the view. Can also be null if the system is loading and caching new data. Not to be confused with 0 tickets
| pretty          | string      | A pretty-printed text approximation of the view count
| fresh           | boolean     | false if the cached data is stale and the system is still loading and caching new data
| active          | boolean     | Only active views if true, inactive views if false, all views if null.

#### Example
```js
{
  "view_count": {
    "view_id": 25,
    "url":     "https://company.zendesk.com/api/v2/views/25/count.json",
    "value":   719,
    "pretty":  "~700",
    "fresh":   true
  }
}
```


### Example Usage

<!-- UsageSnippet language="python" operationID="GetViewCount" method="get" path="/api/v2/views/{view_id}/count" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.get_view_count(view_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `view_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the view                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewCountResponse](../../models/viewcountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## execute_view

Returns the column titles and the rows of the specified view.

The `columns` array lists the view's column titles and includes only views parameters.

The `rows` array lists the values of each column for each ticket and includes parameters from both views and tickets. Though not displayed in the view, a partial ticket object is included with each row object.

**Note**: To get the full ticket objects for a specified view, use [List Tickets from a View](#list-tickets-from-a-view).

This endpoint is rate limited to 5 requests per minute, per view, per agent. This rate limit includes activity in Zendesk Support. An API script is more likely to encounter rate limit errors if the authenticating agent or admin is concurrently active in Zendesk Support.

The view execution system is designed for periodic rather than high-frequency API usage. In particular, views called very frequently may be cached by Zendesk. This means that the API client will still receive a result, but that result may have been computed at any time within the last 10 minutes.

Zendesk recommends using the Incremental Ticket Export endpoint to get the latest changes. You can call it more often, and it returns all the tickets that changed since the last poll. For details and rate limits, see [Incremental Exports](/api-reference/ticketing/ticket-management/incremental_exports/).

View output sorting can be controlled by passing the `sort_by` and `sort_order` parameters in the format described in the table in [Preview Views](#preview-views).

#### Allowed For

* Agents

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).


### Example Usage

<!-- UsageSnippet language="python" operationID="ExecuteView" method="get" path="/api/v2/views/{view_id}/execute" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.execute_view(view_id=25, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `view_id`                                                                                                                                                                                                                                                                                                           | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The ID of the view                                                                                                                                                                                                                                                                                                  |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `sort_by`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The ticket field used for sorting. This will either be a title or a custom field id.                                                                                                                                                                                                                                |
| `sort_order`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The direction the tickets are sorted. May be one of 'asc' or 'desc'                                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ExecuteViewResponse](../../models/executeviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## export_view

Returns the csv attachment of the specified view if possible. Enqueues a job to produce the csv if necessary.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ExportView" method="get" path="/api/v2/views/{view_id}/export" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.export_view(view_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `view_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the view                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewExportResponse](../../models/viewexportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_tickets_from_view

#### Allowed For

* Agents

#### Pagination
* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).


### Example Usage

<!-- UsageSnippet language="python" operationID="ListTicketsFromView" method="get" path="/api/v2/views/{view_id}/tickets" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.list_tickets_from_view(view_id=25, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `view_id`                                                                                                                                                                                                                                                                                                           | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The ID of the view                                                                                                                                                                                                                                                                                                  |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `sort_by`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Sort or group the tickets by a column in the [View columns](#view-columns) table. The `subject` and `submitter` columns are not supported                                                                                                                                                                           |
| `sort_order`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListTicketsFromViewResponse](../../models/listticketsfromviewresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_views

Lists active shared and personal views available to the current user.

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each view, if present
| permissions      | The permissions for each view

#### Pagination

- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListActiveViews" method="get" path="/api/v2/views/active" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.list_active_views()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `access`                                                                                            | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | Only views with given access. May be "personal", "shared", or "account"                             |
| `group_id`                                                                                          | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | Only views belonging to given group                                                                 |
| `sort_by`                                                                                           | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | Possible values are "alphabetical", "created_at", or "updated_at". Defaults to "position"           |
| `sort_order`                                                                                        | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.ViewsResponse](../../models/viewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_compact_views

A compacted list of shared and personal views available to the current user. This endpoint never returns more than 32 records and does not respect the "per_page" option.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListCompactViews" method="get" path="/api/v2/views/compact" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.list_compact_views()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewsResponse](../../models/viewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_views

Returns an approximate count of shared and personal views available to the current user. If the count exceeds 100,000, the count will return a cached result.  This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null.
This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For
* Agents

### Example Usage

<!-- UsageSnippet language="python" operationID="CountViews" method="get" path="/api/v2/views/count" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.count_views()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewsCountResponse](../../models/viewscountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_view_counts

Returns the ticket count of each view in a list of views. Accepts up to 20 view ids per request. For the ticket count of a single view, see [Count Tickets in View](#count-tickets-in-view).

Only returns values for personal and shared views accessible to the user performing the request.

This endpoint is rate limited to 6 requests every 5 minutes.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="GetViewCounts" method="get" path="/api/v2/views/count_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.get_view_counts(ids="1,2,3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | List of view's ids separated by commas.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewCountsResponse](../../models/viewcountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## bulk_delete_views

Deletes the views corresponding to the provided list of IDs.

#### Allowed For
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="BulkDeleteViews" method="delete" path="/api/v2/views/destroy_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.views.bulk_delete_views(ids="1,2,3")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | The IDs of the views to delete                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## preview_views

You can preview views by constructing the conditions in the proper format and nesting them under the `view` property. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference/). The output can also be controlled by passing in any of the following parameters and nesting them under the `output` property.

| Name            | Type    | Comment
| --------------- | ------- | -------
| columns         | Array   | The ticket fields to display. System fields are looked up by name, custom fields by title or id. See the [View columns](#view-columns) table
| group_by        | String  | When present, the field by which the tickets are grouped
| group_order     | String  | The direction the tickets are grouped. May be one of "asc" or "desc"
| sort_order      | String  | The direction the tickets are sorted. May be one of "asc" or "desc"
| sort_by         | String  | The ticket field used for sorting. This will either be a title or a custom field id.

This endpoint is rate limited to 5 requests per minute, per view, per agent.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="PreviewViews" method="post" path="/api/v2/views/preview" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.preview_views(page_size=100)

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

**[models.PreviewViewsResponse](../../models/previewviewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## preview_count

Returns the ticket count for a single preview.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="PreviewCount" method="post" path="/api/v2/views/preview/count" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.preview_count()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewCountResponse](../../models/viewcountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_views

#### Pagination

* Offset pagination only

See [Using Offset Pagination](/api-reference/ticketing/introduction/#using-offset-pagination).

#### Allowed For

* Agents

#### Sideloads

The following sideloads are supported. For more information, see [Side-loading](/documentation/ticketing/using-the-zendesk-api/side_loading/).

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each view, if present
| permissions      | The permissions for each view


### Example Usage

<!-- UsageSnippet language="python" operationID="SearchViews" method="get" path="/api/v2/views/search" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.search_views(query="sales&group_id=25789188", include="permissions")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                           | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | Query string used to find all views with matching title                                                                           |
| `access`                                                                                                                          | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Filter views by access. May be "personal", "shared", or "account"                                                                 |
| `active`                                                                                                                          | *Optional[bool]*                                                                                                                  | :heavy_minus_sign:                                                                                                                | Filter by active views if true or inactive views if false                                                                         |
| `group_id`                                                                                                                        | *Optional[int]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Filter views by group                                                                                                             |
| `sort_by`                                                                                                                         | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | Possible values are "alphabetical", "created_at", "updated_at", and "position". If unspecified, the views are sorted by relevance |
| `sort_order`                                                                                                                      | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                               |
| `include`                                                                                                                         | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | A sideload to include in the response. See [Sideloads](#sideloads-3)                                                              |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |

### Response

**[models.ViewsResponse](../../models/viewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_views_by_id

#### Allowed For

* Agents

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| app_installation | The app installation that requires each view, if present
| permissions      | The permissions for each view


### Example Usage

<!-- UsageSnippet language="python" operationID="ListViewsById" method="get" path="/api/v2/views/show_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.list_views_by_id(ids="1,2,3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | List of view's ids separated by commas.                             |
| `active`                                                            | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Only active views if true, inactive views if false                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewsResponse](../../models/viewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many_views

#### Allowed For

* Agents

#### Request Parameters

The PUT request expects a `views` object that lists the views to update.

Each view may have the following properties:

| Name     | Mandatory | Description
| -------- | --------- | -----------
| id       | yes       | The ID of the view to update
| position | no        | The new position of the view
| active   | no        | The active status of the view (true or false)

#### Example Request Body

```js
{
  "views": [
    {"id": 25, "position": 3},
    {"id": 23, "position": 5},
    {"id": 27, "position": 9},
    {"id": 22, "position": 7}
  ]
}
```


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateManyViews" method="put" path="/api/v2/views/update_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.views.update_many_views()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ViewsResponse](../../models/viewsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |