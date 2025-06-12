# CreateOrCloneWebhookRequest


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `clone_webhook_id`                                                         | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | id of the webhook to clone. Only required if cloning a webhook.            |
| `webhook_create_request`                                                   | [Optional[models.WebhookCreateRequest]](../models/webhookcreaterequest.md) | :heavy_minus_sign:                                                         | Webhook data (required when creating, not when cloning)                    |