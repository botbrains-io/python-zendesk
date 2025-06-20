# IncrementalExport
(*incremental_export*)

## Overview

### Available Operations

* [incremental_sample_export](#incremental_sample_export) - Incremental Sample Export
* [incremental_organization_export](#incremental_organization_export) - Incremental Organization Export
* [incremental_ticket_events](#incremental_ticket_events) - Incremental Ticket Event Export
* [incremental_ticket_export_time](#incremental_ticket_export_time) - Incremental Ticket Export, Time Based
* [incremental_ticket_export_cursor](#incremental_ticket_export_cursor) - Incremental Ticket Export, Cursor Based
* [incremental_user_export_time](#incremental_user_export_time) - Incremental User Export, Time Based
* [incremental_user_export_cursor](#incremental_user_export_cursor) - Incremental User Export, Cursor Based

## incremental_sample_export

Use this endpoint to test the incremental export format. It's more strict in terms of rate limiting,
at 10 requests per 20 minutes instead of 10 requests per minute. It also returns only up to 50
results per request. Otherwise, it's identical to the above APIs.

Use the `incremental_resource` parameter to specify the resource. Possible values are "tickets", "ticket_events", "users", or "organizations".


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_export.incremental_sample_export(start_time=1332034771, incremental_resource="tickets")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                           | *int*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute |
| `incremental_resource`                                                                                                                 | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The resource requested for incremental sample export                                                                                   |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.TimeBasedExportIncrementalTicketsResponse](../../models/timebasedexportincrementalticketsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## incremental_organization_export

#### Allowed For

 * Admins

#### Sideloading

See [Organizations sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints).


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_export.incremental_organization_export(start_time=1332034771)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                           | *int*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute |
| `per_page`                                                                                                                             | *Optional[int]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | The number of records to return per page                                                                                               |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.ExportIncrementalOrganizationsResponse](../../models/exportincrementalorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## incremental_ticket_events

Returns a stream of changes that occurred on tickets, excluding events occuring within one minute of the request. Each event is tied
to an update on a ticket and contains all the fields that were updated in that
change. For more information, see:

- [Exporting ticket events](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#exporting-ticket-events) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api)
- [Time-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#time-based-incremental-exports) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api)

You can include comments in the event stream by using the `comment_events`
sideload. See Sideloading below. If you don't specify the sideload, any comment
present in the ticket update is described only by Boolean `comment_present`
and `comment_public` object properties in the event's `child_events` array.
The comment itself is not included.

#### Allowed For

 * Admins

#### Sideloading

The endpoint supports the `comment_events` sideload. Any comment present in the ticket
update is listed as an object in the event's `child_events` array. Example:

```js
"child_events": [
  {
    "id": 91048994488,
    "via": {
      "channel": "api",
      "source": {"from":{},"to":{},"rel":null}},
    "via_reference_id":null,
    "type": "Comment",
    "author_id": 5031726587,
    "body": "This is a comment",
    "html_body": "&lt;div class="zd-comment"&gt;&lt;p dir="auto"&gt;This is a comment&lt;/p&gt;",
    "public": true,
    "attachments": [],
    "audit_id": 91048994468,
    "created_at": "2009-06-25T10:15:18Z",
    "event_type": "Comment"
  },
  ...
],
...
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

    res = z_client.incremental_export.incremental_ticket_events(start_time=1332034771)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                           | *int*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.ExportIncrementalTicketEventsResponse](../../models/exportincrementalticketeventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## incremental_ticket_export_time

Returns the tickets that changed since the start time. For more information,
see [Exporting tickets](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#exporting-tickets) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api).

This endpoint supports time-based incremental exports.
For more information, see [Time-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#time-based-incremental-exports) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api). You can also return tickets using cursor-based pagination. See [Incremental Ticket Export, Cursor Based](#incremental-ticket-export-cursor-based).

The results include tickets that were updated by the system. See
[Excluding system-updated tickets](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#excluding-system-updated-tickets-time-based-exports) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api).

The endpoint can return tickets with an `updated_at` time that's earlier than the
`start_time` time. The reason is that the API compares the `start_time` with the ticket's
`generated_timestamp` value, not its `updated_at` value. The `updated_at` value is
updated only if the update generates a [ticket event](#incremental-ticket-event-export).
The `generated_timestamp` value is updated for all ticket updates, including system
updates. If a system update occurs after a ticket event, the unchanged
`updated_at` time will become earlier relative to the updated `generated_timestamp`
time.

#### Allowed For

 * Admins

#### Sideloading

See [Tickets sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints). For performance reasons,
`last_audits` sideloads aren't supported.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_export.incremental_ticket_export_time(start_time=1332034771)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                           | *int*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.TimeBasedExportIncrementalTicketsResponse](../../models/timebasedexportincrementalticketsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## incremental_ticket_export_cursor

Returns the tickets that changed since the start time. For more information,
see [Exporting tickets](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#exporting-tickets) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api).

This endpoint supports cursor-based incremental exports.
Cursor-based exports are highly encouraged because they provide more consistent performance and
response body sizes. For more information, see [Cursor-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#cursor-based-incremental-exports) in [Using the Incremental Exports API](/documentation/ticketing/managing-tickets/using-the-incremental-export-api).



#### Allowed For

 * Admins

#### Sideloading

See [Tickets sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints). For performance reasons,
`last_audits` sideloads aren't supported.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_export.incremental_ticket_export_cursor(start_time=1332034771)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                           | *int*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute |
| `cursor`                                                                                                                               | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | The cursor pointer to work with for all subsequent exports after the initial request                                                   |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.CursorBasedExportIncrementalTicketsResponse](../../models/cursorbasedexportincrementalticketsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## incremental_user_export_time

#### Allowed For

 * Admins

#### Sideloading

See [Users sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints).


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_export.incremental_user_export_time(start_time=1332034771)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                           | *int*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute |
| `per_page`                                                                                                                             | *Optional[int]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | The number of records to return per page                                                                                               |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.TimeBasedExportIncrementalUsersResponse](../../models/timebasedexportincrementalusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## incremental_user_export_cursor

#### Allowed For

 * Admins

#### Sideloading

See [Users sideloads](/documentation/ticketing/using-the-zendesk-api/side_loading/#supported-endpoints).


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_export.incremental_user_export_cursor(start_time=1332034771)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                           | *int*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The time to start the incremental export from. Must be at least one minute in the past. Data isn't provided for the most recent minute |
| `cursor`                                                                                                                               | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | The cursor pointer to work with for all subsequent exports after the initial request                                                   |
| `per_page`                                                                                                                             | *Optional[int]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | The number of records to return per page                                                                                               |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |

### Response

**[models.CursorBasedExportIncrementalUsersResponse](../../models/cursorbasedexportincrementalusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |