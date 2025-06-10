# ChannelFrameworkResultStatusObject

The status of the import for the indicated resource


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `code`                                                                                                    | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | A code indicating the status of the import of the resource, as described in [status codes](#status-codes) |
| `description`                                                                                             | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | In the case of an exception, a description of the exception. Otherwise, not present.                      |