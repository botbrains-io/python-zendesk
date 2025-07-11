"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class GroupMembershipTypedDict(TypedDict):
    user_id: int
    r"""The id of an agent"""
    group_id: int
    r"""The id of a group"""
    default: NotRequired[bool]
    r"""If true, tickets assigned directly to the agent will assume this membership's group"""


class GroupMembership(BaseModel):
    user_id: int
    r"""The id of an agent"""

    group_id: int
    r"""The id of a group"""

    default: Optional[bool] = False
    r"""If true, tickets assigned directly to the agent will assume this membership's group"""


class GroupMembershipRequestTypedDict(TypedDict):
    group_membership: GroupMembershipTypedDict


class GroupMembershipRequest(BaseModel):
    group_membership: GroupMembership
