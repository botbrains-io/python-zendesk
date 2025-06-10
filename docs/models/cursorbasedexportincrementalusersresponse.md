# CursorBasedExportIncrementalUsersResponse


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `after_cursor`                                     | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `after_url`                                        | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `before_cursor`                                    | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `before_url`                                       | *OptionalNullable[str]*                            | :heavy_minus_sign:                                 | N/A                                                |
| `end_of_stream`                                    | *Optional[bool]*                                   | :heavy_minus_sign:                                 | N/A                                                |
| `users`                                            | List[[models.UserObject](../models/userobject.md)] | :heavy_minus_sign:                                 | N/A                                                |