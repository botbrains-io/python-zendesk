# ListAuditsForTicketRequest


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `ticket_id`                                                 | *int*                                                       | :heavy_check_mark:                                          | The ID of the ticket                                        | 123456                                                      |
| `page_size`                                                 | *Optional[int]*                                             | :heavy_minus_sign:                                          | Number of records per page (required for cursor pagination) |                                                             |
| `page_after`                                                | *Optional[str]*                                             | :heavy_minus_sign:                                          | Cursor for pagination (opaque string)                       |                                                             |