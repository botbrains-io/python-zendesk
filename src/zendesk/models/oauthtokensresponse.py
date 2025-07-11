"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .oauthtokenobject import OauthTokenObject, OauthTokenObjectTypedDict
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class OAuthTokensResponseTypedDict(TypedDict):
    tokens: NotRequired[List[OauthTokenObjectTypedDict]]


class OAuthTokensResponse(BaseModel):
    tokens: Optional[List[OauthTokenObject]] = None
