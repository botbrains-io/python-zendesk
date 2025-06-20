# SupportAddresses
(*support_addresses*)

## Overview

### Available Operations

* [list_support_addresses](#list_support_addresses) - List Support Addresses
* [create_support_address](#create_support_address) - Create Support Address
* [show_support_address](#show_support_address) - Show Support Address
* [update_support_address](#update_support_address) - Update Support Address
* [delete_recipient_address](#delete_recipient_address) - Delete Support Address
* [verify_support_address_forwarding](#verify_support_address_forwarding) - Verify Support Address Forwarding

## list_support_addresses

Lists all the support addresses for the account.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Admins
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

    res = z_client.support_addresses.list_support_addresses(page_size=100)

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

**[models.ListSupportAddressesResponse](../../models/listsupportaddressesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_support_address

Adds a Zendesk or external support address to your account.

To add a Zendesk address, use the following syntax: `{local-part}@{accountname}.zendesk.com`.
Example: 'sales-team@example.zendesk.com'. The [local-part](https://en.wikipedia.org/wiki/Email_address#Local-part) can be anything you like.

To add an external email address such as help@omniwearshop.com, the email must already exist and you must set up forwarding on your email server. The exact steps depend on your mail server. See [Forwarding incoming email to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203663266). After setting up forwarding, run the [Verify Support Address Forwarding](#verify-support-address-forwarding) endpoint. The address won't work in Zendesk Support until it's been verified.

#### Allowed For

* Admins
* Agents with permission to manage channels and extensions. See the system permissions in [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd) in the Support Help Center


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.support_addresses.create_support_address()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SupportAddressResponse](../../models/supportaddressresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_support_address

#### Allowed For

* Admins
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

    res = z_client.support_addresses.show_support_address(support_address_id=33)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `support_address_id`                                                | *int*                                                               | :heavy_check_mark:                                                  | The ID of the support address                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SupportAddressResponse](../../models/supportaddressresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_support_address

Updates an existing support address for your account.

You can't use this endpoint to update a support address's `email` property.
Instead, you can create a new address using the [Create Support
Address](#create-support-address) endpoint.

#### Allowed For

* Admins
* Agents with permission to manage channels and extensions. See the system permissions in [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd) in the Support Help Center


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.support_addresses.update_support_address(support_address_id=33)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `support_address_id`                                                | *int*                                                               | :heavy_check_mark:                                                  | The ID of the support address                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SupportAddressResponse](../../models/supportaddressresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_recipient_address

Deletes a support address.

#### Allowed For

* Admins
* Agents with permission to manage channels and extensions. See the system permissions in [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd) in the Support Help Center


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.support_addresses.delete_recipient_address(support_address_id=33)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `support_address_id`                                                | *int*                                                               | :heavy_check_mark:                                                  | The ID of the support address                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## verify_support_address_forwarding

Sends a test email to the specified support address to verify that email forwarding for the address works. An external support address won't work in Zendesk Support until it's verified.

**Note**: You don't need to verify Zendesk system support addresses.

The endpoint takes the following body: `{"type": "forwarding"}`. The value of the `type` property defaults to "forwarding" if none is specified, but the values "spf" and "dns" are also accepted.

Use this endpoint after [adding](#create-support-address) an external support address to Zendesk Support and setting up forwarding on your email server. See [Forwarding incoming email to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/203663266).

The endpoint doesn't return the results of the test. Instead, use the [Show Support Address](#show-support-address) endpoint to check that the `forwarding_status` property is "verified".

Other verification checks can also be performed using this API. These include SPF checks and DNS checks.

When calling the endpoint with `type` set to "spf", it will queries the DNS records to check that the SPF records for Zendesk are present for outbound emails.

When calling the endpoint with `type` set to "dns", it runs checks on your CNAME records to make sure they are set up properly in your DNS.

#### Allowed For

* Admins
* Agents with permission to manage channels and extensions. See the system permissions in [Creating custom roles and assigning agents (Enterprise)](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents-Enterprise-#topic_cxn_hig_bd) in the Support Help Center


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.support_addresses.verify_support_address_forwarding(support_address_id=33)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `support_address_id`                                                | *int*                                                               | :heavy_check_mark:                                                  | The ID of the support address                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |