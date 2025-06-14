"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .objecttriggerbulkupdateitem import (
    ObjectTriggerBulkUpdateItem,
    ObjectTriggerBulkUpdateItemTypedDict,
)
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class ObjectTriggerBulkUpdateRequestTypedDict(TypedDict):
    triggers: NotRequired[List[ObjectTriggerBulkUpdateItemTypedDict]]


class ObjectTriggerBulkUpdateRequest(BaseModel):
    triggers: Optional[List[ObjectTriggerBulkUpdateItem]] = None
