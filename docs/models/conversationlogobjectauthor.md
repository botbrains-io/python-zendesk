# ConversationLogObjectAuthor

Object that describes the user who created the event


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `type`                                                                               | [Optional[models.ConversationLogObjectType]](../models/conversationlogobjecttype.md) | :heavy_minus_sign:                                                                   | Either user, agent, or bot                                                           |
| `zen_sunco_user_id`                                                                  | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | A Zendesk resource name prefix describing a messaging user                           |
| `zen_support_user_id`                                                                | *Optional[int]*                                                                      | :heavy_minus_sign:                                                                   | A Zendesk resource name prefix describing a Support user                             |
| `__pydantic_extra__`                                                                 | Dict[str, *Any*]                                                                     | :heavy_minus_sign:                                                                   | N/A                                                                                  |