# Webhooks
(*webhooks*)

## Overview

### Available Operations

* [list_webhooks](#list_webhooks) - List Webhooks
* [create_or_clone_webhook](#create_or_clone_webhook) - Create or Clone Webhook
* [test_webhook](#test_webhook) - Test Webhook
* [show_webhook](#show_webhook) - Show Webhook
* [update_webhook](#update_webhook) - Update Webhook
* [patch_webhook](#patch_webhook) - Patch Webhook
* [delete_webhook](#delete_webhook) - Delete Webhook
* [show_webhook_signing_secret](#show_webhook_signing_secret) - Show Webhook Signing Secret
* [reset_webhook_signing_secret](#reset_webhook_signing_secret) - Reset Webhook Signing Secret

## list_webhooks

List webhooks.

### Example Usage

<!-- UsageSnippet language="python" operationID="listWebhooks" method="get" path="/api/v2/webhooks" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhooks.list_webhooks(page_size=100)

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
| `filter_name_contains`                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters the webhooks by a string in the name                                                                                                                                                                                                                                                                        |
| `filter_status`                                                                                                                                                                                                                                                                                                     | [Optional[models.ListWebhooksFilterStatus]](../../models/listwebhooksfilterstatus.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters the webhooks by webhook status                                                                                                                                                                                                                                                                              |
| `sort`                                                                                                                                                                                                                                                                                                              | [Optional[models.ListWebhooksSort]](../../models/listwebhookssort.md)                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Defines the sorting criteria. Only supports name and status                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListWebhooksResponse](../../models/listwebhooksresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_or_clone_webhook

Creates or clones a webhook. The clone_webhook_id query parameter is only required when cloning a webhook.
A request body is only required when creating a webhook.

Note that admins cannot clone webhooks created by Zendesk apps.

**Webhooks for trial accounts**: Zendesk trial accounts are limited to 10 webhooks.


### Example Usage

<!-- UsageSnippet language="python" operationID="createOrCloneWebhook" method="post" path="/api/v2/webhooks" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhooks.create_or_clone_webhook()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `clone_webhook_id`                                                            | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | id of the webhook to clone. Only required if cloning a webhook.               |
| `webhook_create_request`                                                      | [Optional[models.WebhookCreateRequest]](../../models/webhookcreaterequest.md) | :heavy_minus_sign:                                                            | Webhook data (required when creating, not when cloning)                       |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.WebhookResponse](../../models/webhookresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 403             | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## test_webhook

Tests a new or existing webhook.

When testing an existing webhook, the existing webhook data will be attached automatically as part of the outbound test request.
The data includes the request format, http method, authentication method (only if same type and add_position are attached), and signing secret.
The request payload data will overwrite existing webhook data in the outbound test request.


### Example Usage

<!-- UsageSnippet language="python" operationID="testWebhook" method="post" path="/api/v2/webhooks/test" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhooks.test_webhook(webhook={
        "endpoint": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `webhook`                                                                     | [models.WebhookTestRequestWebhook](../../models/webhooktestrequestwebhook.md) | :heavy_check_mark:                                                            | Webhook configuration for testing                                             |
| `webhook_id`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | The webhook to be tested. Only required for testing an existing webhook.      |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.WebhookTestResponse](../../models/webhooktestresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## show_webhook

Returns the specified webhook.

### Example Usage

<!-- UsageSnippet language="python" operationID="showWebhook" method="get" path="/api/v2/webhooks/{webhook_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhooks.show_webhook(webhook_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Webhook id                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WebhookResponse](../../models/webhookresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 404             | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## update_webhook

Updates the specified webhook.

**Restrictions**: Admins cannot set `external_source` and `signing_secret` when updating a webhook.


### Example Usage

<!-- UsageSnippet language="python" operationID="updateWebhook" method="put" path="/api/v2/webhooks/{webhook_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.webhooks.update_webhook(webhook_id="<id>", webhook={
        "name": "<value>",
        "endpoint": "<value>",
        "http_method": "DELETE",
        "request_format": "xml",
        "status": "active",
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `webhook_id`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | Webhook id                                                                        |
| `webhook`                                                                         | [models.WebhookUpdateRequestWebhook](../../models/webhookupdaterequestwebhook.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 404             | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## patch_webhook

Use the webhook_id to update a webhook.

**Restrictions**: Admins cannot set `external_source` and `signing_secret` when patching a webhook.


### Example Usage

<!-- UsageSnippet language="python" operationID="patchWebhook" method="patch" path="/api/v2/webhooks/{webhook_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.webhooks.patch_webhook(webhook_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `webhook_id`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | Webhook id                                                                                |
| `webhook`                                                                                 | [Optional[models.WebhookPatchRequestWebhook]](../../models/webhookpatchrequestwebhook.md) | :heavy_minus_sign:                                                                        | Partial webhook object with fields to update                                              |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 404             | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## delete_webhook

Deletes the specified webhook.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteWebhook" method="delete" path="/api/v2/webhooks/{webhook_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.webhooks.delete_webhook(webhook_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Webhook id                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 400, 404             | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |

## show_webhook_signing_secret

Returns the webhook's signing secret. Note that admins cannot reveal secrets of webhooks created by Zendesk apps.


### Example Usage

<!-- UsageSnippet language="python" operationID="showWebhookSigningSecret" method="get" path="/api/v2/webhooks/{webhook_id}/signing_secret" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhooks.show_webhook_signing_secret(webhook_id="<id>")

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

<!-- UsageSnippet language="python" operationID="resetWebhookSigningSecret" method="post" path="/api/v2/webhooks/{webhook_id}/signing_secret" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.webhooks.reset_webhook_signing_secret(webhook_id="<id>")

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