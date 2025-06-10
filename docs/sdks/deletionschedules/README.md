# DeletionSchedules
(*deletion_schedules*)

## Overview

### Available Operations

* [list_deletion_schedules](#list_deletion_schedules) - List Deletion Schedules
* [create_deletion_schedule](#create_deletion_schedule) - Create Deletion Schedule
* [get_deletion_schedule](#get_deletion_schedule) - Get Deletion Schedule
* [update_deletion_schedule](#update_deletion_schedule) - Update Deletion Schedule
* [delete_deletion_schedule](#delete_deletion_schedule) - Delete Deletion Schedule

## list_deletion_schedules

Lists all deletion schedules for the account. Deletion schedules are used to automatically delete data from the account after a certain period of time.

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.deletion_schedules.list_deletion_schedules()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListDeletionSchedulesResponse](../../models/listdeletionschedulesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_deletion_schedule

Creates a new deletion schedule.

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.deletion_schedules.create_deletion_schedule(deletion_schedule={
        "active": True,
        "conditions": {
            "all": [
                {
                    "field": "duration_since_last_update",
                    "operator": "greater_than",
                    "value": "P1Y",
                },
            ],
            "any": [],
        },
        "description": "Delete tickets older than 1 year",
        "title": "some schedule",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `deletion_schedule`                                                             | [Optional[models.DeletionScheduleInput]](../../models/deletionscheduleinput.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.CreateDeletionScheduleResponse](../../models/createdeletionscheduleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_deletion_schedule

Gets a deletion schedule by its id.

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.deletion_schedules.get_deletion_schedule(deletion_schedule_id=132828)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `deletion_schedule_id`                                              | *int*                                                               | :heavy_check_mark:                                                  | The id of the deletion schedule                                     | 132828                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetDeletionScheduleResponse](../../models/getdeletionscheduleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_deletion_schedule

Updates a deletion schedule by its id.

**Note**: Updating a condition updates the conditions array, clearing all existing values of the array. Include all your conditions when updating any condition.

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.deletion_schedules.update_deletion_schedule(deletion_schedule_id=132828, deletion_schedule={
        "active": True,
        "conditions": {
            "all": [
                {
                    "field": "duration_since_last_update",
                    "operator": "greater_than",
                    "value": "P1Y",
                },
            ],
            "any": [],
        },
        "description": "Delete tickets older than 1 year",
        "title": "some schedule",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `deletion_schedule_id`                                                          | *int*                                                                           | :heavy_check_mark:                                                              | The id of the deletion schedule                                                 | 132828                                                                          |
| `deletion_schedule`                                                             | [Optional[models.DeletionScheduleInput]](../../models/deletionscheduleinput.md) | :heavy_minus_sign:                                                              | N/A                                                                             |                                                                                 |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Response

**[models.UpdateDeletionScheduleResponse](../../models/updatedeletionscheduleresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_deletion_schedule

Deletes a deletion schedule by its id.

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.deletion_schedules.delete_deletion_schedule(deletion_schedule_id=132828)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `deletion_schedule_id`                                              | *int*                                                               | :heavy_check_mark:                                                  | The id of the deletion schedule                                     | 132828                                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |