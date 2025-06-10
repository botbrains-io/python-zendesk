# LookupRelationships
(*lookup_relationships*)

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

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.lookup_relationships.get_sources_by_target(target_type="zen:custom_object:apartment", target_id=1234, field_id=1234, source_type="zen:custom_object:apartment")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                         | Type                                                                                                                                                                                                              | Required                                                                                                                                                                                                          | Description                                                                                                                                                                                                       | Example                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `target_type`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                | The type of object the relationship field is targeting.<br/>The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"<br/>                                          | zen:custom_object:apartment                                                                                                                                                                                       |
| `target_id`                                                                                                                                                                                                       | *int*                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                | The id of the object the relationship field is targeting<br/>                                                                                                                                                     | 1234                                                                                                                                                                                                              |
| `field_id`                                                                                                                                                                                                        | *int*                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                | The id of the lookup relationship field<br/>                                                                                                                                                                      | 1234                                                                                                                                                                                                              |
| `source_type`                                                                                                                                                                                                     | *str*                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                | The type of object the relationship field belongs to (example. ticket field belongs to a ticket object).<br/>The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"<br/> | zen:custom_object:apartment                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                               |                                                                                                                                                                                                                   |

### Response

**[models.ReverseLookupResponse](../../models/reverselookupresponse.md)**

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

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  | Example                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `target_type`                                                                                                                                                                | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | The target type for which you would like to see filter definitions.<br/>The options are "zen:user", "zen:ticket", "zen:organization", and "zen:custom_object:CUSTOM_OBJECT_KEY"<br/> | zen:custom_object:apartment                                                                                                                                                  |
| `source_type`                                                                                                                                                                | *Optional[str]*                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                           | The source type for which you would like to see filter definitions.<br/>The options are "zen:user", "zen:ticket", and "zen:organization"<br/>                                | zen:user                                                                                                                                                                     |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |                                                                                                                                                                              |

### Response

**[models.RelationshipFilterDefinitionResponse](../../models/relationshipfilterdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |