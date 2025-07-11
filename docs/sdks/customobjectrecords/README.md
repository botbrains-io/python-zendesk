# CustomObjectRecords
(*custom_object_records*)

## Overview

### Available Operations

* [custom_object_record_bulk_jobs](#custom_object_record_bulk_jobs) - Custom Object Record Bulk Jobs
* [list_custom_object_records](#list_custom_object_records) - List Custom Object Records
* [create_custom_object_record](#create_custom_object_record) - Create Custom Object Record
* [upsert_custom_object_record_by_external_id_or_name](#upsert_custom_object_record_by_external_id_or_name) - Set Custom Object Record by External Id Or Name
* [delete_custom_object_record_by_external_id_or_name](#delete_custom_object_record_by_external_id_or_name) - Delete Custom Object Record by External Id Or Name
* [show_custom_object_record](#show_custom_object_record) - Show Custom Object Record
* [update_custom_object_record](#update_custom_object_record) - Update Custom Object Record
* [delete_custom_object_record](#delete_custom_object_record) - Delete Custom Object Record
* [autocomplete_custom_object_record_search](#autocomplete_custom_object_record_search) - Autocomplete Custom Object Record Search
* [count_custom_object_records](#count_custom_object_records) - Count Custom Object Records
* [search_custom_object_records](#search_custom_object_records) - Search Custom Object Records
* [filtered_search_custom_object_records](#filtered_search_custom_object_records) - Filtered Search of Custom Object Records
* [custom_object_records_limit](#custom_object_records_limit) - Custom Object Records Limit

## custom_object_record_bulk_jobs

Queues a background job to perform bulk actions on up to 100 custom object records per single request.
Takes a `job` object with two nested fields:
* `action`, one of:
    * `"create"`
    * `"delete"`
    * `"delete_by_external_id"`
    * `"create_or_update_by_external_id"`
    * `"create_or_update_by_name"`
    * `"update"`
* `items`
    * For a `"create"` action, an array of JSON objects representing the custom object records being created
    * For a `"delete"` action, an array of strings representing Zendesk record ids
    * For a `"delete_by_external_id"` action, an array of strings representing external ids
    * For a `"create_or_update_by_external_id"` action, an array of JSON objects representing the custom object records being created or updated by external id
    * For a `"create_or_update_by_name"` action, an array of JSON objects representing the custom object records being created or updated by name. The `is_unique` property on the custom object's name field must be enabled.
    * For an `"update"` action, an array of JSON objects representing the custom object records being updated

Note: If autonumbering is selected for the custom object's name field, record names aren't allowed in the request body because they are generated automatically. If uniqueness is enabled, the record names must be unique.

#### Allowed For
* Agents

#### Response ###
This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_records.custom_object_record_bulk_jobs(custom_object_key="car", job={
        "action": "create",
        "items": [
            {
                "custom_object_fields": {
                    "color": "Red",
                    "year": 2020,
                },
            },
            {
                "custom_object_fields": {
                    "color": "Blue",
                    "external_id": "ddd444",
                    "year": 2012,
                },
            },
            {
                "custom_object_fields": {
                    "color": "Silver",
                    "external_id": "ddd445",
                    "year": 2017,
                },
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                                                 | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | The key of a custom object                                                                                          |
| `job`                                                                                                               | [Optional[models.CustomObjectRecordsBulkCreateRequestJob]](../../models/customobjectrecordsbulkcreaterequestjob.md) | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.CustomObjectRecordsJobsResponse](../../models/customobjectrecordsjobsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_custom_object_records

Lists all undeleted custom object records for the specified object

 #### Pagination

* [Cursor pagination](/api-reference/introduction/pagination/#cursor-pagination) only.
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

    res = z_client.custom_object_records.list_custom_object_records(custom_object_key="car", filter_ids="id_1,id_2,id_3", filter_external_ids="ex_id_1,ex_id_2,ex_id_3", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The key of a custom object                                                                                                                                                                                                                                                                                          |
| `filter_ids`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Optional comma-separated list of ids to filter records by. If one or more ids are specified, only matching records are returned. The ids must be unique and are case sensitive.                                                                                                                                     |
| `filter_external_ids`                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Optional comma-separated list of external ids to filter records by. If one or more ids are specified, only matching records are returned. The ids must be unique and are case sensitive.                                                                                                                            |
| `sort`                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of `id`, `updated_at`, `-id`, or `-updated_at`. The `-` denotes the sort will be descending.<br/>                                                                                                                                                                                                               |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListCustomObjectRecordsResponse](../../models/listcustomobjectrecordsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_custom_object_record

Creates a custom object record according to all the properties described by a custom object definition. If `autoincrement_enabled` is true, record names aren't allowed in the request body because they are generated automatically. If `is_unique` is true, record names must be unique.
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

    res = z_client.custom_object_records.create_custom_object_record(custom_object_key="car", custom_object_record={
        "custom_object_fields": {
            "make": "Tesla",
            "model": "Y",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `custom_object_key`                                                                 | *str*                                                                               | :heavy_check_mark:                                                                  | The key of a custom object                                                          |
| `custom_object_record`                                                              | [Optional[models.CustomObjectRecordInput]](../../models/customobjectrecordinput.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CustomObjectRecordResponse](../../models/customobjectrecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## upsert_custom_object_record_by_external_id_or_name

If a record exists for the given external id or name, updates it. Only the specified attributes are updated. Otherwise, creates a new record with the provided external id, name and other attributes. The `is_unqiue` property on the custom object's name field must be enabled in order to update or create by name. External id and name cannot be used together in the same request.
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

    res = z_client.custom_object_records.upsert_custom_object_record_by_external_id_or_name(custom_object_key="car", external_id="X90001", name="boat", custom_object_record={
        "custom_object_fields": {
            "make": "Oldsmobile",
            "model": "Cutlass Supreme",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `custom_object_key`                                                                 | *str*                                                                               | :heavy_check_mark:                                                                  | The key of a custom object                                                          |
| `external_id`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | The external id of a custom object record                                           |
| `name`                                                                              | *str*                                                                               | :heavy_check_mark:                                                                  | The name of a custom object record                                                  |
| `custom_object_record`                                                              | [Optional[models.CustomObjectRecordInput]](../../models/customobjectrecordinput.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CustomObjectRecordResponse](../../models/customobjectrecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_custom_object_record_by_external_id_or_name

Deletes a record with the specified external id or name. The `is_unique` property on the custom object's name field must be enabled in order to delete by name. External id and name cannot be used together in the same request.
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

    z_client.custom_object_records.delete_custom_object_record_by_external_id_or_name(custom_object_key="car", external_id="X90001", name="boat")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `external_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The external id of a custom object record                           |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The name of a custom object record                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_custom_object_record

Returns a custom record for a specific object using a provided id.
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

    res = z_client.custom_object_records.show_custom_object_record(custom_object_key="car", custom_object_record_id="01GCSJW391QVSC80GYDH7E93Q6")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `custom_object_record_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The id of a custom object record                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomObjectRecordResponse](../../models/customobjectrecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_custom_object_record

Updates an individual custom object record. The updating rules are as follows:
* Takes a `custom_object_record` object that specifies the properties to update
* The custom object fields should be nested inside a `custom_object_fields` object
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

    res = z_client.custom_object_records.update_custom_object_record(custom_object_key="car", custom_object_record_id="01GCSJW391QVSC80GYDH7E93Q6")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `custom_object_record_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The id of a custom object record                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomObjectRecordResponse](../../models/customobjectrecordresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_custom_object_record

Deletes a record with the specified id
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

    z_client.custom_object_records.delete_custom_object_record(custom_object_key="car", custom_object_record_id="01GCSJW391QVSC80GYDH7E93Q6")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `custom_object_record_id`                                           | *str*                                                               | :heavy_check_mark:                                                  | The id of a custom object record                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## autocomplete_custom_object_record_search

Retrieves an array of custom object records that have a field value that matches the value specified in the `name` parameter.

#### Pagination

* [Cursor pagination](/api-reference/introduction/pagination/#cursor-pagination) only.
* Returns the first 10,000 records sorted by relevancy with page limits.
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

    res = z_client.custom_object_records.autocomplete_custom_object_record_search(custom_object_key="car", page_size=100, requester_id=264817272, assignee_id=7334148660734, organization_id=5633330889598)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The key of a custom object                                                                                                                                                                                                                                                                                          |
| `name`                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Part of a name of the record you are searching for                                                                                                                                                                                                                                                                  |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `field_id`                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The id of the lookup field. If the field has a relationship filter, the filter is applied to the results. Must be used with `source` param.<br/>                                                                                                                                                                    |
| `source`                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of "zen:user", "zen:ticket", "zen:organization", or "zen:custom_object:CUSTOM_OBJECT_KEY". Represents the object `field_id` belongs to. Must be used with field_id param.<br/>                                                                                                                                  |
| `requester_id`                                                                                                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The id of the requester. For use with dynamic filters.<br/>                                                                                                                                                                                                                                                         |
| `assignee_id`                                                                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The id of the selected assignee. For use with dynamic filters.<br/>                                                                                                                                                                                                                                                 |
| `organization_id`                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The id of the organization the requester belongs to. For use with dynamic filters.<br/>                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.AutocompleteCustomObjectRecordSearchResponse](../../models/autocompletecustomobjectrecordsearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_custom_object_records

Returns a total count of records for a specific custom object as well as the time the count was refreshed.
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

    res = z_client.custom_object_records.count_custom_object_records(custom_object_key="car")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `custom_object_key`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The key of a custom object                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountCustomObjectRecordsResponse](../../models/countcustomobjectrecordsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_custom_object_records

Returns an array of custom object records that meet the search criteria

#### Pagination

* [Cursor pagination](/api-reference/introduction/pagination/#cursor-pagination) only.
* Returns the records sorted by relevancy with page limits. Without a `sort` parameter, only the first 10,000 records are returned. With a `sort` parameter, all records are returned.
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

    res = z_client.custom_object_records.search_custom_object_records(custom_object_key="car", page_size=100, query="jdoe")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The key of a custom object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `page_before`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `page_after`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | The query parameter is used to search text-based fields for records that match specific query terms.<br/>The query can be multiple words or numbers. Every record that matches the beginning of any word or number in the query string is returned.<br/><br/><br/><br/>Fuzzy search is supported for the following text-based field types: : Text fields, Multi Line Text fields, and RegExp fields.<br/><br/><br/><br/>For example, you might want to search for records related to Tesla vehicles: `query=Tesla`. In this example the API would return every record for the given custom object where any of the supported text fields contain the word 'Tesla'.<br/><br/><br/><br/>You can include multiple words or numbers in your search. For example: `query=Tesla Honda 2020`. This search phrase would be URL encoded as `query=Tesla%20Honda%202020` and return every record for the custom object for which any of the supported text fields contained 'Tesla', 'Honda', or '2020'.<br/> |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | One of `name`, `created_at`, `updated_at`, `-name`, `-created_at`, or `-updated_at`. The `-` denotes the sort will be descending. Defaults to sorting by relevance.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.SearchCustomObjectRecordsResponse](../../models/searchcustomobjectrecordsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## filtered_search_custom_object_records

Returns an array of custom object records that meet the search and filter criteria.

Filters can contain either an individual [comparison object](#comparison-object) or an array of [comparison objects](#comparison-object) within logical namespaces.

A filter is a JSON object that has the following properties:

| Name      | Type   | Required | Description
| --------- | ------ | -------- | -----------
| ATTRIBUTE | object | no       | A [comparison object](#comparison-object) specifying an attribute value condition to be met for records to match.<br/><br/>Examples are marked below.
| $and      | array  | no       | Array of conjunctive filter objects (logical AND)
| $or       | array  | no       | Array of conjunctive filter objects (logical OR)

##### Examples


```js
{
  "filter": {
    "custom_object_fields.field_key": { "$eq": "value" } // ATTRIBUTE
  }
}
```

```js
// $or
{
  "filter": {
    "$or": [
      { "custom_object_fields.field_key": { "$eq": "value" } }, // ATTRIBUTE
      { "external_id": { "$eq": "Record123" } } // ATTRIBUTE
    ]
  }
}
```

#### Comparison Object

A comparison object defines a condition a record must meet to be considered a match. The condition is based on an attribute value or object type.

A comparison object is a JSON object that has the following properties:

| Name      | Type          | Required | Description
| --------- | ------------- | -------- | -----------
| FIELD_KEY | string        | yes      | When filtering on a custom field, they must be namedspaced with `custom_object_fields.`. ex. `custom_object_fields.field_key`<br/><br/>When filtering on a standard field, no namespace is required. The following fields are considered standard: `created_at`, `updated_at`, `created_by_user`, `updated_by_user`, `name`, `external_id`
| OPERATOR  | string        | yes      | [Supported operators](/documentation/custom-data/v2/searching-custom-object-records/) vary by the value's data type
| VALUE     | string, array | yes      | The value you're filtering for

#### Pagination

* [Cursor pagination](/api-reference/introduction/pagination/#cursor-pagination) only.
* Returns the records sorted by relevancy with page limits. Without a `sort` parameter, only the first 10,000 records are returned. With a `sort` parameter, all records are returned.

#### Allowed For

* Agents
* End users (when an admin [configures](https://support.zendesk.com/hc/en-us/articles/6034260247066) the custom object to be accessible to end users)

### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.custom_object_records.filtered_search_custom_object_records(custom_object_key="car", page_size=100, query="jdoe", request_body=models.CustomObjectRecordsFilteredSearchRequestBasic(
        filter_=models.CustomObjectRecordFilteredSearchCondition(
            **{
                "$and": [
                    {
                        "custom_object_fields.key_one": {
                            "$eq": "foo",
                        },
                    },
                    {
                        "custom_object_fields.key_two": {
                            "$eq": "bar",
                        },
                    },
                ],
                "$or": [
                    {
                        "custom_object_fields.key_three": {
                            "$eq": "foo",
                        },
                    },
                    {
                        "custom_object_fields.key_four": {
                            "$eq": "bar",
                        },
                    },
                ],
            },
        ),
    ))

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_object_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The key of a custom object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `page_before`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `page_after`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | The query parameter is used to search text-based fields for records that match specific query terms.<br/>The query can be multiple words or numbers. Every record that matches the beginning of any word or number in the query string is returned.<br/><br/><br/><br/>Fuzzy search is supported for the following text-based field types: Text fields, Multi Line Text fields, and RegExp fields.<br/><br/><br/><br/>For example, you might want to search for records related to Tesla vehicles: `query=Tesla`. In this example the API would return every record for the given custom object where any of the supported text fields contain the word 'Tesla'.<br/><br/><br/><br/>You can include multiple words or numbers in your search. For example: `query=Tesla Honda 2020`. This search phrase would be URL encoded as `query=Tesla%20Honda%202020` and return every record for the custom object for which any of the supported text fields contained 'Tesla', 'Honda', or '2020'.<br/> |
| `sort`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | One of `name`, `created_at`, `updated_at`, `-name`, `-created_at`, or `-updated_at`. The `-` denotes the sort will be descending. Defaults to sorting by relevance.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `request_body`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[models.FilteredSearchCustomObjectRecordsRequestBody]](../../models/filteredsearchcustomobjectrecordsrequestbody.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

### Response

**[models.FilteredSearchCustomObjectRecordsResponse](../../models/filteredsearchcustomobjectrecordsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## custom_object_records_limit

List the current count and the limit for custom object records
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

    res = z_client.custom_object_records.custom_object_records_limit()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomObjectLimitsResponse](../../models/customobjectlimitsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |