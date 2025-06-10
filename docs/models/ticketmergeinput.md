# TicketMergeInput


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `ids`                                                   | List[*int*]                                             | :heavy_check_mark:                                      | Ids of tickets to merge into the target ticket          |
| `source_comment`                                        | *Optional[str]*                                         | :heavy_minus_sign:                                      | Private comment to add to the source ticket             |
| `source_comment_is_public`                              | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Whether comment in source tickets are public or private |
| `target_comment`                                        | *Optional[str]*                                         | :heavy_minus_sign:                                      | Private comment to add to the target ticket             |
| `target_comment_is_public`                              | *Optional[bool]*                                        | :heavy_minus_sign:                                      | Whether comment in target ticket is public or private   |