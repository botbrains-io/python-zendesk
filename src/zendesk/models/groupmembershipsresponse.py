"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .groupmembershipobject import GroupMembershipObject, GroupMembershipObjectTypedDict
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class GroupMembershipsResponseTypedDict(TypedDict):
    group_memberships: NotRequired[List[GroupMembershipObjectTypedDict]]


class GroupMembershipsResponse(BaseModel):
    group_memberships: Optional[List[GroupMembershipObject]] = None
