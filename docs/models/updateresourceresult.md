# UpdateResourceResult


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `action`                                                      | *str*                                                         | :heavy_check_mark:                                            | the action the job attempted (`"action": "update"`)<br/>      |
| `id`                                                          | *int*                                                         | :heavy_check_mark:                                            | the id of the resource the job attempted to update            |
| `status`                                                      | *str*                                                         | :heavy_check_mark:                                            | the status (`"status": "Updated"`)<br/>                       |
| `success`                                                     | *bool*                                                        | :heavy_check_mark:                                            | whether the action was successful or not (`"success": true`)<br/> |
| `__pydantic_extra__`                                          | Dict[str, *Any*]                                              | :heavy_minus_sign:                                            | N/A                                                           |