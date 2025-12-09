# SatisfactionRatings

## Overview

### Available Operations

* [list_satisfaction_ratings](#list_satisfaction_ratings) - List Satisfaction Ratings
* [show_satisfaction_rating](#show_satisfaction_rating) - Show Satisfaction Rating
* [count_satisfaction_ratings](#count_satisfaction_ratings) - Count Satisfaction Ratings
* [create_ticket_satisfaction_rating](#create_ticket_satisfaction_rating) - Create a Satisfaction Rating

## list_satisfaction_ratings

#### Allowed For
* Admins

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

#### Filters

| Parameter  | Value
| ---------- | -----
| score      | offered, unoffered, received, received\_with\_comment, received\_without\_comment,<br/>good, good\_with\_comment, good\_without\_comment,<br/>bad, bad\_with\_comment, bad\_without\_comment
| start_time | Time of the oldest satisfaction rating, as a [Unix epoch time](https://www.epochconverter.com/)
| end_time   | Time of the most recent satisfaction rating, as a [Unix epoch time](https://www.epochconverter.com/)

If you specify an unqualified score such as `good`, the results include all the records with and without comments.

Examples:

* `/api/v2/satisfaction_ratings.json?score=bad`
* `/api/v2/satisfaction_ratings.json?score=bad&start_time=1498151194`
* `/api/v2/satisfaction_ratings.json?start_time=1340384793&end_time=1371920793`


### Example Usage

<!-- UsageSnippet language="python" operationID="ListSatisfactionRatings" method="get" path="/api/v2/satisfaction_ratings" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.satisfaction_ratings.list_satisfaction_ratings(page_size=100)

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
| `score`                                                                                                                                                                                                                                                                                                             | [Optional[models.ListSatisfactionRatingsScore]](../../models/listsatisfactionratingsscore.md)                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters the results by score. Possible values are "offered", "unoffered", "received", "received_with_comment", "received_without_comment", "good", "good_with_comment", "good_without_comment", "bad", "bad_with_comment", "bad_without_comment"<br/>                                                               |
| `start_time`                                                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Time of the oldest satisfaction rating, as a [Unix epoch time](https://www.epochconverter.com/)<br/>                                                                                                                                                                                                                |
| `end_time`                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Time of the most recent satisfaction rating, as a [Unix epoch time](https://www.epochconverter.com/)<br/>                                                                                                                                                                                                           |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListSatisfactionRatingsResponse](../../models/listsatisfactionratingsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_satisfaction_rating

Returns a specific satisfaction rating. You can get the id from
the [List Satisfaction Ratings](#list-satisfaction-ratings) endpoint.

#### Allowed For

 * Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowSatisfactionRating" method="get" path="/api/v2/satisfaction_ratings/{satisfaction_rating_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.satisfaction_ratings.show_satisfaction_rating(satisfaction_rating_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `satisfaction_rating_id`                                            | *int*                                                               | :heavy_check_mark:                                                  | The id of the satisfaction rating to retrieve                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SatisfactionRatingResponse](../../models/satisfactionratingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_satisfaction_ratings

Returns an approximate count of satisfaction ratings in the account. If the count exceeds 100,000, the count will return a cached result. This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null.
This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For
* Admins

### Example Usage

<!-- UsageSnippet language="python" operationID="CountSatisfactionRatings" method="get" path="/api/v2/satisfaction_ratings/count" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.satisfaction_ratings.count_satisfaction_ratings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SatisfactionRatingsCountResponse](../../models/satisfactionratingscountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_ticket_satisfaction_rating

Creates a CSAT rating for a solved ticket, or for a ticket that was previously
solved and then reopened.

Only the end user listed as the ticket requester can create a satisfaction rating for the ticket.

#### Allowed For

* End user who requested the ticket

The end user must be a verified user.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateTicketSatisfactionRating" method="post" path="/api/v2/tickets/{ticket_id}/satisfaction_rating" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.satisfaction_ratings.create_ticket_satisfaction_rating(ticket_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The id of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SatisfactionRatingResponse](../../models/satisfactionratingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |