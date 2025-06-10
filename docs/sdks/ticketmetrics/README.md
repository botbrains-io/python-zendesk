# TicketMetrics
(*ticket_metrics*)

## Overview

### Available Operations

* [list_ticket_metrics](#list_ticket_metrics) - List Ticket Metrics
* [show_ticket_metrics](#show_ticket_metrics) - Show Ticket Metrics

## list_ticket_metrics

Returns a list of tickets with their metrics.

Tickets are ordered chronologically by created date, from newest to oldest.
The last ticket listed may not be the absolute oldest ticket in your account
due to ticket archiving.

Archived tickets are not included in the response. See
[About archived tickets](https://support.zendesk.com/hc/en-us/articles/203657756) in
Zendesk help.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.


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

    res = z_client.ticket_metrics.list_ticket_metrics()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketMetricsResponse](../../models/ticketmetricsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_ticket_metrics

Returns a specific metric, or the metrics of a specific ticket.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

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

    res = z_client.ticket_metrics.show_ticket_metrics(ticket_metric_id="10001")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_metric_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The id of the ticket metric to retrieve                             | 10001                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TicketMetricsByTicketMetricIDResponse](../../models/ticketmetricsbyticketmetricidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |