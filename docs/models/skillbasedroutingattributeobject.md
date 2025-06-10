# SkillBasedRoutingAttributeObject


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When this record was created                                         |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Automatically assigned when an attribute is created                  |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The name of the attribute                                            |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | When this record was last updated                                    |
| `url`                                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | URL of the attribute                                                 |