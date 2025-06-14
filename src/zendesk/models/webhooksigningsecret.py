"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class WebhookSigningSecretTypedDict(TypedDict):
    r"""Signing secret used to verify webhook requests"""

    algorithm: NotRequired[str]
    r"""Signing algorithm (e.g., sha256)"""
    secret: NotRequired[str]
    r"""The signing secret value"""


class WebhookSigningSecret(BaseModel):
    r"""Signing secret used to verify webhook requests"""

    algorithm: Optional[str] = None
    r"""Signing algorithm (e.g., sha256)"""

    secret: Optional[str] = None
    r"""The signing secret value"""
