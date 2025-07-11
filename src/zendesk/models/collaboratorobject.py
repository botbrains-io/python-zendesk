"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class CollaboratorObjectTypedDict(TypedDict):
    email: NotRequired[str]
    name: NotRequired[str]


class CollaboratorObject(BaseModel):
    email: Optional[str] = None

    name: Optional[str] = None
