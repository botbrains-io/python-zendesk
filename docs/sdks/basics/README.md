# Basics
(*basics*)

## Overview

### Available Operations

* [open_ticket_in_agent_browser](#open_ticket_in_agent_browser) - Open Ticket in Agent's Browser
* [open_users_profile_in_agent_browser](#open_users_profile_in_agent_browser) - Open a User's Profile in an Agent's Browser
* [create_ticket_or_voicemail_ticket](#create_ticket_or_voicemail_ticket) - Create Ticket or Voicemail Ticket

## open_ticket_in_agent_browser

Allows you to instruct an agent's browser to open a ticket.

When the message is successfully delivered to an agent's browser:

```http
Status: 200 OK
```

When `agent_id` or `ticket_id` is invalid:

```http
Status: 404 Not Found
```

#### Allowed For
* Agents

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.basics.open_ticket_in_agent_browser(agent_id=385473779372, ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | ID of an agent                                                      |                                                                     |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                | 123456                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## open_users_profile_in_agent_browser

Allows you to instruct an agent's browser to open a user's profile.

When the message is successfully delivered to an agent's browser:

```http
Status: 200 OK
```

When `agent_id` or `user_id` is invalid:

```http
Status: 404 Not Found
```

#### Allowed For
* Agents

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.basics.open_users_profile_in_agent_browser(agent_id=385473779372, user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | ID of an agent                                                      |                                                                     |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_ticket_or_voicemail_ticket

#### Allowed For
* Agents

### Creating tickets

#### Introduction

Creating tickets using Talk Partner Edition follows the same conventions as the Create Ticket endpoint. See [Create Ticket](/api-reference/ticketing/tickets/tickets/#create-ticket).

#### Request parameters

The POST request takes a mandatory `ticket` object that lists the values to set when the ticket is created.
You may also include an optional `display_to_agent` value such as the ID of the agent that will see the newly created ticket.
The `display_to_agent` is validated before creating the ticket, returning a 422 error if it is invalid.

Tickets created using this endpoint must have a `via_id` parameter. See the following
section for possible values.

#### Zendesk Talk Integration Via IDs

Tickets created using this endpoint must have one of the following `via_id` parameters:

| ID       | Description
| ---------| -------------
| 44       | Voicemail
| 45       | Phone call (inbound)
| 46       | Phone call (outbound)

### Creating voicemail tickets
#### Request parameters

The POST request takes a mandatory `ticket` object that lists the values to set when the ticket is created.
The ticket must have a `voice_comment` with the following values:

| Name               | Type                  | Comment
| ------------------ | ----------------------| -------
| from               | string                | Incoming phone number
| to                 | string                | Dialed phone number
| recording_url      | string                | URL of the recording
| started_at         | date                  | [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) timestamp of the call starting time
| call_duration      | integer               | Duration in seconds of the call
| answered_by_id     | integer               | The agent who answered the call
| transcription_text | string                | Transcription of the call (optional)
| location           | string                | Location of the caller (optional)

### Example Usage

```python
from zendesk import Zendesk, models
from zendesk.utils import parse_datetime


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.basics.create_ticket_or_voicemail_ticket(request={
        "display_to_agent": 1234,
        "ticket": {
            "comment": {
                "body": "My printer is on fire!",
            },
            "priority": "urgent",
            "via_id": 46,
            "voice_comment": {
                "answered_by_id": 28,
                "call_duration": 40,
                "from_": "+16617480240",
                "location": "Dublin, Ireland",
                "recording_url": "http://yourdomain.com/recordings/1.mp3",
                "started_at": parse_datetime("2019-04-16T09:14:57Z"),
                "to": "+16617480123",
                "transcription_text": "The transcription of the call",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.TicketCreateVoicemailTicketRequest](../../models/ticketcreatevoicemailticketrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.TicketResponse](../../models/ticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |