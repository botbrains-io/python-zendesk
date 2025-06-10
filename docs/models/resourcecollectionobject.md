# ResourceCollectionObject


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `created_at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_minus_sign:                                                            | When the resource collection was created                                      |
| `id`                                                                          | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | id for the resource collection. Automatically assigned upon creation          |
| `resources`                                                                   | List[[models.Resource](../models/resource.md)]                                | :heavy_minus_sign:                                                            | Array of resource metadata objects. See [Resource objects](#resource-objects) |
| `updated_at`                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)          | :heavy_minus_sign:                                                            | Last time the resource collection was updated                                 |