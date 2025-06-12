# Tags
(*tags*)

## Overview

### Available Operations

* [autocomplete_tags](#autocomplete_tags) - Search Tags
* [list_tags](#list_tags) - List Tags
* [count_tags](#count_tags) - Count Tags
* [list_ticket_tags](#list_ticket_tags) - List Ticket Tags
* [set_ticket_tags](#set_ticket_tags) - Set Ticket Tags
* [add_ticket_tags](#add_ticket_tags) - Add Tags
* [remove_ticket_tags](#remove_ticket_tags) - Remove Ticket Tags
* [list_organization_tags](#list_organization_tags) - List Organization Tags
* [set_organization_tags](#set_organization_tags) - Set Organization Tags
* [add_organization_tags](#add_organization_tags) - Add Organization Tags
* [remove_organization_tags](#remove_organization_tags) - Remove Organization Tags
* [list_user_tags](#list_user_tags) - List User Tags
* [set_user_tags](#set_user_tags) - Set User Tags
* [add_user_tags](#add_user_tags) - Add User Tags
* [remove_user_tags](#remove_user_tags) - Remove User Tags

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

    res = z_client.tags.list_tags(page_size=100)

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

**[models.ListTagsResponse](../../models/listtagsresponse.md)**

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

## list_ticket_tags

Lists all tags associated with a specific ticket.

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

    res = z_client.tags.list_ticket_tags(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                | 123456                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## set_ticket_tags

Replaces all existing tags on a ticket with the provided tags.

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

    res = z_client.tags.set_ticket_tags(ticket_id=123456, tags=[
        "customer",
        "vip",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                | 123456                                                              |
| `tags`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | An array of tag strings to add or set                               | [<br/>"customer",<br/>"vip"<br/>]                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## add_ticket_tags

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
from zendesk.utils import parse_datetime


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.tags.add_ticket_tags(ticket_id=123456, tags=[
        "customer",
        "vip",
    ], updated_stamp=parse_datetime("2019-09-12T21:45:16Z"), safe_update=models.SafeUpdate.TRUE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        | Example                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `ticket_id`                                                                                                        | *int*                                                                                                              | :heavy_check_mark:                                                                                                 | The ID of the ticket                                                                                               | 123456                                                                                                             |
| `tags`                                                                                                             | List[*str*]                                                                                                        | :heavy_check_mark:                                                                                                 | An array of tag strings to add or set                                                                              | [<br/>"customer",<br/>"vip"<br/>]                                                                                  |
| `updated_stamp`                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                               | :heavy_minus_sign:                                                                                                 | The ticket's latest updated_at timestamp for safe updates.<br/>Must match the current timestamp to prevent collision.<br/> | 2019-09-12T21:45:16Z                                                                                               |
| `safe_update`                                                                                                      | [Optional[models.SafeUpdate]](../../models/safeupdate.md)                                                          | :heavy_minus_sign:                                                                                                 | Enable safe update mode to prevent collisions                                                                      | true                                                                                                               |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |                                                                                                                    |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404, 409         | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## remove_ticket_tags

Removes specified tags from a ticket. You can also delete tags from multiple tickets 
with the Update Many Tickets endpoint.

This endpoint supports safe updates. See the PUT endpoint documentation for details.

#### Allowed For
* Agents


### Example Usage

```python
from zendesk import Zendesk, models
from zendesk.utils import parse_datetime


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.tags.remove_ticket_tags(ticket_id=123456, tags=[
        "customer",
        "vip",
    ], updated_stamp=parse_datetime("2019-09-12T21:45:16Z"), safe_update=models.SafeUpdate.TRUE)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        | Example                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `ticket_id`                                                                                                        | *int*                                                                                                              | :heavy_check_mark:                                                                                                 | The ID of the ticket                                                                                               | 123456                                                                                                             |
| `tags`                                                                                                             | List[*str*]                                                                                                        | :heavy_check_mark:                                                                                                 | An array of tag strings to add or set                                                                              | [<br/>"customer",<br/>"vip"<br/>]                                                                                  |
| `updated_stamp`                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                               | :heavy_minus_sign:                                                                                                 | The ticket's latest updated_at timestamp for safe updates.<br/>Must match the current timestamp to prevent collision.<br/> | 2019-09-12T21:45:16Z                                                                                               |
| `safe_update`                                                                                                      | [Optional[models.SafeUpdate]](../../models/safeupdate.md)                                                          | :heavy_minus_sign:                                                                                                 | Enable safe update mode to prevent collisions                                                                      | true                                                                                                               |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |                                                                                                                    |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404, 409         | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list_organization_tags

Lists all tags associated with a specific organization.

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

    res = z_client.tags.list_organization_tags(organization_id=16)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of an organization                                           | 16                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## set_organization_tags

Replaces all existing tags on an organization with the provided tags.

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

    res = z_client.tags.set_organization_tags(organization_id=16, tags=[
        "customer",
        "vip",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of an organization                                           | 16                                                                  |
| `tags`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | An array of tag strings to add or set                               | [<br/>"customer",<br/>"vip"<br/>]                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## add_organization_tags

Adds tags to an organization.

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

    res = z_client.tags.add_organization_tags(organization_id=16, tags=[
        "customer",
        "vip",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of an organization                                           | 16                                                                  |
| `tags`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | An array of tag strings to add or set                               | [<br/>"customer",<br/>"vip"<br/>]                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## remove_organization_tags

Removes specified tags from an organization.

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

    z_client.tags.remove_organization_tags(organization_id=16, tags=[
        "customer",
        "vip",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of an organization                                           | 16                                                                  |
| `tags`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | An array of tag strings to add or set                               | [<br/>"customer",<br/>"vip"<br/>]                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## list_user_tags

Lists all tags associated with a specific user.

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

    res = z_client.tags.list_user_tags(user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## set_user_tags

Replaces all existing tags on a user with the provided tags.

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

    res = z_client.tags.set_user_tags(user_id=35436, tags=[
        "customer",
        "vip",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `tags`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | An array of tag strings to add or set                               | [<br/>"customer",<br/>"vip"<br/>]                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## add_user_tags

Adds tags to a user.

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

    res = z_client.tags.add_user_tags(user_id=35436, tags=[
        "customer",
        "vip",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `tags`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | An array of tag strings to add or set                               | [<br/>"customer",<br/>"vip"<br/>]                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TagsResponse](../../models/tagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## remove_user_tags

Removes specified tags from a user.

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

    z_client.tags.remove_user_tags(user_id=35436, tags=[
        "customer",
        "vip",
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  | 35436                                                               |
| `tags`                                                              | List[*str*]                                                         | :heavy_check_mark:                                                  | An array of tag strings to add or set                               | [<br/>"customer",<br/>"vip"<br/>]                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |