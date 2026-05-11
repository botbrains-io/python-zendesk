# TicketUpdateInputStatus

The state of the ticket.

If your account has activated custom ticket statuses, this is the ticket's
status category. See [custom ticket statuses](#custom-ticket-statuses).


## Example Usage

```python
from zendesk.models import TicketUpdateInputStatus
value: TicketUpdateInputStatus = "new"
```


## Values

- `"new"`
- `"open"`
- `"pending"`
- `"hold"`
- `"solved"`
- `"closed"`
