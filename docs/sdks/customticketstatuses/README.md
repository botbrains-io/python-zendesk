# CustomTicketStatuses
(*custom_ticket_statuses*)

## Overview

### Available Operations

* [bulk_update_default_custom_status](#bulk_update_default_custom_status) - Bulk Update Default Custom Ticket Status
* [list_custom_statuses](#list_custom_statuses) - List Custom Ticket Statuses
* [create_custom_status](#create_custom_status) - Create Custom Ticket Status
* [show_custom_status](#show_custom_status) - Show Custom Ticket Status
* [update_custom_status](#update_custom_status) - Update Custom Ticket Status
* [create_ticket_form_statuses_for_custom_status](#create_ticket_form_statuses_for_custom_status) - Create Ticket Form Statuses for a Custom Status

## bulk_update_default_custom_status

Updates the default values for many custom ticket statuses at once.

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

    res = z_client.custom_ticket_statuses.bulk_update_default_custom_status(request={
        "ids": "1234567,1234577",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.BulkUpdateDefaultCustomStatusRequest](../../models/bulkupdatedefaultcustomstatusrequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.BulkUpdateDefaultCustomStatusResponse](../../models/bulkupdatedefaultcustomstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_custom_statuses

Lists all undeleted custom ticket statuses for the account. No pagination is provided.

#### Allowed For

* End Users


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_ticket_statuses.list_custom_statuses()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `status_categories`                                                                                                                                                   | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | Filter the list of custom ticket statuses by a comma-separated list of status categories                                                                              |
| `active`                                                                                                                                                              | *Optional[bool]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | If true, show only active custom ticket statuses. If false, show only inactive custom ticket statuses. If the filter is not used, show all custom ticket statuses     |
| `default`                                                                                                                                                             | *Optional[bool]*                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | If true, show only default custom ticket statuses. If false, show only non-default custom ticket statuses. If the filter is not used, show all custom ticket statuses |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |

### Response

**[models.CustomStatusesResponse](../../models/customstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_custom_status

Takes a `custom_status` object that specifies the custom ticket status properties to create.

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

    res = z_client.custom_ticket_statuses.create_custom_status(request={
        "custom_status": {
            "active": True,
            "agent_label": "Responding quickly",
            "description": "Customer needs a response quickly",
            "end_user_description": "Your ticket is being responded to",
            "end_user_label": "Urgent processing",
            "status_category": "open",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.CustomStatusCreateRequest](../../models/customstatuscreaterequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.CustomStatusResponse](../../models/customstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_custom_status

Returns the custom ticket status object.

#### Allowed For

* End Users


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_ticket_statuses.show_custom_status(custom_status_id=1234567)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_status_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The id of the custom status                                         | 1234567                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomStatusResponse](../../models/customstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_custom_status

Takes a `custom_status` object that specifies the properties to update.

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

    res = z_client.custom_ticket_statuses.update_custom_status(custom_status_id=1234567, custom_status={
        "active": True,
        "agent_label": "Responding quickly",
        "description": "Customer needs a response quickly",
        "end_user_description": "Your ticket is being responded to",
        "end_user_label": "Urgent processing",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `custom_status_id`                                                                  | *int*                                                                               | :heavy_check_mark:                                                                  | The id of the custom status                                                         | 1234567                                                                             |
| `custom_status`                                                                     | [Optional[models.CustomStatusUpdateInput]](../../models/customstatusupdateinput.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.CustomStatusResponse](../../models/customstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_ticket_form_statuses_for_custom_status

Creates one or many tickets form status associations for a custom status.

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

    res = z_client.custom_ticket_statuses.create_ticket_form_statuses_for_custom_status(custom_status_id=1234567, ticket_form_status=[
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_status_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The id of the custom status                                         | 1234567                                                             |
| `ticket_form_status`                                                | List[[models.TicketFormStatus](../../models/ticketformstatus.md)]   | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TicketFormStatusesResponse](../../models/ticketformstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |