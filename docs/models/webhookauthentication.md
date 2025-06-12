# WebhookAuthentication

Adds authentication to the webhook's HTTP requests


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [Optional[models.WebhookAuthenticationType]](../models/webhookauthenticationtype.md) | :heavy_minus_sign:                                                                   | N/A                                                                                  |
| `data`                                                                               | [Optional[models.Data]](../models/data.md)                                           | :heavy_minus_sign:                                                                   | Authentication data specific to the type                                             |
| `add_position`                                                                       | [Optional[models.AddPosition]](../models/addposition.md)                             | :heavy_minus_sign:                                                                   | Where to add the authentication (for API key type)                                   |