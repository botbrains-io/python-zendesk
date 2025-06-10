# TicketChatCommentRedactionResponseValue

The value of the chat event object


## Fields

| Field                               | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `chat_id`                           | *Optional[str]*                     | :heavy_minus_sign:                  | Id of the chat session              |
| `history`                           | List[Dict[str, *Any*]]              | :heavy_minus_sign:                  | Chat events within the chat session |
| `visitor_id`                        | *Optional[str]*                     | :heavy_minus_sign:                  | Id assigned to the visitor          |