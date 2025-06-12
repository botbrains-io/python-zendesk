# TriggerCategories
(*trigger_categories*)

## Overview

### Available Operations

* [list_trigger_categories](#list_trigger_categories) - List Ticket Trigger Categories
* [create_trigger_category](#create_trigger_category) - Create Ticket Trigger Category
* [show_trigger_category_by_id](#show_trigger_category_by_id) - Show Ticket Trigger Category
* [update_trigger_category](#update_trigger_category) - Update Ticket Trigger Category
* [delete_trigger_category](#delete_trigger_category) - Delete Ticket Trigger Category
* [batch_operate_trigger_categories](#batch_operate_trigger_categories) - Create Batch Job for Ticket Trigger Categories

## list_trigger_categories

Returns all the ticket trigger categories in the account.

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

    res = z_client.trigger_categories.list_trigger_categories(page_size=100, page={
        "after": "eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9",
        "before": "eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9",
        "size": 50,
    })

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |                                                                                                                                                                                                                                                                                                                     |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |                                                                                                                                                                                                                                                                                                                     |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                     |
| `page`                                                                                                                                                                                                                                                                                                              | [Optional[models.Page]](../../models/page.md)                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Pagination parameters                                                                                                                                                                                                                                                                                               | {<br/>"after": "eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9",<br/>"before": "eyJvIjoiLXNjb3JlLGlkIiwidiI6ImFRSUFBQUFBQUFBQWFRMHBJUUVBQUFBQSJ9",<br/>"size": 50<br/>}                                                                                                                           |
| `sort`                                                                                                                                                                                                                                                                                                              | [Optional[models.ListTriggerCategoriesSort]](../../models/listtriggercategoriessort.md)                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Sort parameters                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                     |
| `include`                                                                                                                                                                                                                                                                                                           | [Optional[models.Include]](../../models/include.md)                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Allowed sideloads                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                     |

### Response

**[models.ListTriggerCategoriesResponse](../../models/listtriggercategoriesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Errors    | 400, 403         | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## create_trigger_category

Creates a ticket trigger category.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.trigger_categories.create_trigger_category(trigger_category={
        "name": "All Notification Triggers",
        "position": 0,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `trigger_category`                                                                                            | [Optional[models.CreateTriggerCategoryTriggerCategory]](../../models/createtriggercategorytriggercategory.md) | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.TriggerCategoryResponse](../../models/triggercategoryresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Errors    | 400, 403         | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## show_trigger_category_by_id

Returns the ticket trigger category with the specified ID.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.trigger_categories.show_trigger_category_by_id(trigger_category_id="10001")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_category_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The id of the ticket trigger category to retrieve                   | 10001                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TriggerCategoryResponse](../../models/triggercategoryresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Errors    | 404              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update_trigger_category

Updates the ticket trigger category with the specified ID.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.trigger_categories.update_trigger_category(trigger_category_id="10001", trigger_category={
        "name": "All Notification Triggers Updated",
        "position": 10,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       | Example                                                                           |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `trigger_category_id`                                                             | *str*                                                                             | :heavy_check_mark:                                                                | The id of the ticket trigger category to update                                   | 10001                                                                             |
| `trigger_category`                                                                | [Optional[models.TriggerCategoryRequest]](../../models/triggercategoryrequest.md) | :heavy_minus_sign:                                                                | N/A                                                                               |                                                                                   |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |                                                                                   |

### Response

**[models.TriggerCategoryResponse](../../models/triggercategoryresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Errors    | 400, 404         | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete_trigger_category

Deletes the ticket trigger category with the specified ID.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.trigger_categories.delete_trigger_category(trigger_category_id="10001")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `trigger_category_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The id of the ticket trigger category to delete                     | 10001                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Errors    | 400, 404         | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## batch_operate_trigger_categories

Creates a job that performs a batch operation for the given ticket trigger categories.

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.trigger_categories.batch_operate_trigger_categories(job={
        "action": models.BatchJobRequestAction.PATCH,
        "items": {
            "trigger_categories": [
                {
                    "id": "10001",
                    "position": 0,
                },
                {
                    "id": "10002",
                    "position": 1,
                },
            ],
            "triggers": [
                {
                    "active": False,
                    "category_id": "10001",
                    "id": "10011",
                    "position": 10,
                },
                {
                    "active": True,
                    "category_id": "10002",
                    "id": "10012",
                    "position": 1,
                },
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `job`                                                                     | [Optional[models.BatchJobRequestJob]](../../models/batchjobrequestjob.md) | :heavy_minus_sign:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.BatchJobResponse](../../models/batchjobresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.BatchJobResponseError | 400                          | application/json             |
| errors.APIError              | 4XX, 5XX                     | \*/\*                        |