"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class ApprovalRequestUserPhotoTypedDict(TypedDict):
    r"""Details for the approval request"""

    content_url: NotRequired[str]
    r"""URL for the user's photo"""


class ApprovalRequestUserPhoto(BaseModel):
    r"""Details for the approval request"""

    content_url: Optional[str] = None
    r"""URL for the user's photo"""


class ApprovalRequestUserTypedDict(TypedDict):
    id: NotRequired[int]
    r"""Unique identifier for the user"""
    name: NotRequired[str]
    r"""Name of the user"""
    photo: NotRequired[ApprovalRequestUserPhotoTypedDict]
    r"""Details for the approval request"""


class ApprovalRequestUser(BaseModel):
    id: Optional[int] = None
    r"""Unique identifier for the user"""

    name: Optional[str] = None
    r"""Name of the user"""

    photo: Optional[ApprovalRequestUserPhoto] = None
    r"""Details for the approval request"""
