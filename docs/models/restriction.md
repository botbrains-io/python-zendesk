# Restriction

Who may access this macro. Will be null when everyone in the account can access it


## Fields

| Field                               | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `id`                                | *Optional[int]*                     | :heavy_minus_sign:                  | The numeric ID of the group or user |
| `ids`                               | List[*int*]                         | :heavy_minus_sign:                  | The numeric IDs of the groups       |
| `type`                              | *Optional[str]*                     | :heavy_minus_sign:                  | Allowed values are Group or User    |
| `__pydantic_extra__`                | Dict[str, *Any*]                    | :heavy_minus_sign:                  | N/A                                 |