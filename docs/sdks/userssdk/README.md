# Users

## Overview

### Available Operations

* [list_deleted_users](#list_deleted_users) - List Deleted Users
* [show_deleted_user](#show_deleted_user) - Show Deleted User
* [permanently_delete_user](#permanently_delete_user) - Permanently Delete User
* [count_deleted_users](#count_deleted_users) - Count Deleted Users
* [list_users](#list_users) - List Users
* [create_user](#create_user) - Create User
* [show_user](#show_user) - Show User
* [update_user](#update_user) - Update User
* [delete_user](#delete_user) - Delete User
* [show_user_compliance_deletion_statuses](#show_user_compliance_deletion_statuses) - Show Compliance Deletion Statuses
* [merge_end_users](#merge_end_users) - Merge End Users
* [show_user_related](#show_user_related) - Show User Related Information
* [autocomplete_users](#autocomplete_users) - Autocomplete Users
* [count_users](#count_users) - Count Users
* [create_many_users](#create_many_users) - Create Many Users
* [create_or_update_user](#create_or_update_user) - Create Or Update User
* [create_or_update_many_users](#create_or_update_many_users) - Create Or Update Many Users
* [destroy_many_users](#destroy_many_users) - Bulk Delete Users
* [logout_many_users](#logout_many_users) - Logout many users
* [show_current_user](#show_current_user) - Show Self
* [request_user_create](#request_user_create) - Request User Create
* [search_users](#search_users) - Search Users
* [show_many_users](#show_many_users) - Show Many Users
* [update_many_users](#update_many_users) - Update Many Users

## list_deleted_users

Returns deleted users, including permanently deleted users.

If the results contains permanently deleted users, the users' properties
that normally contain personal data, such as `email` and `phone`,
are null. The `name` property is "Permanently Deleted User".

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListDeletedUsers" method="get" path="/api/v2/deleted_users" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.list_deleted_users(page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListDeletedUsersResponse](../../models/listdeletedusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_deleted_user

Returns users that have been deleted but not permanently yet. See [Permanently Delete User](#permanently-delete-user).

#### Allowed For:

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowDeletedUser" method="get" path="/api/v2/deleted_users/{deleted_user_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.show_deleted_user(deleted_user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `deleted_user_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of the deleted user                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedUserResponse](../../models/deleteduserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## permanently_delete_user

Before permanently deleting a user, you must delete the user first. See [Delete User](/api-reference/ticketing/users/users/#delete-user).

WARNING: Permanently deleting a user deletes all of their information. This information is not recoverable.

#### Permanent user deletion rate limit

You can permanently delete 700 users every 10 minutes.
The rate limiting mechanism behaves as described in
[Rates Limits](/api-reference/introduction/rate-limits/#monitoring-your-request-activity) in the API introduction.
Zendesk recommends that you obey the Retry-After header values.

#### Allowed For

* Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


### Example Usage

<!-- UsageSnippet language="python" operationID="PermanentlyDeleteUser" method="delete" path="/api/v2/deleted_users/{deleted_user_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.permanently_delete_user(deleted_user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `deleted_user_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of the deleted user                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedUserResponse](../../models/deleteduserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_deleted_users

Returns an approximate count of deleted users, including permanently deleted users. If the count exceeds 100,000, it is updated every 24 hours.

The response includes a `refreshed_at` property in a `count` object that contains a timestamp indicating when the count was last updated.

**Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null.
This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="CountDeletedUsers" method="get" path="/api/v2/deleted_users/count" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.count_deleted_users()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountResponse](../../models/countresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_users

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Admins, Agents and Light Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListUsers" method="get" path="/api/v2/users" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.list_users(page_size=100, role_query_parameter="agent", role_query_parameter1="agent", permission_set=123, external_id="abc")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `role_query_parameter`                                                                                                                                                                                                                                                                                              | [Optional[models.UserRoleFilter]](../../models/userrolefilter.md)                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters the results by role. Possible values are "end-user", "agent", or "admin"<br/>                                                                                                                                                                                                                               |
| `role_query_parameter1`                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters the results by more than one role using the format `role[]={role}&role[]={role}`<br/>                                                                                                                                                                                                                       |
| `permission_set`                                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | For custom roles which is available on the Enterprise plan and above. You can only filter by one role ID per request                                                                                                                                                                                                |
| `external_id`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | List users by external id. External id has to be unique for each user under the same account.                                                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListUsersResponse](../../models/listusersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_user

Create User

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateUser" method="post" path="/api/v2/users" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.create_user(user=models.UserCreateInput(
        agent_brand_ids=[
            8119246973690,
            8119246973691,
            8119246973692,
        ],
        custom_role_id=123456,
        email="roge@example.org",
        identities=[
            models.Identity(
                type="email",
                value="test@user.com",
            ),
            models.Identity(
                type="twitter",
                value="tester84",
            ),
        ],
        name="Roger Wilco",
        organization=models.Organization(
            name="VIP Customers",
        ),
        role="agent",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user`                                                              | [models.UserInput](../../models/userinput.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserResponse](../../models/userresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_user

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowUser" method="get" path="/api/v2/users/{user_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.show_user(user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserResponse](../../models/userresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_user

Update User

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateUser" method="put" path="/api/v2/users/{user_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.update_user(user_id=35436, user=models.UserMergePropertiesInput(
        name="Roger Wilco II",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  |
| `user`                                                              | [models.UserInput](../../models/userinput.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserResponse](../../models/userresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_user

Deletes the user and associated records from the account.

**Warning**:

* Deleted users are not recoverable.
* Both agents and administrators can soft delete users in the agent interface in Zendesk Support. Agents with permission can delete end users, while administrators can delete all users except the account owner.

To comply with GDPR, a further step is needed. See [Permanently Delete User](/api-reference/ticketing/users/users/#permanently-delete-user).

#### Allowed For

* Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteUser" method="delete" path="/api/v2/users/{user_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.delete_user(user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserResponse](../../models/userresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_user_compliance_deletion_statuses

Returns the GDPR status for each user per area of compliance. A Zendesk area of compliance is typically a product like "support/explore" but can be more fine-grained for areas within the product lines.

If the user is not in the account, the request returns a 404 status.

```http
Status: 404
{
  "error":"RecordNotFound",
  "description":"Not found"
}
```

#### Allowed For

* Agents, with restrictions

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowUserComplianceDeletionStatuses" method="get" path="/api/v2/users/{user_id}/compliance_deletion_statuses" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.show_user_compliance_deletion_statuses(user_id=35436, page_size=100, application="chat")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                                                                                                                                                                                           | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The id of the user                                                                                                                                                                                                                                                                                                  |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `application`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Area of compliance                                                                                                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ShowUserComplianceDeletionStatusesResponse](../../models/showusercompliancedeletionstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## merge_end_users

Merges the end user specified in the path parameter into the existing end user specified in the request body.

Any two end users can be merged with the exception of end users created by sharing agreements.

To be eligible for merging, the user in the path parameter must be a requester on 10,000 or fewer tickets. Otherwise, the merge will be blocked.

Agents, admins, and users with more than 10,000 requested tickets cannot be merged.

For more information about how user data is merged, see [Merging a user's duplicate account](https://support.zendesk.com/hc/en-us/articles/4408887695898) in Zendesk help.

#### Allowed For

* Admins or agents with permission to edit end users


### Example Usage

<!-- UsageSnippet language="python" operationID="MergeEndUsers" method="put" path="/api/v2/users/{user_id}/merge" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.merge_end_users(user_id=35436, user=models.UserMergeByIDInput(
        id=35436,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  |
| `user`                                                              | [models.UserInput](../../models/userinput.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserResponse](../../models/userresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_user_related

Show User Related Information

### Example Usage

<!-- UsageSnippet language="python" operationID="ShowUserRelated" method="get" path="/api/v2/users/{user_id}/related" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.show_user_related(user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserRelatedResponse](../../models/userrelatedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## autocomplete_users

Returns an array of users whose name starts with the value specified in the `name` parameter.
It only returns users with no foreign identities.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="AutocompleteUsers" method="get" path="/api/v2/users/autocomplete" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.autocomplete_users(name="gil", source="zen:organization")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                            | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | The name to search for the user.<br/>                                                                                                             |
| `field_id`                                                                                                                                        | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The id of a lookup relationship field.  The type of field is determined<br/>by the `source` param<br/>                                            |
| `source`                                                                                                                                          | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | If a `field_id` is provided, this specifies the type of the field.<br/>For example, if the field is on a "zen:user", it references a field on a user<br/> |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[models.UsersResponse](../../models/usersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_users

Returns an approximate count of users. If the count exceeds 100,000, it is updated every 24 hours.

The response includes a `refreshed_at` property in a `count` object that contains a timestamp indicating when the count was last updated.

**Note**: When the count exceeds 100,000, the `refreshed_at` property may occasionally be null.
This indicates that the count is being updated in the background. The `count` object's `value` property is limited to 100,000 until the update is complete.

#### Allowed For

* Admins, Agents and Light Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="CountUsers" method="get" path="/api/v2/users/count" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.count_users(role_query_parameter="agent", role_query_parameter1="agent", permission_set=123)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `role_query_parameter`                                                                                               | [Optional[models.UserRoleFilter]](../../models/userrolefilter.md)                                                    | :heavy_minus_sign:                                                                                                   | Filters the results by role. Possible values are "end-user", "agent", or "admin"<br/>                                |
| `role_query_parameter1`                                                                                              | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | Filters the results by more than one role using the format `role[]={role}&role[]={role}`<br/>                        |
| `permission_set`                                                                                                     | *Optional[int]*                                                                                                      | :heavy_minus_sign:                                                                                                   | For custom roles which is available on the Enterprise plan and above. You can only filter by one role ID per request |
| `retries`                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                     | :heavy_minus_sign:                                                                                                   | Configuration to override the default retry behavior of the client.                                                  |

### Response

**[models.CountResponse](../../models/countresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_many_users

Accepts an array of up to 100 user objects.

**Note**: To protect the data in your Zendesk account, bulk user imports are not enabled by default in Zendesk accounts. The account owner must contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to enable the imports. A 403 Forbidden
error is returned if data imports are not enabled.

#### Allowed For

* Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members

#### Specifying an organization

You can assign a user to an existing organization by setting an
`organization_id` property in the user object.

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateManyUsers" method="post" path="/api/v2/users/create_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.create_many_users(users=[
        models.UserMergePropertiesInput(
            email="roge@example.org",
            name="Roger Wilco",
            organization_id=567812345,
            **{
                "agent_brand_ids": [
                    8119246973690,
                    8119246973691,
                    8119246973692,
                ],
                "role": "agent",
            },
        ),
        models.UserMergePropertiesInput(
            email="woge@example.org",
            name="Woger Rilco",
            **{
                "role": "admin",
            },
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `users`                                                             | List[[models.UserInput](../../models/userinput.md)]                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_or_update_user

Creates a user if the user does not already exist, or updates an existing user
identified by e-mail address or external ID.

If you don't specify a role parameter, the new user is assigned the role of end user.

If you need to create users without sending out a verification email, include a `"skip_verify_email": true` property in the body.

#### External ID Case Sensitivity

When providing an external id to identify an existing user to update, the search for the user record is not case sensitive.

However, if an existing user is found, the system will update the user's external id to match the case of the external id used to find the user.

#### Response Status Code

- If the user exists in Zendesk, a successful request returns a 200 status code with "Location: /api/v2/users/{user_id}.json".
- If the user does not exist in Zendesk, a successful request returns a 201 status code with "Location: /api/v2/users/{new_user_id}.json".

#### Allowed For

* Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateOrUpdateUser" method="post" path="/api/v2/users/create_or_update" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.create_or_update_user(user=models.UserCreateInput(
        agent_brand_ids=[
            8119246973690,
            8119246973691,
            8119246973692,
        ],
        custom_role_id=123456,
        email="roge@example.org",
        identities=[
            models.Identity(
                type="email",
                value="test@user.com",
            ),
            models.Identity(
                type="twitter",
                value="tester84",
            ),
        ],
        name="Roger Wilco",
        organization=models.Organization(
            name="VIP Customers",
        ),
        role="agent",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user`                                                              | [models.UserInput](../../models/userinput.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserResponse](../../models/userresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_or_update_many_users

Accepts an array of up to 100 user objects. For each user, the user is created if it does not
already exist, or the existing user is updated.

**Note**: To protect the data in your Zendesk account, bulk user imports are not enabled by default in Zendesk accounts. The account owner must contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to enable the imports. A 403 Forbidden
error is returned if data imports are not enabled.    

Each individual user object can identify an existing user by `email` or by `external_id`.

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

* Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) to manage end users or team members


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateOrUpdateManyUsers" method="post" path="/api/v2/users/create_or_update_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.create_or_update_many_users(users=[
        models.UserCreateInput(
            agent_brand_ids=[
                8119246973690,
                8119246973691,
                8119246973692,
            ],
            custom_role_id=123456,
            email="roge@example.org",
            identities=[
                models.Identity(
                    type="email",
                    value="test@user.com",
                ),
                models.Identity(
                    type="twitter",
                    value="tester84",
                ),
            ],
            name="Roger Wilco",
            organization=models.Organization(
                name="VIP Customers",
            ),
            role="agent",
        ),
        models.UserMergePropertiesInput(
            email="woge@example.org",
            name="Woger Rilco",
            **{
                "external_id": "account_54321",
                "role": "admin",
            },
        ),
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `users`                                                             | List[[models.UserInput](../../models/userinput.md)]                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## destroy_many_users

Accepts a comma-separated list of up to 100 user ids.

The request takes an `ids` or an `external_ids` query parameter.

#### Allowed for

- Admins

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.


### Example Usage

<!-- UsageSnippet language="python" operationID="DestroyManyUsers" method="delete" path="/api/v2/users/destroy_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.destroy_many_users(ids="1,2,3", external_ids="abc,def,ghi")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Id of the users to delete. Comma separated                          |
| `external_ids`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | External Id of the users to delete. Comma separated                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## logout_many_users

Accepts a comma-separated list of up to 100 user ids.

#### Allowed For:

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="LogoutManyUsers" method="post" path="/api/v2/users/logout_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.logout_many_users(ids="1,2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Accepts a comma-separated list of up to 100 user ids.<br/>          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_current_user

The endpoint returns [user information](/api-reference/ticketing/users/users/) and an `authenticity_token`. 

#### Allowed For

* Anonymous users

#### Authenticity Token

Zendesk API calls made by end users from a Zendesk help center must include `authenticity_token` in the `X-CSRF-Token` HTTP header. This helps prevent [cross-site request forgery (CSRF)](https://en.wikipedia.org/wiki/Cross-site_request_forgery) attacks.

For an example using an authenticity token, see the AJAX request in the [Upgrading from Templating API v1](https://developer.zendesk.com/documentation/help_center/help-center-templates/v1#jquery) documentation.


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowCurrentUser" method="get" path="/api/v2/users/me" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.show_current_user()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CurrentUserResponse](../../models/currentuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## request_user_create

Sends the owner a reminder email to update their subscription so more agents can be created.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="RequestUserCreate" method="post" path="/api/v2/users/request_create" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.request_user_create(user=models.UserMergePropertiesInput(
        email="roge@example.org",
        name="Roger Wilco",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user`                                                              | [models.UserInput](../../models/userinput.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_users

Returns an array of users who meet the search criteria.

Returns up to 100 records per page to a maximum of 10,000 records per query. See [Using offset pagination](/api-reference/introduction/pagination/#using-offset-pagination).

#### Pagination

* Offset pagination only

See [Using Offset Pagination](/api-reference/ticketing/introduction/#using-offset-pagination).

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="SearchUsers" method="get" path="/api/v2/users/search" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.search_users(query="jdoe", external_id="abc124")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                         | The `query` parameter supports the Zendesk search syntax for more advanced<br/>user searches. It can specify a partial or full value of any<br/>user property, including name, email address, notes, or phone. Example:<br/>`query="jdoe"`.<br/>See the [Search API](/api-reference/ticketing/ticket-management/search/).<br/> |
| `external_id`                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                         | The `external_id` parameter does not support the search syntax. It only accepts ids.<br/>                                                                                                                                                                                                                  |
| `retries`                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                        |

### Response

**[models.UsersResponse](../../models/usersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_many_users

Accepts a comma-separated list of up to 100 user ids or external ids.

#### Allowed For:

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowManyUsers" method="get" path="/api/v2/users/show_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.show_many_users(ids="1,2", external_ids="abc,def")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Accepts a comma-separated list of up to 100 user ids.<br/>          |
| `external_ids`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Accepts a comma-separated list of up to 100 external ids.<br/>      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UsersResponse](../../models/usersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many_users

Update Many Users

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateManyUsers" method="put" path="/api/v2/users/update_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.users.update_many_users(request_body=models.UpdateManyUsersUserRequest(
        user=models.UserMergePropertiesInput(
            organization_id=1,
        ),
    ), ids="1,2,3", external_ids="abc,def,ghi")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request_body`                                                                  | [models.UpdateManyUsersRequestBody](../../models/updatemanyusersrequestbody.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `ids`                                                                           | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | Id of the users to update. Comma separated                                      |
| `external_ids`                                                                  | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | External Id of the users to update. Comma separated                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |