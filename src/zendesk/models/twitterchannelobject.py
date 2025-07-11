"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TwitterChannelObjectTypedDict(TypedDict):
    id: int
    r"""Automatically assigned upon creation"""
    screen_name: str
    r"""The X handle"""
    twitter_user_id: int
    r"""The country's code"""
    allow_reply: NotRequired[bool]
    r"""If replies are allowed for this handle"""
    avatar_url: NotRequired[str]
    r"""The profile image url of the handle"""
    brand_id: NotRequired[int]
    r"""What brand the handle is associated with"""
    can_reply: NotRequired[bool]
    r"""If replies are allowed for this handle"""
    created_at: NotRequired[datetime]
    r"""The time the handle was created"""
    name: NotRequired[str]
    r"""The profile name of the handle"""
    updated_at: NotRequired[datetime]
    r"""The time of the last update of the handle"""


class TwitterChannelObject(BaseModel):
    id: int
    r"""Automatically assigned upon creation"""

    screen_name: str
    r"""The X handle"""

    twitter_user_id: int
    r"""The country's code"""

    allow_reply: Optional[bool] = None
    r"""If replies are allowed for this handle"""

    avatar_url: Optional[str] = None
    r"""The profile image url of the handle"""

    brand_id: Optional[int] = None
    r"""What brand the handle is associated with"""

    can_reply: Optional[bool] = None
    r"""If replies are allowed for this handle"""

    created_at: Optional[datetime] = None
    r"""The time the handle was created"""

    name: Optional[str] = None
    r"""The profile name of the handle"""

    updated_at: Optional[datetime] = None
    r"""The time of the last update of the handle"""
