"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .objecttriggerbulkupdaterequest import (
    ObjectTriggerBulkUpdateRequest,
    ObjectTriggerBulkUpdateRequestTypedDict,
)
from typing_extensions import Annotated, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata, RequestMetadata


class UpdateManyObjectTriggersRequestTypedDict(TypedDict):
    custom_object_key: str
    r"""The key of a custom object"""
    object_trigger_bulk_update_request: ObjectTriggerBulkUpdateRequestTypedDict


class UpdateManyObjectTriggersRequest(BaseModel):
    custom_object_key: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The key of a custom object"""

    object_trigger_bulk_update_request: Annotated[
        ObjectTriggerBulkUpdateRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
