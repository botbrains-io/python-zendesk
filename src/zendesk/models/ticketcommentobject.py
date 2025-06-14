"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .attachmentobject import AttachmentObject, AttachmentObjectTypedDict
from .ticketauditviaobject import TicketAuditViaObject, TicketAuditViaObjectTypedDict
from datetime import datetime
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TicketCommentObjectTypedDict(TypedDict):
    attachments: NotRequired[List[AttachmentObjectTypedDict]]
    r"""Attachments, if any. See [Attachment](/api-reference/ticketing/tickets/ticket-attachments/)"""
    audit_id: NotRequired[int]
    r"""The id of the ticket audit record. See [Show Audit](/api-reference/ticketing/tickets/ticket_audits/#show-audit)"""
    author_id: NotRequired[int]
    r"""The id of the comment author. See [Author id](#author-id)"""
    body: NotRequired[str]
    r"""The comment string. See [Bodies](#bodies)"""
    created_at: NotRequired[datetime]
    r"""The time the comment was created"""
    html_body: NotRequired[str]
    r"""The comment formatted as HTML. See [Bodies](#bodies)"""
    id: NotRequired[int]
    r"""Automatically assigned when the comment is created"""
    metadata: NotRequired[Dict[str, Any]]
    r"""System information (web client, IP address, etc.) and comment flags, if any. See [Comment flags](#comment-flags)"""
    plain_body: NotRequired[str]
    r"""The comment presented as plain text. See [Bodies](#bodies)"""
    public: NotRequired[bool]
    r"""true if a public comment; false if an internal note. The initial value set on ticket creation persists for any additional comment unless you change it"""
    type: NotRequired[str]
    r"""`Comment` or `VoiceComment`. The JSON object for adding voice comments to tickets is different. See [Adding voice comments to tickets](/documentation/ticketing/managing-tickets/adding-voice-comments-to-tickets)"""
    uploads: NotRequired[List[str]]
    r"""List of tokens received from [uploading files](/api-reference/ticketing/tickets/ticket-attachments/#upload-files) for comment attachments. The files are attached by creating or updating tickets with the tokens. See [Attaching files](/api-reference/ticketing/tickets/tickets/#attaching-files) in Tickets"""
    via: NotRequired[TicketAuditViaObjectTypedDict]
    r"""Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)"""


class TicketCommentObject(BaseModel):
    attachments: Optional[List[AttachmentObject]] = None
    r"""Attachments, if any. See [Attachment](/api-reference/ticketing/tickets/ticket-attachments/)"""

    audit_id: Optional[int] = None
    r"""The id of the ticket audit record. See [Show Audit](/api-reference/ticketing/tickets/ticket_audits/#show-audit)"""

    author_id: Optional[int] = None
    r"""The id of the comment author. See [Author id](#author-id)"""

    body: Optional[str] = None
    r"""The comment string. See [Bodies](#bodies)"""

    created_at: Optional[datetime] = None
    r"""The time the comment was created"""

    html_body: Optional[str] = None
    r"""The comment formatted as HTML. See [Bodies](#bodies)"""

    id: Optional[int] = None
    r"""Automatically assigned when the comment is created"""

    metadata: Optional[Dict[str, Any]] = None
    r"""System information (web client, IP address, etc.) and comment flags, if any. See [Comment flags](#comment-flags)"""

    plain_body: Optional[str] = None
    r"""The comment presented as plain text. See [Bodies](#bodies)"""

    public: Optional[bool] = None
    r"""true if a public comment; false if an internal note. The initial value set on ticket creation persists for any additional comment unless you change it"""

    type: Optional[str] = None
    r"""`Comment` or `VoiceComment`. The JSON object for adding voice comments to tickets is different. See [Adding voice comments to tickets](/documentation/ticketing/managing-tickets/adding-voice-comments-to-tickets)"""

    uploads: Optional[List[str]] = None
    r"""List of tokens received from [uploading files](/api-reference/ticketing/tickets/ticket-attachments/#upload-files) for comment attachments. The files are attached by creating or updating tickets with the tokens. See [Attaching files](/api-reference/ticketing/tickets/tickets/#attaching-files) in Tickets"""

    via: Optional[TicketAuditViaObject] = None
    r"""Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)"""
