"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .triggeractionobject import TriggerActionObject, TriggerActionObjectTypedDict
from .triggerconditionsobject import (
    TriggerConditionsObject,
    TriggerConditionsObjectTypedDict,
)
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata


class TriggerObjectInputTypedDict(TypedDict):
    actions: List[TriggerActionObjectTypedDict]
    r"""An array of actions describing what the ticket trigger will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)"""
    conditions: TriggerConditionsObjectTypedDict
    r"""An object that describes the circumstances under which the trigger performs its actions. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)"""
    title: str
    r"""The title of the ticket trigger"""
    active: NotRequired[bool]
    r"""Whether the ticket trigger is active"""
    category_id: NotRequired[str]
    r"""The ID of the category the ticket trigger belongs to"""
    description: NotRequired[str]
    r"""The description of the ticket trigger"""
    position: NotRequired[int]
    r"""Position of the ticket trigger, determines the order they will execute in"""
    raw_title: NotRequired[str]
    r"""The raw format of the title of the ticket trigger"""


class TriggerObjectInput(BaseModel):
    actions: Annotated[List[TriggerActionObject], FieldMetadata(query=True)]
    r"""An array of actions describing what the ticket trigger will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)"""

    conditions: Annotated[TriggerConditionsObject, FieldMetadata(query=True)]
    r"""An object that describes the circumstances under which the trigger performs its actions. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)"""

    title: Annotated[str, FieldMetadata(query=True)]
    r"""The title of the ticket trigger"""

    active: Annotated[Optional[bool], FieldMetadata(query=True)] = None
    r"""Whether the ticket trigger is active"""

    category_id: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""The ID of the category the ticket trigger belongs to"""

    description: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""The description of the ticket trigger"""

    position: Annotated[Optional[int], FieldMetadata(query=True)] = None
    r"""Position of the ticket trigger, determines the order they will execute in"""

    raw_title: Annotated[Optional[str], FieldMetadata(query=True)] = None
    r"""The raw format of the title of the ticket trigger"""
