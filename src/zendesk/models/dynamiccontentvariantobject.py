"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class DynamicContentVariantObjectTypedDict(TypedDict):
    content: str
    r"""The content of the variant"""
    locale_id: int
    r"""An active locale"""
    active: NotRequired[bool]
    r"""If the variant is active and useable"""
    created_at: NotRequired[datetime]
    r"""When the variant was created"""
    default: NotRequired[bool]
    r"""If the variant is the default for the item it belongs to"""
    id: NotRequired[int]
    r"""Automatically assigned when the variant is created"""
    outdated: NotRequired[bool]
    r"""If the variant is outdated"""
    updated_at: NotRequired[datetime]
    r"""When the variant was last updated"""
    url: NotRequired[str]
    r"""The API url of the variant"""


class DynamicContentVariantObject(BaseModel):
    content: str
    r"""The content of the variant"""

    locale_id: int
    r"""An active locale"""

    active: Optional[bool] = None
    r"""If the variant is active and useable"""

    created_at: Optional[datetime] = None
    r"""When the variant was created"""

    default: Optional[bool] = None
    r"""If the variant is the default for the item it belongs to"""

    id: Optional[int] = None
    r"""Automatically assigned when the variant is created"""

    outdated: Optional[bool] = None
    r"""If the variant is outdated"""

    updated_at: Optional[datetime] = None
    r"""When the variant was last updated"""

    url: Optional[str] = None
    r"""The API url of the variant"""
