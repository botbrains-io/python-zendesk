# TestWebhookRequest


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `webhook_id`                                                             | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The webhook to be tested. Only required for testing an existing webhook. |
| `webhook_test_request`                                                   | [models.WebhookTestRequest](../models/webhooktestrequest.md)             | :heavy_check_mark:                                                       | N/A                                                                      |