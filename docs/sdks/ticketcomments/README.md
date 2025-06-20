# TicketComments
(*ticket_comments*)

## Overview

### Available Operations

* [redact_chat_comment_attachment](#redact_chat_comment_attachment) - Redact Chat Comment Attachment
* [redact_chat_comment](#redact_chat_comment) - Redact Chat Comment
* [redact_ticket_comment_in_agent_workspace](#redact_ticket_comment_in_agent_workspace) - Redact Ticket Comment In Agent Workspace
* [list_ticket_comments](#list_ticket_comments) - List Comments
* [make_ticket_comment_private](#make_ticket_comment_private) - Make Comment Private
* [redact_string_in_comment](#redact_string_in_comment) - Redact String in Comment
* [count_ticket_comments](#count_ticket_comments) - Count Ticket Comments

## redact_chat_comment_attachment

Permanently removes one or more chat attachments from a chat ticket.

**Note**: This does not work on active chats. For chat tickets that predate March 2020, consider using [Redact Ticket Comment In Agent Workspace](#redact-ticket-comment-in-agent-workspace).

#### Allowed For

- Agents

[Agent Workspace](https://support.zendesk.com/hc/en-us/articles/360024218473) must enabled for the account. Deleting tickets must be enabled for agents.

#### Request Body Properties

| Name         | Type    | Required | Description                                                                                                                                                                                                                                            |
| ------------ | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| chat_id      | string  | true     | The `chat_id` in the `ChatStartedEvent` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits)                                                                                                                 |
| chat_indexes | array   | false    | The array of `chat_index` in the `ChatFileAttachment` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits). Mandatory if `message_ids` is not used                                                           |
| message_ids  | array   | false    | The array of `message_id` in the `ChatFileAttachment` event in the ticket audit that is part of a `ChatStartedEvent` history. Used when redacting a ChatFileAttachment that is part of a conversation history. Mandatory if `chat_indexes` is not used |

To get the required body properties, make a request to the [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits) endpoint. Example response:

```http
Status 200 OK
{
  "audits": [
    "events": [
      {
        "id": 1932802680168,
        "type": "ChatStartedEvent",
        "value": {
          "visitor_id": "10502823-16EkM3T6VNq7KMd",
          "chat_id": "2109.10502823.Sjuj2YrBpXwei",
          "history": [
            {
              "chat_index": 0,
              "type": "ChatFileAttachment",
              "filename": "image1.jpg"
            },
            {
              "chat_index": 1,
              "type": "ChatFileAttachment",
              "filename": "image2.jpg"
            }
          ]
        }
      }
    ]
  ]
}
```


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_comments.redact_chat_comment_attachment(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketChatCommentRedactionResponse](../../models/ticketchatcommentredactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## redact_chat_comment

Permanently removes words or strings from a chat ticket's comment. 

Wrap `<redact>` tags around the content in the chat comment you want redacted. Example: 

```json
{
  "text": "My ID number is <redact>847564</redact>!"
}
```

The characters contained in the tag will be replaced by the ▇ symbol.

**Note**: This does not work on active chats. For chat tickets that predate March 2020, consider using [Redact Ticket Comment In Agent Workspace](#redact-ticket-comment-in-agent-workspace).

#### Allowed For

- Agents

[Agent Workspace](https://support.zendesk.com/hc/en-us/articles/360024218473) must enabled for the account. Deleting tickets must be enabled for agents.

#### Request Body Properties

| Name                     | Type    | Required | Description                                                                                                                                                                                                                                       |
| ------------------------ | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| chat_id                  | string  | true     | The `chat_id` in the `ChatStartedEvent` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits)                                                                                                            |
| chat_index               | integer | false    | The `chat_index` in the `ChatMessage` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits). Mandatory if `message_id` is not used                                                                       |
| message_id               | string  | false    | The `message_id` of the `ChatMessage` event in the ticket audit that is part of a `ChatStartedEvent` history. Used when redacting a ChatMessage that is part of a conversation history. Mandatory if `chat_index` is not used                     |
| text                     | string  | true     | The `message` in the `ChatMessage` event in the ticket audit. See [Ticket Audits](/api-reference/ticketing/tickets/ticket_audits).  Wrap `message` with `<redact>` tags                                                                           |

To get the required body properties, make a request to the [Ticket Audit](/api-reference/ticketing/tickets/ticket_audits) endpoint. Example response:

```http
Status 200 OK
{
  "audits": [
    "events": [
      {
        "id": 1932802680168,
        "type": "ChatStartedEvent",
        "value": {
          "visitor_id": "10502823-16EkM3T6VNq7KMd",
          "chat_id": "2109.10502823.Sjuj2YrBpXwei",
          "history": [
            {
              "chat_index": 0,
              "type": "ChatMessage",
              "message": "My ID number is 847564!"
            }
          ]
        }
      }
    ]
  ]
}
```


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_comments.redact_chat_comment(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketChatCommentRedactionResponse](../../models/ticketchatcommentredactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## redact_ticket_comment_in_agent_workspace

Redaction allows you to permanently remove words, strings, or attachments from a ticket comment.

In the `html_body` of the comment, wrap the content you want redacted in `<redact>` tags. Example:

```json
{
  "html_body": "<div class=\"zd-comment\" dir=\"auto\">My ID number is <redact>847564</redact>!</div>",
  "ticket_id":100
}
```

The characters in the redact tag will be replaced by the ▇ symbol.

To redact HTML elements such inline images, anchor tags, and links, add the `redact` tag attribute to the element as well as the `<redact>` tag to inner text, if any. Example: 

`<a href="http://example.com" redact><redact>some link</redact></a>`

The `redact` attribute only redacts the tag. Any inner text will be left behind if not enclosed in a `<redact>` tag.

Redaction is permanent and can not be undone. Data is permanently deleted from Zendesk servers with no way to recover it.

This endpoint provides all the same functionality that the [Redact String in Comment](/api-reference/ticketing/tickets/ticket_comments/#redact-string-in-comment) endpoint provides, plus:

- Redaction of comments in closed tickets

- Redaction of comments in archived tickets

- Redaction of formatted text (bold, italics, hyperlinks)

**Limitations**: When content is redacted from an email comment, the content is also redacted from the original email through a background job. It may take a while for the changes to be completed.

**Note**: We recommend using this endpoint instead of the [Redact String in Comment](/api-reference/ticketing/tickets/ticket_comments/#redact-string-in-comment) endpoint, which will eventually be deprecated.

#### Allowed For

- Agents

[Agent Workspace](https://support.zendesk.com/hc/en-us/articles/360024218473) must be enabled on the account. For professional accounts, deleting tickets must be enabled for agents. On Enterprise accounts, you can assign agents to a custom role with permissions to redact ticket content.

#### Request Body Properties

| Name                     | Type    | Required | Description                                                                                                                                      |
| -------------------------| ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ticket_id                | integer | true     | The ID of the ticket                                                                                                                             |
| html_body                | string  | false    | The `html_body` of the comment containing `<redact>` tags or `redact` attributes                                           |
| external_attachment_urls | array   | false    | Array of attachment URLs belonging to the comment to be redacted. See [`content_url` property of Attachment](/api-reference/ticketing/tickets/ticket-attachments/) |


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_comments.redact_ticket_comment_in_agent_workspace(ticket_comment_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_comment_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket comment                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketCommentResponse](../../models/ticketcommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_comments

Returns the comments added to the ticket.

Each comment may include a `content_url` for an attachment or a `recording_url` for a voice comment that points to a file that may be hosted externally. For security reasons, take care not to inadvertently send Zendesk authentication credentials to third parties when attempting to access these files. See [Working with url properties](/documentation/ticketing/managing-tickets/working-with-url-properties).

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Sorting

By default, comments are sorted by creation date in ascending order.

When using cursor pagination, use the following parameter to change the sort order:

| Name   | Type   | Required | Comments
| ------ | ------ | -------- | --------
| `sort` | string | no       | Possible values are "created_at" (ascending order) or "-created_at" (descending order)

When using offset pagination, use the following parameters to change the sort order:

| Name         | Type   | Required | Comments
| ------------ | ------ | -------- | --------
| `sort_order` | string | no       | One of `asc`, `desc`. Defaults to `asc`

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

    res = z_client.ticket_comments.list_ticket_comments(ticket_id=123456, page_size=100, sort="created_at")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ticket_id`                                                                                                                                                                                                                                                                                                         | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The ID of the ticket                                                                                                                                                                                                                                                                                                |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                              | [Optional[models.ListTicketCommentsSort]](../../models/listticketcommentssort.md)                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Sort order - "created_at" (ascending) or "-created_at" (descending)                                                                                                                                                                                                                                                 |
| `include_inline_images`                                                                                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Default is false. When true, inline images are also listed as attachments in the response                                                                                                                                                                                                                           |
| `include`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Accepts "users". Use this parameter to list email CCs by side-loading users. Example: `?include=users`. **Note**: If the comment source is email, a deleted user will be represented as the CCd email address. If the comment source is anything else, a deleted user will be represented as the user name.         |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListTicketCommentsResponse](../../models/listticketcommentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## make_ticket_comment_private

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

    res = z_client.ticket_comments.make_ticket_comment_private(ticket_id=123456, ticket_comment_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `ticket_comment_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket comment                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## redact_string_in_comment

Permanently removes words or strings from a ticket comment. Specify the string to redact in an object with a `text` property. Example: `'{"text": "987-65-4320"}'`. The characters of the word or string are replaced by the ▇ symbol.

If the comment was made by email, the endpoint also attempts to redact the string from the original email retained by Zendesk for audit purposes.

**Note**: If you use the rich text editor, support for redacting formatted text (bold, italics, hyperlinks) is limited.

Redaction is permanent. You can't undo the redaction or see *what* was removed. Once a ticket is closed, you can no longer redact strings from its comments.

To use this endpoint, the "Agents can delete tickets" option must be enabled in the Zendesk Support admin interface at **Admin** > **Settings** > **Agents**.

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

    res = z_client.ticket_comments.redact_string_in_comment(ticket_id=123456, ticket_comment_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `ticket_comment_id`                                                 | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket comment                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketCommentResponse](../../models/ticketcommentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_ticket_comments

Returns an approximate count of the comments added to the ticket. If the count exceeds 100,000, the count will return a cached result.  This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null.
This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

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

    res = z_client.ticket_comments.count_ticket_comments(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketCommentsCountResponse](../../models/ticketcommentscountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |