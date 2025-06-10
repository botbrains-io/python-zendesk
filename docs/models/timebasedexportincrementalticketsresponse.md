# TimeBasedExportIncrementalTicketsResponse

See [Tickets](/api-reference/ticketing/tickets/tickets/) for a detailed example.



## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `count`                                                | *Optional[int]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `end_of_stream`                                        | *Optional[bool]*                                       | :heavy_minus_sign:                                     | N/A                                                    |
| `end_time`                                             | *Optional[int]*                                        | :heavy_minus_sign:                                     | N/A                                                    |
| `next_page`                                            | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `tickets`                                              | List[[models.TicketObject](../models/ticketobject.md)] | :heavy_minus_sign:                                     | N/A                                                    |