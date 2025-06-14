"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class CountOrganizationObjectTypedDict(TypedDict):
    refreshed_at: NotRequired[str]
    value: NotRequired[int]


class CountOrganizationObject(BaseModel):
    refreshed_at: Optional[str] = None

    value: Optional[int] = None
