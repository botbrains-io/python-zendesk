# FailedResult


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `action`                                                     | *str*                                                        | :heavy_check_mark:                                           | The action the job attempted (`"action": "update"`)          |
| `details`                                                    | *str*                                                        | :heavy_check_mark:                                           | The details of the error                                     |
| `error`                                                      | *str*                                                        | :heavy_check_mark:                                           | The error message                                            |
| `id`                                                         | *int*                                                        | :heavy_check_mark:                                           | The id of the resource the job attempted to update           |
| `success`                                                    | *bool*                                                       | :heavy_check_mark:                                           | Whether the action was successful or not (`"success": true`) |
| `__pydantic_extra__`                                         | Dict[str, *Any*]                                             | :heavy_minus_sign:                                           | N/A                                                          |