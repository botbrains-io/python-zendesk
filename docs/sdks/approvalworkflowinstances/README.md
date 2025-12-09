# ApprovalWorkflowInstances

## Overview

### Available Operations

* [create_approval_workflow_instance](#create_approval_workflow_instance) - Create Approval Workflow Instance

## create_approval_workflow_instance

Creates an approval workflow instance attached to a ticket. The request must include a name for the workflow and a ticket id to associate with the workflow instance.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateApprovalWorkflowInstance" method="post" path="/api/v2/approval_workflow_instances" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.approval_workflow_instances.create_approval_workflow_instance()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ApprovalWorkflowInstanceObject](../../models/approvalworkflowinstanceobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |