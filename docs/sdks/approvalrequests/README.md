# ApprovalRequests
(*approval_requests*)

## Overview

### Available Operations

* [create_approval_request](#create_approval_request) - Create an Approval Request
* [show_approval_request](#show_approval_request) - Show Approval Request
* [update_decision_approval_request](#update_decision_approval_request) - Update Approval Request Status
* [search_approvals](#search_approvals) - Get Approvals by Approval Workflow Id

## create_approval_request

Creates an approval request that is attached to a ticket. The request must include all of the following information:
- A subject and message for the approval
- A ticket the request should be associated with
- A [workflow instance id](/api-reference/ticketing/approvals/approval_workflow_instances/#approval-workflow-instances) for the request
- An assignee that will act as an approver

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateApprovalRequest" method="post" path="/api/v2/approval_workflow_instances/{approval_workflow_instance_id}/approval_requests" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.approval_requests.create_approval_request(approval_workflow_instance_id="360002783572", assignee_user=1, message="Please approve the request for a new laptop", subject="Approval Workflow for Laptop Request", ticket_id=137, workflow_instance_id="1AB2C3D4")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `approval_workflow_instance_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The id of the approval workflow instance                            |
| `assignee_user`                                                     | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | User id of the request approver                                     |
| `message`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Details for the approval request                                    |
| `subject`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Subject for the approval request                                    |
| `ticket_id`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Ticket id to attach the approval request to                         |
| `workflow_instance_id`                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Workflow instance id for the approval request                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ApprovalRequestObject](../../models/approvalrequestobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_approval_request

Shows an approval request.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowApprovalRequest" method="get" path="/api/v2/approval_workflow_instances/{approval_workflow_instance_id}/approval_requests/{approval_request_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.approval_requests.show_approval_request(approval_workflow_instance_id="360002783572", approval_request_id="360002783572")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `approval_workflow_instance_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The id of the approval workflow instance                            |
| `approval_request_id`                                               | *str*                                                               | :heavy_check_mark:                                                  | The id of the approval request                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ApprovalRequestObject](../../models/approvalrequestobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_decision_approval_request

Updates the  approver's decision about an approval request.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateDecisionApprovalRequest" method="patch" path="/api/v2/approval_workflow_instances/{approval_workflow_instance_id}/approval_requests/{approval_request_id}/decision" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.approval_requests.update_decision_approval_request(approval_workflow_instance_id="360002783572", approval_request_id="360002783572", notes="Approved by manager", status="approved")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `approval_workflow_instance_id`                                                                             | *str*                                                                                                       | :heavy_check_mark:                                                                                          | The id of the approval workflow instance                                                                    |
| `approval_request_id`                                                                                       | *str*                                                                                                       | :heavy_check_mark:                                                                                          | The id of the approval request                                                                              |
| `notes`                                                                                                     | *Optional[str]*                                                                                             | :heavy_minus_sign:                                                                                          | Notes for the decision                                                                                      |
| `status`                                                                                                    | [Optional[models.UpdateDecisionApprovalRequestStatus]](../../models/updatedecisionapprovalrequeststatus.md) | :heavy_minus_sign:                                                                                          | The status of the approval request                                                                          |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.ApprovalRequestObject](../../models/approvalrequestobject.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_approvals

Returns a list of approvals associated with a specific [workflow instance](/api-reference/ticketing/approvals/approval_workflow_instances/#approval-workflow-instances). Results can be filtered by approval request status.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="SearchApprovals" method="post" path="/api/v2/approval_workflow_instances/{approval_workflow_instance_id}/approval_requests/search" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.approval_requests.search_approvals(approval_workflow_instance_id="360002783572")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `approval_workflow_instance_id`                                     | *str*                                                               | :heavy_check_mark:                                                  | The id of the approval workflow instance                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ApprovalRequestsSearchResponse](../../models/approvalrequestssearchresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |