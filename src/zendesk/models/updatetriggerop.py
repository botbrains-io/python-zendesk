"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .triggerwithcategoryrequest import (
    TriggerWithCategoryRequest,
    TriggerWithCategoryRequestTypedDict,
)
from typing_extensions import Annotated, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata, RequestMetadata


class UpdateTriggerRequestTypedDict(TypedDict):
    trigger_id: int
    r"""The ID of the trigger"""
    trigger_with_category_request: TriggerWithCategoryRequestTypedDict


class UpdateTriggerRequest(BaseModel):
    trigger_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the trigger"""

    trigger_with_category_request: Annotated[
        TriggerWithCategoryRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
