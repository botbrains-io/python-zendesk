"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TriggerCategoryRequestTypedDict(TypedDict):
    name: NotRequired[str]
    position: NotRequired[int]


class TriggerCategoryRequest(BaseModel):
    name: Optional[str] = None

    position: Optional[int] = None
