# BrandAgentObject


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `brand_id`                                                           | *int*                                                                | :heavy_check_mark:                                                   | The id of a brand                                                    |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time the brand membership was created                            |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Automatically assigned upon creation                                 |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time of the last update of the brand membership                  |
| `url`                                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The API url of this record                                           |
| `user_id`                                                            | *int*                                                                | :heavy_check_mark:                                                   | The id of an agent                                                   |