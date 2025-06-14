"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .viewcountobject import ViewCountObject, ViewCountObjectTypedDict
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class ViewCountsResponseTypedDict(TypedDict):
    view_counts: NotRequired[List[ViewCountObjectTypedDict]]


class ViewCountsResponse(BaseModel):
    view_counts: Optional[List[ViewCountObject]] = None
