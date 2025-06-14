"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing_extensions import Annotated, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata


class DeleteUploadRequestTypedDict(TypedDict):
    token: str
    r"""The token of the uploaded attachment"""


class DeleteUploadRequest(BaseModel):
    token: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The token of the uploaded attachment"""
