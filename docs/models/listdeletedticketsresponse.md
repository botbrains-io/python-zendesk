# ListDeletedTicketsResponse


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `deleted_tickets`                                        | List[[models.DeletedTicket](../models/deletedticket.md)] | :heavy_minus_sign:                                       | N/A                                                      |
| `count`                                                  | *Optional[int]*                                          | :heavy_minus_sign:                                       | the total record count                                   |
| `next_page`                                              | *OptionalNullable[str]*                                  | :heavy_minus_sign:                                       | the URL of the next page                                 |
| `previous_page`                                          | *OptionalNullable[str]*                                  | :heavy_minus_sign:                                       | the URL of the previous page                             |