# Organizations
(*organizations*)

## Overview

### Available Operations

* [show_organization_merge](#show_organization_merge) - Show Organization Merge
* [list_organizations](#list_organizations) - List Organizations
* [create_organization](#create_organization) - Create Organization
* [show_organization](#show_organization) - Show Organization
* [update_organization](#update_organization) - Update Organization
* [delete_organization](#delete_organization) - Delete Organization
* [create_organization_merge](#create_organization_merge) - Merge Organization With Another Organization
* [list_organization_merges](#list_organization_merges) - List Organization Merges
* [organization_related](#organization_related) - Show Organization's Related Information
* [autocomplete_organizations](#autocomplete_organizations) - Autocomplete Organizations
* [count_organizations](#count_organizations) - Count Organizations
* [create_many_organizations](#create_many_organizations) - Create Many Organizations
* [create_or_update_organization](#create_or_update_organization) - Create Or Update Organization
* [delete_many_organizations](#delete_many_organizations) - Bulk Delete Organizations
* [search_organizations](#search_organizations) - Search Organizations
* [show_many_organizations](#show_many_organizations) - Show Many Organizations
* [update_many_organizations](#update_many_organizations) - Update Many Organizations

## show_organization_merge

Retrieves the details of a specific organization merge operation. This endpoint is useful for obtaining the status and outcome of a merge that was previously initiated. It provides information such as the winning and losing organization IDs, the status of the merge, and the associated URLs.

This endpoint can be used to determine if a merge is still in progress, has completed successfully, or has encountered an error.

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.show_organization_merge(organization_merge_id="01HPZM6206BF4G63783E5349AD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_merge_id`                                             | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization merge                                    | 01HPZM6206BF4G63783E5349AD                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationMergeResponse](../../models/organizationmergeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_organizations

#### Pagination

* Cursor pagination (recommended)
* Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

#### Allowed For

* Agents, with certain restrictions

If the agent has a custom agent role that restricts their access to only users in their own organization, a 403 Forbidden error is returned. See [Creating custom agent roles](https://support.zendesk.com/hc/en-us/articles/203662026-Creating-custom-roles-and-assigning-agents#topic_cxn_hig_bd) in Zendesk help.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.list_organizations(page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListOrganizationsResponse](../../models/listorganizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_organization

You must provide a unique `name` for each organization. Normally
the system doesn't allow records to be created with identical names.
However, a race condition can occur if you make two or more identical
POSTs very close to each other, causing the records to have identical
organization names.

#### Allowed For

* Admins
* Agents assigned to a custom role with permissions to manage organizations (Enterprise only)


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.create_organization(organization={
        "name": "My Organization",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [models.OrganizationObjectInput](../../models/organizationobjectinput.md)                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | {<br/>"created_at": "2009-07-20T22:55:29Z",<br/>"details": "This is a kind of organization",<br/>"domain_names": [<br/>"example.com",<br/>"test.com"<br/>],<br/>"external_id": "ABC123",<br/>"group_id": null,<br/>"id": 35436,<br/>"name": "One Organization",<br/>"notes": "",<br/>"organization_fields": {<br/>"org_decimal": 5.2,<br/>"org_dropdown": "option_1"<br/>},<br/>"shared_comments": true,<br/>"shared_tickets": true,<br/>"tags": [<br/>"enterprise",<br/>"other_tag"<br/>],<br/>"updated_at": "2011-05-05T10:38:52Z",<br/>"url": "https://company.zendesk.com/api/v2/organizations/35436.json"<br/>} |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Response

**[models.OrganizationResponse](../../models/organizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_organization

#### Allowed For

* Admins
* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.show_organization(organization_id=16)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of an organization                                           | 16                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationResponse](../../models/organizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_organization

#### Allowed For

* Admins
* Agents

Agents with no permissions restrictions can only update "notes" on organizations.

**Note:** Updating an organization's `domain_names` property overwrites all existing `domain_names` values. To prevent this, submit a complete list of `domain_names` for the organization in your request.

#### Example Request

```js
{
  "organization": {
    "notes": "Something interesting"
  }
}
```


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.update_organization(organization_id=16)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of an organization                                           | 16                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationResponse](../../models/organizationresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Errors    | 429              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete_organization

#### Allowed For

* Admins
* Agents assigned to a custom role with permissions to manage organizations (Enterprise only)


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.organizations.delete_organization(organization_id=16)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of an organization                                           | 16                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_organization_merge

Merges two organizations by moving all users, tickets, and domain names from the organization specified by `{organization_id}` to the organization specified by `winner_id`. After the merge:

- The "losing" organization will be deleted.
- Other organization fields and their values will not be carried over to the "winning" organization.
- The merge operation creates an `Organization Merge` record which contains a status indicating the progress of the merge.

**Note**: This operation is irreversible.

#### Merge Statuses

| Status | Description |
|--------|-------------|
| new | A job has been queued to merge the two organizations. |
| in progress | The job to merge the two organizations has started. |
| error | An error occurred during the merge job. The merge can be retried by repeating the API call. | 
| complete | The merge has been completed successfully. |

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.create_organization_merge(organization_id=16, organization_merge={
        "winner_id": 54321,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             | Example                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                       | *int*                                                                                                                   | :heavy_check_mark:                                                                                                      | The ID of an organization                                                                                               | 16                                                                                                                      |
| `organization_merge`                                                                                                    | [Optional[models.OrganizationMergeRequestOrganizationMerge]](../../models/organizationmergerequestorganizationmerge.md) | :heavy_minus_sign:                                                                                                      | N/A                                                                                                                     |                                                                                                                         |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |                                                                                                                         |

### Response

**[models.OrganizationMergeResponse](../../models/organizationmergeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_organization_merges

Retrieves a list of all organization merge operations associated with a given organization. This endpoint allows you to track the history of merge actions for an organization, including ongoing and completed merges.

Each entry in the list contains details such as the ID of the merge, the winning and losing organization IDs, the current status of the merge, and a URL to access the `Organization Merge` record.

#### Pagination

- Cursor pagination is used for this endpoint.
- A maximum of 100 records can be returned per page.

See [Pagination](/api-reference/introduction/pagination/) for more details.

#### Allowed For

* Admins


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.list_organization_merges(organization_id=16, page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                                                                                                                                   | *int*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The ID of an organization                                                                                                                                                                                                                                                                                           | 16                                                                                                                                                                                                                                                                                                                  |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |                                                                                                                                                                                                                                                                                                                     |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |                                                                                                                                                                                                                                                                                                                     |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                     |

### Response

**[models.ListOrganizationMergesResponse](../../models/listorganizationmergesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## organization_related

#### Allowed For

* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.organization_related(organization_id=16)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of an organization                                           | 16                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationsRelatedResponse](../../models/organizationsrelatedresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## autocomplete_organizations

Returns an array of organizations whose name starts with the
value specified in the `name` parameter.

#### Pagination

* Offset pagination only

See [Using Offset Pagination](/api-reference/ticketing/introduction/#using-offset-pagination).

#### Allowed For

* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.autocomplete_organizations(name="imp", source="zen:organization")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       | Example                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                            | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | A substring of an organization to search for                                                                                                      | imp                                                                                                                                               |
| `field_id`                                                                                                                                        | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The id of a lookup relationship field.  The type of field is determined<br/>by the `source` param<br/>                                            |                                                                                                                                                   |
| `source`                                                                                                                                          | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | If a `field_id` is provided, this specifies the type of the field.<br/>For example, if the field is on a "zen:user", it references a field on a user<br/> |                                                                                                                                                   |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |                                                                                                                                                   |

### Response

**[models.OrganizationsResponse](../../models/organizationsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Errors    | 400, 429         | application/json |
| errors.Errors    | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## count_organizations

Returns an approximate count of organizations. If the count exceeds
100,000, it is updated every 24 hours.

The `refreshed_at` property of the `count` object is a timestamp that indicates
when the count was last updated.

When the count exceeds 100,000, the `refreshed_at` property may
occasionally be null. This indicates that the count is being
updated in the background and the `value` property of the `count` object is limited to
100,000 until the update is complete.

#### Allowed For

* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.count_organizations()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CountOrganizationResponse](../../models/countorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_many_organizations

Accepts an array of up to 100 organization objects.

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

* Agents, with restrictions applying on certain actions


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.create_many_organizations()

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

## create_or_update_organization

Creates an organization if it doesn't already exist, or updates
an existing organization. Using this method means one less call
to check if an organization exists before creating it. You need
to specify the id or external id when updating
an organization to avoid a duplicate error response. Name is
not available as a matching criteria.

#### Allowed For

* Agents, with restrictions on certain actions


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.create_or_update_organization()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OrganizationResponse](../../models/organizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_many_organizations

Accepts a comma-separated list of up to 100 organization ids or external ids.

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

* Admins
* Agents assigned to a custom role with permissions to manage organizations (Enterprise only)


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.delete_many_organizations(ids="35436,20057623", external_ids="1764,42156")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A list of organization ids                                          | 35436,20057623                                                      |
| `external_ids`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A list of external ids                                              | 1764,42156                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_organizations

Returns an array of organizations matching the criteria. You may search by an organization's `external_id` or `name`, but not both:

#### Searching by `external_id`

If you set the `external_id` value of an organization to associate it to an external record, you can use it to search for the organization.

For an organization to be returned, its `external_id` must exactly match the value provided (case insensitive).

#### Searching by `name`

For an organization to be returned, its `name` must exactly match the value provided (case insensitive).

#### Allowed For:

* Admins
* Agents assigned to a custom role with permissions to add or modify organizations (Enterprise only)

See [Creating custom agent roles](https://support.zendesk.com/hc/en-us/articles/203662026#topic_cxn_hig_bd) in the Support Help Center.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.search_organizations(external_id=1234, name="ACME Incorporated")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_id`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The external id of an organization                                  | 1234                                                                |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The name of an organization                                         | ACME Incorporated                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationsResponse](../../models/organizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_many_organizations

Accepts a comma-separated list of up to 100 organization ids or external ids.

#### Allowed For

* Admins
* Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.show_many_organizations(ids="35436,20057623", external_ids="1764,42156")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A list of organization ids                                          | 35436,20057623                                                      |
| `external_ids`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A list of external ids                                              | 1764,42156                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationsResponse](../../models/organizationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many_organizations

Bulk or batch updates up to 100 organizations.

#### Bulk update

To make the same change to multiple organizations, use the following endpoint and data format:

`https://{subdomain}.zendesk.com/api/v2/organizations/update_many.json?ids=1,2,3`

```js
{
  "organization": {
    "notes": "Priority"
  }
}
```

#### Batch update

To make different changes to multiple organizations, use the following endpoint and data format:

`https://{subdomain}.zendesk.com/api/v2/organizations/update_many.json`

```js
{
  "organizations": [
    { "id": 1, "notes": "Priority" },
    { "id": 2, "notes": "Normal" }
  ]
}
```

#### Response

This endpoint returns a `job_status` [JSON object](/api-reference/ticketing/ticket-management/job_statuses/#json-format) and queues a background job to do the work. Use the [Show Job Status](/api-reference/ticketing/ticket-management/job_statuses/#show-job-status) endpoint to check for the job's completion. Only a certain number of jobs can be queued or running at the same time. See [Job limit](/api-reference/introduction/rate-limits/#job-limit) for more information.

#### Allowed For

* Admins
* Agents

Agents with no permissions restrictions can only update "notes" on organizations.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.organizations.update_many_organizations(ids="35436,20057623", external_ids="1764,42156")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A list of organization ids                                          | 35436,20057623                                                      |
| `external_ids`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A list of external ids                                              | 1764,42156                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.JobStatusResponse](../../models/jobstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |