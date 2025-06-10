# UserIdentities
(*user_identities*)

## Overview

### Available Operations

* [list_user_identities](#list_user_identities) - List Identities
* [create_user_identity](#create_user_identity) - Create Identity
* [show_user_identity](#show_user_identity) - Show Identity
* [update_user_identity](#update_user_identity) - Update Identity
* [delete_user_identity](#delete_user_identity) - Delete Identity
* [make_user_identity_primary](#make_user_identity_primary) - Make Identity Primary
* [request_user_verfication](#request_user_verfication) - Request User Verification
* [verify_user_identity](#verify_user_identity) - Verify Identity

## list_user_identities

Returns a list of identities for the given user.

Use the first endpoint if authenticating as an agent. Use the second if authenticating as an end user. End users can only list email and phone number identities.

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page for cursor pagination.

#### Allowed For

* Agents
* Verified end users


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.user_identities.list_user_identities(user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `user_id`                                                                                     | *int*                                                                                         | :heavy_check_mark:                                                                            | The id of the user                                                                            | 35436                                                                                         |
| `type`                                                                                        | [Optional[models.ListUserIdentitiesType]](../../models/listuseridentitiestype.md)             | :heavy_minus_sign:                                                                            | Filters results by one or more identity types using the format `?type[]={type}&type[]={type}` |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.UserIdentitiesResponse](../../models/useridentitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_user_identity

Adds an identity to a user's profile. An agent can add an identity to any user profile.

Supported identity types:

| Type             | Example |
| ---------------- | ------- |
| email            | `{ "type" : "email", "value" : "someone@example.com" }` |
| twitter          | `{ "type" : "twitter", "value" : "screen_name" }` |
| facebook         | `{ "type" : "facebook", "value" : "855769377321" }` |
| google           | `{ "type" : "google", "value" : "example@gmail.com" }` |
| agent_forwarding | `{ "type" : "agent_forwarding", "value" : "+1 555-123-4567" }` |
| phone_number     | `{ "type" : "phone_number", "value" : "+1 555-123-4567" }` |

To create an identity without sending out a verification email, include a `"skip_verify_email": true` property. The `"skip_verify_email": true` property does not apply when updating your own agent profile. A welcome or verification email will be sent regardless of this setting.

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

    res = z_client.user_identities.create_user_identity(user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `user_id`                                                                                     | *int*                                                                                         | :heavy_check_mark:                                                                            | The id of the user                                                                            | 35436                                                                                         |
| `type`                                                                                        | [Optional[models.CreateUserIdentityType]](../../models/createuseridentitytype.md)             | :heavy_minus_sign:                                                                            | Filters results by one or more identity types using the format `?type[]={type}&type[]={type}` |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.UserIdentityResponse](../../models/useridentityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_user_identity

Shows the identity with the given id for a given user.

Use the first endpoint if authenticating as an agent. Use the second if authenticating as an end user. End users can only view email or phone number identity.

#### Allowed For

* Agents
* Verified end users


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.user_identities.show_user_identity(user_id=35436, user_identity_id=77938)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `user_identity_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The ID of the user identity                                         | 77938                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UserIdentityResponse](../../models/useridentityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_user_identity

This endpoint allows you to:

* Set the specified identity as verified (by setting `verified` to "true" or `verification_method` to "low")
* Unverify a verified identity (by setting `verified` to "false" or `verification_method` to "none")
* Update the `value` property of the specified identity

You can't change an identity's `primary` attribute with this endpoint. You must use the [Make Identity Primary](#make-identity-primary) endpoint instead.

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

    res = z_client.user_identities.update_user_identity(user_id=35436, user_identity_id=77938)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `user_identity_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The ID of the user identity                                         | 77938                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UserIdentityResponse](../../models/useridentityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_user_identity

Deletes the identity for a given user.
In certain cases, a phone number associated with an identity is still visible on the user profile after the identity has been deleted via API. You can remove the phone number from the user profile by updating the `phone` attribute of the user to an empty string. See [Update User via API](/api-reference/ticketing/users/users/#update-user) for details and examples.

Deleting identities with type `messaging` could break messaging functionality. For example, an agent may stop being able to send messages via the messaging channel.

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

    z_client.user_identities.delete_user_identity(user_id=35436, user_identity_id=77938)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `user_identity_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The ID of the user identity                                         | 77938                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## make_user_identity_primary

Sets the specified identity as primary. To change other attributes, use the [Update  Identity](#update-identity) endpoint. This is a collection-level operation and the correct behavior for an API client is to subsequently reload the entire collection.

The first endpoint is the preferred option if authenticating as an agent. If authenticating as an end user, you can only use the second endpoint. In addition, an end user can only make an email identity primary if the email is verified.

#### Allowed For

* Agents
* Verified end users


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.user_identities.make_user_identity_primary(user_id=35436, user_identity_id=77938)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `user_identity_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The ID of the user identity                                         | 77938                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UserIdentitiesResponse](../../models/useridentitiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## request_user_verfication

Sends the user a verification email with a link to verify ownership of the email address.

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

    res = z_client.user_identities.request_user_verfication(user_id=35436, user_identity_id=77938)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `user_identity_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The ID of the user identity                                         | 77938                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## verify_user_identity

Sets the specified identity as verified.

For security reasons, you can't use this endpoint to update the email identity of the account owner. To verify the person's identity, send a verification email. See [Verifying the account owner's email address](https://support.zendesk.com/hc/en-us/articles/4408828975130) in Zendesk help.

If [automatic mapping of users to organizations using the email domain](https://support.zendesk.com/hc/en-us/articles/4408882246298-Creating-organizations#topic_nxl_vdt_bc) is enabled and the user is not already a member of an organization, they will be automatically added to the organization associated with the email domain once the email identity is verified.

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

    res = z_client.user_identities.verify_user_identity(user_id=35436, user_identity_id=77938)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `user_identity_id`                                                  | *int*                                                               | :heavy_check_mark:                                                  | The ID of the user identity                                         | 77938                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UserIdentityResponse](../../models/useridentityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |