# TicketRelatedInformation


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `followup_source_ids`                                | List[*str*]                                          | :heavy_minus_sign:                                   | N/A                                                  |
| `from_archive`                                       | *Optional[bool]*                                     | :heavy_minus_sign:                                   | Is true if the current ticket is archived            |
| `incidents`                                          | *Optional[int]*                                      | :heavy_minus_sign:                                   | A count of related incident occurrences              |
| `jira_issue_ids`                                     | List[*str*]                                          | :heavy_minus_sign:                                   | N/A                                                  |
| `topic_id`                                           | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | Related topic in the Web portal (deprecated feature) |