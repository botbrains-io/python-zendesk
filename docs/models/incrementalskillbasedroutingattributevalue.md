# IncrementalSkillBasedRoutingAttributeValue


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `attribute_id`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Id of the associated attribute                                       |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Automatically assigned when an attribute value is created            |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The name of the attribute value                                      |
| `time`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time the attribute value was created, updated, or deleted        |
| `type`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | One of "create", "update", or "delete"                               |