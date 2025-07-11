"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .auditobject import AuditObject, AuditObjectTypedDict
from .ticketobject import TicketObject, TicketObjectTypedDict
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TicketUpdateResponseTypedDict(TypedDict):
    audit: NotRequired[AuditObjectTypedDict]
    ticket: NotRequired[TicketObjectTypedDict]


class TicketUpdateResponse(BaseModel):
    audit: Optional[AuditObject] = None

    ticket: Optional[TicketObject] = None
