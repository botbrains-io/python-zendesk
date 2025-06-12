# JobStatuses
(*job_statuses*)

## Overview

### Available Operations

* [list_job_statuses](#list_job_statuses) - List Job Statuses
* [show_job_status](#show_job_status) - Show Job Status
* [show_many_job_statuses](#show_many_job_statuses) - Show Many Job Statuses
* [bulk_set_agent_attribute_values_job](#bulk_set_agent_attribute_values_job) - Bulk Set Agent Attribute Values Job

## list_job_statuses

Shows the statuses for background jobs. Statuses are sorted first by completion date and then by creation date in descending order.

#### Allowed For:

* Agents

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

    res = z_client.job_statuses.list_job_statuses(page_size=100)

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

**[models.ListJobStatusesResponse](../../models/listjobstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_job_status

Shows the status of a background job.

#### Allowed For:

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

    res = z_client.job_statuses.show_job_status(job_status_id="8b726e606741012ffc2d782bcb7848fe")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_status_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | the Id of the Job status                                            | 8b726e606741012ffc2d782bcb7848fe                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_many_job_statuses

Accepts a comma-separated list of job status ids.

#### Allowed For:

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

    res = z_client.job_statuses.show_many_job_statuses(ids="8b726e606741012ffc2d782bcb7848fe,e7665094164c498781ebe4c8db6d2af5")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *str*                                                               | :heavy_check_mark:                                                  | Comma-separated list of job status ids.                             | 8b726e606741012ffc2d782bcb7848fe,e7665094164c498781ebe4c8db6d2af5   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.JobStatusesResponse](../../models/jobstatusesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## bulk_set_agent_attribute_values_job

Adds, replaces or removes multiple attributes for up to 100 agents.

#### Allowed For
* Admins
* [Agents in custom role with permission to manage skills](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents)

#### Available Parameters

The request takes a data object with the following properties:
| Name       | Type   | Required | Description                                                                                       |
| ---------- | ------ | -------- | ------------------------------------------------------------------------------------------------- |
| action     | string | true     | The action to perform on the attribute values. One of the following: "upsert", "update", "delete" |
| attributes | object | true     | The attribute values to update. See [Attribute Values](#attribute-values)                         |
| items      | array  | true     | The list of agent ids                                                                             |

Action can be one of the following:
  * upsert: Adds new attribute values to the agents
  * update: Replaces all the current attribute values of the agents with the new values
  * delete: Removes specified attribute values from the agents

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.job_statuses.bulk_set_agent_attribute_values_job(job={
        "attributes": {
            "attribute_values": [
                {},
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `job`                                                                                                             | [Optional[models.BulkSkillBasedRoutingAttributeValueJob]](../../models/bulkskillbasedroutingattributevaluejob.md) | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.SkillBasedRoutingAttributeValuesError | 400                                          | application/json                             |
| errors.APIError                              | 4XX, 5XX                                     | \*/\*                                        |