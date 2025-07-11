"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing_extensions import Annotated, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata


class DeleteTicketFieldOptionRequestTypedDict(TypedDict):
    ticket_field_id: int
    r"""The ID of the ticket field"""
    ticket_field_option_id: int
    r"""The ID of the ticket field option"""


class DeleteTicketFieldOptionRequest(BaseModel):
    ticket_field_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the ticket field"""

    ticket_field_option_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the ticket field option"""
