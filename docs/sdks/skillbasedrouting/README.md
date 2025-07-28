# SkillBasedRouting
(*skill_based_routing*)

## Overview

### Available Operations

* [list_a_gent_attribute_values](#list_a_gent_attribute_values) - List Agent Attribute Values
* [set_agent_attribute_values](#set_agent_attribute_values) - Set Agent Attribute Values
* [list_many_agents_attribute_values](#list_many_agents_attribute_values) - List Attribute Values for Many Agents
* [bulk_set_agent_attribute_values_job](#bulk_set_agent_attribute_values_job) - Bulk Set Agent Attribute Values Job
* [list_account_attributes](#list_account_attributes) - List Account Attributes
* [create_attribute](#create_attribute) - Create Attribute
* [show_attribute](#show_attribute) - Show Attribute
* [update_attribute](#update_attribute) - Update Attribute
* [delete_attribute](#delete_attribute) - Delete Attribute
* [list_attribute_values](#list_attribute_values) - List Attribute Values for an Attribute
* [create_attribute_value](#create_attribute_value) - Create Attribute Value
* [show_attribute_value](#show_attribute_value) - Show Attribute Value
* [update_attribute_value](#update_attribute_value) - Update Attribute Value
* [delete_attribute_value](#delete_attribute_value) - Delete Attribute Value
* [list_routing_attribute_definitions](#list_routing_attribute_definitions) - List Routing Attribute Definitions
* [list_tickets_fullfilled_by_user](#list_tickets_fullfilled_by_user) - List Tickets Fulfilled by a User
* [list_ticket_attribute_values](#list_ticket_attribute_values) - List Ticket Attribute Values
* [set_ticket_attribute_values](#set_ticket_attribute_values) - Set Ticket Attribute Values

## list_a_gent_attribute_values

Returns an attribute value.

#### Allowed For

* Agents and admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ListAGentAttributeValues" method="get" path="/api/v2/routing/agents/{user_id}/instance_values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.list_a_gent_attribute_values(user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeValuesResponse](../../models/skillbasedroutingattributevaluesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## set_agent_attribute_values

Adds the specified attributes if no attributes exists, or replaces all existing attributes with the specified attributes.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="SetAgentAttributeValues" method="post" path="/api/v2/routing/agents/{user_id}/instance_values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.set_agent_attribute_values(user_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *int*                                                               | :heavy_check_mark:                                                  | The id of the user                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeValuesResponse](../../models/skillbasedroutingattributevaluesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_many_agents_attribute_values

Accepts a comma-separated list of up to 100 agent ids and returns attribute values for each agent in the list.

#### Allowed For
* Admins
* [Agents in custom role with permission to manage skills](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents)

#### Pagination
* [Cursor pagination](/api-reference/introduction/pagination/#cursor-pagination) only.
Note: `page[before]` and `page[after]` can't be used together in the same request.


### Example Usage

<!-- UsageSnippet language="python" operationID="ListManyAgentsAttributeValues" method="get" path="/api/v2/routing/agents/instance_values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.list_many_agents_attribute_values(filter_agent_ids="224,225", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filter_agent_ids`                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | A comma-separated list of agent ids                                                                                                                                                                                                                                                                                 |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListManyAgentsAttributeValuesResponse](../../models/listmanyagentsattributevaluesresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.SkillBasedRoutingAttributeValuesError | 400                                          | application/json                             |
| errors.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## bulk_set_agent_attribute_values_job

Adds, replaces or removes multiple attributes for up to 100 agents.

#### Allowed For
* Admins
* [Agents in custom role with permission to manage skills](https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents)

#### Available Parameters

The request takes a data object with the following properties:
| Name       | Type   | Required | Description                                                                                       |
| ---------- | ------ | -------- | ------------------------------------------------------------------------------------------------- |
| action     | string | true     | The action to perform on the attribute values. One of the following: "upsert", "update", "delete" |
| attributes | object | true     | The attribute values to update. See [Attribute Values](#attribute-values)                         |
| items      | array  | true     | The list of agent ids                                                                             |

Action can be one of the following:
  * upsert: Adds new attribute values to the agents
  * update: Replaces all the current attribute values of the agents with the new values
  * delete: Removes specified attribute values from the agents

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion.


### Example Usage

<!-- UsageSnippet language="python" operationID="BulkSetAgentAttributeValuesJob" method="post" path="/api/v2/routing/agents/instance_values/job" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.bulk_set_agent_attribute_values_job(job={
        "attributes": {
            "attribute_values": [
                {},
            ],
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `job`                                                                                                             | [Optional[models.BulkSkillBasedRoutingAttributeValueJob]](../../models/bulkskillbasedroutingattributevaluejob.md) | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.SkillBasedRoutingAttributeValuesError | 400                                          | application/json                             |
| errors.APIError                              | 4XX, 5XX                                     | \*/\*                                        |

## list_account_attributes

Returns a list of attributes for the account.

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| attribute_values | The attribute values available on the account

#### Allowed For

* Agents and admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ListAccountAttributes" method="get" path="/api/v2/routing/attributes" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.list_account_attributes()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributesResponse](../../models/skillbasedroutingattributesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_attribute

Creates an attribute.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAttribute" method="post" path="/api/v2/routing/attributes" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.create_attribute()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeResponse](../../models/skillbasedroutingattributeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_attribute

Returns an attribute.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowAttribute" method="get" path="/api/v2/routing/attributes/{attribute_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.show_attribute(attribute_id="6e279587-e930-11e8-a292-09cfcdea1b75")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attribute_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeResponse](../../models/skillbasedroutingattributeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_attribute

Updates an attribute.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAttribute" method="put" path="/api/v2/routing/attributes/{attribute_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.update_attribute(attribute_id="6e279587-e930-11e8-a292-09cfcdea1b75")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attribute_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeResponse](../../models/skillbasedroutingattributeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_attribute

Deletes an attribute.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteAttribute" method="delete" path="/api/v2/routing/attributes/{attribute_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.skill_based_routing.delete_attribute(attribute_id="6e279587-e930-11e8-a292-09cfcdea1b75")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attribute_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_attribute_values

Returns a list of attribute values for a provided attribute.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ListAttributeValues" method="get" path="/api/v2/routing/attributes/{attribute_id}/values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.list_attribute_values(attribute_id="6e279587-e930-11e8-a292-09cfcdea1b75")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attribute_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeValuesResponse](../../models/skillbasedroutingattributevaluesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_attribute_value

Creates an attribute value.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAttributeValue" method="post" path="/api/v2/routing/attributes/{attribute_id}/values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.create_attribute_value(attribute_id="6e279587-e930-11e8-a292-09cfcdea1b75")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attribute_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeValueResponse](../../models/skillbasedroutingattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_attribute_value

Returns an attribute value.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowAttributeValue" method="get" path="/api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.show_attribute_value(attribute_id="6e279587-e930-11e8-a292-09cfcdea1b75", attribute_value_id="b376b35a-e38b-11e8-a292-e3b6377c5575")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attribute_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute                         |
| `attribute_value_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute value                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeValueResponse](../../models/skillbasedroutingattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_attribute_value

Updates the name and ticket conditions of a skill. When a ticket is created, the skill is applied to a ticket  if the ticket meets the specified condition or conditions. See the [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference/) for more information.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAttributeValue" method="patch" path="/api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.update_attribute_value(attribute_id="6e279587-e930-11e8-a292-09cfcdea1b75", attribute_value_id="b376b35a-e38b-11e8-a292-e3b6377c5575")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attribute_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute                         |
| `attribute_value_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute value                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeValueResponse](../../models/skillbasedroutingattributevalueresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_attribute_value

Deletes an attribute value.

#### Allowed For

* Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteAttributeValue" method="delete" path="/api/v2/routing/attributes/{attribute_id}/values/{attribute_value_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.skill_based_routing.delete_attribute_value(attribute_id="6e279587-e930-11e8-a292-09cfcdea1b75", attribute_value_id="b376b35a-e38b-11e8-a292-e3b6377c5575")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attribute_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute                         |
| `attribute_value_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the skill-based routing attribute value                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_routing_attribute_definitions

Returns the condition definitions that can be configured to apply attributes to a ticket.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ListRoutingAttributeDefinitions" method="get" path="/api/v2/routing/attributes/definitions" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.list_routing_attribute_definitions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeDefinitions](../../models/skillbasedroutingattributedefinitions.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_tickets_fullfilled_by_user

Returns a list of ticket ids that contain attributes matching the current user's attributes. Accepts a `ticket_ids` parameter for relevant tickets to check for matching attributes.

#### Allowed For

* Agents and admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ListTicketsFullfilledByUser" method="get" path="/api/v2/routing/requirements/fulfilled" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.list_tickets_fullfilled_by_user(ticket_ids=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_ids`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The IDs of the relevant tickets to check for matching attributes    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingTicketFulfilledResponse](../../models/skillbasedroutingticketfulfilledresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_attribute_values

Returns a list of attributes values for the ticket.

#### Allowed For

* Agents and admins


### Example Usage

<!-- UsageSnippet language="python" operationID="ListTicketAttributeValues" method="get" path="/api/v2/routing/tickets/{ticket_id}/instance_values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.list_ticket_attribute_values(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeValuesResponse](../../models/skillbasedroutingattributevaluesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## set_ticket_attribute_values

Adds the specified attributes if no attributes exists, or replaces all existing attributes with the specified attributes.

Invalid or deleted attributes are ignored.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="SetTicketAttributeValues" method="post" path="/api/v2/routing/tickets/{ticket_id}/instance_values" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.skill_based_routing.set_ticket_attribute_values(ticket_id=123456)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SkillBasedRoutingAttributeValuesResponse](../../models/skillbasedroutingattributevaluesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |