"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .bookmarkobject import BookmarkObject, BookmarkObjectTypedDict
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class BookmarkResponseTypedDict(TypedDict):
    bookmark: NotRequired[BookmarkObjectTypedDict]


class BookmarkResponse(BaseModel):
    bookmark: Optional[BookmarkObject] = None
