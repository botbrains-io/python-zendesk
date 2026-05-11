# WebhookRequestFormat

The format of the data that the webhook will send. To subscribe the webhook to Zendesk events, this must be "json"

## Example Usage

```python
from zendesk.models import WebhookRequestFormat
value: WebhookRequestFormat = "json"
```


## Values

- `"json"`
- `"xml"`
- `"form_encoded"`
