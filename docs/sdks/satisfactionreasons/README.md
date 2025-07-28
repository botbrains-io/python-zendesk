# SatisfactionReasons
(*satisfaction_reasons*)

## Overview

### Available Operations

* [list_satisfaction_rating_reasons](#list_satisfaction_rating_reasons) - List Reasons for Satisfaction Rating
* [show_satisfaction_ratings](#show_satisfaction_ratings) - Show Reason for Satisfaction Rating

## list_satisfaction_rating_reasons

List all reasons for an account

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ListSatisfactionRatingReasons" method="get" path="/api/v2/satisfaction_reasons" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.satisfaction_reasons.list_satisfaction_rating_reasons()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SatisfactionReasonsResponse](../../models/satisfactionreasonsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_satisfaction_ratings

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowSatisfactionRatings" method="get" path="/api/v2/satisfaction_reasons/{satisfaction_reason_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.satisfaction_reasons.show_satisfaction_ratings(satisfaction_reason_id=35121)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `satisfaction_reason_id`                                            | *int*                                                               | :heavy_check_mark:                                                  | The id of the satisfaction rating reason                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SatisfactionReasonResponse](../../models/satisfactionreasonresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |