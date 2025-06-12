# Test


## Fields

| Field                                     | Type                                      | Required                                  | Description                               |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `status`                                  | *Optional[str]*                           | :heavy_minus_sign:                        | Test status (e.g., "success", "failed")   |
| `message`                                 | *Optional[str]*                           | :heavy_minus_sign:                        | Test result message                       |
| `response_code`                           | *Optional[int]*                           | :heavy_minus_sign:                        | HTTP response code from the test endpoint |
| `response_body`                           | *Optional[str]*                           | :heavy_minus_sign:                        | Response body from the test endpoint      |