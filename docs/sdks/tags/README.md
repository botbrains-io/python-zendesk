# Tags
(*tags*)

## Overview

### Available Operations

* [autocomplete_tags](#autocomplete_tags) - Search Tags
* [list_tags](#list_tags) - List Tags
* [count_tags](#count_tags) - Count Tags
* [list_resource_tags](#list_resource_tags) - List Resource Tags
* [set_tags_ticket](#set_tags_ticket) - Set Tags
* [put_tags_ticket](#put_tags_ticket) - Add Tags
* [delete_tags_ticket](#delete_tags_ticket) - Remove Tags

## autocomplete_tags

Returns an array of registered and recent tag names that start with the characters specified in the `name` query parameter. You must specify at least 2 characters.

#### Pagination

* Offset pagination only

See [Using Offset Pagination](/api-reference/ticketing/introduction/#using-offset-pagination).


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

    res = z_client.tags.autocomplete_tags(name="att")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A substring of a tag to search for                                  | att                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsByObjectIDResponse](../../models/tagsbyobjectidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_tags

Lists up to the 20,000 most popular tags in the last 60 days, in decreasing popularity.

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

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

    res = z_client.tags.list_tags()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_tags

Returns an approximate count of tags. If the count exceeds 100,000, it
is updated every 24 hours.

The `refreshed_at` property of the `count` object is a timestamp that indicates when
the count was last updated.

**Note**: When the count exceeds 100,000, the `refreshed_at` property in the `count` object may
occasionally be null. This indicates that the count is being
updated in the background and the `value` property in the `count` object is limited to
100,000 until the update is complete.

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

    res = z_client.tags.count_tags()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TagCountResponse](../../models/tagcountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_resource_tags

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

    res = z_client.tags.list_resource_tags(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                | 123456                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsByObjectIDResponse](../../models/tagsbyobjectidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## set_tags_ticket

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

    res = z_client.tags.set_tags_ticket(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                | 123456                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsByObjectIDResponse](../../models/tagsbyobjectidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## put_tags_ticket

You can also add tags to multiple tickets with the [Update Many
Tickets](/api-reference/ticketing/tickets/tickets/#update-many-tickets) endpoint.

#### Safe Update

If the same ticket is updated by multiple API requests at
the same time, some tags could be lost because of ticket
update collisions. Include `updated_stamp` and `safe_update`
properties in the request body to make a safe update.

For `updated_stamp`, retrieve and specify the ticket's
latest `updated_at` timestamp. The tag update only occurs
if the `updated_stamp` timestamp matches the ticket's
actual `updated_at` timestamp at the time of the request.
If the timestamps don't match (in other words, if the
ticket was updated since you retrieved the ticket's
last `updated_at` timestamp), the request returns a
409 Conflict error.

#### Example

```js
{
  "tags": ["customer"],
  "updated_stamp":"2019-09-12T21:45:16Z",
  "safe_update":"true"
}
```

For details, see [Protecting against ticket update collisions](/api-reference/ticketing/tickets/tickets/#protecting-against-ticket-update-collisions).

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

    res = z_client.tags.put_tags_ticket(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                | 123456                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsByObjectIDResponse](../../models/tagsbyobjectidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_tags_ticket

You can also delete tags from multiple tickets with the
[Update Many Tickets](/api-reference/ticketing/tickets/tickets/#update-many-tickets) endpoint.

This endpoint supports safe updates. See [Safe Update](/api-reference/ticketing/ticket-management/tags/#safe-update).

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

    z_client.tags.delete_tags_ticket(ticket_id=123456)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                | 123456                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |