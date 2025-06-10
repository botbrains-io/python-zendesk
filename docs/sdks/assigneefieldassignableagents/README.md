# AssigneeFieldAssignableAgents
(*assignee_field_assignable_agents*)

## Overview

### Available Operations

* [list_assignee_field_assignable_groups_and_agents_search](#list_assignee_field_assignable_groups_and_agents_search) - List assignable groups and agents based on query matched against name
* [list_assignee_field_assignable_groups](#list_assignee_field_assignable_groups) - List assignable groups on the AssigneeField
* [list_assignee_field_assignable_group_agents](#list_assignee_field_assignable_group_agents) - List assignable agents from a group on the AssigneeField

## list_assignee_field_assignable_groups_and_agents_search

List assignable groups and agents based on query matched against name

#### Allowed For

* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_agents.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `name`                                                                      | *str*                                                                       | :heavy_check_mark:                                                          | Query string used to search assignable groups & agents in the AssigneeField | Johnny Agent                                                                |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.AssigneeFieldAssignableGroupsAndAgentsSearchResponse](../../models/assigneefieldassignablegroupsandagentssearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_assignee_field_assignable_groups

List assignable groups on the AssigneeField

#### Allowed For

* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_agents.list_assignee_field_assignable_groups()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AssigneeFieldAssignableGroupsResponse](../../models/assigneefieldassignablegroupsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_assignee_field_assignable_group_agents

List assignable agents from a group on the AssigneeField

#### Allowed For

* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_agents.list_assignee_field_assignable_group_agents(group_id=122)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the group                                                 | 122                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AssigneeFieldAssignableGroupAgentsResponse](../../models/assigneefieldassignablegroupagentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |