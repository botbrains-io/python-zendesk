# GroupSLAPolicies
(*group_sla_policies*)

## Overview

### Available Operations

* [list_group_sla_policies](#list_group_sla_policies) - List Group SLA Policies
* [create_group_sla_policy](#create_group_sla_policy) - Create Group SLA Policy
* [show_group_sla_policy](#show_group_sla_policy) - Show Group SLA Policy
* [update_group_sla_policy](#update_group_sla_policy) - Update Group SLA Policy
* [delete_group_sla_policy](#delete_group_sla_policy) - Delete Group SLA Policy
* [retrieve_group_sla_policy_filter_definition_items](#retrieve_group_sla_policy_filter_definition_items) - Retrieve Supported Filter Definition Items
* [reorder_group_sla_policies](#reorder_group_sla_policies) - Reorder Group SLA Policies

## list_group_sla_policies

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ListGroupSLAPolicies" method="get" path="/api/v2/group_slas/policies" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.group_sla_policies.list_group_sla_policies()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GroupSLAPoliciesResponse](../../models/groupslapoliciesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_group_sla_policy

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateGroupSLAPolicy" method="post" path="/api/v2/group_slas/policies" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.group_sla_policies.create_group_sla_policy()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GroupSLAPolicyResponse](../../models/groupslapolicyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_group_sla_policy

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowGroupSLAPolicy" method="get" path="/api/v2/group_slas/policies/{group_sla_policy_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.group_sla_policies.show_group_sla_policy(group_sla_policy_id=36)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_sla_policy_id`                                               | *int*                                                               | :heavy_check_mark:                                                  | The id of the Group SLA policy                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GroupSLAPolicyResponse](../../models/groupslapolicyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_group_sla_policy

Updates the specified policy.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateGroupSLAPolicy" method="put" path="/api/v2/group_slas/policies/{group_sla_policy_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.group_sla_policies.update_group_sla_policy(group_sla_policy_id=36)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_sla_policy_id`                                               | *int*                                                               | :heavy_check_mark:                                                  | The id of the Group SLA policy                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GroupSLAPolicyResponse](../../models/groupslapolicyresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_group_sla_policy

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteGroupSLAPolicy" method="delete" path="/api/v2/group_slas/policies/{group_sla_policy_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.group_sla_policies.delete_group_sla_policy(group_sla_policy_id=36)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_sla_policy_id`                                               | *int*                                                               | :heavy_check_mark:                                                  | The id of the Group SLA policy                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_group_sla_policy_filter_definition_items

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveGroupSLAPolicyFilterDefinitionItems" method="get" path="/api/v2/group_slas/policies/definitions" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.group_sla_policies.retrieve_group_sla_policy_filter_definition_items()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GroupSLAPolicyFilterDefinitionResponse](../../models/groupslapolicyfilterdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## reorder_group_sla_policies

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ReorderGroupSLAPolicies" method="put" path="/api/v2/group_slas/policies/reorder" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.group_sla_policies.reorder_group_sla_policies()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `group_sla_policy_ids`                                              | List[*str*]                                                         | :heavy_minus_sign:                                                  | The ids of the Group SLA policies to reorder                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |