# GrantTypeTokens
(*grant_type_tokens*)

## Overview

### Available Operations

* [create_token_for_grant_type](#create_token_for_grant_type) - Create Token for Grant Type

## create_token_for_grant_type

Returns an OAuth access token in exchange for an [authorization code](https://support.zendesk.com/hc/en-us/articles/203663836#topic_pvr_ncl_1l) valid for 120 seconds.

Using a Zendesk username and password to gain an OAuth access token (password grant type flow) has been deprecated and is highly discouraged.

An access token can be revoked. Use the [OAuth Tokens API](/api-reference/ticketing/oauth/oauth_tokens) to list, show, or revoke tokens.

The refresh token grant type allows for refreshing an access token that has either expired or is about to expire. See [Oauth Tokens for Grant Types](/api-reference/ticketing/oauth/grant_type_tokens/).

#### Request parameters

The POST request takes the following parameters, which must be formatted as JSON:

| Name          | Description
| ------------- | --------------------------------------------------
| grant_type    | "authorization_code" or "refresh_token"
| code          | Authorization grant flow only. The authorization code you received from Zendesk after the user granted access. See [Handle the user's authorization decision](https://support.zendesk.com/hc/en-us/articles/203663836#topic_tfc_cdl_1l) in Help Center
| client_id     | The **Unique Identifier** specified in an OAuth client in the Support admin interface (**Admin** > **Channels** > **API** > **OAuth Clients**). See [Registering your application with Zendesk](https://support.zendesk.com/hc/en-us/articles/203663836#topic_s21_lfs_qk)
| client_secret | The **Secret** specified in an OAuth client in the Support admin interface (**Admin** > **Channels** > **API** > **OAuth Clients**). See [Registering your application with Zendesk](https://support.zendesk.com/hc/en-us/articles/203663836#topic_s21_lfs_qk)
| redirect_uri  | Authorization grant flow only. The redirect URL you specified when you sent the user to the Zendesk authorization page. For ID purposes only. See [Send the user to the Zendesk authorization page](https://support.zendesk.com/hc/en-us/articles/203663836#topic_qk3_d3s_qk)
| scope         | Valid scope for this token. A string of space-separated values. See [Scope](#scope) below
| expires_in    | Number of seconds the access token is valid. Must be more than 300 seconds (5 minutes) and less than 172,800 seconds (2 days), or less than `refresh_token_expires_in`, whichever is the smallest. Defaults to null
| refresh_token_expires_in | Number of seconds the refresh token is valid. Must be more than 604,800 seconds (7 days) or `expires_in` (if given), and less than 7,776,000 seconds (90 days). Defaults to 2,592,000 seconds (30 days)
| refresh_token | The refresh token

**Example Node.js authorization code grant flow**

```javascript
const tokenResponse = await axios.post(
  `https://${ZENDESK_SUBDOMAIN}.zendesk.com/oauth/tokens`,
  {
    grant_type: "authorization_code",
    code: req.query.code,
    client_id: ZENDESK_CLIENT_ID,
    redirect_uri: REDIRECT_URI_PKCE,
    scope: "read write",
    code_verifier: CODE_VERIFIER,
    expires_in: 86400,
    refresh_token_expires_in: 604800,
  },
  { headers: { "Content-Type": "application/json" } }
);
```

**Example Node.js refresh token grant flow**

```javascript
const tokenResponse = await axios.post(
  `https://${ZENDESK_SUBDOMAIN}.zendesk.com/oauth/tokens`,
  {
    grant_type: "refresh_token",
    refresh_token: refresh_token,
    client_id: ZENDESK_CLIENT_ID,
    client_secret: ZENDESK_CLIENT_SECRET,
    scopes: "tickets:write",
    expires_in: 86400,
    refresh_token_expires_in: 604800,
  },
  { headers: { "Content-Type": "application/json" } }
);
```

#### Scope

You must specify a scope to control the app's access to Zendesk resources. The "read" scope gives access to GET endpoints. It includes permission to sideload related resources. The "write" scope gives access to POST, PUT, and DELETE endpoints for creating, updating, and deleting resources.

**Note**: Don't confuse the **scope** parameter (singular) with the **scopes** parameter (plural) for non-grant-type tokens described in [OAuth Tokens](/api-reference/ticketing/oauth/oauth_tokens).

The "impersonate" scope allows a Zendesk admin to make requests on behalf of end users. See [Making API requests on behalf of end users](/documentation/ticketing/using-the-zendesk-api/making-api-requests-on-behalf-of-end-users/).

For example, the following parameter gives read access to all resources:

`"scope": "read"`

The following parameter gives read and write access to all resources:

`"scope": "read write"`

You can fine-tune the scope of the following resources:

- tickets
- users
- auditlogs (read only)
- organizations
- hc
- apps
- triggers
- automations
- targets
- webhooks

The syntax is as follows:

`"scope": "resource:scope"`

For example, the following parameter restricts the scope to only reading tickets:

`"scope": "tickets:read"`

To give read and write access to a resource, specify both scopes:

`"scope": "users:read users:write"`

To give write access only to one resource, such as organizations, and read access to everything else:

`"scope": "organizations:write read"`

**Note**: The endpoint returns an access token even if you specify an invalid scope such as `"scope": ["read", "write"]` (no parentheses). Any request you make with the token will return a "Forbidden" error.

#### Tokens for Implicit Grant Type

The implicit grant flow has been deprecated. It's considered insecure and its use is highly discouraged.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.grant_type_tokens.create_token_for_grant_type()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OAuthTokenForGrantTypesObject](../../models/oauthtokenforgranttypesobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |