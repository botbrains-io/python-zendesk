# TicketFields
(*ticket_fields*)

## Overview

### Available Operations

* [list_ticket_fields](#list_ticket_fields) - List Ticket Fields
* [create_ticket_field](#create_ticket_field) - Create Ticket Field
* [show_ticketfield](#show_ticketfield) - Show Ticket Field
* [update_ticket_field](#update_ticket_field) - Update Ticket Field
* [delete_ticket_field](#delete_ticket_field) - Delete Ticket Field
* [list_ticket_field_options](#list_ticket_field_options) - List Ticket Field Options
* [create_or_update_ticket_field_option](#create_or_update_ticket_field_option) - Create or Update Ticket Field Option
* [show_ticket_field_option](#show_ticket_field_option) - Show Ticket Field Option
* [delete_ticket_field_option](#delete_ticket_field_option) - Delete Ticket Field Option
* [count_ticket_fields](#count_ticket_fields) - Count Ticket Fields
* [reorder_ticket_fields](#reorder_ticket_fields) - Reorder Ticket Fields

## list_ticket_fields

Returns a list of all system and custom ticket fields in your account.

For end users, only the ticket fields with visible_in_portal set to true are returned.

Cursor pagination returns a maximum of 100 records per page and fields are returned in the order specified by their id.

If the results are not paginated, every field is returned in the response and fields are returned in the order specified by the position.

You can adjust the position of ticket fields by:

- Using the [Update Ticket Field](/api-reference/ticketing/tickets/ticket_fields/#update-ticket-field) endpoint
- Using the [Reorder Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/#reorder-ticket-fields) endpoint
- Ticket Fields page in the Admin Center (**Admin Center** > **Manage** > **Ticket** > **Fields** > **Actions** > **Edit order**)

These adjustments determine the order in which fields are displayed in various locations. For accounts without access to multiple ticket forms, the order will also be used to display field values within tickets. However, for accounts with access to multiple ticket forms, the field order on the ticket page is defined within each form.

Consider caching this resource to use with the [Tickets](/api-reference/ticketing/tickets/tickets/#json-format) API.

#### Pagination

- Cursor pagination (recommended)
- No pagination

See [Pagination](/api-reference/introduction/pagination/).

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| users            | The user or users that created the ticket field

#### Allowed For

* Anyone


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_fields.list_ticket_fields(page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                               | Forces the `title_in_portal` property to return a dynamic content variant for the specified locale.<br/> Only accepts [active locale ids](/api-reference/ticketing/account-configuration/locales/#list-locales).<br/>Example: `locale="de"`.<br/>                |
| `creator`                                                                                                                                                                                                                                                        | *Optional[bool]*                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                               | Displays the `creator_user_id` and `creator_app_name` properties. If the ticket field is created<br/> by an app, `creator_app_name` is the name of the app and `creator_user_id` is `-1`. If the ticket field<br/> is not created by an app, `creator_app_name` is null<br/> |
| `page_size`                                                                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                               | Number of records per page (required for cursor pagination)                                                                                                                                                                                                      |
| `page_after`                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                               | Cursor for pagination (opaque string)                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                                                                                                              |

### Response

**[models.ListTicketFieldsResponse](../../models/listticketfieldsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_ticket_field

Creates any of the following custom field types:

| Custom field type | Description                                                                                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| text              | Default custom field type when `type` is not specified                                                                                                          |
| textarea          | For multi-line text                                                                                                                                             |
| checkbox          | To capture a boolean value. Allowed values are true or false. Optionally, you can specify a tag to be added to the ticket when the value is true.               |
| date              | Example: 2021-04-16                                                                                                                                             |
| integer           | String composed of numbers. May contain an optional decimal point                                                                                               |
| decimal           | For numbers containing decimals                                                                                                                                 |
| regexp            | Matches the Regex pattern found in the custom field settings                                                                                                    |
| partialcreditcard | A credit card number. Only the last 4 digits are retained                                                                                                       |
| multiselect       | Enables users to choose multiple options from a dropdown menu. It contains one or more tag values belonging to the field's options.                             |
| tagger            | Single-select dropdown menu. It contains one or more tag values belonging to the field's options. Example: ( {"id": 21938362, "value": ["hd_3000", "hd_5555"]}) |
| lookup            | A field to create a relationship (see [lookup relationships](/api-reference/ticketing/lookup_relationships/lookup_relationships/)) to another object such as a user, ticket, or organization |

**Note**: Tags can't be re-used across custom ticket fields. For example, if you configure a tag for a checkbox field, you can't use that tag value for a dropdown (tagger) field option. The use of tags isn't validated and can prevent editing in the future.

See [About custom field types](https://support.zendesk.com/hc/en-us/articles/203661866) in the Zendesk Help Center.

#### Allowed For

* Admins

#### Field limits

We recommend the following best practices for ticket fields limits. Creating more than these amounts can affect performance.

* 400 ticket fields per account if your account doesn't have ticket forms
* 400 ticket fields per ticket form if your account has ticket forms


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_fields.create_ticket_field()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFieldResponse](../../models/ticketfieldresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_ticketfield

#### Allowed for

* Agents

#### Sideloads

The following sideloads are supported:

| Name             | Will sideload
| ---------------- | -------------
| users            | The user or users that created the ticket field


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_fields.show_ticketfield(ticket_field_id=34)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ticket_field_id`                                                                                                                                                                                                                                                              | *int*                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                             | The ID of the ticket field                                                                                                                                                                                                                                                     | 34                                                                                                                                                                                                                                                                             |
| `creator`                                                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | If true, displays the `creator_user_id` and `creator_app_name` properties. If the ticket field is created<br/> by an app, `creator_app_name` is the name of the app and `creator_user_id` is `-1`. If the ticket field<br/> is not created by an app, then `creator_app_name` is null<br/> |                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                |

### Response

**[models.TicketFieldResponse](../../models/ticketfieldresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_ticket_field

#### Updating drop-down field options

You can also use the update endpoint to add, update, or remove options in a drop-down custom field. Updating field options for multi-select fields works exactly the same as drop-down field options.

**Important**: Unless you want to remove some options, you must specify all existing options in any update request. Omitting an option removes it from the drop-down field, which removes its values from any tickets or macros.

Use the `custom_field_options` attribute to update the options. The attribute consists of an array of option objects, with each object consisting of a `name` and `value` property. The properties correspond to the "Title" and "Tag" text boxes in the admin interface. Example request body:

```json
{"ticket_field": {
    "custom_field_options": [
      {"name": "Apple Pie", "value": "apple"},
      {"name": "Pecan Pie", "value": "pecan"}
    ]
  }
}
```

#### Example Request

```bash
curl https://{subdomain}.zendesk.com/api/v2/ticket_fields/{id}.json \
  -d '{"ticket_field": {"custom_field_options": [{"name": "Apple Pie", "value": "apple"}, {"name": "Pecan Pie", "value": "pecan"}]}}' \
  -H "Content-Type: application/json" -X PUT \
  -v -u {email_address}/token:{api_token}
```

#### Example Response

```http
Status: 200 OK

{
  "ticket_field": {
    "id":21938362,
    "type":"tagger",
    "title":"Pies",
    ...
    "custom_field_options": [
      {
        "id":21029772,
        "name":"Apple Pie",
        "raw_name":"Apple Pie",
        "value":"apple",
        "default":false
      },
      ...
    ]
  }
}
```

#### Allowed for

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

    res = z_client.ticket_fields.update_ticket_field(ticket_field_id=34)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ticket_field_id`                                                                                                                                                                                                                                                              | *int*                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                             | The ID of the ticket field                                                                                                                                                                                                                                                     | 34                                                                                                                                                                                                                                                                             |
| `creator`                                                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | If true, displays the `creator_user_id` and `creator_app_name` properties. If the ticket field is created<br/> by an app, `creator_app_name` is the name of the app and `creator_user_id` is `-1`. If the ticket field<br/> is not created by an app, then `creator_app_name` is null<br/> |                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                |

### Response

**[models.TicketFieldResponse](../../models/ticketfieldresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_ticket_field

#### Allowed for

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

    z_client.ticket_fields.delete_ticket_field(ticket_field_id=34)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ticket_field_id`                                                                                                                                                                                                                                                              | *int*                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                             | The ID of the ticket field                                                                                                                                                                                                                                                     | 34                                                                                                                                                                                                                                                                             |
| `creator`                                                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | If true, displays the `creator_user_id` and `creator_app_name` properties. If the ticket field is created<br/> by an app, `creator_app_name` is the name of the app and `creator_user_id` is `-1`. If the ticket field<br/> is not created by an app, then `creator_app_name` is null<br/> |                                                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_ticket_field_options

Returns a list of custom ticket field options for the given drop-down ticket field.

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

    res = z_client.ticket_fields.list_ticket_field_options(ticket_field_id=34)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_field_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket field                                          | 34                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomFieldOptionsResponse](../../models/customfieldoptionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_or_update_ticket_field_option

Creates or updates an option for the given drop-down ticket field.

To update an option, include the id of the option in the `custom_field_option` object. Example:

`{"custom_field_option": {"id": 10002, "name": "Pineapples", ... }`

If an option exists for the given ID, the option will be updated. Otherwise, a new option will be created.

#### Response

Returns one of the following status codes:

- 200 with `Location: /api/v2/ticket_fields/{ticket_field_id}/options.json` if the ticket field option already exists in the database
- 201 with `Location: /api/v2/ticket_fields/{ticket_field_id}/options.json` if the ticket field option is new

#### Allowed For

* Admins

#### Rate Limit
You can make 100 requests every 1 minute using this endpoint.
The rate limiting mechanism behaves as described in
[Monitoring your request activity](/api-reference/ticketing/account-configuration/usage_limits/#monitoring-your-request-activity) in the API introduction.

#### Field Option Limits

* 2000 options per ticket field


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_fields.create_or_update_ticket_field_option(ticket_field_id=34)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_field_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket field                                          | 34                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomFieldOptionResponse](../../models/customfieldoptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_ticket_field_option

#### Allowed for
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

    res = z_client.ticket_fields.show_ticket_field_option(ticket_field_id=34, ticket_field_option_id=10001)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_field_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket field                                          | 34                                                                  |
| `ticket_field_option_id`                                            | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket field option                                   | 10001                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.CustomFieldOptionResponse](../../models/customfieldoptionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_ticket_field_option

#### Allowed for
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

    z_client.ticket_fields.delete_ticket_field_option(ticket_field_id=34, ticket_field_option_id=10001)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_field_id`                                                   | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket field                                          | 34                                                                  |
| `ticket_field_option_id`                                            | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket field option                                   | 10001                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_ticket_fields

Returns an approximate count of system and custom ticket fields in the account. If the count exceeds 100,000, the count will return a cached result.  This cached result will update every 24 hours.

The `count[refreshed_at]` property is a timestamp that indicates when the count was last updated.

**Note**: When the count exceeds 100,000, `count[refreshed_at]` may occasionally be null.
This indicates that the count is being updated in the background, and `count[value]` is limited to 100,000 until the update is complete.

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

    res = z_client.ticket_fields.count_ticket_fields()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TicketFieldCountResponse](../../models/ticketfieldcountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## reorder_ticket_fields

#### Allowed For
* Admins

#### Request Parameters

You can pass in the following parameter in the payload:

| Name                | Type   | Comment
| ------------------- | ------ | --------
| ticket_field_ids    | array  | An array of ticket field ids. Example: "[2, 23, 46, 50]". Not all ticket_field_ids are necessary in the payload; only those provided will be assigned to the first positions. Missing IDs will be assigned incremental positions automatically.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.ticket_fields.reorder_ticket_fields()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |