"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .triggerchangeobject import TriggerChangeObject, TriggerChangeObjectTypedDict
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TriggerActionDiffObjectTypedDict(TypedDict):
    field: NotRequired[List[TriggerChangeObjectTypedDict]]
    r"""An array of [change](#change) objects."""
    value: NotRequired[List[TriggerChangeObjectTypedDict]]
    r"""An array of [change](#change) objects."""


class TriggerActionDiffObject(BaseModel):
    field: Optional[List[TriggerChangeObject]] = None
    r"""An array of [change](#change) objects."""

    value: Optional[List[TriggerChangeObject]] = None
    r"""An array of [change](#change) objects."""
