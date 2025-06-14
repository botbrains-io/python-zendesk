"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .objecttriggerdefinitionobject import (
    ObjectTriggerDefinitionObject,
    ObjectTriggerDefinitionObjectTypedDict,
)
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class ObjectTriggerDefinitionResponseTypedDict(TypedDict):
    definitions: NotRequired[ObjectTriggerDefinitionObjectTypedDict]


class ObjectTriggerDefinitionResponse(BaseModel):
    definitions: Optional[ObjectTriggerDefinitionObject] = None
