# UserCreateInput


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `agent_brand_ids`                                          | List[*int*]                                                | :heavy_minus_sign:                                         | N/A                                                        |
| `custom_role_id`                                           | *Optional[int]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `email`                                                    | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `external_id`                                              | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `identities`                                               | List[[models.Identity](../models/identity.md)]             | :heavy_minus_sign:                                         | N/A                                                        |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        |
| `organization`                                             | [Optional[models.Organization]](../models/organization.md) | :heavy_minus_sign:                                         | N/A                                                        |
| `organization_id`                                          | *Optional[int]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `role`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        |
| `__pydantic_extra__`                                       | Dict[str, *Any*]                                           | :heavy_minus_sign:                                         | N/A                                                        |