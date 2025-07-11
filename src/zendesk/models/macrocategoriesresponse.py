"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class MacroCategoriesResponseTypedDict(TypedDict):
    categories: NotRequired[List[str]]


class MacroCategoriesResponse(BaseModel):
    categories: Optional[List[str]] = None
