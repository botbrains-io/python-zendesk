# AssigneeFieldAssignableGroups
(*assignee_field_assignable_groups*)

## Overview

### Available Operations

* [list_assignee_field_assignable_groups_and_agents_search](#list_assignee_field_assignable_groups_and_agents_search) - List assignable groups and agents based on query matched against name

## list_assignee_field_assignable_groups_and_agents_search

List assignable groups and agents based on query matched against name

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListAssigneeFieldAssignableGroupsAndAgentsSearch" method="get" path="/api/lotus/assignables/autocomplete.json" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `name`                                                                      | *str*                                                                       | :heavy_check_mark:                                                          | Query string used to search assignable groups & agents in the AssigneeField |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.AssigneeFieldAssignableGroupsAndAgentsSearchResponse](../../models/assigneefieldassignablegroupsandagentssearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |