# CustomRoles
(*custom_roles*)

## Overview

### Available Operations

* [list_custom_roles](#list_custom_roles) - List Custom Roles
* [create_custom_role](#create_custom_role) - Create Custom Role
* [show_custom_role_by_id](#show_custom_role_by_id) - Show Custom Role
* [update_custom_role_by_id](#update_custom_role_by_id) - Update Custom Role
* [delete_custom_role_by_id](#delete_custom_role_by_id) - Delete Custom Role

## list_custom_roles

#### Availability

* Accounts on the Enterprise plan or above

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListCustomRoles" method="get" path="/api/v2/custom_roles" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_roles.list_custom_roles()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomRolesResponse](../../models/customrolesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_custom_role

#### Availability

* Accounts on the Enterprise plan or above

#### Allowed for

* Administrators
* Agents with the `manage_roles` permission


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateCustomRole" method="post" path="/api/v2/custom_roles" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_roles.create_custom_role()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomRoleResponse](../../models/customroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_custom_role_by_id

#### Availability

* Accounts on the Enterprise plan or above

#### Allowed for

* Administrators
* Agents with the `manage_roles` permission


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowCustomRoleById" method="get" path="/api/v2/custom_roles/{custom_role_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_roles.show_custom_role_by_id(custom_role_id=10127)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_role_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the custom agent role                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomRoleResponse](../../models/customroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_custom_role_by_id

#### Availability

* Accounts on the Enterprise plan or above

#### Allowed for

* Administrators
Agents with the `manage_roles` permission


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateCustomRoleById" method="put" path="/api/v2/custom_roles/{custom_role_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_roles.update_custom_role_by_id(custom_role_id=10127)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_role_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the custom agent role                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomRoleResponse](../../models/customroleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_custom_role_by_id

#### Availability

* Accounts on the Enterprise plan or above

#### Allowed for

* Administrators
* Agents with the `manage_roles` permission


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteCustomRoleById" method="delete" path="/api/v2/custom_roles/{custom_role_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.custom_roles.delete_custom_role_by_id(custom_role_id=10127)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_role_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the custom agent role                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |