# CursorBasedExportIncrementalTicketsResponse

See [Tickets](/api-reference/ticketing/tickets/tickets/) for a detailed example.



## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `after_cursor`                                         | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `after_url`                                            | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `before_cursor`                                        | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `before_url`                                           | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `end_of_stream`                                        | *Optional[bool]*                                       | :heavy_minus_sign:                                     | N/A                                                    |
| `tickets`                                              | List[[models.TicketObject](../models/ticketobject.md)] | :heavy_minus_sign:                                     | N/A                                                    |