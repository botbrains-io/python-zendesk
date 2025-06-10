# TriggerBulkUpdateItem


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `active`                                                        | *Optional[bool]*                                                | :heavy_minus_sign:                                              | The active status of the ticket trigger (true or false)         |
| `category_id`                                                   | *Optional[str]*                                                 | :heavy_minus_sign:                                              | The ID of the new category the ticket trigger is to be moved to |
| `id`                                                            | *int*                                                           | :heavy_check_mark:                                              | The ID of the ticket trigger to update                          |
| `position`                                                      | *Optional[int]*                                                 | :heavy_minus_sign:                                              | The new position of the ticket trigger                          |