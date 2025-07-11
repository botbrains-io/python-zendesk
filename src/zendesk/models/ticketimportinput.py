"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ticketauditviaobject_input import (
    TicketAuditViaObjectInput,
    TicketAuditViaObjectInputTypedDict,
)
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TicketImportInputCommentTypedDict(TypedDict):
    value: NotRequired[str]
    r"""The comment string value"""
    author_id: NotRequired[int]
    r"""The id of the comment author. See [Author id](#author-id)"""
    body: NotRequired[str]
    r"""The comment string. See [Bodies](#bodies)"""
    html_body: NotRequired[str]
    r"""The comment formatted as HTML. See [Bodies](#bodies)"""
    public: NotRequired[bool]
    r"""true if a public comment; false if an internal note. The initial value set on ticket creation persists for any additional comment unless you change it"""
    uploads: NotRequired[List[str]]
    r"""List of tokens received from [uploading files](/api-reference/ticketing/tickets/ticket-attachments/#upload-files) for comment attachments. The files are attached by creating or updating tickets with the tokens. See [Attaching files](/api-reference/ticketing/tickets/tickets/#attaching-files) in Tickets"""
    via: NotRequired[TicketAuditViaObjectInputTypedDict]
    r"""Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)"""


class TicketImportInputComment(BaseModel):
    value: Optional[str] = None
    r"""The comment string value"""

    author_id: Optional[int] = None
    r"""The id of the comment author. See [Author id](#author-id)"""

    body: Optional[str] = None
    r"""The comment string. See [Bodies](#bodies)"""

    html_body: Optional[str] = None
    r"""The comment formatted as HTML. See [Bodies](#bodies)"""

    public: Optional[bool] = None
    r"""true if a public comment; false if an internal note. The initial value set on ticket creation persists for any additional comment unless you change it"""

    uploads: Optional[List[str]] = None
    r"""List of tokens received from [uploading files](/api-reference/ticketing/tickets/ticket-attachments/#upload-files) for comment attachments. The files are attached by creating or updating tickets with the tokens. See [Attaching files](/api-reference/ticketing/tickets/tickets/#attaching-files) in Tickets"""

    via: Optional[TicketAuditViaObjectInput] = None
    r"""Describes how the object was created. See the [Via object reference](/documentation/ticketing/reference-guides/via-object-reference)"""


class TicketImportInputTypedDict(TypedDict):
    assignee_id: NotRequired[int]
    r"""The agent currently assigned to the ticket"""
    comments: NotRequired[List[TicketImportInputCommentTypedDict]]
    r"""The conversation between requesters, collaborators, and agents"""
    description: NotRequired[str]
    r"""Read-only first comment on the ticket. When [creating a ticket](#create-ticket), use `comment` to set the description. See [Description and first comment](#description-and-first-comment)"""
    requester_id: NotRequired[int]
    r"""The user who requested this ticket"""
    subject: NotRequired[str]
    r"""The value of the subject field for this ticket"""
    tags: NotRequired[List[str]]
    r"""The array of tags applied to this ticket"""


class TicketImportInput(BaseModel):
    assignee_id: Optional[int] = None
    r"""The agent currently assigned to the ticket"""

    comments: Optional[List[TicketImportInputComment]] = None
    r"""The conversation between requesters, collaborators, and agents"""

    description: Optional[str] = None
    r"""Read-only first comment on the ticket. When [creating a ticket](#create-ticket), use `comment` to set the description. See [Description and first comment](#description-and-first-comment)"""

    requester_id: Optional[int] = None
    r"""The user who requested this ticket"""

    subject: Optional[str] = None
    r"""The value of the subject field for this ticket"""

    tags: Optional[List[str]] = None
    r"""The array of tags applied to this ticket"""
