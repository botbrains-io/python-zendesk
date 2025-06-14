"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from typing import Mapping, Optional
from zendesk import errors, models, utils
from zendesk._hooks import HookContext
from zendesk.types import OptionalNullable, UNSET
from zendesk.utils import get_security_from_env


class ChannelFramework(BaseSDK):
    def report_channelback_error(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> str:
        r"""Report Channelback Error to Zendesk

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


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        req = self._build_request(
            method="POST",
            path="/api/v2/any_channel/channelback/report_error",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="ReportChannelbackError",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, str)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def report_channelback_error_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> str:
        r"""Report Channelback Error to Zendesk

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


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        req = self._build_request_async(
            method="POST",
            path="/api/v2/any_channel/channelback/report_error",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="ReportChannelbackError",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, str)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def push_content_to_support(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ChannelFrameworkPushResultsResponse:
        r"""Push Content to Support

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


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        req = self._build_request(
            method="POST",
            path="/api/v2/any_channel/push",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="PushContentToSupport",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.ChannelFrameworkPushResultsResponse
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def push_content_to_support_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.ChannelFrameworkPushResultsResponse:
        r"""Push Content to Support

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


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        req = self._build_request_async(
            method="POST",
            path="/api/v2/any_channel/push",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="PushContentToSupport",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.ChannelFrameworkPushResultsResponse
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def validate_token(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> str:
        r"""Validate Token

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


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        req = self._build_request(
            method="POST",
            path="/api/v2/any_channel/validate_token",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="ValidateToken",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, str)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise errors.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def validate_token_async(
        self,
        *,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> str:
        r"""Validate Token

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


        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)
        req = self._build_request_async(
            method="POST",
            path="/api/v2/any_channel/validate_token",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="ValidateToken",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, str)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise errors.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
