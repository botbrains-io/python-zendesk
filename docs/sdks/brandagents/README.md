# BrandAgents
(*brand_agents*)

## Overview

### Available Operations

* [list_brand_agents](#list_brand_agents) - List Brand Agent Memberships
* [show_brand_agent_by_id](#show_brand_agent_by_id) - Show Brand Agent Membership

## list_brand_agents

Returns a list of all brand agent memberships for your account.


#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For:

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.brand_agents.list_brand_agents(user_id=12345, brand_id=67890)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Filter by user ID                                                   | 12345                                                               |
| `brand_id`                                                          | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Filter by brand ID                                                  | 67890                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.BrandAgentsResponse](../../models/brandagentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_brand_agent_by_id

Returns a brand agent membership for your account.


#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.brand_agents.show_brand_agent_by_id(brand_agent_id="123ABC")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `brand_agent_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The id of the brand agent                                           | 123ABC                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.BrandAgentResponse](../../models/brandagentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |