# HostMappingObject


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `cname`                                                              | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The canonical name record for a host mapping                         |
| `expected_cnames`                                                    | List[*str*]                                                          | :heavy_minus_sign:                                                   | Array of expected CNAME records for host mapping(s) of a given brand |
| `is_valid`                                                           | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | Whether a host mapping is valid or not for a given brand             |
| `reason`                                                             | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Reason why a host mapping is valid or not                            |