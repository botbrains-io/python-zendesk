"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .triggeractionobject import TriggerActionObject, TriggerActionObjectTypedDict
from .triggerconditionsobject import (
    TriggerConditionsObject,
    TriggerConditionsObjectTypedDict,
)
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TriggerObjectTypedDict(TypedDict):
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
    created_at: NotRequired[str]
    r"""The time the ticket trigger was created"""
    default: NotRequired[bool]
    r"""If true, the ticket trigger is a standard trigger"""
    description: NotRequired[str]
    r"""The description of the ticket trigger"""
    id: NotRequired[int]
    r"""Automatically assigned when created"""
    position: NotRequired[int]
    r"""Position of the ticket trigger, determines the order they will execute in"""
    raw_title: NotRequired[str]
    r"""The raw format of the title of the ticket trigger"""
    updated_at: NotRequired[str]
    r"""The time of the last update of the ticket trigger"""
    url: NotRequired[str]
    r"""The url of the ticket trigger"""


class TriggerObject(BaseModel):
    actions: List[TriggerActionObject]
    r"""An array of actions describing what the ticket trigger will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)"""

    conditions: TriggerConditionsObject
    r"""An object that describes the circumstances under which the trigger performs its actions. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)"""

    title: str
    r"""The title of the ticket trigger"""

    active: Optional[bool] = None
    r"""Whether the ticket trigger is active"""

    category_id: Optional[str] = None
    r"""The ID of the category the ticket trigger belongs to"""

    created_at: Optional[str] = None
    r"""The time the ticket trigger was created"""

    default: Optional[bool] = None
    r"""If true, the ticket trigger is a standard trigger"""

    description: Optional[str] = None
    r"""The description of the ticket trigger"""

    id: Optional[int] = None
    r"""Automatically assigned when created"""

    position: Optional[int] = None
    r"""Position of the ticket trigger, determines the order they will execute in"""

    raw_title: Optional[str] = None
    r"""The raw format of the title of the ticket trigger"""

    updated_at: Optional[str] = None
    r"""The time of the last update of the ticket trigger"""

    url: Optional[str] = None
    r"""The url of the ticket trigger"""
