# ListCommentsRequest


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     | Example                                                         |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `request_id`                                                    | *int*                                                           | :heavy_check_mark:                                              | The ID of the request                                           | 33                                                              |
| `since`                                                         | *Optional[str]*                                                 | :heavy_minus_sign:                                              | Filters the comments from the given datetime                    |                                                                 |
| `role`                                                          | *Optional[str]*                                                 | :heavy_minus_sign:                                              | One of "agent", "end_user". If not specified it does not filter |                                                                 |