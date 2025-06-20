# XChannel
(*x_channel*)

## Overview

### Available Operations

* [list_monitored_twitter_handles](#list_monitored_twitter_handles) - List Monitored X Handles
* [show_monitored_twitter_handle](#show_monitored_twitter_handle) - Show Monitored X Handle
* [create_ticket_from_tweet](#create_ticket_from_tweet) - Create Ticket from Tweet
* [getting_twicket_status](#getting_twicket_status) - List Ticket statuses

## list_monitored_twitter_handles

#### Allowed For

* Admins
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

    res = z_client.x_channel.list_monitored_twitter_handles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TwitterChannelsResponse](../../models/twitterchannelsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_monitored_twitter_handle

#### Allowed For

* Admins
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

    res = z_client.x_channel.show_monitored_twitter_handle(monitored_twitter_handle_id=431)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `monitored_twitter_handle_id`                                       | *int*                                                               | :heavy_check_mark:                                                  | The ID of the custom agent role                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TwitterChannelResponse](../../models/twitterchannelresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_ticket_from_tweet

Turns a tweet into a ticket. You must provide the tweet id as well as the id of a monitored X (formerly Twitter) handle configured for your account.

The submitter of the ticket is set to be the user submitting the API request.

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

    res = z_client.x_channel.create_ticket_from_tweet()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## getting_twicket_status

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

    res = z_client.x_channel.getting_twicket_status(comment_id=654321, ids="1,3,5")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `comment_id`                                                                    | *int*                                                                           | :heavy_check_mark:                                                              | The ID of the comment                                                           |
| `ids`                                                                           | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Optional comment ids to retrieve tweet information for only particular comments |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.TwitterChannelTwicketStatusResponse](../../models/twitterchanneltwicketstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |