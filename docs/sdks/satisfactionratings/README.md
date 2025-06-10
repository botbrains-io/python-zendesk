# SatisfactionRatings
(*satisfaction_ratings*)

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

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.satisfaction_ratings.list_satisfaction_ratings()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SatisfactionRatingsResponse](../../models/satisfactionratingsresponse.md)**

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `satisfaction_rating_id`                                            | *int*                                                               | :heavy_check_mark:                                                  | The id of the satisfaction rating to retrieve                       | 35436                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The id of the ticket                                                | 35436                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SatisfactionRatingResponse](../../models/satisfactionratingresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |