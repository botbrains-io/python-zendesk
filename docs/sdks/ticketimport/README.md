# TicketImport

## Overview

### Available Operations

* [ticket_import](#ticket_import) - Ticket Import
* [ticket_bulk_import](#ticket_bulk_import) - Ticket Bulk Import

## ticket_import

#### Allowed For

* Admins

### Example Usage

<!-- UsageSnippet language="python" operationID="TicketImport" method="post" path="/api/v2/imports/tickets" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_import.ticket_import(ticket_import_request={
        "ticket": {
            "assignee_id": 19,
            "comments": [
                {
                    "value": "This is a comment",
                    "author_id": 827,
                },
                {
                    "value": "This is a private comment",
                    "author_id": 19,
                    "public": False,
                },
            ],
            "description": "A description",
            "requester_id": 827,
            "subject": "Help",
            "tags": [
                "foo",
                "bar",
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `archive_immediately`                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | If `true`, any ticket created with a `closed` status bypasses the normal ticket lifecycle and will be created directly in your ticket archive |
| `ticket_import_request`                                                                                                                       | [Optional[models.TicketImportRequest]](../../models/ticketimportrequest.md)                                                                   | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.TicketResponse](../../models/ticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## ticket_bulk_import

Accepts an array of up to 100 ticket objects.

#### Allowed For

* Admins

### Example Usage

<!-- UsageSnippet language="python" operationID="TicketBulkImport" method="post" path="/api/v2/imports/tickets/create_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_import.ticket_bulk_import(ticket_bulk_import_request={
        "tickets": [
            {
                "assignee_id": 19,
                "comments": [
                    {
                        "value": "This is a comment",
                        "author_id": 827,
                    },
                    {
                        "value": "This is a private comment",
                        "author_id": 19,
                        "public": False,
                    },
                ],
                "description": "A description",
                "requester_id": 827,
                "subject": "Help",
                "tags": [
                    "foo",
                    "bar",
                ],
            },
            {
                "assignee_id": 21,
                "comments": [
                    {
                        "value": "This is a comment",
                        "author_id": 830,
                    },
                    {
                        "value": "This is a private comment",
                        "author_id": 21,
                        "public": False,
                    },
                ],
                "description": "A description",
                "requester_id": 830,
                "subject": "Missing Item",
                "tags": [
                    "foo",
                    "bar",
                ],
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `archive_immediately`                                                                                                                         | *Optional[bool]*                                                                                                                              | :heavy_minus_sign:                                                                                                                            | If `true`, any ticket created with a `closed` status bypasses the normal ticket lifecycle and will be created directly in your ticket archive |
| `ticket_bulk_import_request`                                                                                                                  | [Optional[models.TicketBulkImportRequest]](../../models/ticketbulkimportrequest.md)                                                           | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |