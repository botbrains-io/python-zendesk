# python-zendesk

Provided by botBrains. This SDK is generated for the [Zendesk Support API](https://developer.zendesk.com/api-reference/ticketing/introduction/) openapi spec (also known as Zendesk Ticketing API). We slightly modified it to comply with the OpenAPI spec and to work with the speakeasy codegen tool, as well as adding partial pagination support.

## How to regenerate the SDK

```bash
speakeasy run
find src/zendesk -type f -name "*.py" ! -name "enums.py" -exec sed -i '' 's/type=type,/type_=type_,/g' {} +
```

<!-- Start Summary [summary] -->

## Summary

Support API: Zendesk Support API endpoints

<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->

## Table of Contents

<!-- $toc-max-depth=2 -->

- [python-zendesk](#python-zendesk)
  - [How to regenerate the SDK](#how-to-regenerate-the-sdk)
  - [SDK Installation](#sdk-installation)
  - [IDE Support](#ide-support)
  - [SDK Example Usage](#sdk-example-usage)
  - [Authentication](#authentication)
  - [Available Resources and Operations](#available-resources-and-operations)
  - [Pagination](#pagination)
  - [Retries](#retries)
  - [Error Handling](#error-handling)
  - [Server Selection](#server-selection)
  - [Custom HTTP Client](#custom-http-client)
  - [Resource Management](#resource-management)
  - [Debugging](#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->

## SDK Installation

> [!NOTE] > **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either _pip_ or _poetry_ package managers.

### PIP

_PIP_ is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install python-zendesk
```

### Poetry

_Poetry_ is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add python-zendesk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from python-zendesk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "python-zendesk",
# ]
# ///

from zendesk import Zendesk

sdk = Zendesk(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.

<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->

## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->

## SDK Example Usage

### Example

```python
# Synchronous Example
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from zendesk import Zendesk, models

async def main():

    async with Zendesk(
        security=models.Security(
            username="",
            password="",
        ),
    ) as z_client:

        res = await z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search_async(name="Johnny Agent")

        # Handle response
        print(res)

asyncio.run(main())
```

<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->

## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                      | Type | Scheme     | Environment Variable                      |
| ------------------------- | ---- | ---------- | ----------------------------------------- |
| `username`<br/>`password` | http | HTTP Basic | `ZENDESK_USERNAME`<br/>`ZENDESK_PASSWORD` |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent")

    # Handle response
    print(res)

```

<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->

## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [account_settings](docs/sdks/accountsettings/README.md)

- [show_account_settings](docs/sdks/accountsettings/README.md#show_account_settings) - Show Settings
- [update_account_settings](docs/sdks/accountsettings/README.md#update_account_settings) - Update Account Settings

### [activity_stream](docs/sdks/activitystream/README.md)

- [list_activities](docs/sdks/activitystream/README.md#list_activities) - List Activities
- [show_activity](docs/sdks/activitystream/README.md#show_activity) - Show Activity
- [count_activities](docs/sdks/activitystream/README.md#count_activities) - Count Activities

### [approval_requests](docs/sdks/approvalrequests/README.md)

- [create_approval_request](docs/sdks/approvalrequests/README.md#create_approval_request) - Create an Approval Request
- [show_approval_request](docs/sdks/approvalrequests/README.md#show_approval_request) - Show Approval Request
- [update_decision_approval_request](docs/sdks/approvalrequests/README.md#update_decision_approval_request) - Update Approval Request Status
- [search_approvals](docs/sdks/approvalrequests/README.md#search_approvals) - Get Approvals by Approval Workflow Id

### [approval_workflow_instances](docs/sdks/approvalworkflowinstances/README.md)

- [create_approval_workflow_instance](docs/sdks/approvalworkflowinstances/README.md#create_approval_workflow_instance) - Create Approval Workflow Instance

### [assignee_field_assignable_agents](docs/sdks/assigneefieldassignableagents/README.md)

- [list_assignee_field_assignable_groups_and_agents_search](docs/sdks/assigneefieldassignableagents/README.md#list_assignee_field_assignable_groups_and_agents_search) - List assignable groups and agents based on query matched against name
- [list_assignee_field_assignable_groups](docs/sdks/assigneefieldassignableagents/README.md#list_assignee_field_assignable_groups) - List assignable groups on the AssigneeField
- [list_assignee_field_assignable_group_agents](docs/sdks/assigneefieldassignableagents/README.md#list_assignee_field_assignable_group_agents) - List assignable agents from a group on the AssigneeField

### [assignee_field_assignable_groups](docs/sdks/assigneefieldassignablegroups/README.md)

- [list_assignee_field_assignable_groups_and_agents_search](docs/sdks/assigneefieldassignablegroups/README.md#list_assignee_field_assignable_groups_and_agents_search) - List assignable groups and agents based on query matched against name

### [attachments](docs/sdks/attachments/README.md)

- [show_attachment](docs/sdks/attachments/README.md#show_attachment) - Show Attachment
- [update_attachment](docs/sdks/attachments/README.md#update_attachment) - Update Attachment for Malware
- [redact_comment_attachment](docs/sdks/attachments/README.md#redact_comment_attachment) - Redact Comment Attachment
- [upload_files](docs/sdks/attachments/README.md#upload_files) - Upload Files
- [delete_upload](docs/sdks/attachments/README.md#delete_upload) - Delete Upload

### [audit_logs](docs/sdks/auditlogs/README.md)

- [list_audit_logs](docs/sdks/auditlogs/README.md#list_audit_logs) - List Audit Logs
- [show_audit_log](docs/sdks/auditlogs/README.md#show_audit_log) - Show Audit Log
- [export_audit_logs](docs/sdks/auditlogs/README.md#export_audit_logs) - Export Audit Logs

### [automations](docs/sdks/automations/README.md)

- [list_automations](docs/sdks/automations/README.md#list_automations) - List Automations
- [create_automation](docs/sdks/automations/README.md#create_automation) - Create Automation
- [show_automation](docs/sdks/automations/README.md#show_automation) - Show Automation
- [update_automation](docs/sdks/automations/README.md#update_automation) - Update Automation
- [delete_automation](docs/sdks/automations/README.md#delete_automation) - Delete Automation
- [list_active_automations](docs/sdks/automations/README.md#list_active_automations) - List Active Automations
- [bulk_delete_automations](docs/sdks/automations/README.md#bulk_delete_automations) - Bulk Delete Automations
- [search_automations](docs/sdks/automations/README.md#search_automations) - Search Automations
- [update_many_automations](docs/sdks/automations/README.md#update_many_automations) - Update Many Automations

### [basics](docs/sdks/basics/README.md)

- [open_ticket_in_agent_browser](docs/sdks/basics/README.md#open_ticket_in_agent_browser) - Open Ticket in Agent's Browser
- [open_users_profile_in_agent_browser](docs/sdks/basics/README.md#open_users_profile_in_agent_browser) - Open a User's Profile in an Agent's Browser
- [create_ticket_or_voicemail_ticket](docs/sdks/basics/README.md#create_ticket_or_voicemail_ticket) - Create Ticket or Voicemail Ticket

### [bookmarks](docs/sdks/bookmarks/README.md)

- [list_bookmarks](docs/sdks/bookmarks/README.md#list_bookmarks) - List Bookmarks
- [create_bookmark](docs/sdks/bookmarks/README.md#create_bookmark) - Create Bookmark
- [delete_bookmark](docs/sdks/bookmarks/README.md#delete_bookmark) - Delete Bookmark

### [brand_agents](docs/sdks/brandagents/README.md)

- [list_brand_agents](docs/sdks/brandagents/README.md#list_brand_agents) - List Brand Agent Memberships
- [show_brand_agent_by_id](docs/sdks/brandagents/README.md#show_brand_agent_by_id) - Show Brand Agent Membership

### [brands](docs/sdks/brands/README.md)

- [list_brands](docs/sdks/brands/README.md#list_brands) - List Brands
- [create_brand](docs/sdks/brands/README.md#create_brand) - Create Brand
- [show_brand](docs/sdks/brands/README.md#show_brand) - Show a Brand
- [update_brand](docs/sdks/brands/README.md#update_brand) - Update a Brand
- [delete_brand](docs/sdks/brands/README.md#delete_brand) - Delete a Brand
- [check_host_mapping_validity_for_existing_brand](docs/sdks/brands/README.md#check_host_mapping_validity_for_existing_brand) - Check Host Mapping Validity for an Existing Brand
- [check_host_mapping_validity](docs/sdks/brands/README.md#check_host_mapping_validity) - Check Host Mapping Validity

### [channel_framework](docs/sdks/channelframework/README.md)

- [report_channelback_error](docs/sdks/channelframework/README.md#report_channelback_error) - Report Channelback Error to Zendesk
- [push_content_to_support](docs/sdks/channelframework/README.md#push_content_to_support) - Push Content to Support
- [validate_token](docs/sdks/channelframework/README.md#validate_token) - Validate Token

### [conversation_log](docs/sdks/conversationlog/README.md)

- [list_conversation_log_for_ticket](docs/sdks/conversationlog/README.md#list_conversation_log_for_ticket) - List Conversation log for Ticket

### [custom_object_fields](docs/sdks/customobjectfields/README.md)

- [list_custom_object_fields](docs/sdks/customobjectfields/README.md#list_custom_object_fields) - List Custom Object Fields
- [create_custom_object_field](docs/sdks/customobjectfields/README.md#create_custom_object_field) - Create Custom Object Field
- [show_custom_object_field](docs/sdks/customobjectfields/README.md#show_custom_object_field) - Show Custom Object Field
- [update_custom_object_field](docs/sdks/customobjectfields/README.md#update_custom_object_field) - Update Custom Object Field
- [delete_custom_object_field](docs/sdks/customobjectfields/README.md#delete_custom_object_field) - Delete Custom Object Field
- [reorder_custom_object_fields](docs/sdks/customobjectfields/README.md#reorder_custom_object_fields) - Reorder Custom Fields of an Object
- [custom_object_fields_limit](docs/sdks/customobjectfields/README.md#custom_object_fields_limit) - Custom Object Fields Limit

### [custom_object_records](docs/sdks/customobjectrecords/README.md)

- [custom_object_record_bulk_jobs](docs/sdks/customobjectrecords/README.md#custom_object_record_bulk_jobs) - Custom Object Record Bulk Jobs
- [list_custom_object_records](docs/sdks/customobjectrecords/README.md#list_custom_object_records) - List Custom Object Records
- [create_custom_object_record](docs/sdks/customobjectrecords/README.md#create_custom_object_record) - Create Custom Object Record
- [upsert_custom_object_record_by_external_id_or_name](docs/sdks/customobjectrecords/README.md#upsert_custom_object_record_by_external_id_or_name) - Set Custom Object Record by External Id Or Name
- [delete_custom_object_record_by_external_id_or_name](docs/sdks/customobjectrecords/README.md#delete_custom_object_record_by_external_id_or_name) - Delete Custom Object Record by External Id Or Name
- [show_custom_object_record](docs/sdks/customobjectrecords/README.md#show_custom_object_record) - Show Custom Object Record
- [update_custom_object_record](docs/sdks/customobjectrecords/README.md#update_custom_object_record) - Update Custom Object Record
- [delete_custom_object_record](docs/sdks/customobjectrecords/README.md#delete_custom_object_record) - Delete Custom Object Record
- [autocomplete_custom_object_record_search](docs/sdks/customobjectrecords/README.md#autocomplete_custom_object_record_search) - Autocomplete Custom Object Record Search
- [count_custom_object_records](docs/sdks/customobjectrecords/README.md#count_custom_object_records) - Count Custom Object Records
- [search_custom_object_records](docs/sdks/customobjectrecords/README.md#search_custom_object_records) - Search Custom Object Records
- [filtered_search_custom_object_records](docs/sdks/customobjectrecords/README.md#filtered_search_custom_object_records) - Filtered Search of Custom Object Records
- [custom_object_records_limit](docs/sdks/customobjectrecords/README.md#custom_object_records_limit) - Custom Object Records Limit

### [custom_objects](docs/sdks/customobjects/README.md)

- [list_custom_objects](docs/sdks/customobjects/README.md#list_custom_objects) - List Custom Objects
- [create_custom_object](docs/sdks/customobjects/README.md#create_custom_object) - Create Custom Object
- [show_custom_object](docs/sdks/customobjects/README.md#show_custom_object) - Show Custom Object
- [update_custom_object](docs/sdks/customobjects/README.md#update_custom_object) - Update Custom Object
- [delete_custom_object](docs/sdks/customobjects/README.md#delete_custom_object) - Delete Custom Object
- [custom_objects_limit](docs/sdks/customobjects/README.md#custom_objects_limit) - Custom Objects Limit

### [custom_roles](docs/sdks/customroles/README.md)

- [list_custom_roles](docs/sdks/customroles/README.md#list_custom_roles) - List Custom Roles
- [create_custom_role](docs/sdks/customroles/README.md#create_custom_role) - Create Custom Role
- [show_custom_role_by_id](docs/sdks/customroles/README.md#show_custom_role_by_id) - Show Custom Role
- [update_custom_role_by_id](docs/sdks/customroles/README.md#update_custom_role_by_id) - Update Custom Role
- [delete_custom_role_by_id](docs/sdks/customroles/README.md#delete_custom_role_by_id) - Delete Custom Role

### [custom_ticket_statuses](docs/sdks/customticketstatuses/README.md)

- [bulk_update_default_custom_status](docs/sdks/customticketstatuses/README.md#bulk_update_default_custom_status) - Bulk Update Default Custom Ticket Status
- [list_custom_statuses](docs/sdks/customticketstatuses/README.md#list_custom_statuses) - List Custom Ticket Statuses
- [create_custom_status](docs/sdks/customticketstatuses/README.md#create_custom_status) - Create Custom Ticket Status
- [show_custom_status](docs/sdks/customticketstatuses/README.md#show_custom_status) - Show Custom Ticket Status
- [update_custom_status](docs/sdks/customticketstatuses/README.md#update_custom_status) - Update Custom Ticket Status
- [create_ticket_form_statuses_for_custom_status](docs/sdks/customticketstatuses/README.md#create_ticket_form_statuses_for_custom_status) - Create Ticket Form Statuses for a Custom Status

### [deletion_schedules](docs/sdks/deletionschedules/README.md)

- [list_deletion_schedules](docs/sdks/deletionschedules/README.md#list_deletion_schedules) - List Deletion Schedules
- [create_deletion_schedule](docs/sdks/deletionschedules/README.md#create_deletion_schedule) - Create Deletion Schedule
- [get_deletion_schedule](docs/sdks/deletionschedules/README.md#get_deletion_schedule) - Get Deletion Schedule
- [update_deletion_schedule](docs/sdks/deletionschedules/README.md#update_deletion_schedule) - Update Deletion Schedule
- [delete_deletion_schedule](docs/sdks/deletionschedules/README.md#delete_deletion_schedule) - Delete Deletion Schedule

### [dynamic_content](docs/sdks/dynamiccontent/README.md)

- [list_dynamic_contents](docs/sdks/dynamiccontent/README.md#list_dynamic_contents) - List Items
- [create_dynamic_content](docs/sdks/dynamiccontent/README.md#create_dynamic_content) - Create Item
- [show_dynamic_content_item](docs/sdks/dynamiccontent/README.md#show_dynamic_content_item) - Show Item
- [update_dynamic_content_item](docs/sdks/dynamiccontent/README.md#update_dynamic_content_item) - Update Item
- [delete_dynamic_content_item](docs/sdks/dynamiccontent/README.md#delete_dynamic_content_item) - Delete Item
- [show_many_dynamic_contents](docs/sdks/dynamiccontent/README.md#show_many_dynamic_contents) - Show Many Items

### [dynamic_content_item_variants](docs/sdks/dynamiccontentitemvariants/README.md)

- [dynamic_content_list_variants](docs/sdks/dynamiccontentitemvariants/README.md#dynamic_content_list_variants) - List Variants
- [create_dynamic_content_variant](docs/sdks/dynamiccontentitemvariants/README.md#create_dynamic_content_variant) - Create Variant
- [show_dynamic_content_variant](docs/sdks/dynamiccontentitemvariants/README.md#show_dynamic_content_variant) - Show Variant
- [update_dynamic_content_variant](docs/sdks/dynamiccontentitemvariants/README.md#update_dynamic_content_variant) - Update Variant
- [delete_dynamic_content_variant](docs/sdks/dynamiccontentitemvariants/README.md#delete_dynamic_content_variant) - Delete Variant
- [create_many_dynamic_content_variants](docs/sdks/dynamiccontentitemvariants/README.md#create_many_dynamic_content_variants) - Create Many Variants
- [update_many_dynamic_content_variants](docs/sdks/dynamiccontentitemvariants/README.md#update_many_dynamic_content_variants) - Update Many Variants

### [email_notifications](docs/sdks/emailnotifications/README.md)

- [list_email_notifications](docs/sdks/emailnotifications/README.md#list_email_notifications) - List Email Notifications
- [show_email_notification](docs/sdks/emailnotifications/README.md#show_email_notification) - Show Email Notification
- [show_many_email_notifications](docs/sdks/emailnotifications/README.md#show_many_email_notifications) - Show Many Email Notifications

### [essentials_card](docs/sdks/essentialscard/README.md)

- [show_essentials_card](docs/sdks/essentialscard/README.md#show_essentials_card) - Show Essentials Card
- [update_essentials_card](docs/sdks/essentialscard/README.md#update_essentials_card) - Update Essentials Card
- [delete_essentials_card](docs/sdks/essentialscard/README.md#delete_essentials_card) - Delete Essentials Card
- [show_essentials_cards](docs/sdks/essentialscard/README.md#show_essentials_cards) - List of Essentials Cards

### [global_clients](docs/sdks/globalclients/README.md)

- [list_global_o_auth_clients](docs/sdks/globalclients/README.md#list_global_o_auth_clients) - List Global OAuth Clients

### [grant_type_tokens](docs/sdks/granttypetokens/README.md)

- [create_token_for_grant_type](docs/sdks/granttypetokens/README.md#create_token_for_grant_type) - Create Token for Grant Type

### [group_memberships](docs/sdks/groupmemberships/README.md)

- [list_group_memberships](docs/sdks/groupmemberships/README.md#list_group_memberships) - List Memberships
- [create_group_membership](docs/sdks/groupmemberships/README.md#create_group_membership) - Create Membership
- [show_group_membership_by_id](docs/sdks/groupmemberships/README.md#show_group_membership_by_id) - Show Membership
- [delete_group_membership](docs/sdks/groupmemberships/README.md#delete_group_membership) - Delete Membership
- [list_assignable_group_memberships](docs/sdks/groupmemberships/README.md#list_assignable_group_memberships) - List Assignable Memberships
- [group_membership_bulk_create](docs/sdks/groupmemberships/README.md#group_membership_bulk_create) - Bulk Create Memberships
- [group_membership_bulk_delete](docs/sdks/groupmemberships/README.md#group_membership_bulk_delete) - Bulk Delete Memberships
- [group_membership_set_default](docs/sdks/groupmemberships/README.md#group_membership_set_default) - Set Membership as Default

### [group_sla_policies](docs/sdks/groupslapolicies/README.md)

- [list_group_sla_policies](docs/sdks/groupslapolicies/README.md#list_group_sla_policies) - List Group SLA Policies
- [create_group_sla_policy](docs/sdks/groupslapolicies/README.md#create_group_sla_policy) - Create Group SLA Policy
- [show_group_sla_policy](docs/sdks/groupslapolicies/README.md#show_group_sla_policy) - Show Group SLA Policy
- [update_group_sla_policy](docs/sdks/groupslapolicies/README.md#update_group_sla_policy) - Update Group SLA Policy
- [delete_group_sla_policy](docs/sdks/groupslapolicies/README.md#delete_group_sla_policy) - Delete Group SLA Policy
- [retrieve_group_sla_policy_filter_definition_items](docs/sdks/groupslapolicies/README.md#retrieve_group_sla_policy_filter_definition_items) - Retrieve Supported Filter Definition Items
- [reorder_group_sla_policies](docs/sdks/groupslapolicies/README.md#reorder_group_sla_policies) - Reorder Group SLA Policies

### [groups](docs/sdks/groups/README.md)

- [list_groups](docs/sdks/groups/README.md#list_groups) - List Groups
- [create_group](docs/sdks/groups/README.md#create_group) - Create Group
- [show_group_by_id](docs/sdks/groups/README.md#show_group_by_id) - Show Group
- [update_group](docs/sdks/groups/README.md#update_group) - Update Group
- [delete_group](docs/sdks/groups/README.md#delete_group) - Delete Group
- [list_assignable_groups](docs/sdks/groups/README.md#list_assignable_groups) - List Assignable Groups
- [count_groups](docs/sdks/groups/README.md#count_groups) - Count Groups

### [incremental_export](docs/sdks/incrementalexport/README.md)

- [incremental_sample_export](docs/sdks/incrementalexport/README.md#incremental_sample_export) - Incremental Sample Export
- [incremental_organization_export](docs/sdks/incrementalexport/README.md#incremental_organization_export) - Incremental Organization Export
- [incremental_ticket_events](docs/sdks/incrementalexport/README.md#incremental_ticket_events) - Incremental Ticket Event Export
- [incremental_ticket_export_time](docs/sdks/incrementalexport/README.md#incremental_ticket_export_time) - Incremental Ticket Export, Time Based
- [incremental_ticket_export_cursor](docs/sdks/incrementalexport/README.md#incremental_ticket_export_cursor) - Incremental Ticket Export, Cursor Based
- [incremental_user_export_time](docs/sdks/incrementalexport/README.md#incremental_user_export_time) - Incremental User Export, Time Based
- [incremental_user_export_cursor](docs/sdks/incrementalexport/README.md#incremental_user_export_cursor) - Incremental User Export, Cursor Based

### [incremental_skill_based_routing](docs/sdks/incrementalskillbasedroutingsdk/README.md)

- [incremental_skil_based_routing_attribute_values_export](docs/sdks/incrementalskillbasedroutingsdk/README.md#incremental_skil_based_routing_attribute_values_export) - Incremental Attributes Values Export
- [incremental_skil_based_routing_attributes_export](docs/sdks/incrementalskillbasedroutingsdk/README.md#incremental_skil_based_routing_attributes_export) - Incremental Attributes Export
- [incremental_skil_based_routing_instance_values_export](docs/sdks/incrementalskillbasedroutingsdk/README.md#incremental_skil_based_routing_instance_values_export) - Incremental Instance Values Export

### [job_statuses](docs/sdks/jobstatuses/README.md)

- [list_job_statuses](docs/sdks/jobstatuses/README.md#list_job_statuses) - List Job Statuses
- [show_job_status](docs/sdks/jobstatuses/README.md#show_job_status) - Show Job Status
- [show_many_job_statuses](docs/sdks/jobstatuses/README.md#show_many_job_statuses) - Show Many Job Statuses
- [bulk_set_agent_attribute_values_job](docs/sdks/jobstatuses/README.md#bulk_set_agent_attribute_values_job) - Bulk Set Agent Attribute Values Job

### [locales](docs/sdks/locales/README.md)

- [list_locales](docs/sdks/locales/README.md#list_locales) - List Locales
- [show_locale_by_id](docs/sdks/locales/README.md#show_locale_by_id) - Show Locale
- [list_locales_for_agent](docs/sdks/locales/README.md#list_locales_for_agent) - List Locales for Agent
- [show_current_locale](docs/sdks/locales/README.md#show_current_locale) - Show Current Locale
- [detect_best_locale](docs/sdks/locales/README.md#detect_best_locale) - Detect Best Language for User
- [list_available_public_locales](docs/sdks/locales/README.md#list_available_public_locales) - List Available Public Locales

### [lookup_relationships](docs/sdks/lookuprelationships/README.md)

- [get_sources_by_target](docs/sdks/lookuprelationships/README.md#get_sources_by_target) - Get sources by target
- [get_relationship_filter_definitions](docs/sdks/lookuprelationships/README.md#get_relationship_filter_definitions) - Filter Definitions

### [macros](docs/sdks/macros/README.md)

- [list_macros](docs/sdks/macros/README.md#list_macros) - List Macros
- [create_macro](docs/sdks/macros/README.md#create_macro) - Create Macro
- [show_macro](docs/sdks/macros/README.md#show_macro) - Show Macro
- [update_macro](docs/sdks/macros/README.md#update_macro) - Update Macro
- [delete_macro](docs/sdks/macros/README.md#delete_macro) - Delete Macro
- [show_changes_to_ticket](docs/sdks/macros/README.md#show_changes_to_ticket) - Show Changes to Ticket
- [list_macro_attachments](docs/sdks/macros/README.md#list_macro_attachments) - List Macro Attachments
- [create_associated_macro_attachment](docs/sdks/macros/README.md#create_associated_macro_attachment) - Create Macro Attachment
- [list_macros_actions](docs/sdks/macros/README.md#list_macros_actions) - List Supported Actions for Macros
- [list_active_macros](docs/sdks/macros/README.md#list_active_macros) - List Active Macros
- [create_macro_attachment](docs/sdks/macros/README.md#create_macro_attachment) - Create Unassociated Macro Attachment
- [show_macro_attachment](docs/sdks/macros/README.md#show_macro_attachment) - Show Macro Attachment
- [list_macro_categories](docs/sdks/macros/README.md#list_macro_categories) - List Macro Categories
- [list_macro_action_definitions](docs/sdks/macros/README.md#list_macro_action_definitions) - List Macro Action Definitions
- [delete_many_macros](docs/sdks/macros/README.md#delete_many_macros) - Bulk Delete Macros
- [show_derived_macro](docs/sdks/macros/README.md#show_derived_macro) - Show Macro Replica
- [search_macro](docs/sdks/macros/README.md#search_macro) - Search Macros
- [update_many_macros](docs/sdks/macros/README.md#update_many_macros) - Update Many Macros
- [show_ticket_after_changes](docs/sdks/macros/README.md#show_ticket_after_changes) - Show Ticket After Changes

### [o_auth_clients](docs/sdks/oauthclients/README.md)

- [list_o_auth_clients](docs/sdks/oauthclients/README.md#list_o_auth_clients) - List Clients
- [create_o_auth_client](docs/sdks/oauthclients/README.md#create_o_auth_client) - Create Client
- [show_client](docs/sdks/oauthclients/README.md#show_client) - Show Client
- [update_client](docs/sdks/oauthclients/README.md#update_client) - Update Client
- [delete_client](docs/sdks/oauthclients/README.md#delete_client) - Delete Client
- [client_generate_secret](docs/sdks/oauthclients/README.md#client_generate_secret) - Generate Secret

### [o_auth_tokens](docs/sdks/oauthtokens/README.md)

- [list_o_auth_tokens](docs/sdks/oauthtokens/README.md#list_o_auth_tokens) - List Tokens
- [create_o_auth_token](docs/sdks/oauthtokens/README.md#create_o_auth_token) - Create Token
- [show_token](docs/sdks/oauthtokens/README.md#show_token) - Show Token
- [revoke_o_auth_token](docs/sdks/oauthtokens/README.md#revoke_o_auth_token) - Revoke Token

### [object_triggers](docs/sdks/objecttriggers/README.md)

- [list_object_triggers](docs/sdks/objecttriggers/README.md#list_object_triggers) - List Object Triggers
- [create_object_trigger](docs/sdks/objecttriggers/README.md#create_object_trigger) - Create Object Trigger
- [get_object_trigger](docs/sdks/objecttriggers/README.md#get_object_trigger) - Show Object Trigger
- [update_object_trigger](docs/sdks/objecttriggers/README.md#update_object_trigger) - Update Object Trigger
- [delete_object_trigger](docs/sdks/objecttriggers/README.md#delete_object_trigger) - Delete Object Trigger
- [list_active_object_triggers](docs/sdks/objecttriggers/README.md#list_active_object_triggers) - List Active Object Triggers
- [list_object_triggers_definitions](docs/sdks/objecttriggers/README.md#list_object_triggers_definitions) - List Object Trigger Action and Condition Definitions
- [delete_many_object_triggers](docs/sdks/objecttriggers/README.md#delete_many_object_triggers) - Delete Many Object Triggers
- [search_object_triggers](docs/sdks/objecttriggers/README.md#search_object_triggers) - Search Object Triggers
- [update_many_object_triggers](docs/sdks/objecttriggers/README.md#update_many_object_triggers) - Update Many Object Triggers

### [omnichannel_routing_queues](docs/sdks/omnichannelroutingqueues/README.md)

- [list_queues](docs/sdks/omnichannelroutingqueues/README.md#list_queues) - List queues
- [create_queue](docs/sdks/omnichannelroutingqueues/README.md#create_queue) - Create Queue
- [show_queue_by_id](docs/sdks/omnichannelroutingqueues/README.md#show_queue_by_id) - Show Queue
- [update_queue](docs/sdks/omnichannelroutingqueues/README.md#update_queue) - Update Queue
- [delete_queue](docs/sdks/omnichannelroutingqueues/README.md#delete_queue) - Delete Queue
- [list_queue_definitions](docs/sdks/omnichannelroutingqueues/README.md#list_queue_definitions) - List Queue Definitions
- [reorder_queues](docs/sdks/omnichannelroutingqueues/README.md#reorder_queues) - Reorder Queues

### [organization_fields](docs/sdks/organizationfieldssdk/README.md)

- [list_organization_fields](docs/sdks/organizationfieldssdk/README.md#list_organization_fields) - List Organization Fields
- [create_organization_field](docs/sdks/organizationfieldssdk/README.md#create_organization_field) - Create Organization Field
- [reorder_organization_field](docs/sdks/organizationfieldssdk/README.md#reorder_organization_field) - Reorder Organization Field

### [organization_memberships](docs/sdks/organizationmemberships/README.md)

- [list_organization_memberships](docs/sdks/organizationmemberships/README.md#list_organization_memberships) - List Memberships
- [create_organization_membership](docs/sdks/organizationmemberships/README.md#create_organization_membership) - Create Membership
- [show_organization_membership_by_id](docs/sdks/organizationmemberships/README.md#show_organization_membership_by_id) - Show Membership
- [delete_organization_membership](docs/sdks/organizationmemberships/README.md#delete_organization_membership) - Delete Membership
- [create_many_organization_memberships](docs/sdks/organizationmemberships/README.md#create_many_organization_memberships) - Create Many Memberships
- [delete_many_organization_memberships](docs/sdks/organizationmemberships/README.md#delete_many_organization_memberships) - Bulk Delete Memberships
- [set_organization_membership_as_default](docs/sdks/organizationmemberships/README.md#set_organization_membership_as_default) - Set Membership as Default
- [unassign_organization](docs/sdks/organizationmemberships/README.md#unassign_organization) - Unassign Organization
- [set_organization_as_default](docs/sdks/organizationmemberships/README.md#set_organization_as_default) - Set Organization as Default

### [organization_subscriptions](docs/sdks/organizationsubscriptions/README.md)

- [list_organization_subscriptions](docs/sdks/organizationsubscriptions/README.md#list_organization_subscriptions) - List Organization Subscriptions
- [create_organization_subscription](docs/sdks/organizationsubscriptions/README.md#create_organization_subscription) - Create Organization Subscription
- [show_organization_subscription](docs/sdks/organizationsubscriptions/README.md#show_organization_subscription) - Show Organization Subscription
- [delete_organization_subscription](docs/sdks/organizationsubscriptions/README.md#delete_organization_subscription) - Delete Organization Subscription

### [organizations](docs/sdks/organizations/README.md)

- [show_organization_merge](docs/sdks/organizations/README.md#show_organization_merge) - Show Organization Merge
- [list_organizations](docs/sdks/organizations/README.md#list_organizations) - List Organizations
- [create_organization](docs/sdks/organizations/README.md#create_organization) - Create Organization
- [show_organization](docs/sdks/organizations/README.md#show_organization) - Show Organization
- [update_organization](docs/sdks/organizations/README.md#update_organization) - Update Organization
- [delete_organization](docs/sdks/organizations/README.md#delete_organization) - Delete Organization
- [create_organization_merge](docs/sdks/organizations/README.md#create_organization_merge) - Merge Organization With Another Organization
- [list_organization_merges](docs/sdks/organizations/README.md#list_organization_merges) - List Organization Merges
- [organization_related](docs/sdks/organizations/README.md#organization_related) - Show Organization's Related Information
- [autocomplete_organizations](docs/sdks/organizations/README.md#autocomplete_organizations) - Autocomplete Organizations
- [count_organizations](docs/sdks/organizations/README.md#count_organizations) - Count Organizations
- [create_many_organizations](docs/sdks/organizations/README.md#create_many_organizations) - Create Many Organizations
- [create_or_update_organization](docs/sdks/organizations/README.md#create_or_update_organization) - Create Or Update Organization
- [delete_many_organizations](docs/sdks/organizations/README.md#delete_many_organizations) - Bulk Delete Organizations
- [search_organizations](docs/sdks/organizations/README.md#search_organizations) - Search Organizations
- [show_many_organizations](docs/sdks/organizations/README.md#show_many_organizations) - Show Many Organizations
- [update_many_organizations](docs/sdks/organizations/README.md#update_many_organizations) - Update Many Organizations

### [push_notification_devices](docs/sdks/pushnotificationdevices/README.md)

- [push_notification_devices](docs/sdks/pushnotificationdevices/README.md#push_notification_devices) - Bulk Unregister Push Notification Devices

### [requests](docs/sdks/requests/README.md)

- [list_requests](docs/sdks/requests/README.md#list_requests) - List Requests
- [create_request](docs/sdks/requests/README.md#create_request) - Create Request
- [show_request](docs/sdks/requests/README.md#show_request) - Show Request
- [update_request](docs/sdks/requests/README.md#update_request) - Update Request
- [list_comments](docs/sdks/requests/README.md#list_comments) - Listing Comments
- [show_comment](docs/sdks/requests/README.md#show_comment) - Getting Comments
- [search_requests](docs/sdks/requests/README.md#search_requests) - Search Requests

### [reseller](docs/sdks/reseller/README.md)

- [create_trial_account](docs/sdks/reseller/README.md#create_trial_account) - Create Trial Account
- [verify_subdomain_availability](docs/sdks/reseller/README.md#verify_subdomain_availability) - Verify Subdomain Availability

### [resource_collections](docs/sdks/resourcecollections/README.md)

- [list_resource_collections](docs/sdks/resourcecollections/README.md#list_resource_collections) - List Resource Collections
- [create_resource_collection](docs/sdks/resourcecollections/README.md#create_resource_collection) - Create Resource Collection
- [retrieve_resource_collection](docs/sdks/resourcecollections/README.md#retrieve_resource_collection) - Show Resource Collection
- [update_resource_collection](docs/sdks/resourcecollections/README.md#update_resource_collection) - Update Resource Collection
- [delete_resource_collection](docs/sdks/resourcecollections/README.md#delete_resource_collection) - Delete Resource Collection

### [satisfaction_ratings](docs/sdks/satisfactionratings/README.md)

- [list_satisfaction_ratings](docs/sdks/satisfactionratings/README.md#list_satisfaction_ratings) - List Satisfaction Ratings
- [show_satisfaction_rating](docs/sdks/satisfactionratings/README.md#show_satisfaction_rating) - Show Satisfaction Rating
- [count_satisfaction_ratings](docs/sdks/satisfactionratings/README.md#count_satisfaction_ratings) - Count Satisfaction Ratings
- [create_ticket_satisfaction_rating](docs/sdks/satisfactionratings/README.md#create_ticket_satisfaction_rating) - Create a Satisfaction Rating

### [satisfaction_reasons](docs/sdks/satisfactionreasons/README.md)

- [list_satisfaction_rating_reasons](docs/sdks/satisfactionreasons/README.md#list_satisfaction_rating_reasons) - List Reasons for Satisfaction Rating
- [show_satisfaction_ratings](docs/sdks/satisfactionreasons/README.md#show_satisfaction_ratings) - Show Reason for Satisfaction Rating

### [search](docs/sdks/search/README.md)

- [list_search_results](docs/sdks/search/README.md#list_search_results) - List Search Results
- [count_search_results](docs/sdks/search/README.md#count_search_results) - Show Results Count
- [export_search_results](docs/sdks/search/README.md#export_search_results) - Export Search Results

### [sessions](docs/sdks/sessions/README.md)

- [list_sessions](docs/sdks/sessions/README.md#list_sessions) - List Sessions
- [bulk_delete_sessions_by_user_id](docs/sdks/sessions/README.md#bulk_delete_sessions_by_user_id) - Bulk Delete Sessions
- [show_session](docs/sdks/sessions/README.md#show_session) - Show Session
- [delete_session](docs/sdks/sessions/README.md#delete_session) - Delete Session
- [delete_authenticated_session](docs/sdks/sessions/README.md#delete_authenticated_session) - Delete the Authenticated Session
- [show_currently_authenticated_session](docs/sdks/sessions/README.md#show_currently_authenticated_session) - Show the Currently Authenticated Session
- [renew_current_session](docs/sdks/sessions/README.md#renew_current_session) - Renew the current session

### [sharing_agreements](docs/sdks/sharingagreements/README.md)

- [list_sharing_agreements](docs/sdks/sharingagreements/README.md#list_sharing_agreements) - List Sharing Agreements
- [create_sharing_agreement](docs/sdks/sharingagreements/README.md#create_sharing_agreement) - Create Sharing Agreement
- [show_sharing_agreement](docs/sdks/sharingagreements/README.md#show_sharing_agreement) - Show a Sharing Agreement
- [update_sharing_agreement](docs/sdks/sharingagreements/README.md#update_sharing_agreement) - Update a Sharing Agreement
- [delete_sharing_agreement](docs/sdks/sharingagreements/README.md#delete_sharing_agreement) - Delete a Sharing Agreement

### [skill_based_routing](docs/sdks/skillbasedrouting/README.md)

- [list_a_gent_attribute_values](docs/sdks/skillbasedrouting/README.md#list_a_gent_attribute_values) - List Agent Attribute Values
- [set_agent_attribute_values](docs/sdks/skillbasedrouting/README.md#set_agent_attribute_values) - Set Agent Attribute Values
- [list_many_agents_attribute_values](docs/sdks/skillbasedrouting/README.md#list_many_agents_attribute_values) - List Attribute Values for Many Agents
- [bulk_set_agent_attribute_values_job](docs/sdks/skillbasedrouting/README.md#bulk_set_agent_attribute_values_job) - Bulk Set Agent Attribute Values Job
- [list_account_attributes](docs/sdks/skillbasedrouting/README.md#list_account_attributes) - List Account Attributes
- [create_attribute](docs/sdks/skillbasedrouting/README.md#create_attribute) - Create Attribute
- [show_attribute](docs/sdks/skillbasedrouting/README.md#show_attribute) - Show Attribute
- [update_attribute](docs/sdks/skillbasedrouting/README.md#update_attribute) - Update Attribute
- [delete_attribute](docs/sdks/skillbasedrouting/README.md#delete_attribute) - Delete Attribute
- [list_attribute_values](docs/sdks/skillbasedrouting/README.md#list_attribute_values) - List Attribute Values for an Attribute
- [create_attribute_value](docs/sdks/skillbasedrouting/README.md#create_attribute_value) - Create Attribute Value
- [show_attribute_value](docs/sdks/skillbasedrouting/README.md#show_attribute_value) - Show Attribute Value
- [update_attribute_value](docs/sdks/skillbasedrouting/README.md#update_attribute_value) - Update Attribute Value
- [delete_attribute_value](docs/sdks/skillbasedrouting/README.md#delete_attribute_value) - Delete Attribute Value
- [list_routing_attribute_definitions](docs/sdks/skillbasedrouting/README.md#list_routing_attribute_definitions) - List Routing Attribute Definitions
- [list_tickets_fullfilled_by_user](docs/sdks/skillbasedrouting/README.md#list_tickets_fullfilled_by_user) - List Tickets Fulfilled by a User
- [list_ticket_attribute_values](docs/sdks/skillbasedrouting/README.md#list_ticket_attribute_values) - List Ticket Attribute Values
- [set_ticket_attribute_values](docs/sdks/skillbasedrouting/README.md#set_ticket_attribute_values) - Set Ticket Attribute Values

### [sla_policies](docs/sdks/slapolicies/README.md)

- [list_sla_policies](docs/sdks/slapolicies/README.md#list_sla_policies) - List SLA Policies
- [create_sla_policy](docs/sdks/slapolicies/README.md#create_sla_policy) - Create SLA Policy
- [show_sla_policy](docs/sdks/slapolicies/README.md#show_sla_policy) - Show SLA Policy
- [update_sla_policy](docs/sdks/slapolicies/README.md#update_sla_policy) - Update SLA Policy
- [delete_sla_policy](docs/sdks/slapolicies/README.md#delete_sla_policy) - Delete SLA Policy
- [retrieve_sla_policy_filter_definition_items](docs/sdks/slapolicies/README.md#retrieve_sla_policy_filter_definition_items) - Retrieve Supported Filter Definition Items
- [reorder_sla_policies](docs/sdks/slapolicies/README.md#reorder_sla_policies) - Reorder SLA Policies

### [support_addresses](docs/sdks/supportaddresses/README.md)

- [list_support_addresses](docs/sdks/supportaddresses/README.md#list_support_addresses) - List Support Addresses
- [create_support_address](docs/sdks/supportaddresses/README.md#create_support_address) - Create Support Address
- [show_support_address](docs/sdks/supportaddresses/README.md#show_support_address) - Show Support Address
- [update_support_address](docs/sdks/supportaddresses/README.md#update_support_address) - Update Support Address
- [delete_recipient_address](docs/sdks/supportaddresses/README.md#delete_recipient_address) - Delete Support Address
- [verify_support_address_forwarding](docs/sdks/supportaddresses/README.md#verify_support_address_forwarding) - Verify Support Address Forwarding

### [suspended_tickets](docs/sdks/suspendedtickets/README.md)

- [list_suspended_tickets](docs/sdks/suspendedtickets/README.md#list_suspended_tickets) - List Suspended Tickets
- [show_suspended_tickets](docs/sdks/suspendedtickets/README.md#show_suspended_tickets) - Show Suspended Ticket
- [delete_suspended_ticket](docs/sdks/suspendedtickets/README.md#delete_suspended_ticket) - Delete Suspended Ticket
- [recover_suspended_ticket](docs/sdks/suspendedtickets/README.md#recover_suspended_ticket) - Recover Suspended Ticket
- [suspended_tickets_attachments](docs/sdks/suspendedtickets/README.md#suspended_tickets_attachments) - Suspended Ticket Attachments
- [delete_suspended_tickets](docs/sdks/suspendedtickets/README.md#delete_suspended_tickets) - Delete Multiple Suspended Tickets
- [export_suspended_tickets](docs/sdks/suspendedtickets/README.md#export_suspended_tickets) - Export Suspended Tickets
- [recover_suspended_tickets](docs/sdks/suspendedtickets/README.md#recover_suspended_tickets) - Recover Multiple Suspended Tickets

### [tags](docs/sdks/tags/README.md)

- [autocomplete_tags](docs/sdks/tags/README.md#autocomplete_tags) - Search Tags
- [list_tags](docs/sdks/tags/README.md#list_tags) - List Tags
- [count_tags](docs/sdks/tags/README.md#count_tags) - Count Tags
- [list_resource_tags](docs/sdks/tags/README.md#list_resource_tags) - List Resource Tags
- [set_tags_ticket](docs/sdks/tags/README.md#set_tags_ticket) - Set Tags
- [put_tags_ticket](docs/sdks/tags/README.md#put_tags_ticket) - Add Tags
- [delete_tags_ticket](docs/sdks/tags/README.md#delete_tags_ticket) - Remove Tags

### [target_failures](docs/sdks/targetfailures/README.md)

- [list_target_failures](docs/sdks/targetfailures/README.md#list_target_failures) - List Target Failures
- [show_target_failure](docs/sdks/targetfailures/README.md#show_target_failure) - Show Target Failure

### [targets](docs/sdks/targets/README.md)

- [list_targets](docs/sdks/targets/README.md#list_targets) - List Targets
- [create_target](docs/sdks/targets/README.md#create_target) - Create Target
- [show_target](docs/sdks/targets/README.md#show_target) - Show Target
- [update_target](docs/sdks/targets/README.md#update_target) - Update Target
- [delete_target](docs/sdks/targets/README.md#delete_target) - Delete Target

### [ticket_audits](docs/sdks/ticketaudits/README.md)

- [list_ticket_audits](docs/sdks/ticketaudits/README.md#list_ticket_audits) - List All Ticket Audits
- [list_audits_for_ticket](docs/sdks/ticketaudits/README.md#list_audits_for_ticket) - List Audits for a Ticket
- [show_ticket_audit](docs/sdks/ticketaudits/README.md#show_ticket_audit) - Show Audit
- [make_ticket_comment_private_from_audits](docs/sdks/ticketaudits/README.md#make_ticket_comment_private_from_audits) - Change a Comment From Public To Private
- [count_audits_for_ticket](docs/sdks/ticketaudits/README.md#count_audits_for_ticket) - Count Audits for a Ticket

### [ticket_comments](docs/sdks/ticketcomments/README.md)

- [redact_chat_comment_attachment](docs/sdks/ticketcomments/README.md#redact_chat_comment_attachment) - Redact Chat Comment Attachment
- [redact_chat_comment](docs/sdks/ticketcomments/README.md#redact_chat_comment) - Redact Chat Comment
- [redact_ticket_comment_in_agent_workspace](docs/sdks/ticketcomments/README.md#redact_ticket_comment_in_agent_workspace) - Redact Ticket Comment In Agent Workspace
- [list_ticket_comments](docs/sdks/ticketcomments/README.md#list_ticket_comments) - List Comments
- [make_ticket_comment_private](docs/sdks/ticketcomments/README.md#make_ticket_comment_private) - Make Comment Private
- [redact_string_in_comment](docs/sdks/ticketcomments/README.md#redact_string_in_comment) - Redact String in Comment
- [count_ticket_comments](docs/sdks/ticketcomments/README.md#count_ticket_comments) - Count Ticket Comments

### [ticket_fields](docs/sdks/ticketfields/README.md)

- [list_ticket_fields](docs/sdks/ticketfields/README.md#list_ticket_fields) - List Ticket Fields
- [create_ticket_field](docs/sdks/ticketfields/README.md#create_ticket_field) - Create Ticket Field
- [show_ticketfield](docs/sdks/ticketfields/README.md#show_ticketfield) - Show Ticket Field
- [update_ticket_field](docs/sdks/ticketfields/README.md#update_ticket_field) - Update Ticket Field
- [delete_ticket_field](docs/sdks/ticketfields/README.md#delete_ticket_field) - Delete Ticket Field
- [list_ticket_field_options](docs/sdks/ticketfields/README.md#list_ticket_field_options) - List Ticket Field Options
- [create_or_update_ticket_field_option](docs/sdks/ticketfields/README.md#create_or_update_ticket_field_option) - Create or Update Ticket Field Option
- [show_ticket_field_option](docs/sdks/ticketfields/README.md#show_ticket_field_option) - Show Ticket Field Option
- [delete_ticket_field_option](docs/sdks/ticketfields/README.md#delete_ticket_field_option) - Delete Ticket Field Option
- [count_ticket_fields](docs/sdks/ticketfields/README.md#count_ticket_fields) - Count Ticket Fields
- [reorder_ticket_fields](docs/sdks/ticketfields/README.md#reorder_ticket_fields) - Reorder Ticket Fields

### [ticket_form_statuses](docs/sdks/ticketformstatuses/README.md)

- [create_ticket_form_statuses_for_custom_status](docs/sdks/ticketformstatuses/README.md#create_ticket_form_statuses_for_custom_status) - Create Ticket Form Statuses for a Custom Status
- [list_ticket_form_statuses](docs/sdks/ticketformstatuses/README.md#list_ticket_form_statuses) - List Ticket Form Statuses
- [show_many_ticket_form_statuses](docs/sdks/ticketformstatuses/README.md#show_many_ticket_form_statuses) - Show Many Ticket Form Statuses
- [ticket_form_ticket_form_statuses](docs/sdks/ticketformstatuses/README.md#ticket_form_ticket_form_statuses) - List Ticket Form Statuses of a Ticket Form
- [create_ticket_form_statuses](docs/sdks/ticketformstatuses/README.md#create_ticket_form_statuses) - Create Ticket Form Statuses
- [update_ticket_form_statuses](docs/sdks/ticketformstatuses/README.md#update_ticket_form_statuses) - Bulk Update Ticket Form Statuses of a Ticket Form
- [delete_ticket_form_statuses](docs/sdks/ticketformstatuses/README.md#delete_ticket_form_statuses) - Delete Ticket Form Statuses
- [update_ticket_form_status_by_id](docs/sdks/ticketformstatuses/README.md#update_ticket_form_status_by_id) - Update Ticket Form Status By Id
- [delete_ticket_form_status_by_id](docs/sdks/ticketformstatuses/README.md#delete_ticket_form_status_by_id) - Delete Ticket Form Status By Id

### [ticket_forms](docs/sdks/ticketforms/README.md)

- [list_ticket_forms](docs/sdks/ticketforms/README.md#list_ticket_forms) - List Ticket Forms
- [create_ticket_form](docs/sdks/ticketforms/README.md#create_ticket_form) - Create Ticket Form
- [show_ticket_form](docs/sdks/ticketforms/README.md#show_ticket_form) - Show Ticket Form
- [update_ticket_form](docs/sdks/ticketforms/README.md#update_ticket_form) - Update Ticket Form
- [delete_ticket_form](docs/sdks/ticketforms/README.md#delete_ticket_form) - Delete Ticket Form
- [clone_ticket_form](docs/sdks/ticketforms/README.md#clone_ticket_form) - Clone an Already Existing Ticket Form
- [ticket_form_ticket_form_statuses](docs/sdks/ticketforms/README.md#ticket_form_ticket_form_statuses) - List Ticket Form Statuses of a Ticket Form
- [create_ticket_form_statuses](docs/sdks/ticketforms/README.md#create_ticket_form_statuses) - Create Ticket Form Statuses
- [update_ticket_form_statuses](docs/sdks/ticketforms/README.md#update_ticket_form_statuses) - Bulk Update Ticket Form Statuses of a Ticket Form
- [update_ticket_form_status_by_id](docs/sdks/ticketforms/README.md#update_ticket_form_status_by_id) - Update Ticket Form Status By Id
- [reorder_ticket_forms](docs/sdks/ticketforms/README.md#reorder_ticket_forms) - Reorder Ticket Forms
- [show_many_ticket_forms](docs/sdks/ticketforms/README.md#show_many_ticket_forms) - Show Many Ticket Forms

### [ticket_import](docs/sdks/ticketimport/README.md)

- [ticket_import](docs/sdks/ticketimport/README.md#ticket_import) - Ticket Import
- [ticket_bulk_import](docs/sdks/ticketimport/README.md#ticket_bulk_import) - Ticket Bulk Import

### [ticket_metric_events](docs/sdks/ticketmetricevents/README.md)

- [list_ticket_metric_events](docs/sdks/ticketmetricevents/README.md#list_ticket_metric_events) - List Ticket Metric Events

### [ticket_metrics](docs/sdks/ticketmetrics/README.md)

- [list_ticket_metrics](docs/sdks/ticketmetrics/README.md#list_ticket_metrics) - List Ticket Metrics
- [show_ticket_metrics](docs/sdks/ticketmetrics/README.md#show_ticket_metrics) - Show Ticket Metrics

### [ticket_skips](docs/sdks/ticketskips/README.md)

- [record_new_skip](docs/sdks/ticketskips/README.md#record_new_skip) - Record a New Skip for the Current User
- [list_ticket_skips](docs/sdks/ticketskips/README.md#list_ticket_skips) - List Ticket Skips

### [tickets](docs/sdks/tickets/README.md)

- [list_deleted_tickets](docs/sdks/tickets/README.md#list_deleted_tickets) - List Deleted Tickets
- [delete_ticket_permanently](docs/sdks/tickets/README.md#delete_ticket_permanently) - Delete Ticket Permanently
- [restore_deleted_ticket](docs/sdks/tickets/README.md#restore_deleted_ticket) - Restore a Previously Deleted Ticket
- [bulk_permanently_delete_tickets](docs/sdks/tickets/README.md#bulk_permanently_delete_tickets) - Delete Multiple Tickets Permanently
- [bulk_restore_deleted_tickets](docs/sdks/tickets/README.md#bulk_restore_deleted_tickets) - Restore Previously Deleted Tickets in Bulk
- [list_ticket_problems](docs/sdks/tickets/README.md#list_ticket_problems) - List Ticket Problems
- [autocomplete_problems](docs/sdks/tickets/README.md#autocomplete_problems) - Autocomplete Problems
- [list_tickets](docs/sdks/tickets/README.md#list_tickets) - List Tickets
- [create_ticket](docs/sdks/tickets/README.md#create_ticket) - Create Ticket
- [show_ticket](docs/sdks/tickets/README.md#show_ticket) - Show Ticket
- [update_ticket](docs/sdks/tickets/README.md#update_ticket) - Update Ticket
- [delete_ticket](docs/sdks/tickets/README.md#delete_ticket) - Delete Ticket
- [list_ticket_collaborators](docs/sdks/tickets/README.md#list_ticket_collaborators) - List Collaborators for a Ticket
- [list_ticket_email_c_cs](docs/sdks/tickets/README.md#list_ticket_email_c_cs) - List Email CCs for a Ticket
- [list_ticket_followers](docs/sdks/tickets/README.md#list_ticket_followers) - List Followers for a Ticket
- [list_ticket_incidents](docs/sdks/tickets/README.md#list_ticket_incidents) - List Ticket Incidents
- [mark_ticket_as_spam_and_suspend_requester](docs/sdks/tickets/README.md#mark_ticket_as_spam_and_suspend_requester) - Mark Ticket as Spam and Suspend Requester
- [merge_tickets_into_target_ticket](docs/sdks/tickets/README.md#merge_tickets_into_target_ticket) - Merge Tickets into Target Ticket
- [ticket_related_information](docs/sdks/tickets/README.md#ticket_related_information) - Ticket Related Information
- [count_tickets](docs/sdks/tickets/README.md#count_tickets) - Count Tickets
- [tickets_create_many](docs/sdks/tickets/README.md#tickets_create_many) - Create Many Tickets
- [bulk_delete_tickets](docs/sdks/tickets/README.md#bulk_delete_tickets) - Bulk Delete Tickets
- [mark_many_tickets_as_spam](docs/sdks/tickets/README.md#mark_many_tickets_as_spam) - Bulk Mark Tickets as Spam
- [tickets_show_many](docs/sdks/tickets/README.md#tickets_show_many) - Show Multiple Tickets
- [tickets_update_many](docs/sdks/tickets/README.md#tickets_update_many) - Update Many Tickets

### [trigger_categories](docs/sdks/triggercategories/README.md)

- [list_trigger_categories](docs/sdks/triggercategories/README.md#list_trigger_categories) - List Ticket Trigger Categories
- [create_trigger_category](docs/sdks/triggercategories/README.md#create_trigger_category) - Create Ticket Trigger Category
- [show_trigger_category_by_id](docs/sdks/triggercategories/README.md#show_trigger_category_by_id) - Show Ticket Trigger Category
- [update_trigger_category](docs/sdks/triggercategories/README.md#update_trigger_category) - Update Ticket Trigger Category
- [delete_trigger_category](docs/sdks/triggercategories/README.md#delete_trigger_category) - Delete Ticket Trigger Category
- [batch_operate_trigger_categories](docs/sdks/triggercategories/README.md#batch_operate_trigger_categories) - Create Batch Job for Ticket Trigger Categories

### [triggers](docs/sdks/triggers/README.md)

- [list_triggers](docs/sdks/triggers/README.md#list_triggers) - List Ticket Triggers
- [create_trigger](docs/sdks/triggers/README.md#create_trigger) - Create Trigger
- [get_trigger](docs/sdks/triggers/README.md#get_trigger) - Show Ticket Trigger
- [update_trigger](docs/sdks/triggers/README.md#update_trigger) - Update Ticket Trigger
- [delete_trigger](docs/sdks/triggers/README.md#delete_trigger) - Delete Ticket Trigger
- [list_trigger_revisions](docs/sdks/triggers/README.md#list_trigger_revisions) - List Ticket Trigger Revisions
- [trigger_revision](docs/sdks/triggers/README.md#trigger_revision) - Show Ticket Trigger Revision
- [list_active_triggers](docs/sdks/triggers/README.md#list_active_triggers) - List Active Ticket Triggers
- [list_trigger_action_condition_definitions](docs/sdks/triggers/README.md#list_trigger_action_condition_definitions) - List Ticket Trigger Action and Condition Definitions
- [delete_many_triggers](docs/sdks/triggers/README.md#delete_many_triggers) - Bulk Delete Ticket Triggers
- [reorder_triggers](docs/sdks/triggers/README.md#reorder_triggers) - Reorder Ticket Triggers
- [search_triggers](docs/sdks/triggers/README.md#search_triggers) - Search Ticket Triggers
- [update_many_triggers](docs/sdks/triggers/README.md#update_many_triggers) - Update Many Ticket Triggers

### [user_fields](docs/sdks/userfields/README.md)

- [list_user_fields](docs/sdks/userfields/README.md#list_user_fields) - List User Fields
- [create_user_field](docs/sdks/userfields/README.md#create_user_field) - Create User Field
- [reorder_user_field](docs/sdks/userfields/README.md#reorder_user_field) - Reorder User Field

### [user_identities](docs/sdks/useridentities/README.md)

- [list_user_identities](docs/sdks/useridentities/README.md#list_user_identities) - List Identities
- [create_user_identity](docs/sdks/useridentities/README.md#create_user_identity) - Create Identity
- [show_user_identity](docs/sdks/useridentities/README.md#show_user_identity) - Show Identity
- [update_user_identity](docs/sdks/useridentities/README.md#update_user_identity) - Update Identity
- [delete_user_identity](docs/sdks/useridentities/README.md#delete_user_identity) - Delete Identity
- [make_user_identity_primary](docs/sdks/useridentities/README.md#make_user_identity_primary) - Make Identity Primary
- [request_user_verfication](docs/sdks/useridentities/README.md#request_user_verfication) - Request User Verification
- [verify_user_identity](docs/sdks/useridentities/README.md#verify_user_identity) - Verify Identity

### [user_passwords](docs/sdks/userpasswords/README.md)

- [set_user_password](docs/sdks/userpasswords/README.md#set_user_password) - Set a User's Password
- [change_own_password](docs/sdks/userpasswords/README.md#change_own_password) - Change Your Password
- [get_user_password_requirements](docs/sdks/userpasswords/README.md#get_user_password_requirements) - List password requirements

### [users](docs/sdks/userssdk/README.md)

- [list_deleted_users](docs/sdks/userssdk/README.md#list_deleted_users) - List Deleted Users
- [show_deleted_user](docs/sdks/userssdk/README.md#show_deleted_user) - Show Deleted User
- [permanently_delete_user](docs/sdks/userssdk/README.md#permanently_delete_user) - Permanently Delete User
- [count_deleted_users](docs/sdks/userssdk/README.md#count_deleted_users) - Count Deleted Users
- [list_users](docs/sdks/userssdk/README.md#list_users) - List Users
- [create_user](docs/sdks/userssdk/README.md#create_user) - Create User
- [show_user](docs/sdks/userssdk/README.md#show_user) - Show User
- [update_user](docs/sdks/userssdk/README.md#update_user) - Update User
- [delete_user](docs/sdks/userssdk/README.md#delete_user) - Delete User
- [show_user_compliance_deletion_statuses](docs/sdks/userssdk/README.md#show_user_compliance_deletion_statuses) - Show Compliance Deletion Statuses
- [merge_end_users](docs/sdks/userssdk/README.md#merge_end_users) - Merge End Users
- [show_user_related](docs/sdks/userssdk/README.md#show_user_related) - Show User Related Information
- [autocomplete_users](docs/sdks/userssdk/README.md#autocomplete_users) - Autocomplete Users
- [count_users](docs/sdks/userssdk/README.md#count_users) - Count Users
- [create_many_users](docs/sdks/userssdk/README.md#create_many_users) - Create Many Users
- [create_or_update_user](docs/sdks/userssdk/README.md#create_or_update_user) - Create Or Update User
- [create_or_update_many_users](docs/sdks/userssdk/README.md#create_or_update_many_users) - Create Or Update Many Users
- [destroy_many_users](docs/sdks/userssdk/README.md#destroy_many_users) - Bulk Delete Users
- [logout_many_users](docs/sdks/userssdk/README.md#logout_many_users) - Logout many users
- [show_current_user](docs/sdks/userssdk/README.md#show_current_user) - Show Self
- [request_user_create](docs/sdks/userssdk/README.md#request_user_create) - Request User Create
- [search_users](docs/sdks/userssdk/README.md#search_users) - Search Users
- [show_many_users](docs/sdks/userssdk/README.md#show_many_users) - Show Many Users
- [update_many_users](docs/sdks/userssdk/README.md#update_many_users) - Update Many Users

### [views](docs/sdks/views/README.md)

- [list_views](docs/sdks/views/README.md#list_views) - List Views
- [create_view](docs/sdks/views/README.md#create_view) - Create View
- [show_view](docs/sdks/views/README.md#show_view) - Show View
- [update_view](docs/sdks/views/README.md#update_view) - Update View
- [delete_view](docs/sdks/views/README.md#delete_view) - Delete View
- [get_view_count](docs/sdks/views/README.md#get_view_count) - Count Tickets in View
- [execute_view](docs/sdks/views/README.md#execute_view) - Execute View
- [export_view](docs/sdks/views/README.md#export_view) - Export View
- [list_tickets_from_view](docs/sdks/views/README.md#list_tickets_from_view) - List Tickets From a View
- [list_active_views](docs/sdks/views/README.md#list_active_views) - List Active Views
- [list_compact_views](docs/sdks/views/README.md#list_compact_views) - List Views - Compact
- [count_views](docs/sdks/views/README.md#count_views) - Count Views
- [get_view_counts](docs/sdks/views/README.md#get_view_counts) - Count Tickets in Views
- [bulk_delete_views](docs/sdks/views/README.md#bulk_delete_views) - Bulk Delete Views
- [preview_views](docs/sdks/views/README.md#preview_views) - Preview Views
- [preview_count](docs/sdks/views/README.md#preview_count) - Preview Ticket Count
- [search_views](docs/sdks/views/README.md#search_views) - Search Views
- [list_views_by_id](docs/sdks/views/README.md#list_views_by_id) - List Views By ID
- [update_many_views](docs/sdks/views/README.md#update_many_views) - Update Many Views

### [webhook_invocations](docs/sdks/webhookinvocations/README.md)

- [list_webhook_invocations](docs/sdks/webhookinvocations/README.md#list_webhook_invocations) - List Webhook Invocations
- [list_webhook_invocation_attempts](docs/sdks/webhookinvocations/README.md#list_webhook_invocation_attempts) - List Webhook Invocation Attempts

### [webhook_security](docs/sdks/webhooksecurity/README.md)

- [show_webhook_signing_secret](docs/sdks/webhooksecurity/README.md#show_webhook_signing_secret) - Show Webhook Signing Secret
- [reset_webhook_signing_secret](docs/sdks/webhooksecurity/README.md#reset_webhook_signing_secret) - Reset Webhook Signing Secret

### [webhooks](docs/sdks/webhooks/README.md)

- [list_webhooks](docs/sdks/webhooks/README.md#list_webhooks) - List Webhooks
- [create_or_clone_webhook](docs/sdks/webhooks/README.md#create_or_clone_webhook) - Create or Clone Webhook
- [test_webhook](docs/sdks/webhooks/README.md#test_webhook) - Test Webhook
- [show_webhook](docs/sdks/webhooks/README.md#show_webhook) - Show Webhook
- [update_webhook](docs/sdks/webhooks/README.md#update_webhook) - Update Webhook
- [patch_webhook](docs/sdks/webhooks/README.md#patch_webhook) - Patch Webhook
- [delete_webhook](docs/sdks/webhooks/README.md#delete_webhook) - Delete Webhook

### [workspaces](docs/sdks/workspaces/README.md)

- [list_workspaces](docs/sdks/workspaces/README.md#list_workspaces) - List Workspaces
- [create_workspace](docs/sdks/workspaces/README.md#create_workspace) - Create Workspace
- [show_workspace](docs/sdks/workspaces/README.md#show_workspace) - Show Workspace
- [update_workspace](docs/sdks/workspaces/README.md#update_workspace) - Update Workspace
- [delete_workspace](docs/sdks/workspaces/README.md#delete_workspace) - Delete Workspace
- [destroy_many_workspaces](docs/sdks/workspaces/README.md#destroy_many_workspaces) - Bulk Delete Workspaces
- [reorder_workspaces](docs/sdks/workspaces/README.md#reorder_workspaces) - Reorder Workspaces

### [x_channel](docs/sdks/xchannel/README.md)

- [list_monitored_twitter_handles](docs/sdks/xchannel/README.md#list_monitored_twitter_handles) - List Monitored X Handles
- [show_monitored_twitter_handle](docs/sdks/xchannel/README.md#show_monitored_twitter_handle) - Show Monitored X Handle
- [create_ticket_from_tweet](docs/sdks/xchannel/README.md#create_ticket_from_tweet) - Create Ticket from Tweet
- [getting_twicket_status](docs/sdks/xchannel/README.md#getting_twicket_status) - List Ticket statuses

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Pagination [pagination] -->

## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:

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

<!-- End Pagination [pagination] -->

<!-- Start Retries [retries] -->

## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:

```python
from zendesk import Zendesk, models
from zendesk.utils import BackoffStrategy, RetryConfig


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent",
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:

```python
from zendesk import Zendesk, models
from zendesk.utils import BackoffStrategy, RetryConfig


with Zendesk(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent")

    # Handle response
    print(res)

```

<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->

## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.APIError exception, which has the following properties:

| Property        | Type             | Description           |
| --------------- | ---------------- | --------------------- |
| `.status_code`  | _int_            | The HTTP status code  |
| `.message`      | _str_            | The error message     |
| `.raw_response` | _httpx.Response_ | The raw HTTP response |
| `.body`         | _str_            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective _Errors_ tables in SDK docs for more details on possible exception types for each operation. For example, the `bulk_set_agent_attribute_values_job_async` method may raise the following exceptions:

| Error Type                                   | Status Code | Content Type     |
| -------------------------------------------- | ----------- | ---------------- |
| errors.SkillBasedRoutingAttributeValuesError | 400         | application/json |
| errors.APIError                              | 4XX, 5XX    | \*/\*            |

### Example

```python
from zendesk import Zendesk, errors, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:
    res = None
    try:

        res = z_client.job_statuses.bulk_set_agent_attribute_values_job(job={
            "attributes": {
                "attribute_values": [
                    {},
                ],
            },
        })

        # Handle response
        print(res)

    except errors.SkillBasedRoutingAttributeValuesError as e:
        # handle e.data: errors.SkillBasedRoutingAttributeValuesErrorData
        raise(e)
    except errors.APIError as e:
        # handle exception
        raise(e)
```

<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->

## Server Selection

### Server Variables

The default server `https://{subdomain}.{domain}.com` contains variables and is set to `https://example.zendesk.com` by default. To override default values, the following parameters are available when initializing the SDK client instance:

| Variable    | Parameter        | Default     | Description |
| ----------- | ---------------- | ----------- | ----------- |
| `domain`    | `domain: str`    | `"zendesk"` |             |
| `subdomain` | `subdomain: str` | `"example"` |             |

#### Example

```python
from zendesk import Zendesk, models


with Zendesk(
    domain="unwelcome-bidet.info"
    subdomain="<value>"
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent")

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:

```python
from zendesk import Zendesk, models


with Zendesk(
    server_url="https://example.zendesk.com",
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent")

    # Handle response
    print(res)

```

<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->

## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library. In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:

```python
from zendesk import Zendesk
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Zendesk(client=http_client)
```

or you could wrap the client with your own custom logic:

```python
from zendesk import Zendesk
from zendesk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Zendesk(async_client=CustomClient(httpx.AsyncClient()))
```

<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->

## Resource Management

The `Zendesk` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from zendesk import Zendesk, models
def main():

    with Zendesk(
        security=models.Security(
            username="",
            password="",
        ),
    ) as z_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Zendesk(
        security=models.Security(
            username="",
            password="",
        ),
    ) as z_client:
        # Rest of application here...
```

<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->

## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.

```python
from zendesk import Zendesk
import logging

logging.basicConfig(level=logging.DEBUG)
s = Zendesk(debug_logger=logging.getLogger("zendesk"))
```

You can also enable a default debug logger by setting an environment variable `ZENDESK_DEBUG` to true.

<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->
