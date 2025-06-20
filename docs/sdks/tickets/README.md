# Tickets
(*tickets*)

## Overview

### Available Operations

* [list_deleted_tickets](#list_deleted_tickets) - List Deleted Tickets
* [delete_ticket_permanently](#delete_ticket_permanently) - Delete Ticket Permanently
* [restore_deleted_ticket](#restore_deleted_ticket) - Restore a Previously Deleted Ticket
* [bulk_permanently_delete_tickets](#bulk_permanently_delete_tickets) - Delete Multiple Tickets Permanently
* [bulk_restore_deleted_tickets](#bulk_restore_deleted_tickets) - Restore Previously Deleted Tickets in Bulk
* [list_ticket_problems](#list_ticket_problems) - List Ticket Problems
* [autocomplete_problems](#autocomplete_problems) - Autocomplete Problems
* [list_tickets](#list_tickets) - List Tickets
* [create_ticket](#create_ticket) - Create Ticket
* [show_ticket](#show_ticket) - Show Ticket
* [update_ticket](#update_ticket) - Update Ticket
* [delete_ticket](#delete_ticket) - Delete Ticket
* [list_ticket_collaborators](#list_ticket_collaborators) - List Collaborators for a Ticket
* [list_ticket_email_c_cs](#list_ticket_email_c_cs) - List Email CCs for a Ticket
* [list_ticket_followers](#list_ticket_followers) - List Followers for a Ticket
* [list_ticket_incidents](#list_ticket_incidents) - List Ticket Incidents
* [mark_ticket_as_spam_and_suspend_requester](#mark_ticket_as_spam_and_suspend_requester) - Mark Ticket as Spam and Suspend Requester
* [merge_tickets_into_target_ticket](#merge_tickets_into_target_ticket) - Merge Tickets into Target Ticket
* [ticket_related_information](#ticket_related_information) - Ticket Related Information
* [count_tickets](#count_tickets) - Count Tickets
* [tickets_create_many](#tickets_create_many) - Create Many Tickets
* [bulk_delete_tickets](#bulk_delete_tickets) - Bulk Delete Tickets
* [mark_many_tickets_as_spam](#mark_many_tickets_as_spam) - Bulk Mark Tickets as Spam
* [tickets_show_many](#tickets_show_many) - Show Multiple Tickets
* [tickets_update_many](#tickets_update_many) - Update Many Tickets

## list_deleted_tickets

Returns a maximum of 100 deleted tickets per page. See [Pagination](/api-reference/introduction/pagination/).

The results includes all deleted (and not yet archived) tickets that
have not yet been [scrubbed](https://support.zendesk.com/hc/en-us/articles/4408845703194#topic_fv5_w51_sdb) in the past 30 days. Archived tickets are
not included in the results. See [About archived tickets](https://support.zendesk.com/hc/en-us/articles/203657756)
in the Support Help Center.

The tickets are ordered chronologically by created date, from oldest to newest.
The first ticket listed may not be the oldest ticket in your
account due to [ticket archiving](https://support.zendesk.com/hc/en-us/articles/203657756).

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Agents

#### Rate Limit

You can make 10 requests every 1 minute using this endpoint.
When making requests beyond page 100, you can make 5 requests every 1 minute.
The rate limiting mechanism behaves as described in
[Monitoring your request activity](/api-reference/ticketing/account-configuration/usage_limits/#monitoring-your-request-activity) in the API introduction.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.list_deleted_tickets(page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sort_by`                                                                                                                                                                                                                                                                                                           | [Optional[models.TicketSortBy]](../../models/ticketsortby.md)                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Sort by                                                                                                                                                                                                                                                                                                             |
| `sort_order`                                                                                                                                                                                                                                                                                                        | [Optional[models.TicketSortOrder]](../../models/ticketsortorder.md)                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Sort order. Defaults to "asc"                                                                                                                                                                                                                                                                                       |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListDeletedTicketsResponseResponse](../../models/listdeletedticketsresponseresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_ticket_permanently

Permanently deletes a soft-deleted ticket. See [Soft delete](https://support.zendesk.com/hc/en-us/articles/4408834005530#topic_zrm_wbj_1db)
in the Zendesk GDPR docs. To soft delete a ticket, use the [Delete Ticket](#delete-ticket) endpoint.

This endpoint enqueues a ticket deletion job and returns a payload with the jobs status.

If the job succeeds, the ticket is permanently deleted. This operation can't be undone.

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work.
Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion.

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

    res = z_client.tickets.delete_ticket_permanently(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## restore_deleted_ticket

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

    res = z_client.tickets.restore_deleted_ticket(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## bulk_permanently_delete_tickets

Permanently deletes up to 100 soft-deleted tickets. See [Soft delete](https://support.zendesk.com/hc/en-us/articles/4408834005530#topic_zrm_wbj_1db)
in the Zendesk GDPR docs. To soft delete tickets, use the [Bulk Delete Tickets](#bulk-delete-tickets) endpoint.

This endpoint accepts a comma-separated list of up to 100 ticket ids. It enqueues
a ticket deletion job and returns a payload with the jobs status.

If one ticket fails to be deleted, the endpoint still attempts to delete the others. If the job succeeds,
the tickets that were successfully deleted are permanently deleted. This operation can't be undone.

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

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

    res = z_client.tickets.bulk_permanently_delete_tickets(ids="35436,35437")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of ticket ids                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## bulk_restore_deleted_tickets

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

    res = z_client.tickets.bulk_restore_deleted_tickets(ids="35436,35437")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of ticket ids                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_problems

The response is always ordered by `updated_at` in descending order

#### Allowed For

* Agents

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.list_ticket_problems(page_size=100)

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

**[models.ListTicketProblemsResponse](../../models/listticketproblemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## autocomplete_problems

Returns tickets whose type is "problem" and whose subject contains the string specified in the `text` parameter.

You can specify the `text` parameter in the request body rather than the query string. Example:

`{"text": "fire"}`

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

    res = z_client.tickets.autocomplete_problems(request_body={
        "text": "fire",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `text`                                                                                              | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | The text to search for                                                                              |
| `request_body`                                                                                      | [Optional[models.AutocompleteProblemsRequestBody]](../../models/autocompleteproblemsrequestbody.md) | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[Dict[str, Any]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_tickets

List Tickets

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.list_tickets(page_size=100, sort="id")

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
| `sort`                                                                                                                                                                                                                                                                                                              | [Optional[models.ListTicketsSort]](../../models/listticketssort.md)                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Sort tickets by field (for cursor pagination use "field" for ascending or "-field" for descending)                                                                                                                                                                                                                  |
| `external_id`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Lists tickets by external id. External ids don't have to be unique for each ticket. As a result, the request may return multiple tickets with the same external id.                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListTicketsResponse](../../models/listticketsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_ticket

Create Ticket

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.create_ticket(request={
        "ticket": {
            "comment": {
                "body": "The smoke is very colorful.",
            },
            "priority": "urgent",
            "subject": "My printer is on fire!",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TicketCreateRequest](../../models/ticketcreaterequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateTicketResponse](../../models/createticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_ticket

Returns a number of ticket properties though not the ticket comments. To get the comments, use [List Comments](/api-reference/ticketing/tickets/ticket_comments/#list-comments)

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

    res = z_client.tickets.show_ticket(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketResponse](../../models/ticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_ticket

Update Ticket

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.update_ticket(ticket_id=123456, ticket={
        "comment": {
            "body": "Thanks for choosing Acme Jet Motors.",
            "public": True,
        },
        "custom_status_id": 321,
        "status": "solved",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `ticket_id`                                                             | *int*                                                                   | :heavy_check_mark:                                                      | The ID of the ticket                                                    |
| `ticket`                                                                | [Optional[models.TicketUpdateInput]](../../models/ticketupdateinput.md) | :heavy_minus_sign:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.TicketUpdateResponse](../../models/ticketupdateresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_ticket

#### Allowed For

* Admins
* Agents with permission to delete tickets

Agent delete permissions are set in Support. See
[Deleting tickets](https://support.zendesk.com/hc/en-us/articles/203690936)
in the Support Help Center.

#### Ticket deletion rate limit

You can delete 400 tickets every 1 minute using this endpoint.
The rate limiting mechanism behaves as described in
[Rate limits](/api-reference/introduction/rate-limits/) in the API introduction.
Zendesk recommends that you obey the Retry-After header values.
To delete many tickets, you may use [Bulk Delete Tickets](/api-reference/ticketing/tickets/tickets/#bulk-delete-tickets).

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.tickets.delete_ticket(ticket_id=123456)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_collaborators

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

    res = z_client.tickets.list_ticket_collaborators(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Dict[str, Any]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_email_c_cs

Returns any users cc'd on the ticket.

#### Availability

The [CCs and Followers](https://support.zendesk.com/hc/en-us/articles/203690846) feature must be enabled in Zendesk Support.

If the feature is not enabled, the default CC functionality is used. In that case, use [List Collaborators](/api-reference/ticketing/tickets/tickets/#list-collaborators-for-a-ticket) to list the users cc'ed on the ticket.

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

    res = z_client.tickets.list_ticket_email_c_cs(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Dict[str, Any]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_followers

Returns any users who follow the ticket.

#### Availability

The [CCs and Followers](https://support.zendesk.com/hc/en-us/articles/203690846) feature must be enabled in Zendesk Support.

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

    res = z_client.tickets.list_ticket_followers(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Dict[str, Any]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_incidents

#### Allowed For

* Agents

#### Pagination
* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.list_ticket_incidents(ticket_id=123456, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ticket_id`                                                                                                                                                                                                                                                                                                         | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The ID of the ticket                                                                                                                                                                                                                                                                                                |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListTicketIncidentsResponse](../../models/listticketincidentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## mark_ticket_as_spam_and_suspend_requester

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

    res = z_client.tickets.mark_ticket_as_spam_and_suspend_requester(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## merge_tickets_into_target_ticket

Merges one or more tickets into the ticket with the specified id.

See [Merging tickets](https://support.zendesk.com/hc/en-us/articles/203690916)
in the Support Help Center for ticket merging rules.

Any attachment to the source ticket is copied to the target ticket.

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

* Agents

Agents in the Enterprise account must have merge permissions.
See [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026)
in the Support Help Center.

#### Available parameters

The request takes a data object with the following properties:

| Name                     | Type    | Required | Comments                                                |
| ------------------------ | ------- | -------- | ------------------------------------------------------- |
| ids                      | array   | yes      | Ids of tickets to merge into the target ticket          |
| target_comment           | string  | no       | Private comment to add to the target ticket. This comment is optional but strongly recommended |
| source_comment           | string  | no       | Private comment to add to the source ticket. This comment is optional but strongly recommended |
| target_comment_is_public | boolean | no       | Whether comments in the target ticket are public or private   |
| source_comment_is_public | boolean | no       | Whether comments in the source tickets are public or private |

`target_comment` and `source_comment` can be used to provide a reason for the merge for recordkeeping purposes. If the source ticket has attachments, they are included in `target_comment`.

Comments are private and can't be modified in the following cases:

  * Any of the sources or target tickets are private
  * Any of the sources or target tickets were created through X (formerly Twitter), Facebook or the Channel framework

In any other case, comments default to private but can be modified with the comment privacy parameters.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.merge_tickets_into_target_ticket(ticket_id=123456, ids=[
        123,
        456,
        789,
    ], source_comment="Closing in favor of #111", target_comment="Combining with #123, #456, #789")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `ids`                                                               | List[*int*]                                                         | :heavy_check_mark:                                                  | Ids of tickets to merge into the target ticket                      |
| `source_comment`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Private comment to add to the source ticket                         |
| `source_comment_is_public`                                          | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether comment in source tickets are public or private             |
| `target_comment`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Private comment to add to the target ticket                         |
| `target_comment_is_public`                                          | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Whether comment in target ticket is public or private               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## ticket_related_information

The request returns a data object with the following properties:

| Name                | Type    | Comment
| ------------------- | ------- | -------
| topic_id            | string  | Related topic in the Web portal (deprecated feature)
| jira_issue_ids      | array   | Array of associated jira issues
| followup_source_ids | array   | Sources to follow up
| from_archive        | boolean | Is true if the current ticket is archived
| incidents           | integer | A count of related incident occurrences

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

    res = z_client.tickets.ticket_related_information(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketRelatedInformation](../../models/ticketrelatedinformation.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_tickets

Returns an approximate count of tickets in the account. If the count exceeds 100,000, it is updated every 24 hours.

`ccd` lists tickets that the specified user is cc'd on.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null.
This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

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

    res = z_client.tickets.count_tickets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountTicketsResponse](../../models/countticketsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## tickets_create_many

Accepts an array of up to 100 ticket objects. **Note**: Every ticket created with this endpoint may be affected by your business rules, which can include sending email notifications to your end users. If you are importing historical tickets or creating more than 1000 tickets, consider using the [Ticket Bulk Import](/api-reference/ticketing/tickets/ticket_import/#ticket-bulk-import) endpoint.

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

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

    res = z_client.tickets.tickets_create_many(request={
        "tickets": [
            {
                "comment": {
                    "body": "The smoke is very colorful.",
                },
                "priority": "urgent",
                "subject": "My printer is on fire!",
            },
            {
                "comment": {
                    "body": "This is a comment",
                },
                "priority": "normal",
                "subject": "Help",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TicketsCreateRequest](../../models/ticketscreaterequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## bulk_delete_tickets

Accepts a comma-separated list of up to 100 ticket ids.

#### Allowed For

* Admins
* Agents with permission to delete tickets

Agent delete permissions are set in Support. See
[Deleting tickets](https://support.zendesk.com/hc/en-us/articles/203690936)
in the Support Help Center.

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.bulk_delete_tickets(ids="35436,35437")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of ticket ids                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## mark_many_tickets_as_spam

Accepts a comma-separated list of up to 100 ticket ids.

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

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

    res = z_client.tickets.mark_many_tickets_as_spam(ids="35436,35437")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of ticket ids                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## tickets_show_many

Accepts a comma-separated list of ticket ids to return.

This endpoint will return up to 100 tickets records.

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

    res = z_client.tickets.tickets_show_many(ids="35436,35437")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of ticket ids                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketsResponse](../../models/ticketsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## tickets_update_many

Accepts an array of up to 100 ticket objects, or a comma-separated list of up to 100 ticket ids.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tickets.tickets_update_many(ids="35436,35437")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Comma-separated list of ticket ids                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |