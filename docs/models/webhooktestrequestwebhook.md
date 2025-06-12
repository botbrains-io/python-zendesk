# WebhookTestRequestWebhook

Webhook configuration for testing


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `endpoint`                                                                   | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `http_method`                                                                | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `request_format`                                                             | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | N/A                                                                          |
| `authentication`                                                             | [Optional[models.WebhookAuthentication]](../models/webhookauthentication.md) | :heavy_minus_sign:                                                           | Adds authentication to the webhook's HTTP requests                           |
| `custom_headers`                                                             | Dict[str, *str*]                                                             | :heavy_minus_sign:                                                           | N/A                                                                          |