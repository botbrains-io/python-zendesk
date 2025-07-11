"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .groupobject import GroupObject, GroupObjectTypedDict
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class GroupsResponseTypedDict(TypedDict):
    groups: NotRequired[List[GroupObjectTypedDict]]


class GroupsResponse(BaseModel):
    groups: Optional[List[GroupObject]] = None
