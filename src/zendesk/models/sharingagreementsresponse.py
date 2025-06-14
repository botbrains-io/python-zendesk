"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sharingagreementobject import (
    SharingAgreementObject,
    SharingAgreementObjectTypedDict,
)
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class SharingAgreementsResponseTypedDict(TypedDict):
    sharing_agreements: NotRequired[List[SharingAgreementObjectTypedDict]]


class SharingAgreementsResponse(BaseModel):
    sharing_agreements: Optional[List[SharingAgreementObject]] = None
