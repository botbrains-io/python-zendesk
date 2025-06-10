# MacroAttachmentObject


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `content_type`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The content type of the image. Example value: "image/png"            |
| `content_url`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | A full URL where the attachment image file can be downloaded         |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time when this attachment was created                            |
| `filename`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The name of the image file                                           |
| `id`                                                                 | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Automatically assigned when created                                  |
| `size`                                                               | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The size of the image file in bytes                                  |