# LookupRelationships

## Overview

### Available Operations

* [get_sources_by_target](#get_sources_by_target) - Get sources by target
* [get_relationship_filter_definitions](#get_relationship_filter_definitions) - Filter Definitions

## get_sources_by_target

Returns a list of source objects whose values are populated with the id of a related target object.  For example,
if you have a lookup field called "Success Manager" on a ticket, this endpoint can answer the question,
"What tickets (sources) is this user (found by `target_type` and `target_id`)
assigned as the 'Success Manager' (field referenced by `field_id`)?"

#### Allowed For

* Agents

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).


### Example Usage

<!-- UsageSnippet language="python" operationID="GetSourcesByTarget" method="get" path="/api/v2/{target_type}/{target_id}/relationship_fields/{field_id}/{source_type}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.lookup_relationships.get_sources_by_target(target_type="zen:custom_object:apartment", target_id=1234, field_id=1234, source_type="zen:custom_object:apartment", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `target_type`                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The type of object the relationship field is targeting.<br/>The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"<br/>                                                                                                                                            |
| `target_id`                                                                                                                                                                                                                                                                                                         | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The id of the object the relationship field is targeting<br/>                                                                                                                                                                                                                                                       |
| `field_id`                                                                                                                                                                                                                                                                                                          | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The id of the lookup relationship field<br/>                                                                                                                                                                                                                                                                        |
| `source_type`                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The type of object the relationship field belongs to (example. ticket field belongs to a ticket object).<br/>The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"<br/>                                                                                           |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.GetSourcesByTargetResponse](../../models/getsourcesbytargetresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_relationship_filter_definitions

Returns filter definitions based on the given target type.  Target types
include users (zen:user), tickets (zen:ticket), organizations (zen:organization), or custom objects (zen:custom_object:CUSTOM_OBJECT_KEY).
The returned filter definitions are the options that you can use to build a custom field or ticket field's
`relationship_filter`.


### Example Usage

<!-- UsageSnippet language="python" operationID="GetRelationshipFilterDefinitions" method="get" path="/api/v2/relationships/definitions/{target_type}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.lookup_relationships.get_relationship_filter_definitions(target_type="zen:custom_object:apartment", source_type="zen:user")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `target_type`                                                                                                                                                                | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | The target type for which you would like to see filter definitions.<br/>The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"<br/> |
| `source_type`                                                                                                                                                                | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | The source type for which you would like to see filter definitions.<br/>The options are "zen:user", "zen:ticket", and "zen:organization"<br/>                                |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |

### Response

**[models.RelationshipFilterDefinitionResponse](../../models/relationshipfilterdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |