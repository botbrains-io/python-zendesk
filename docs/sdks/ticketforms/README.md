# TicketForms
(*ticket_forms*)

## Overview

### Available Operations

* [list_ticket_forms](#list_ticket_forms) - List Ticket Forms
* [create_ticket_form](#create_ticket_form) - Create Ticket Form
* [show_ticket_form](#show_ticket_form) - Show Ticket Form
* [update_ticket_form](#update_ticket_form) - Update Ticket Form
* [delete_ticket_form](#delete_ticket_form) - Delete Ticket Form
* [clone_ticket_form](#clone_ticket_form) - Clone an Already Existing Ticket Form
* [ticket_form_ticket_form_statuses](#ticket_form_ticket_form_statuses) - List Ticket Form Statuses of a Ticket Form
* [create_ticket_form_statuses](#create_ticket_form_statuses) - Create Ticket Form Statuses
* [update_ticket_form_statuses](#update_ticket_form_statuses) - Bulk Update Ticket Form Statuses of a Ticket Form
* [update_ticket_form_status_by_id](#update_ticket_form_status_by_id) - Update Ticket Form Status By Id
* [reorder_ticket_forms](#reorder_ticket_forms) - Reorder Ticket Forms
* [show_many_ticket_forms](#show_many_ticket_forms) - Show Many Ticket Forms

## list_ticket_forms

Returns a list of all ticket forms for your account if accessed as an admin or agent. End users only see ticket forms that have `end_user_visible` set to true.

#### Allowed For

* Anyone


### Example Usage

<!-- UsageSnippet language="python" operationID="ListTicketForms" method="get" path="/api/v2/ticket_forms" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_forms.list_ticket_forms()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `active`                                                                                                                                           | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | true returns active ticket forms; false returns inactive ticket forms. If not present, returns both                                                |
| `end_user_visible`                                                                                                                                 | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | true returns ticket forms where `end_user_visible`; false returns ticket forms that are not end-user visible. If not present, returns both         |
| `fallback_to_default`                                                                                                                              | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | true returns the default ticket form when the criteria defined by the parameters results in a set without active and end-user visible ticket forms |
| `associated_to_brand`                                                                                                                              | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | true returns the ticket forms of the brand specified by the url's subdomain                                                                        |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.TicketFormsResponse](../../models/ticketformsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_ticket_form

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateTicketForm" method="post" path="/api/v2/ticket_forms" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_forms.create_ticket_form()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormResponse](../../models/ticketformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_ticket_form

#### Allowed For

* Admins, Agents, and End Users


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowTicketForm" method="get" path="/api/v2/ticket_forms/{ticket_form_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_forms.show_ticket_form(ticket_form_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_form_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket form                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormResponse](../../models/ticketformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_ticket_form

#### Allowed For
* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateTicketForm" method="put" path="/api/v2/ticket_forms/{ticket_form_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_forms.update_ticket_form(ticket_form_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_form_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket form                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormResponse](../../models/ticketformresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_ticket_form

#### Allowed For
* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteTicketForm" method="delete" path="/api/v2/ticket_forms/{ticket_form_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.ticket_forms.delete_ticket_form(ticket_form_id=47)

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

## clone_ticket_form

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="CloneTicketForm" method="post" path="/api/v2/ticket_forms/{ticket_form_id}/clone" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_forms.clone_ticket_form(ticket_form_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_form_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket form                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormResponse](../../models/ticketformresponse.md)**

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

    res = z_client.ticket_forms.ticket_form_ticket_form_statuses(ticket_form_id=47)

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

    res = z_client.ticket_forms.create_ticket_form_statuses(ticket_form_id=47, ticket_form_status=[
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

    res = z_client.ticket_forms.update_ticket_form_statuses(ticket_form_id=47, ticket_form_status=[
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

    res = z_client.ticket_forms.update_ticket_form_status_by_id(ticket_form_id=47, ticket_form_status_id="abcdef", ticket_form_status=[
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

## reorder_ticket_forms

#### Allowed For
* Admins

#### Request Parameters

You can pass in the following parameter in the payload:

| Name                | Type   | Comment
| ------------------- | ------ | --------
| ticket_form_ids     | array  | An array of ticket form ids. Example: "[2, 23, 46, 50]"


### Example Usage

<!-- UsageSnippet language="python" operationID="ReorderTicketForms" method="put" path="/api/v2/ticket_forms/reorder" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_forms.reorder_ticket_forms()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFormsResponse](../../models/ticketformsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_many_ticket_forms

Takes an `ids` query parameter that accepts a comma-separated list of up to 100 ticket form ids. This endpoint is used primarily by the [mobile SDK](/documentation/classic-web-widget-sdks/) and the [Web Widget](/api-reference/widget/introduction/).

#### Allowed For

* Anyone


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowManyTicketForms" method="get" path="/api/v2/ticket_forms/show_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_forms.show_many_ticket_forms(ids="1,2,3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ids`                                                                                                                                              | *str*                                                                                                                                              | :heavy_check_mark:                                                                                                                                 | IDs of the ticket forms to be shown                                                                                                                |
| `active`                                                                                                                                           | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | true returns active ticket forms; false returns inactive ticket forms. If not present, returns both                                                |
| `end_user_visible`                                                                                                                                 | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | true returns ticket forms where `end_user_visible`; false returns ticket forms that are not end-user visible. If not present, returns both         |
| `fallback_to_default`                                                                                                                              | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | true returns the default ticket form when the criteria defined by the parameters results in a set without active and end-user visible ticket forms |
| `associated_to_brand`                                                                                                                              | *Optional[bool]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                 | true returns the ticket forms of the brand specified by the url's subdomain                                                                        |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.TicketFormsResponse](../../models/ticketformsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |