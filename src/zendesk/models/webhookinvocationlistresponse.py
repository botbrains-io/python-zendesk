"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paginationlinks import PaginationLinks, PaginationLinksTypedDict
from .paginationmeta import PaginationMeta, PaginationMetaTypedDict
from .webhookinvocation import WebhookInvocation, WebhookInvocationTypedDict
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class WebhookInvocationListResponseTypedDict(TypedDict):
    invocations: NotRequired[List[WebhookInvocationTypedDict]]
    meta: NotRequired[PaginationMetaTypedDict]
    links: NotRequired[PaginationLinksTypedDict]


class WebhookInvocationListResponse(BaseModel):
    invocations: Optional[List[WebhookInvocation]] = None

    meta: Optional[PaginationMeta] = None

    links: Optional[PaginationLinks] = None
