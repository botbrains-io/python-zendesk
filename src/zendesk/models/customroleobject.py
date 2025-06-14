"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customroleconfigurationobject import (
    CustomRoleConfigurationObject,
    CustomRoleConfigurationObjectTypedDict,
)
from datetime import datetime
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class CustomRoleObjectTypedDict(TypedDict):
    name: str
    r"""Name of the custom role"""
    role_type: int
    r"""The user's role. 0 stands for a custom agent, 1 for a light agent, 2 for a chat agent, 3 for a contributor, 4 for an admin and 5 for a billing admin. See [Understanding standard agent roles in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4409155971354-Understanding-standard-agent-roles-in-Zendesk-Support) in Zendesk help"""
    configuration: NotRequired[CustomRoleConfigurationObjectTypedDict]
    r"""Configuration settings for the role. See [Configuration](#configuration)"""
    created_at: NotRequired[datetime]
    r"""The time the record was created"""
    description: NotRequired[str]
    r"""A description of the role"""
    id: NotRequired[int]
    r"""Automatically assigned on creation"""
    team_member_count: NotRequired[int]
    r"""The number of team members assigned to this role"""
    updated_at: NotRequired[datetime]
    r"""The time the record was last updated"""


class CustomRoleObject(BaseModel):
    name: str
    r"""Name of the custom role"""

    role_type: int
    r"""The user's role. 0 stands for a custom agent, 1 for a light agent, 2 for a chat agent, 3 for a contributor, 4 for an admin and 5 for a billing admin. See [Understanding standard agent roles in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4409155971354-Understanding-standard-agent-roles-in-Zendesk-Support) in Zendesk help"""

    configuration: Optional[CustomRoleConfigurationObject] = None
    r"""Configuration settings for the role. See [Configuration](#configuration)"""

    created_at: Optional[datetime] = None
    r"""The time the record was created"""

    description: Optional[str] = None
    r"""A description of the role"""

    id: Optional[int] = None
    r"""Automatically assigned on creation"""

    team_member_count: Optional[int] = None
    r"""The number of team members assigned to this role"""

    updated_at: Optional[datetime] = None
    r"""The time the record was last updated"""
