# WebhookInvocations
(*webhook_invocations*)

## Overview

### Available Operations

* [list_webhook_invocations](#list_webhook_invocations) - List Webhook Invocations
* [list_webhook_invocation_attempts](#list_webhook_invocation_attempts) - List Webhook Invocation Attempts

## list_webhook_invocations

Returns up to 7 days of invocations for a webhook.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhook_invocations.list_webhook_invocations(webhook_id="<id>", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | Webhook id                                                                                                                                                                                                                                                                                                          |
| `filter_from_ts`                                                                                                                                                                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters invocations by from timestamp. Use ISO 8601 UTC format                                                                                                                                                                                                                                                      |
| `filter_status`                                                                                                                                                                                                                                                                                                     | [Optional[models.ListWebhookInvocationsFilterStatus]](../../models/listwebhookinvocationsfilterstatus.md)                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters invocations by invocation status                                                                                                                                                                                                                                                                            |
| `filter_to_ts`                                                                                                                                                                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters invocations by timestamp. Use ISO 8601 UTC format                                                                                                                                                                                                                                                           |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                              | [Optional[models.ListWebhookInvocationsSort]](../../models/listwebhookinvocationssort.md)                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Defines a invocation attribute to sort invocations                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListWebhookInvocationsResponse](../../models/listwebhookinvocationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_webhook_invocation_attempts

Returns the invocation attempts for the specified webhook.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhook_invocations.list_webhook_invocation_attempts(webhook_id="<id>", invocation_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Webhook id                                                          |
| `invocation_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Webhook invocation id                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhookInvocationAttemptListResponse](../../models/webhookinvocationattemptlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |