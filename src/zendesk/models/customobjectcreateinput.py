"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class CustomObjectCreateInputTypedDict(TypedDict):
    key: NotRequired[str]
    r"""Unique identifier. Writable on create only"""
    title: NotRequired[str]
    r"""Display name for the object"""
    title_pluralized: NotRequired[str]
    r"""Pluralized version of the object's title"""


class CustomObjectCreateInput(BaseModel):
    key: Optional[str] = None
    r"""Unique identifier. Writable on create only"""

    title: Optional[str] = None
    r"""Display name for the object"""

    title_pluralized: Optional[str] = None
    r"""Pluralized version of the object's title"""
