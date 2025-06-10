# DynamicContent
(*dynamic_content*)

## Overview

### Available Operations

* [list_dynamic_contents](#list_dynamic_contents) - List Items
* [create_dynamic_content](#create_dynamic_content) - Create Item
* [show_dynamic_content_item](#show_dynamic_content_item) - Show Item
* [update_dynamic_content_item](#update_dynamic_content_item) - Update Item
* [delete_dynamic_content_item](#delete_dynamic_content_item) - Delete Item
* [show_many_dynamic_contents](#show_many_dynamic_contents) - Show Many Items

## list_dynamic_contents

Returns a list of all dynamic content items for your account if accessed as an admin or agents who have permission to manage dynamic content.

#### Allowed For

* Admins, Agents

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.dynamic_content.list_dynamic_contents()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DynamicContentsResponse](../../models/dynamiccontentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_dynamic_content

Create a new content item, with one or more variants in the item's `variants` array. See [Specifying item variants](#specifying-item-variants).

The `default_locale_id` and variant `locale_id` values must be one of the locales the account has active. You can get the list with the [List Locales](/api-reference/ticketing/account-configuration/locales/#list-locales) endpoint.

#### Allowed For

* Admins, Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.dynamic_content.create_dynamic_content()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DynamicContentResponse](../../models/dynamiccontentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_dynamic_content_item

#### Allowed For

* Admins, Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.dynamic_content.show_dynamic_content_item(dynamic_content_item_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DynamicContentResponse](../../models/dynamiccontentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_dynamic_content_item

The only attribute you can change is the name.

To add a variant to the item, or to update or delete the variants of the item, use the [Item Variants API](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#update-many-variants).

#### Allowed For

* Admins, Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.dynamic_content.update_dynamic_content_item(dynamic_content_item_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DynamicContentResponse](../../models/dynamiccontentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_dynamic_content_item

#### Allowed For

* Admins, Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.dynamic_content.delete_dynamic_content_item(dynamic_content_item_id=47)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_many_dynamic_contents

#### Stability

* Development

#### Allowed For

* Admins, Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.dynamic_content.show_many_dynamic_contents(identifiers="item1,item2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifiers`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Identifiers for the dynamic contents                                | item1,item2                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DynamicContentsResponse](../../models/dynamiccontentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |