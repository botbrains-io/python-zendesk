# IncrementalSkillBasedRoutingSDK
(*incremental_skill_based_routing*)

## Overview

### Available Operations

* [incremental_skil_based_routing_attribute_values_export](#incremental_skil_based_routing_attribute_values_export) - Incremental Attributes Values Export
* [incremental_skil_based_routing_attributes_export](#incremental_skil_based_routing_attributes_export) - Incremental Attributes Export
* [incremental_skil_based_routing_instance_values_export](#incremental_skil_based_routing_instance_values_export) - Incremental Instance Values Export

## incremental_skil_based_routing_attribute_values_export

Returns a stream of changes that occurred on routing attribute values.

#### Allowed For

* Admins

#### Parameters

Optional

| Name   | Type   | Comment
| ------ | ------ | -------
| cursor | string | The `cursor` parameter is a non-human-readable argument you can use to move forward or backward in time. The cursor is a read-only URL parameter that's only available in API responses. See [Pagination](#pagination).


### Example Usage

<!-- UsageSnippet language="python" operationID="IncrementalSkilBasedRoutingAttributeValuesExport" method="get" path="/api/v2/incremental/routing/attribute_values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_skill_based_routing.incremental_skil_based_routing_attribute_values_export()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncrementalSkillBasedRouting](../../models/incrementalskillbasedrouting.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## incremental_skil_based_routing_attributes_export

Returns a stream of changes that occurred on routing attributes.

#### Allowed For

* Admins

#### Parameters

Optional


| Name   | Type   | Comment
| ------ | ------ | -------
| cursor | string | The `cursor` parameter is a non-human-readable argument you can use to move forward or backward in time. The cursor is a read-only URL parameter that's only available in API responses. See [Pagination](#pagination).


### Example Usage

<!-- UsageSnippet language="python" operationID="IncrementalSkilBasedRoutingAttributesExport" method="get" path="/api/v2/incremental/routing/attributes" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_skill_based_routing.incremental_skil_based_routing_attributes_export()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncrementalSkillBasedRouting](../../models/incrementalskillbasedrouting.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## incremental_skil_based_routing_instance_values_export

Returns a stream of changes that occurred on routing instance values. Changes are grouped by `attribute_value_id`,
with associate type events listed alongside unassociate type events based on the unassociate event’s timestamp.

#### Allowed For

* Admins

#### Parameters

Optional

| Name   | Type   | Comment
| ------ | ------ | -------
| cursor | string | The `cursor` parameter is a non-human-readable argument you can use to move forward or backward in time. The cursor is a read-only URL parameter that's only available in API responses. See [Pagination](#pagination).


### Example Usage

<!-- UsageSnippet language="python" operationID="IncrementalSkilBasedRoutingInstanceValuesExport" method="get" path="/api/v2/incremental/routing/instance_values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.incremental_skill_based_routing.incremental_skil_based_routing_instance_values_export()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.IncrementalSkillBasedRouting](../../models/incrementalskillbasedrouting.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |