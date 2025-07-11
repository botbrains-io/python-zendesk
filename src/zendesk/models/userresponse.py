"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .userobject import UserObject, UserObjectTypedDict
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class UserResponseTypedDict(TypedDict):
    user: NotRequired[UserObjectTypedDict]


class UserResponse(BaseModel):
    user: Optional[UserObject] = None
