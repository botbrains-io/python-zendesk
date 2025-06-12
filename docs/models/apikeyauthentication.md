# APIKeyAuthentication

API key authentication configuration


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `type`                                                                   | [models.APIKeyAuthenticationType](../models/apikeyauthenticationtype.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `data`                                                                   | [models.APIKeyAuthenticationData](../models/apikeyauthenticationdata.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `add_position`                                                           | [Optional[models.AddPosition]](../models/addposition.md)                 | :heavy_minus_sign:                                                       | Where to add the API key (header or query string)                        |