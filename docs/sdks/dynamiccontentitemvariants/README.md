# DynamicContentItemVariants
(*dynamic_content_item_variants*)

## Overview

### Available Operations

* [dynamic_content_list_variants](#dynamic_content_list_variants) - List Variants
* [create_dynamic_content_variant](#create_dynamic_content_variant) - Create Variant
* [show_dynamic_content_variant](#show_dynamic_content_variant) - Show Variant
* [update_dynamic_content_variant](#update_dynamic_content_variant) - Update Variant
* [delete_dynamic_content_variant](#delete_dynamic_content_variant) - Delete Variant
* [create_many_dynamic_content_variants](#create_many_dynamic_content_variants) - Create Many Variants
* [update_many_dynamic_content_variants](#update_many_dynamic_content_variants) - Update Many Variants

## dynamic_content_list_variants

Returns all the variants of the specified dynamic content item.

#### Allowed For

* Admins
* Agents who have permission to manage dynamic content

#### Pagination

* Cursor pagination

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

    res = z_client.dynamic_content_item_variants.dynamic_content_list_variants(dynamic_content_item_id=47, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dynamic_content_item_id`                                                                                                                                                                                                                                                                                           | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The ID of the dynamic content item                                                                                                                                                                                                                                                                                  | 47                                                                                                                                                                                                                                                                                                                  |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |                                                                                                                                                                                                                                                                                                                     |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |                                                                                                                                                                                                                                                                                                                     |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                     |

### Response

**[models.DynamicContentListVariantsResponse](../../models/dynamiccontentlistvariantsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_dynamic_content_variant

You can only create one variant for each locale id. If a locale variant already exists, the request is rejected.

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

    res = z_client.dynamic_content_item_variants.create_dynamic_content_variant(dynamic_content_item_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DynamicContentVariantResponse](../../models/dynamiccontentvariantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_dynamic_content_variant

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

    res = z_client.dynamic_content_item_variants.show_dynamic_content_variant(dynamic_content_item_id=47, dynammic_content_variant_id=23)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `dynammic_content_variant_id`                                       | *int*                                                               | :heavy_check_mark:                                                  | The ID of the variant                                               | 23                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DynamicContentVariantResponse](../../models/dynamiccontentvariantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_dynamic_content_variant

Updates the specified variant. You don't need to include all the properties. If you just want to update content, for example, then include just that.

You can't switch the active state of the default variant of an item. Similarly, you can't switch the default to false if the variant is the default. You must make another variant default instead.

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

    res = z_client.dynamic_content_item_variants.update_dynamic_content_variant(dynamic_content_item_id=47, dynammic_content_variant_id=23)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `dynammic_content_variant_id`                                       | *int*                                                               | :heavy_check_mark:                                                  | The ID of the variant                                               | 23                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DynamicContentVariantResponse](../../models/dynamiccontentvariantresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_dynamic_content_variant

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

    z_client.dynamic_content_item_variants.delete_dynamic_content_variant(dynamic_content_item_id=47, dynammic_content_variant_id=23)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `dynammic_content_variant_id`                                       | *int*                                                               | :heavy_check_mark:                                                  | The ID of the variant                                               | 23                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_many_dynamic_content_variants

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

    res = z_client.dynamic_content_item_variants.create_many_dynamic_content_variants(dynamic_content_item_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DynamicContentVariantsResponse](../../models/dynamiccontentvariantsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many_dynamic_content_variants

Updates one or more variants. See [Update Variant](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#update-variant).

You must specify the variants by id in the body. To get the variant ids, see [List Variants](/api-reference/ticketing/ticket-management/dynamic_content_item_variants/#list-variants).

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

    res = z_client.dynamic_content_item_variants.update_many_dynamic_content_variants(dynamic_content_item_id=47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dynamic_content_item_id`                                           | *int*                                                               | :heavy_check_mark:                                                  | The ID of the dynamic content item                                  | 47                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DynamicContentVariantsResponse](../../models/dynamiccontentvariantsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |