# Macros
(*macros*)

## Overview

### Available Operations

* [list_macros](#list_macros) - List Macros
* [create_macro](#create_macro) - Create Macro
* [show_macro](#show_macro) - Show Macro
* [update_macro](#update_macro) - Update Macro
* [delete_macro](#delete_macro) - Delete Macro
* [show_changes_to_ticket](#show_changes_to_ticket) - Show Changes to Ticket
* [list_macro_attachments](#list_macro_attachments) - List Macro Attachments
* [create_associated_macro_attachment](#create_associated_macro_attachment) - Create Macro Attachment
* [list_macros_actions](#list_macros_actions) - List Supported Actions for Macros
* [list_active_macros](#list_active_macros) - List Active Macros
* [create_macro_attachment](#create_macro_attachment) - Create Unassociated Macro Attachment
* [show_macro_attachment](#show_macro_attachment) - Show Macro Attachment
* [list_macro_categories](#list_macro_categories) - List Macro Categories
* [list_macro_action_definitions](#list_macro_action_definitions) - List Macro Action Definitions
* [delete_many_macros](#delete_many_macros) - Bulk Delete Macros
* [show_derived_macro](#show_derived_macro) - Show Macro Replica
* [search_macro](#search_macro) - Search Macros
* [update_many_macros](#update_many_macros) - Update Many Macros
* [show_ticket_after_changes](#show_ticket_after_changes) - Show Ticket After Changes

## list_macros

Lists all shared and personal macros available to the current user. For admins, the API returns all macros for the account, including the personal macros of agents and other admins.

#### Pagination

- Cursor pagination (recommended)
- Offset pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 100 records per page.

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

    res = z_client.macros.list_macros(page_size=100, include="usage_7d", access="personal", active=True, category=25, group_id=25, only_viewable=False, sort_by="alphabetical", sort_order="asc")

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
| `include`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A sideload to include in the response. See [Sideloads](#sideloads-2)                                                                                                                                                                                                                                                |
| `access`                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter macros by access. Possible values are "personal", "agents", "shared", or "account". The "agents" value returns all personal macros for the account's agents and is only available to admins.                                                                                                                 |
| `active`                                                                                                                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter by active macros if true or inactive macros if false                                                                                                                                                                                                                                                         |
| `category`                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter macros by category                                                                                                                                                                                                                                                                                           |
| `group_id`                                                                                                                                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Filter macros by group                                                                                                                                                                                                                                                                                              |
| `only_viewable`                                                                                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | If true, returns only macros that can be applied to tickets. If false, returns all macros the current user can manage. Default is false                                                                                                                                                                             |
| `sort_by`                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", "usage_7d", or "usage_30d". Defaults to alphabetical                                                                                                                                                                       |
| `sort_order`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |

### Response

**[models.ListMacrosResponse](../../models/listmacrosresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_macro

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

    res = z_client.macros.create_macro(request=models.CreateMacroRequest(
        macro=models.MacroInput(
            actions=[
                models.ActionObject(
                    field="status",
                    value="solved",
                ),
            ],
            title="Roger Wilco",
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.CreateMacroRequest](../../models/createmacrorequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateMacroResponse](../../models/createmacroresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_macro

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

    res = z_client.macros.show_macro(macro_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `macro_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the macro                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroResponse](../../models/macroresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_macro

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

    res = z_client.macros.update_macro(macro_id=25, macro=models.MacroInput(
        actions=[
            models.ActionObject(
                field="status",
                value="solved",
            ),
        ],
        title="Sets the ticket status to `solved`",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `macro_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the macro                                                 |
| `macro`                                                             | [Optional[models.MacroInput]](../../models/macroinput.md)           | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateMacroResponse](../../models/updatemacroresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_macro

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

    z_client.macros.delete_macro(macro_id=25)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `macro_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the macro                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_changes_to_ticket

Returns the changes the macro would make to a ticket. It doesn't actually
change a ticket. You can use the response data in a subsequent API call
to the [Tickets](/api-reference/ticketing/tickets/tickets/) endpoint to update the ticket.

The response includes only the ticket fields that would be changed by the
macro. To get the full ticket object after the macro is applied,
see [Show Ticket After Changes](#show-ticket-after-changes).

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

    res = z_client.macros.show_changes_to_ticket(macro_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `macro_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the macro                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroApplyTicketResponse](../../models/macroapplyticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_macro_attachments

Lists the attachments associated with a macro.

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

    res = z_client.macros.list_macro_attachments(macro_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `macro_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the macro                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroAttachmentsResponse](../../models/macroattachmentsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_associated_macro_attachment

Allows an attachment to be uploaded and associated with a macro at the same time.

**Note:** A macro can be associated with up to five attachments.

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

    res = z_client.macros.create_associated_macro_attachment(macro_id=25)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `macro_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the macro                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroAttachmentResponse](../../models/macroattachmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_macros_actions

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

    res = z_client.macros.list_macros_actions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListMacrosActionsResponse](../../models/listmacrosactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_active_macros

Lists all active shared and personal macros available to the current user.

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

    res = z_client.macros.list_active_macros(include="usage_7d", access="personal", category=25, group_id=25, sort_by="alphabetical", sort_order="asc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | A sideload to include in the response. See [Sideloads](#sideloads-2)                                                                                                                                |
| `access`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Filter macros by access. Possible values are "personal", "agents", "shared", or "account". The "agents" value returns all personal macros for the account's agents and is only available to admins. |
| `category`                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Filter macros by category                                                                                                                                                                           |
| `group_id`                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Filter macros by group                                                                                                                                                                              |
| `sort_by`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Possible values are "alphabetical", "created_at", "updated_at", "usage_1h", "usage_24h", "usage_7d", or "usage_30d". Defaults to alphabetical                                                       |
| `sort_order`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                                                                 |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.MacrosResponse](../../models/macrosresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_macro_attachment

Allows an attachment to be uploaded that can be associated with a macro at a later time.

**Note:** To ensure an uploaded attachment is not lost, associate it with a macro as soon as possible. From time to time, old attachments that are not not associated with any macro are purged.

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

    res = z_client.macros.create_macro_attachment()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroAttachmentResponse](../../models/macroattachmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_macro_attachment

Shows the properties of the specified macro attachment.

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

    res = z_client.macros.show_macro_attachment(attachment_id=498483)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attachment_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | The ID of the attachment                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroAttachmentResponse](../../models/macroattachmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_macro_categories

Lists all macro categories available to the current user.

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

    res = z_client.macros.list_macro_categories()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroCategoriesResponse](../../models/macrocategoriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## list_macro_action_definitions

Returns the definitions of the actions a macro can perform. For example,
one action can set the status of a ticket. The definition of the action
includes a title ("Status"), a type ("list"), and possible values. For a
list of support actions, see [Actions reference](/documentation/ticketing/reference-guides/actions-reference).

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

    res = z_client.macros.list_macro_action_definitions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListMacroActionDefinitionsResponse](../../models/listmacroactiondefinitionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_many_macros

Deletes the macros corresponding to the provided comma-separated list of IDs.

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

    z_client.macros.delete_many_macros(ids=[
        1,
        2,
        3,
    ])

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ids`                                                               | List[*int*]                                                         | :heavy_check_mark:                                                  | The IDs of the macros to delete                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_derived_macro

Returns an unpersisted macro representation derived from a ticket or macro.

The endpoint takes one of the following query parameters: `macro_id` or `ticket_id`. If you include both, `macro_id` is used.

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

    res = z_client.macros.show_derived_macro(macro_id=25, ticket_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `macro_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the macro to replicate                                    |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket from which to build a macro replica            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroResponse](../../models/macroresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## search_macro

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

    res = z_client.macros.search_macro(query="close", include="usage_7d", access="personal", active=True, category=25, group_id=25, only_viewable=False, sort_by="alphabetical", sort_order="asc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                           | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                             | *str*                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                  | Query string used to find macros with matching titles                                                                                                                                               |
| `include`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | A sideload to include in the response. See [Sideloads](#sideloads-2)                                                                                                                                |
| `access`                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Filter macros by access. Possible values are "personal", "agents", "shared", or "account". The "agents" value returns all personal macros for the account's agents and is only available to admins. |
| `active`                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Filter by active macros if true or inactive macros if false                                                                                                                                         |
| `category`                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Filter macros by category                                                                                                                                                                           |
| `group_id`                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Filter macros by group                                                                                                                                                                              |
| `only_viewable`                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | If true, returns only macros that can be applied to tickets. If false, returns all macros the current user can manage. Default is false                                                             |
| `sort_by`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | Possible values are "alphabetical", "created_at", "updated_at", or "position". Defaults to alphabetical                                                                                             |
| `sort_order`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                  | One of "asc" or "desc". Defaults to "asc" for alphabetical and position sort, "desc" for all others                                                                                                 |
| `retries`                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                 |

### Response

**[models.MacrosResponse](../../models/macrosresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many_macros

Updates the provided macros with the specified changes.

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

    res = z_client.macros.update_many_macros(request={
        "macros": [
            {
                "active": False,
                "id": 25,
            },
            {
                "id": 23,
                "position": 5,
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.MacroUpdateManyInput](../../models/macroupdatemanyinput.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacrosResponse](../../models/macrosresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## show_ticket_after_changes

Returns the full ticket object as it would be after applying the macro to the ticket.
It doesn't actually change the ticket.

To get only the ticket fields that would be changed by the macro,
see [Show Changes to Ticket](#show-changes-to-ticket).

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

    res = z_client.macros.show_ticket_after_changes(macro_id=25, ticket_id=35436)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `macro_id`                                                          | *int*                                                               | :heavy_check_mark:                                                  | The ID of the macro                                                 |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MacroApplyTicketResponse](../../models/macroapplyticketresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |