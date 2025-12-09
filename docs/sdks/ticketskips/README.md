# TicketSkips

## Overview

### Available Operations

* [record_new_skip](#record_new_skip) - Record a New Skip for the Current User
* [list_ticket_skips](#list_ticket_skips) - List Ticket Skips

## record_new_skip

Record a new ticket skip for the current user.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="RecordNewSkip" method="post" path="/api/v2/skips" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_skips.record_new_skip()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketSkipCreation](../../models/ticketskipcreation.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_skips

Archived tickets are not included in the response. See
[About archived tickets](https://support.zendesk.com/hc/en-us/articles/203657756) in
the Support Help Center.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For
* Agents with "View only" or higher reports permissions in Support.
  These permissions are distinct from Explore permissions.
* Agents retrieving their own skips


### Example Usage

<!-- UsageSnippet language="python" operationID="ListTicketSkips" method="get" path="/api/v2/users/{user_id}/skips" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_skips.list_ticket_skips(user_id=35436, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                                                                                                                                                                                           | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | User ID of an agent                                                                                                                                                                                                                                                                                                 |
| `sort_order`                                                                                                                                                                                                                                                                                                        | [Optional[models.TicketSortOrder]](../../models/ticketsortorder.md)                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Sort order. Defaults to "asc"                                                                                                                                                                                                                                                                                       |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListTicketSkipsResponse](../../models/listticketskipsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |