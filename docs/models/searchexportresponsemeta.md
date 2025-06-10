# SearchExportResponseMeta

Metadata for the export query response.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `after_cursor`                                                 | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | The cursor id for the next object.                             |
| `before_cursor`                                                | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | The cursor id for the previous object.                         |
| `has_more`                                                     | *Optional[bool]*                                               | :heavy_minus_sign:                                             | Whether there are more items yet to be returned by the cursor. |