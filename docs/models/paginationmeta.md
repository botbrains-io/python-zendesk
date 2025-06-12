# PaginationMeta


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `has_more`                                        | *Optional[bool]*                                  | :heavy_minus_sign:                                | Whether there are more results available          |
| `after_cursor`                                    | *Optional[str]*                                   | :heavy_minus_sign:                                | Cursor for the next page of results               |
| `before_cursor`                                   | *Optional[str]*                                   | :heavy_minus_sign:                                | Cursor for the previous page of results           |
| `count`                                           | *Optional[int]*                                   | :heavy_minus_sign:                                | Total number of items (may not always be present) |