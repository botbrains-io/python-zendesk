"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .triggercategoryrequest import (
    TriggerCategoryRequest,
    TriggerCategoryRequestTypedDict,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata, RequestMetadata


class UpdateTriggerCategoryRequestBodyTypedDict(TypedDict):
    trigger_category: NotRequired[TriggerCategoryRequestTypedDict]


class UpdateTriggerCategoryRequestBody(BaseModel):
    trigger_category: Optional[TriggerCategoryRequest] = None


class UpdateTriggerCategoryRequestTypedDict(TypedDict):
    trigger_category_id: str
    r"""The id of the ticket trigger category to update"""
    request_body: UpdateTriggerCategoryRequestBodyTypedDict


class UpdateTriggerCategoryRequest(BaseModel):
    trigger_category_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The id of the ticket trigger category to update"""

    request_body: Annotated[
        UpdateTriggerCategoryRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
