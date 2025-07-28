# ResourceCollections
(*resource_collections*)

## Overview

### Available Operations

* [list_resource_collections](#list_resource_collections) - List Resource Collections
* [create_resource_collection](#create_resource_collection) - Create Resource Collection
* [retrieve_resource_collection](#retrieve_resource_collection) - Show Resource Collection
* [update_resource_collection](#update_resource_collection) - Update Resource Collection
* [delete_resource_collection](#delete_resource_collection) - Delete Resource Collection

## list_resource_collections

Lists resource collections for the account.

#### Allowed for

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ListResourceCollections" method="get" path="/api/v2/resource_collections" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.resource_collections.list_resource_collections()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ResourceCollectionsResponse](../../models/resourcecollectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_resource_collection

Creates a resource collection from a provided `payload` object. The `payload` object is specified the same way as the content of a requirements.json file in a Zendesk app. See [Specifying Apps Requirements](/documentation/apps/app-developer-guide/apps_requirements/) in the Zendesk Apps framework docs.

The response includes a [job
status](/api-reference/ticketing/ticket-management/job_statuses/) for creation of the specified resources.

#### Allowed for

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateResourceCollection" method="post" path="/api/v2/resource_collections" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.resource_collections.create_resource_collection()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## retrieve_resource_collection

Retrieves details for a specified resource collection.

#### Allowed for

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="RetrieveResourceCollection" method="get" path="/api/v2/resource_collections/{resource_collection_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.resource_collections.retrieve_resource_collection(resource_collection_id=10002)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `resource_collection_id`                                            | *int*                                                               | :heavy_check_mark:                                                  | The id of the resource collection                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ResourceCollectionResponse](../../models/resourcecollectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_resource_collection

Updates a resource collection using a provided `payload` object. The `payload` object  is specified the same way as the content of a requirements.json file in a Zendesk app. See [Specifying Apps Requirements](/documentation/apps/app-developer-guide/apps_requirements/) in the Zendesk Apps framework docs.

The response includes a [job
status](/api-reference/ticketing/ticket-management/job_statuses/) for the resource updates.

#### Allowed for

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateResourceCollection" method="put" path="/api/v2/resource_collections/{resource_collection_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.resource_collections.update_resource_collection(resource_collection_id=10002)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `resource_collection_id`                                            | *int*                                                               | :heavy_check_mark:                                                  | The id of the resource collection                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_resource_collection

Deletes a specified resource collection.

The response includes a [job
status](/api-reference/ticketing/ticket-management/job_statuses/) for deletion of the collection's resources.

#### Allowed for

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteResourceCollection" method="delete" path="/api/v2/resource_collections/{resource_collection_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.resource_collections.delete_resource_collection(resource_collection_id=10002)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `resource_collection_id`                                            | *int*                                                               | :heavy_check_mark:                                                  | The id of the resource collection                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |