# ChannelFramework

## Overview

### Available Operations

* [report_channelback_error](#report_channelback_error) - Report Channelback Error to Zendesk
* [push_content_to_support](#push_content_to_support) - Push Content to Support
* [validate_token](#validate_token) - Validate Token

## report_channelback_error

#### Allowed For

* Admins

#### Request parameters

The POST request takes a JSON object parameter which contains information about the
problematic [channelback](/documentation/channel_framework/understanding-the-channel-framework/channelback/).

| Name               | Type      | Required  | Comments
| ------------------ | ----------| --------- | -------------------
| instance_push_id   | string    | yes       | The ID of the account to which data will be pushed.  This was passed to the integration service when the administrator set up the account
| external_id        | string    | yes       | Unique identifier of the external resource from the original channelback (string)
| description        | string    | no        | A human readable description of the error
| request_id         | string    | no        | A unique identifier for the request


#### Response format

The response does not include a response body


### Example Usage

<!-- UsageSnippet language="python" operationID="ReportChannelbackError" method="post" path="/api/v2/any_channel/channelback/report_error" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.channel_framework.report_channelback_error()

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

## push_content_to_support

Pushes Channel framework content to Zendesk.

#### Allowed For

* Admins

#### Request parameters

The POST request takes a JSON object parameter which contains data about all
the resources that the client is pushing.

| Name               | Type      | Required  | Comments
| ------------------ | ----------| --------- | -------------------
| instance_push_id   | string    | yes       | The account ID where data will be pushed. This was passed to the integration service when the administrator set up the account
| request_id         | string    | no        | A unique identifier for the push request
| external_resources | array     | yes       | The [resources](#external_resource-object) to push

#### external_resource object

| Name               | Type                               | Max length | Mandatory | Comments
|------------------- | ---------------------------------- |------------| --------- | ----------
| external_id        | string                             | 255        | yes       | Unique identifier of the external resource. Must be ASCII characters
| internal_note      | boolean                            |            | no        | If true creates a new internal note comment
| message            | string                             | 65535      | yes       | Text to be converted to a ticket or comment
| html_message       | string                             | 65535      | no        | HTML version of message
| parent_id          | string                             | 511        | no        | Unique identifier of the external resource for which this is a response. Used to choose the correct thread. Responses may include `parent_id` or `thread_id`, but not both. See [Conversation threads](/documentation/channel_framework/understanding-the-channel-framework/pull_endpoint/#conversation-threads)
| thread_id          | string                             | 255        | no        | Arbitrary identifier of the thread to which this item should belong. Responses may include `parent_id` or `thread_id`, but not both. See [Conversation threads](/documentation/channel_framework/understanding-the-channel-framework/pull_endpoint/#conversation-threads)
| created_at         | string                             |            | yes       | When the resource was created in the origin system, as an ISO 8601 extended format date-time. Example: '2015-09-08T22:48:09Z'
| author             | object                             |            | yes       | See [author object](#author-object) below
| display_info       | array                              |            | no        | Array of integration-specific data used by apps to modify the agent UI. See [display_info object](#display_info-object) below
| allow_channelback  | boolean                            |            | no        | If false, prevents the agent from making additional comments on the message in the Zendesk interface
| fields             | array                              |            | no        | Array of ticket fields to set in Zendesk and their values. See [fields array](#fields-array)
| file_urls          | array                              | 10         | no        | Array of files to be imported into Zendesk. See [file urls](/documentation/channel_framework/understanding-the-channel-framework/pull_endpoint/#file-urls) in the Channel framework docs

#### author object

| Name        | Type   | Max chars | Mandatory | Comments
|------------ | ------ |---------- |---------- |-----------
| external_id | string | 255       | yes       | Unique identifier of the user in the origin service
| name        | string | 255       | no        | If not supplied, defaults to external id
| image_url   | string | 255       | no        | URL to an image for the user
| locale      | String | 255       | no        | The user's locale. Must be one of the supported [locales](/api-reference/ticketing/account-configuration/locales/#list-available-public-locales) in Zendesk
| fields      | array  |           | no        | Array of items containing user field identifier ('id') and value of field ('value'.)  For system fields ('notes' or 'details'), the identifier is the English name. For custom fields, the identifier may be the ID or the name

#### display_info object

| Name | Type   | Max chars | Mandatory | Comments
|----- | ------ |---------- |---------- |-----------
| type | string | 255       | yes       | Globally unique type identifier defined by the integration origin service. Examples: a GUID or URI
| data | string | 65535     | yes       | JSON data containing display hints

#### fields array

The `fields` array lists ticket fields to set in Zendesk and their values. Each item consists of a field identifier (`id`) and a value (`value`) for the field. For Zendesk system fields such as `subject`, the identifier is the English name. For custom fields, the identifier may be a field ID or a name. See [Ticket Fields](/api-reference/ticketing/tickets/ticket_fields/).

The `fields` array can only set ticket values on ticket creation, not on ticket updates.

#### Response format

The response is a JSON object containing a single key:

| Name      | Type     | Comments
| --------- | -------- | -------------------
| results   | array    | An array of [result objects](#result-object)

The `results` array contains an entry for each item in the incoming `external_resources` array, in the
same order.  For example, if you call `push` with 3 external resources, a successful response will include
`results` with three entries, corresponding to your 3 resources.

#### result object

| Name                 | Type                           | Comments
| -------------------- | ------------------------------ | -------------------
| external_resource_id | string                         | The external ID of the resource, as passed in
| status               | object                         | The status of the import for the indicated resource. See [status object](#status-object)

#### status object

| Name        | Type   | Comments
| ----------- | ------ | -------------------
| code        | string | A code indicating the status of the import of the resource, as described in [status codes](#status-codes)
| description | string | In the case of an exception, a description of the exception. Otherwise, not present.

#### status codes

| Key                                       | Description
| ----------------------------------------- | ----------------
| success                                   | The external resource was successfully converted to a ticket or comment
| already_imported                          | Reimport of the external resource was skipped due to a pre-existing ticket or comment for the resource
| could_not_locate_parent_external_resource | The parent resource, as identified by parent_id in the [request](#request-parameters), could not be found. The unrecognized parent ID is returned in the description of the [status](#status-object)
| processing_error                          | An internal exception occurred while processing the resource. See `description` in the [status object](#status-object)
| halted                                    | This resource was not processed because processing of previous resources failed


### Example Usage

<!-- UsageSnippet language="python" operationID="PushContentToSupport" method="post" path="/api/v2/any_channel/push" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.channel_framework.push_content_to_support()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChannelFrameworkPushResultsResponse](../../models/channelframeworkpushresultsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## validate_token

#### Allowed For

* Admins

#### Request parameters

The POST request takes a JSON object parameter which contains the token to be validated.

| Name               | Type      | Required  | Comments
| ------------------ | ----------| --------- | -------------------
| instance_push_id   | string    | yes       | The ID of the account to which data will be pushed. This was passed to the integration service when the administrator set up the account
| request_id         | string    | no        | A unique identifier for the push request

#### Response format

The response body is empty.


### Example Usage

<!-- UsageSnippet language="python" operationID="ValidateToken" method="post" path="/api/v2/any_channel/validate_token" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.channel_framework.validate_token()

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