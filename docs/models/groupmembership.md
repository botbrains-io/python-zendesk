# GroupMembership


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `user_id`                                                                           | *int*                                                                               | :heavy_check_mark:                                                                  | The id of an agent                                                                  |
| `group_id`                                                                          | *int*                                                                               | :heavy_check_mark:                                                                  | The id of a group                                                                   |
| `default`                                                                           | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | If true, tickets assigned directly to the agent will assume this membership's group |