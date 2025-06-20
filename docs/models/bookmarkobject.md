# BookmarkObject


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `created_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | The time the bookmark was created                                          |
| `id`                                                                       | *Optional[int]*                                                            | :heavy_minus_sign:                                                         | Automatically assigned when the bookmark is created                        |
| `ticket`                                                                   | [Optional[models.BookmarkObjectTicket]](../models/bookmarkobjectticket.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `url`                                                                      | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The API url of this bookmark                                               |