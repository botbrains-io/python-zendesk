# Requests
(*requests*)

## Overview

### Available Operations

* [list_requests](#list_requests) - List Requests
* [create_request](#create_request) - Create Request
* [show_request](#show_request) - Show Request
* [update_request](#update_request) - Update Request
* [list_comments](#list_comments) - Listing Comments
* [show_comment](#show_comment) - Getting Comments
* [search_requests](#search_requests) - Search Requests

## list_requests

#### Allowed for

* End Users

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).


### Example Usage

<!-- UsageSnippet language="python" operationID="ListRequests" method="get" path="/api/v2/requests" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.requests.list_requests(page_size=100)

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
| `sort_by`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Possible values are "updated_at", "created_at"                                                                                                                                                                                                                                                                      |
| `sort_order`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of "asc", "desc". Defaults to "asc"                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListRequestsResponse](../../models/listrequestsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_request

Accepts a `request` object that sets one or more properties.

#### Allowed for

* End users
* Anonymous users (rate limit of 5 requests per hour for [trial accounts](/documentation/developer-tools/getting-started/getting-a-trial-or-sponsored-account-for-development/))

#### Additional properties

In addition to the writable request properties in the [JSON Format table](#json-format) above, you can set the following properties when creating a request.

| Name                | Type   | Mandatory | Comment
| ----------------    | -------| --------- | -------
| comment             | object | yes       | Describes the problem, incident, question, or task. See [Request comments](#request-comments)
| collaborators       | array  | no        | Adds collaborators (cc's) to the request. An email notification is sent to them when the ticket is created. See [Setting collaborators](/documentation/ticketing/managing-tickets/creating-and-managing-requests#setting-collaborators)
| requester           | object | yes*      | \*Required for anonymous requests. Specifies the requester of the anonymous request. See [Creating anonymous requests](/documentation/ticketing/managing-tickets/creating-and-managing-requests#creating-anonymous-requests)

#### Creating follow-up requests

Once a ticket is closed (as distinct from solved), it can't be reopened. However, you can create a new request that references the closed ticket. To create the follow-up request, include a `via_followup_source_id` property in the `request` object that specifies the closed ticket. The parameter only works with closed tickets. It has no effect with other tickets.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateRequest" method="post" path="/api/v2/requests" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.requests.create_request()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RequestResponse](../../models/requestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_request

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| users            | The email ccs for a request by side-loading users

#### Allowed For

* End Users


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowRequest" method="get" path="/api/v2/requests/{request_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.requests.show_request(request_id=33)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the request                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RequestResponse](../../models/requestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_request

Updates a request with a comment or collaborators (cc's). The end user who created the request can also use it to mark the request as solved. The endpoint can't be used to update other request attributes.

#### Writable properties
This endpoint can only update the following properties in the request.

| Name                     | Type    | Required | Description                                          |
| ------------------------ | ------- | -------- | ---------------------------------------------------- |
| comment                  | object  | no       | Adds a comment to the request. See [Request comments](#request-comments) |
| solved                   | boolean | no       | Marks the request as solved. Example: `{"request": {"solved": "true"}}`. End users can mark requests as solved only if the request's `can_be_solved_by_me` property is true. The property is true only when the ticket is assigned to an agent and the ticket type is not a problem but a question, task, or incident |
| additional_collaborators | array   | no       | Adds collaborators to the request. An email notification is sent to them when the ticket is updated. See [Adding collaborators](/documentation/ticketing/managing-tickets/creating-and-managing-requests#adding-collaborators) |

#### Allowed For

* End users


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateRequest" method="put" path="/api/v2/requests/{request_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.requests.update_request(request_id=33)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the request                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RequestResponse](../../models/requestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_comments

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

#### Sorting

By default, comments are sorted by creation date in ascending order.

When using cursor pagination, use the following parameter to change the sort order:

| Name   | Type   | Required | Comments
| ------ | ------ | -------- | --------
| `sort` | string | no       | Possible values are "created_at" (ascending order) or "-created_at" (descending order)

When using offset pagination, use the following parameters to change the sort order:

| Name         | Type   | Required | Comments
| ------------ | ------ | -------- | --------
| `sort_by`    | string | no       | One of `created_at`, `updated_at`
| `sort_order` | string | no       | One of `asc`, `desc`

#### Allowed For

* End Users


### Example Usage

<!-- UsageSnippet language="python" operationID="ListComments" method="get" path="/api/v2/requests/{request_id}/comments" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.requests.list_comments(request_id=33, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_id`                                                                                                                                                                                                                                                                                                        | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The ID of the request                                                                                                                                                                                                                                                                                               |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                              | [Optional[models.ListCommentsSort]](../../models/listcommentssort.md)                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how to sort the comments. Possible values are "created_at" (ascending order) or "-created_at" (descending order)<br/>                                                                                                                                                                                     |
| `since`                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters the comments from the given datetime                                                                                                                                                                                                                                                                        |
| `role`                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of "agent", "end_user". If not specified it does not filter                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListCommentsResponse](../../models/listcommentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_comment

#### Allowed For

* End Users


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowComment" method="get" path="/api/v2/requests/{request_id}/comments/{ticket_comment_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.requests.show_comment(request_id=33, ticket_comment_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the request                                               |
| `ticket_comment_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket comment                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketCommentResponse](../../models/ticketcommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_requests

Examples:

* `GET /api/v2/requests/search.json?query=printer`
* `GET /api/v2/requests/search.json?query=printer&organization_id=1`
* `GET /api/v2/requests/search.json?query=printer&cc_id=true`
* `GET /api/v2/requests/search.json?query=printer&status=hold,open`

#### Pagination

* Offset pagination only

See [Using Offset Pagination](/api-reference/ticketing/introduction/#using-offset-pagination).

#### Results limit

The Search Requests endpoint returns up to 1,000 results per query, with a maximum of 100 results per page. See [Pagination](/api-reference/ticketing/introduction/#pagination). If you request a page past the limit (`page=11` at 100 results per page), a 422 Insufficient Resource Error is returned.

#### Allowed For

* End Users


### Example Usage

<!-- UsageSnippet language="python" operationID="SearchRequests" method="get" path="/api/v2/requests/search" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.requests.search_requests()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                            | The syntax and matching logic for the string is detailed in the [Zendesk Support search reference](https://support.zendesk.com/hc/en-us/articles/203663226). See also [Query basics](/api-reference/ticketing/ticket-management/search/#query-basics) in the Tickets API doc. |
| `retries`                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                           |

### Response

**[models.RequestsResponse](../../models/requestsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |