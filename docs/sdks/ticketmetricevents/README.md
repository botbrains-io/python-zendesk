# TicketMetricEvents
(*ticket_metric_events*)

## Overview

### Available Operations

* [list_ticket_metric_events](#list_ticket_metric_events) - List Ticket Metric Events

## list_ticket_metric_events

Returns ticket metric events that occurred on or after the start time.

Cursor pagination returns a maximum of 100 records per page. Events are listed in chronological order.

If the results are not paginated, events will be returned as a time-based incremental export.

See [Time-based incremental exports](/documentation/ticketing/managing-tickets/using-the-incremental-export-api#time-based-incremental-exports).

#### Pagination
* Cursor pagination

See [Pagination](/api-reference/introduction/pagination/).

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

    res = z_client.ticket_metric_events.list_ticket_metric_events(start_time=1332034771)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       | Example                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `start_time`                                                                                                                      | *int*                                                                                                                             | :heavy_check_mark:                                                                                                                | The Unix UTC epoch time of the oldest event you're interested in. Example: 1332034771.                                            | 1332034771                                                                                                                        |
| `include_changes`                                                                                                                 | *Optional[bool]*                                                                                                                  | :heavy_minus_sign:                                                                                                                | This optional parameter enhances incremental data retrieval, delivering a consistent and accurate representation of data changes. |                                                                                                                                   |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |                                                                                                                                   |

### Response

**[models.TicketMetricEventsResponse](../../models/ticketmetriceventsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |