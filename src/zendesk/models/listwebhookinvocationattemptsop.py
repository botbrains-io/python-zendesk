"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing_extensions import Annotated, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata


class ListWebhookInvocationAttemptsRequestTypedDict(TypedDict):
    webhook_id: str
    r"""Webhook id"""
    invocation_id: str
    r"""Webhook invocation id"""


class ListWebhookInvocationAttemptsRequest(BaseModel):
    webhook_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Webhook id"""

    invocation_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Webhook invocation id"""
