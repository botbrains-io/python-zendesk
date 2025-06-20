# AuditLogs
(*audit_logs*)

## Overview

### Available Operations

* [list_audit_logs](#list_audit_logs) - List Audit Logs
* [show_audit_log](#show_audit_log) - Show Audit Log
* [export_audit_logs](#export_audit_logs) - Export Audit Logs

## list_audit_logs

#### Allowed For

* Admins on accounts that have audit log access

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.audit_logs.list_audit_logs(page_size=100)

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
| `filter_source_type`                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter audit logs by the source type. For example, user or rule                                                                                                                                                                                                                                                     |
| `filter_source_id`                                                                                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter audit logs by the source id. Requires `filter[source_type]` to also be set                                                                                                                                                                                                                                   |
| `filter_actor_id`                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter audit logs by the actor id                                                                                                                                                                                                                                                                                   |
| `filter_ip_address`                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter audit logs by the ip address                                                                                                                                                                                                                                                                                 |
| `filter_created_at`                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter audit logs by the time of creation. When used, you must specify `filter[created_at]` twice in your request, first with the start time and again with an end time                                                                                                                                             |
| `filter_action`                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter audit logs by the action                                                                                                                                                                                                                                                                                     |
| `sort`                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Cursor pagination only. Sort audit logs. Default is `sort=-created_at`                                                                                                                                                                                                                                              |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListAuditLogsResponse](../../models/listauditlogsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_audit_log

#### Allowed For

* Admins on accounts that have audit-log access


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.audit_logs.show_audit_log(audit_log_id=498483)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `audit_log_id`                                                      | *int*                                                               | :heavy_check_mark:                                                  | The ID of the audit log                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AuditLogResponse](../../models/auditlogresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## export_audit_logs

#### Allowed For

* Admins on accounts that have audit log access


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.audit_logs.export_audit_logs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_source_type`                                                                                                                                                    | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Filter audit logs by the source type. For example, user or rule                                                                                                         |
| `filter_source_id`                                                                                                                                                      | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Filter audit logs by the source id. Requires `filter[source_type]` to also be set.                                                                                      |
| `filter_actor_id`                                                                                                                                                       | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Filter audit logs by the actor id                                                                                                                                       |
| `filter_ip_address`                                                                                                                                                     | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Filter audit logs by the ip address                                                                                                                                     |
| `filter_created_at`                                                                                                                                                     | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Filter audit logs by the time of creation. When used, you must specify `filter[created_at]` twice in your request, first with the start time and again with an end time |
| `filter_action`                                                                                                                                                         | *Optional[str]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Filter audit logs by the action                                                                                                                                         |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |