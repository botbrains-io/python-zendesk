"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class AccountSettingsUserObjectTypedDict(TypedDict):
    r"""User settings. See [Users](#users)"""

    agent_created_welcome_emails: NotRequired[bool]
    end_user_phone_number_validation: NotRequired[bool]
    have_gravatars_enabled: NotRequired[bool]
    language_selection: NotRequired[bool]
    multiple_organizations: NotRequired[bool]
    tagging: NotRequired[bool]
    time_zone_selection: NotRequired[bool]


class AccountSettingsUserObject(BaseModel):
    r"""User settings. See [Users](#users)"""

    agent_created_welcome_emails: Optional[bool] = None

    end_user_phone_number_validation: Optional[bool] = None

    have_gravatars_enabled: Optional[bool] = None

    language_selection: Optional[bool] = None

    multiple_organizations: Optional[bool] = None

    tagging: Optional[bool] = None

    time_zone_selection: Optional[bool] = None
