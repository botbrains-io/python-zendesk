"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .ticketmetriceventsresponse import (
    TicketMetricEventsResponse,
    TicketMetricEventsResponseTypedDict,
)
import pydantic
from typing import Callable, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, QueryParamMetadata


class ListTicketMetricEventsRequestTypedDict(TypedDict):
    start_time: int
    r"""The Unix UTC epoch time of the oldest event you're interested in. Example: 1332034771."""
    page_before: NotRequired[str]
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """
    page_after: NotRequired[str]
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """
    page_size: NotRequired[int]
    r"""Specifies how many records should be returned in the response. You can specify up to 100 records per page.

    """
    include_changes: NotRequired[bool]
    r"""This optional parameter enhances incremental data retrieval, delivering a consistent and accurate representation of data changes."""


class ListTicketMetricEventsRequest(BaseModel):
    start_time: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""The Unix UTC epoch time of the oldest event you're interested in. Example: 1332034771."""

    page_before: Annotated[
        Optional[str],
        pydantic.Field(alias="page[before]"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """

    page_after: Annotated[
        Optional[str],
        pydantic.Field(alias="page[after]"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="page[size]"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100
    r"""Specifies how many records should be returned in the response. You can specify up to 100 records per page.

    """

    include_changes: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""This optional parameter enhances incremental data retrieval, delivering a consistent and accurate representation of data changes."""


class ListTicketMetricEventsResponseTypedDict(TypedDict):
    result: TicketMetricEventsResponseTypedDict


class ListTicketMetricEventsResponse(BaseModel):
    next: Callable[[], Optional[ListTicketMetricEventsResponse]]

    result: TicketMetricEventsResponse
