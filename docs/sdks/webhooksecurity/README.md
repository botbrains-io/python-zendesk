# WebhookSecurity
(*webhook_security*)

## Overview

### Available Operations

* [show_webhook_signing_secret](#show_webhook_signing_secret) - Show Webhook Signing Secret
* [reset_webhook_signing_secret](#reset_webhook_signing_secret) - Reset Webhook Signing Secret

## show_webhook_signing_secret

Returns the webhook's signing secret. Note that admins cannot reveal secrets of webhooks created by Zendesk apps.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhook_security.show_webhook_signing_secret(webhook_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Webhook id                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhookSigningSecretResponse](../../models/webhooksigningsecretresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 403, 404             | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## reset_webhook_signing_secret

Resets a signing secret for the specified webhook. Note that admins cannot reset secrets of webhooks created by Zendesk apps.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhook_security.reset_webhook_signing_secret(webhook_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Webhook id                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhookSigningSecretResponse](../../models/webhooksigningsecretresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 403, 404             | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |