"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customstatuscreateinput import (
    CustomStatusCreateInput,
    CustomStatusCreateInputTypedDict,
)
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class CustomStatusCreateRequestTypedDict(TypedDict):
    custom_status: NotRequired[CustomStatusCreateInputTypedDict]


class CustomStatusCreateRequest(BaseModel):
    custom_status: Optional[CustomStatusCreateInput] = None
