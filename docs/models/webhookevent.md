# WebhookEvent


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `id`                                                         | *int*                                                        | :heavy_check_mark:                                           | Automatically assigned when the event is created             |
| `type`                                                       | [models.TypeWebhookEvent](../models/typewebhookevent.md)     | :heavy_check_mark:                                           | N/A                                                          |
| `via`                                                        | [Optional[models.AuditEventVia]](../models/auditeventvia.md) | :heavy_minus_sign:                                           | How the webhook event was triggered                          |