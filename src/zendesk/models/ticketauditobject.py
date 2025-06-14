"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ticketauditviaobject import TicketAuditViaObject, TicketAuditViaObjectTypedDict
from datetime import datetime
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TicketAuditObjectTypedDict(TypedDict):
    author_id: NotRequired[int]
    r"""The user who created the audit"""
    created_at: NotRequired[datetime]
    r"""The time the audit was created"""
    events: NotRequired[List[Dict[str, Any]]]
    r"""An array of the events that happened in this audit. See the [Ticket Audit events reference](/documentation/ticketing/reference-guides/ticket-audit-events-reference)"""
    id: NotRequired[int]
    r"""Automatically assigned when creating audits"""
    metadata: NotRequired[Dict[str, Any]]
    r"""Metadata for the audit, custom and system data"""
    ticket_id: NotRequired[int]
    r"""The ID of the associated ticket"""
    via: NotRequired[TicketAuditViaObjectTypedDict]
    r"""Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)"""


class TicketAuditObject(BaseModel):
    author_id: Optional[int] = None
    r"""The user who created the audit"""

    created_at: Optional[datetime] = None
    r"""The time the audit was created"""

    events: Optional[List[Dict[str, Any]]] = None
    r"""An array of the events that happened in this audit. See the [Ticket Audit events reference](/documentation/ticketing/reference-guides/ticket-audit-events-reference)"""

    id: Optional[int] = None
    r"""Automatically assigned when creating audits"""

    metadata: Optional[Dict[str, Any]] = None
    r"""Metadata for the audit, custom and system data"""

    ticket_id: Optional[int] = None
    r"""The ID of the associated ticket"""

    via: Optional[TicketAuditViaObject] = None
    r"""Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)"""
