# EmailNotifications
(*email_notifications*)

## Overview

### Available Operations

* [list_email_notifications](#list_email_notifications) - List Email Notifications
* [show_email_notification](#show_email_notification) - Show Email Notification
* [show_many_email_notifications](#show_many_email_notifications) - Show Many Email Notifications

## list_email_notifications

#### Allowed For

* Agents

#### Filters

* By notification: `api/v2/email_notifications.json?filter[notification_id]=7824075373693`
* By comment: `api/v2/email_notifications.json?filter[comment_id]=7824075373565`
* By ticket: `api/v2/email_notifications.json?filter[ticket_id]=623`

#### Pagination

By default, a maximum of 100 email notifications are included per page. Use cursor-based pagination parameters (`page[after]` and `page[before]`) to navigate the records (can't be used together in the same request). See [Pagination](/api-reference/introduction/pagination/) for more details.

* Limit items per-page: `api/v2/email_notifications.json?page[size]=25`
* Retrieve next page: `api/v2/email_notifications.json?page[size]=25&page[after]=xxx`
* Retrieve previous page: `api/v2/email_notifications.json?page[size]=25&page[before]=yyy`

The values `xxx` and `yyy` are placeholder values that represent cursors.

#### Sorting

By default, email notifications are sorted by creation time (newest first). The query parameter is not supported for this endpoint.

* By creation time (oldest first): `api/v2/email_notifications.json?sort=created_at`
* By creation time (newest first): `api/v2/email_notifications.json?sort=-created_at`
* By modification time (recently updated first): `api/v2/email_notifications.json?sort=updated_at`
* By modification time (recently updated last): `api/v2/email_notifications.json?sort=-updated_at`


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.email_notifications.list_email_notifications(sort="updated_at", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_`                                                                                                                                                                                                                                                                                                           | [Optional[models.EmailNotificationsFilter]](../../models/emailnotificationsfilter.md)                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filters the email notifications by ticket, comment, or notification id.<br/>                                                                                                                                                                                                                                        |
| `per_page`                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The number of records to return per page                                                                                                                                                                                                                                                                            |
| `sort`                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The field to sort the list.  Possible values are "created_at", "updated_at" (ascending order) or "-created_at", "-updated_at" (descending order)                                                                                                                                                                    |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListEmailNotificationsResponse](../../models/listemailnotificationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_email_notification

Shows details on an email notification. You can get the value of the `notification_id` parameter by listing the ticket's outbound emails.

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

    res = z_client.email_notifications.show_email_notification(notification_id=7824075373693)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `notification_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The id of the email notification                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EmailNotificationResponse](../../models/emailnotificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_many_email_notifications

Shows details of many email notifications. Allows you to query by providing a list of notifications, comments, or tickets IDs.

#### Allowed For

* Agents

#### Filters

* By notification: `?ids=8433702508541,8433348111869`
* By comment: `?comment_ids=8433348111741,8433544226045,8433702508413`
* By ticket: `?ticket_ids=730,723`


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.email_notifications.show_many_email_notifications(ids="8433702508541,8433348111869", comment_ids="8433348111741,8433544226045,8433702508413", ticket_ids="35436,35437")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of notification ids                            |
| `comment_ids`                                                       | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of comment ids                                 |
| `ticket_ids`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of ticket ids                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EmailNotificationResponse](../../models/emailnotificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |