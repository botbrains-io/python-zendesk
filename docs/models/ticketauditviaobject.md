# TicketAuditViaObject

Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `channel`                                                                                                 | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | This tells you how the ticket or event was created. Examples: "web", "mobile", "rule", "system"           |
| `source`                                                                                                  | Dict[str, *Any*]                                                                                          | :heavy_minus_sign:                                                                                        | For some channels a source object gives more information about how or why the ticket or event was created |