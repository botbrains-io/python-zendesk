"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class ChannelFrameworkResultStatusObjectTypedDict(TypedDict):
    r"""The status of the import for the indicated resource"""

    code: NotRequired[str]
    r"""A code indicating the status of the import of the resource, as described in [status codes](#status-codes)"""
    description: NotRequired[str]
    r"""In the case of an exception, a description of the exception. Otherwise, not present."""


class ChannelFrameworkResultStatusObject(BaseModel):
    r"""The status of the import for the indicated resource"""

    code: Optional[str] = None
    r"""A code indicating the status of the import of the resource, as described in [status codes](#status-codes)"""

    description: Optional[str] = None
    r"""In the case of an exception, a description of the exception. Otherwise, not present."""
