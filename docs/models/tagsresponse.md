# TagsResponse


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `count`                                                        | *Optional[int]*                                                | :heavy_minus_sign:                                             | The number of pages                                            |
| `next_page`                                                    | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | The url of the previous page                                   |
| `previous_page`                                                | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | The url of the next page                                       |
| `tags`                                                         | List[[models.TagListTagObject](../models/taglisttagobject.md)] | :heavy_minus_sign:                                             | N/A                                                            |