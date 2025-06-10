# OAuthTokens
(*o_auth_tokens*)

## Overview

### Available Operations

* [list_o_auth_tokens](#list_o_auth_tokens) - List Tokens
* [create_o_auth_token](#create_o_auth_token) - Create Token
* [show_token](#show_token) - Show Token
* [revoke_o_auth_token](#revoke_o_auth_token) - Revoke Token

## list_o_auth_tokens

Returns the properties of the tokens for the current user. Admins can view OAuth token properties for all users using the [all](/api-reference/ticketing/oauth/oauth_tokens/#parameters) parameter. The [client_id](/api-reference/ticketing/oauth/oauth_tokens/#parameters) parameter can be included to filter that list by a global or local OAuth client ID. For security reasons, only the first 10 characters of each access token are included.

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

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

    res = z_client.o_auth_tokens.list_o_auth_tokens(client_id=223443, global_client_id=334556, all=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `client_id`                                                                 | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | The id of the OAuth client                                                  | 223443                                                                      |
| `global_client_id`                                                          | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | The id of the global OAuth client                                           | 334556                                                                      |
| `all`                                                                       | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | A boolean that returns all OAuth tokens in the account. Requires admin role | true                                                                        |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.OAuthTokensResponse](../../models/oauthtokensresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_o_auth_token

Returns an OAuth access token with a specified [scope](#scopes).

Refresh tokens aren't used. An access token doesn't expire but it can be [revoked](#revoke-token).

For a tutorial, see [Creating and using OAuth tokens with the API](/documentation/ticketing/working-with-oauth/creating-and-using-oauth-tokens-with-the-api/).

**Note**: For OAuth authorization code, use the [Create Token for Grant Type](/api-reference/ticketing/oauth/grant_type_tokens/#create-token-for-grant-type) endpoint.
The two APIs don't share the same path, JSON format, or request parameters. However, both APIs return access tokens that can be used to [authenticate API requests](/api-reference/ticketing/introduction/#oauth-access-token).

#### Allowed For

* Admins

#### Request parameters

The POST request takes a "token" object that contains an OAuth client's resource id and scopes.

| Name      | Type    | Description
| --------- | ------- | --------------------------------------------------
| client_id | integer | The resource `id` of an [OAuth client](/api-reference/ticketing/oauth/oauth_clients/#json-format) (not the client's unique identifier). For the ids, see [List Clients](/api-reference/ticketing/oauth/oauth_clients/#list-clients)
| scopes    | array   | Valid scopes for the token. See [Scopes](#scopes) below

#### Scopes

The **scopes** parameter defines whether requests authenticated with the token can
post, put, and delete data, or only get data.

**Note**: Don't confuse the **scopes** parameter (plural) with the **scope** parameter (singular)
for [grant-type tokens](/api-reference/ticketing/oauth/grant_type_tokens/).

The **scopes** parameter is an array of strings, each specifying a resource name and
an access setting. Access is either "read" or "write". If you don't specify a resource,
access to all resources is assumed. If you don't specify the access, read and write
access are assumed.

The syntax is as follows:

`"scopes": [resource:scope, ...]`

where `resource` is optional.

**Examples**

`"scopes": ["read"]`

`"scopes": ["tickets:read"]`

To give read and write access to a resource, specify both scopes:

`"scopes": ["users:read", "users:write"]`

To give write access only to one resource and read access to everything
else:

`"scopes": ["organizations:write", "read"]`

**Note**: The endpoint returns an access token even if you specify an
invalid scope. Any request you make with the token will return
a "Forbidden" error.

**Available scopes**

* `read` - gives access to GET endpoints. Includes
permission to sideload related resources
* `write` - gives access to POST, PUT, and DELETE endpoints
* `impersonate` - allows Zendesk Support admins to make requests on behalf of
end users. See [Making API requests on behalf of end users](/documentation/ticketing/using-the-zendesk-api/making-api-requests-on-behalf-of-end-users/)

**Resources that can be scoped**

* tickets
* users
* auditlogs (read only)
* organizations
* hc
* apps
* triggers
* automations
* targets
* webhooks
* macros
* requests
* satisfaction_ratings
* dynamic_content
* any_channel (write only)
* web_widget (write only)


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.o_auth_tokens.create_o_auth_token(client_id=223443, global_client_id=334556, all=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `client_id`                                                                 | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | The id of the OAuth client                                                  | 223443                                                                      |
| `global_client_id`                                                          | *Optional[int]*                                                             | :heavy_minus_sign:                                                          | The id of the global OAuth client                                           | 334556                                                                      |
| `all`                                                                       | *Optional[bool]*                                                            | :heavy_minus_sign:                                                          | A boolean that returns all OAuth tokens in the account. Requires admin role | true                                                                        |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |                                                                             |

### Response

**[models.OAuthTokenResponse](../../models/oauthtokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_token

Returns the properties of the specified token. For security reasons, only the first 10 characters of the access token are included.

In the first endpoint, `id` is a token id, not the full token.

In the second endpoint, include an `Authorization: Bearer` header with the full token to get its associated properties. Example:

```sh
curl https://{subdomain}.zendesk.com/api/v2/oauth/tokens/current.json \
  -H 'Authorization: Bearer ${authToken}' \
  -v -u {email_address}/token:{api_token}
```

#### Allowed for

* Admins, Agents, End Users


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.o_auth_tokens.show_token(oauth_token_id=223443)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `oauth_token_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the OAuth token                                           | 223443                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OAuthTokenResponse](../../models/oauthtokenresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## revoke_o_auth_token

#### Allowed for
 * Admins, Agents, End Users


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.o_auth_tokens.revoke_o_auth_token(oauth_token_id=223443)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `oauth_token_id`                                                    | *int*                                                               | :heavy_check_mark:                                                  | The ID of the OAuth token                                           | 223443                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |