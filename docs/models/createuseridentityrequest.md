# CreateUserIdentityRequest


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `user_id`                                                                                     | *int*                                                                                         | :heavy_check_mark:                                                                            | The id of the user                                                                            |
| `type`                                                                                        | [Optional[models.CreateUserIdentityType]](../models/createuseridentitytype.md)                | :heavy_minus_sign:                                                                            | Filters results by one or more identity types using the format `?type[]={type}&type[]={type}` |