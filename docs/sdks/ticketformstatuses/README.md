# TicketFormStatuses

## Overview

### Available Operations

* [create_ticket_form_statuses_for_custom_status](#create_ticket_form_statuses_for_custom_status) - Create Ticket Form Statuses for a Custom Status
* [list_ticket_form_statuses](#list_ticket_form_statuses) - List Ticket Form Statuses
* [show_many_ticket_form_statuses](#show_many_ticket_form_statuses) - Show Many Ticket Form Statuses
* [ticket_form_ticket_form_statuses](#ticket_form_ticket_form_statuses) - List Ticket Form Statuses of a Ticket Form
* [create_ticket_form_statuses](#create_ticket_form_statuses) - Create Ticket Form Statuses
* [update_ticket_form_statuses](#update_ticket_form_statuses) - Bulk Update Ticket Form Statuses of a Ticket Form
* [delete_ticket_form_statuses](#delete_ticket_form_statuses) - Delete Ticket Form Statuses
* [update_ticket_form_status_by_id](#update_ticket_form_status_by_id) - Update Ticket Form Status By Id
* [delete_ticket_form_status_by_id](#delete_ticket_form_status_by_id) - Delete Ticket Form Status By Id

## create_ticket_form_statuses_for_custom_status

Creates one or many tickets form status associations for a custom status.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateTicketFormStatusesForCustomStatus" method="post" path="/api/v2/custom_statuses/{custom_status_id}/ticket_form_statuses" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_form_statuses.create_ticket_form_statuses_for_custom_status(custom_status_id=1234567, ticket_form_status=[
        {
            "ticket_form_id": 1,
        },
        {
            "ticket_form_id": 2,
        },
        {
            "ticket_form_id": 3,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_status_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The id of the custom status                                         |
| `ticket_form_status`                                                | List[[models.TicketFormStatus](../../models/ticketformstatus.md)]   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormStatusesResponse](../../models/ticketformstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_form_statuses

Fetches all of the ticket form statuses for the account.

#### Allowed For

* Admins
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListTicketFormStatuses" method="get" path="/api/v2/ticket_form_statuses" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_form_statuses.list_ticket_form_statuses()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormStatusesResponse](../../models/ticketformstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_many_ticket_form_statuses

Fetches all of the ticket form statuses specified by a comma separated list of ids.
#### Allowed For
* Admins
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowManyTicketFormStatuses" method="get" path="/api/v2/ticket_form_statuses/show_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_form_statuses.show_many_ticket_form_statuses(ids="abc,def,ghi")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Ticket form status ids to retrieve records for                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormStatusesResponse](../../models/ticketformstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## ticket_form_ticket_form_statuses

Fetches all of the associated ticket form statuses of a ticket form.

#### Allowed For

* Admins
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="TicketFormTicketFormStatuses" method="get" path="/api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_form_statuses.ticket_form_ticket_form_statuses(ticket_form_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_form_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket form                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormStatusesResponse](../../models/ticketformstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_ticket_form_statuses

Creates one or many ticket form status associations

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateTicketFormStatuses" method="post" path="/api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_form_statuses.create_ticket_form_statuses(ticket_form_id=47, ticket_form_status=[
        {
            "custom_status_id": 1234,
        },
        {
            "custom_status_id": 1235,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `ticket_form_id`                                                                              | *int*                                                                                         | :heavy_check_mark:                                                                            | The ID of the ticket form                                                                     |
| `ticket_form_status`                                                                          | List[[models.TicketFormStatusesCreateParams](../../models/ticketformstatusescreateparams.md)] | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.TicketFormStatusesResponse](../../models/ticketformstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_ticket_form_statuses

Updates or deletes ticket form status associations. This is a bulk operation that can both add and remove ticket form status associations for a form in one call.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateTicketFormStatuses" method="put" path="/api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_form_statuses.update_ticket_form_statuses(ticket_form_id=47, ticket_form_status=[
        {
            "destroy": "1",
            "id": "abcdef",
        },
        {
            "custom_status_id": 1,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `ticket_form_id`                                                                              | *int*                                                                                         | :heavy_check_mark:                                                                            | The ID of the ticket form                                                                     |
| `ticket_form_status`                                                                          | List[[models.TicketFormStatusesUpdateParams](../../models/ticketformstatusesupdateparams.md)] | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.TicketFormStatusesResponse](../../models/ticketformstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_ticket_form_statuses

Deletes all of of the ticket form statuses by id.

#### Allowed For

* Admins
* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteTicketFormStatuses" method="delete" path="/api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.ticket_form_statuses.delete_ticket_form_statuses(ticket_form_id=47)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_form_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket form                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_ticket_form_status_by_id

Updates or deletes ticket form status association by id.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateTicketFormStatusById" method="put" path="/api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses/{ticket_form_status_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_form_statuses.update_ticket_form_status_by_id(ticket_form_id=47, ticket_form_status_id="abcdef", ticket_form_status=[
        {
            "custom_status_id": 1,
        },
        {
            "custom_status_id": 2,
        },
        {
            "custom_status_id": 3,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `ticket_form_id`                                                                              | *int*                                                                                         | :heavy_check_mark:                                                                            | The ID of the ticket form                                                                     |
| `ticket_form_status_id`                                                                       | *str*                                                                                         | :heavy_check_mark:                                                                            | The id of the ticket form status                                                              |
| `ticket_form_status`                                                                          | List[[models.TicketFormStatusesUpdateParams](../../models/ticketformstatusesupdateparams.md)] | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.TicketFormStatusesResponse](../../models/ticketformstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_ticket_form_status_by_id

Deletes a ticket form status by id.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteTicketFormStatusById" method="delete" path="/api/v2/ticket_forms/{ticket_form_id}/ticket_form_statuses/{ticket_form_status_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.ticket_form_statuses.delete_ticket_form_status_by_id(ticket_form_id=47, ticket_form_status_id="abcdef")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_form_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket form                                           |
| `ticket_form_status_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | The id of the ticket form status                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |