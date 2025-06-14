"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .relationshipfilterdefinition import (
    RelationshipFilterDefinition,
    RelationshipFilterDefinitionTypedDict,
)
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class RelationshipFilterDefinitionResponseTypedDict(TypedDict):
    definitions: NotRequired[RelationshipFilterDefinitionTypedDict]


class RelationshipFilterDefinitionResponse(BaseModel):
    definitions: Optional[RelationshipFilterDefinition] = None
