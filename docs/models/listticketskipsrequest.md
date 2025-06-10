# ListTicketSkipsRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `user_id`                                                        | *int*                                                            | :heavy_check_mark:                                               | User ID of an agent                                              | 35436                                                            |
| `sort_order`                                                     | [Optional[models.TicketSortOrder]](../models/ticketsortorder.md) | :heavy_minus_sign:                                               | Sort order. Defaults to "asc"                                    |                                                                  |