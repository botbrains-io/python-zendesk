# ApprovalRequestDecision


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `decided_at`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_minus_sign:                                                       | The time the decision was made                                           |
| `decided_by_user`                                                        | [Optional[models.ApprovalRequestUser]](../models/approvalrequestuser.md) | :heavy_minus_sign:                                                       | N/A                                                                      |
| `decision_notes`                                                         | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Notes for the decision                                                   |
| `id`                                                                     | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Unique identifier for the decision                                       |
| `status`                                                                 | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Status of the decision                                                   |