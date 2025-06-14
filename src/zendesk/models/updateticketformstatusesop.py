"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .updateticketformstatusesparams import (
    UpdateTicketFormStatusesParams,
    UpdateTicketFormStatusesParamsTypedDict,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata, RequestMetadata


class UpdateTicketFormStatusesRequestTypedDict(TypedDict):
    ticket_form_id: int
    r"""The ID of the ticket form"""
    update_ticket_form_statuses_params: NotRequired[
        UpdateTicketFormStatusesParamsTypedDict
    ]


class UpdateTicketFormStatusesRequest(BaseModel):
    ticket_form_id: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the ticket form"""

    update_ticket_form_statuses_params: Annotated[
        Optional[UpdateTicketFormStatusesParams],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
