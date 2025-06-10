# IncrementalSkillBasedRoutingAttribute


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Automatically assigned when an attribute is created                  |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The name of the attribute                                            |
| `time`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time the attribute was created, updated, or deleted              |
| `type`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | One of "create", "update", or "delete"                               |