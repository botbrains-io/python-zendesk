"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dynamiccontentobject import DynamicContentObject, DynamicContentObjectTypedDict
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class DynamicContentResponseTypedDict(TypedDict):
    item: NotRequired[DynamicContentObjectTypedDict]


class DynamicContentResponse(BaseModel):
    item: Optional[DynamicContentObject] = None
