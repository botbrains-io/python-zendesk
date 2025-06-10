# UserFieldsResponse


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `count`                                                      | *Optional[int]*                                              | :heavy_minus_sign:                                           | Total count of records retrieved                             |
| `next_page`                                                  | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | URL of the next page                                         |
| `previous_page`                                              | *OptionalNullable[str]*                                      | :heavy_minus_sign:                                           | URL of the previous page                                     |
| `user_fields`                                                | List[[models.UserFieldObject](../models/userfieldobject.md)] | :heavy_minus_sign:                                           | N/A                                                          |