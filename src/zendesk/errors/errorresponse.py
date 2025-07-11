"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import List, Optional
from zendesk import utils
from zendesk.models import errorresponse as models_errorresponse
from zendesk.types import BaseModel


class ErrorResponseData(BaseModel):
    error: Optional[models_errorresponse.ErrorResponseError1] = None

    errors: Optional[List[models_errorresponse.ErrorResponseError2]] = None
    r"""Field-specific validation errors"""


class ErrorResponse(Exception):
    data: ErrorResponseData

    def __init__(self, data: ErrorResponseData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ErrorResponseData)
