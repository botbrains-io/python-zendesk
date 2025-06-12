# WebhookSigningSecret

Signing secret used to verify webhook requests


## Fields

| Field                            | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `algorithm`                      | *Optional[str]*                  | :heavy_minus_sign:               | Signing algorithm (e.g., sha256) |
| `secret`                         | *Optional[str]*                  | :heavy_minus_sign:               | The signing secret value         |