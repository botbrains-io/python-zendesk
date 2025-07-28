# Attachments
(*attachments*)

## Overview

### Available Operations

* [show_attachment](#show_attachment) - Show Attachment
* [update_attachment](#update_attachment) - Update Attachment for Malware
* [redact_comment_attachment](#redact_comment_attachment) - Redact Comment Attachment
* [upload_files](#upload_files) - Upload Files
* [delete_upload](#delete_upload) - Delete Upload

## show_attachment

Shows attachment details. You can get the value of the `attachment_id` parameter by listing the ticket's comments.
See [List Comments](/api-reference/ticketing/tickets/ticket_comments/#list-comments). Each comment
in the list has an `attachments` list that specifies an `id` for each attachment.


 #### Allowed for

 * Agents


### Example Usage

<!-- UsageSnippet language="python" operationID="ShowAttachment" method="get" path="/api/v2/attachments/{attachment_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.attachments.show_attachment(attachment_id=498483)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `attachment_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | The ID of the attachment                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AttachmentResponse](../../models/attachmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_attachment

Toggles enabling or restricting agent access to attachments with detected malware.

#### Allowed For

* Admins


### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateAttachment" method="put" path="/api/v2/attachments/{attachment_id}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.attachments.update_attachment(attachment_id=498483, attachment={
        "malware_access_override": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `attachment_id`                                                                 | *int*                                                                           | :heavy_check_mark:                                                              | The ID of the attachment                                                        |
| `attachment`                                                                    | [Optional[models.AttachmentUpdateInput]](../../models/attachmentupdateinput.md) | :heavy_minus_sign:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.AttachmentResponse](../../models/attachmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## redact_comment_attachment

Redaction allows you to permanently remove attachments from an existing comment on a ticket. Once removed from a comment, the attachment is replaced with an empty "redacted.txt" file.

The redaction is permanent. It is not possible to undo redaction or see what was removed. Once a ticket is closed, redacting its attachments is no longer possible.

Also, if you want to redact an inline attachment, you can use the `include_inline_images` parameter in the [List Comments](/api-reference/ticketing/tickets/ticket_comments/#list-comments) operation to obtain the inline attachment ID, and use it in the request URL.

#### Allowed For

* Admins
* Agents when [deleting tickets is enabled for agents on professional accounts](https://support.zendesk.com/hc/en-us/articles/360002128107)
* Agents assigned to a custom role with permissions to redact ticket content (Enterprise only)


### Example Usage

<!-- UsageSnippet language="python" operationID="RedactCommentAttachment" method="put" path="/api/v2/tickets/{ticket_id}/comments/{comment_id}/attachments/{attachment_id}/redact" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.attachments.redact_comment_attachment(ticket_id=123456, comment_id=654321, attachment_id=498483)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ticket_id`                                                         | *int*                                                               | :heavy_check_mark:                                                  | The ID of the ticket                                                |
| `comment_id`                                                        | *int*                                                               | :heavy_check_mark:                                                  | The ID of the comment                                               |
| `attachment_id`                                                     | *int*                                                               | :heavy_check_mark:                                                  | The ID of the attachment                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AttachmentResponse](../../models/attachmentresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## upload_files

Uploads a file that can be attached to a ticket comment. It doesn't attach the file to the comment. For details and examples, see [Attaching ticket comments with the API](/documentation/ticketing/using-the-zendesk-api/adding-ticket-attachments-with-the-api).

The endpoint has a required `filename` query parameter. The parameter specifies what the file will be named when attached to the ticket comment (to give the agent more context about the file). The parameter does not specify the file on the local system to be uploaded. While the two names can be different, their file extensions must be the same. If they don't match, the agent's browser or file reader could give an error when attempting to open the attachment.

The `Content-Type` header must contain a recognized MIME type that correctly describes the type of the uploaded file. Failing to send a recognized, correct type may cause undesired behavior. For example, in-browser audio playback may be interrupted by the browser's security mechanisms for MP3s uploaded with an incorrect type.

Adding multiple files to the same upload is handled by splitting requests and passing the API token received from the first request to each subsequent request. The token is valid for 60 minutes.

**Note**: Even if [private attachments](https://support.zendesk.com/hc/en-us/articles/204265396) are enabled in the Zendesk Support instance, uploaded files are visible to any authenticated user at the `content_URL` specified in the [JSON response](#json-format) until the upload token is consumed. Once a file is associated with a ticket or post, visibility is restricted to users with access to the ticket or post with the attachment.

#### Allowed For

* End users


### Example Usage

<!-- UsageSnippet language="python" operationID="UploadFiles" method="post" path="/api/v2/uploads" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.attachments.upload_files()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AttachmentUploadResponse](../../models/attachmentuploadresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_upload

#### Allowed for

* End Users


### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteUpload" method="delete" path="/api/v2/uploads/{token}" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    z_client.attachments.delete_upload(token="6bk3gql82em5nmf")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The token of the uploaded attachment                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |