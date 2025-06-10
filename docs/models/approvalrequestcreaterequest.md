# ApprovalRequestCreateRequest


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `assignee_user`                               | *Optional[int]*                               | :heavy_minus_sign:                            | User id of the request approver               |
| `message`                                     | *Optional[str]*                               | :heavy_minus_sign:                            | Details for the approval request              |
| `subject`                                     | *Optional[str]*                               | :heavy_minus_sign:                            | Subject for the approval request              |
| `ticket_id`                                   | *Optional[int]*                               | :heavy_minus_sign:                            | Ticket id to attach the approval request to   |
| `workflow_instance_id`                        | *Optional[str]*                               | :heavy_minus_sign:                            | Workflow instance id for the approval request |