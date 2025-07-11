"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .essentialscardobject import EssentialsCardObject, EssentialsCardObjectTypedDict
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class EssentialsCardResponseTypedDict(TypedDict):
    object_layout: NotRequired[EssentialsCardObjectTypedDict]


class EssentialsCardResponse(BaseModel):
    object_layout: Optional[EssentialsCardObject] = None
