"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing_extensions import Annotated, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata


class ShowMacroAttachmentRequestTypedDict(TypedDict):
    attachment_id: int
    r"""The ID of the attachment"""


class ShowMacroAttachmentRequest(BaseModel):
    attachment_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the attachment"""
