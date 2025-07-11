"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .emailnotificationsfilter import EmailNotificationsFilter
from .emailnotificationsresponse import (
    EmailNotificationsResponse,
    EmailNotificationsResponseTypedDict,
)
import pydantic
from typing import Callable, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, QueryParamMetadata


class ListEmailNotificationsRequestTypedDict(TypedDict):
    filter_: NotRequired[EmailNotificationsFilter]
    r"""Filters the email notifications by ticket, comment, or notification id.

    """
    per_page: NotRequired[int]
    r"""The number of records to return per page"""
    sort: NotRequired[str]
    r"""The field to sort the list.  Possible values are \"created_at\", \"updated_at\" (ascending order) or \"-created_at\", \"-updated_at\" (descending order)"""
    page_before: NotRequired[str]
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """
    page_after: NotRequired[str]
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """
    page_size: NotRequired[int]
    r"""Specifies how many records should be returned in the response. You can specify up to 100 records per page.

    """


class ListEmailNotificationsRequest(BaseModel):
    filter_: Annotated[
        Optional[EmailNotificationsFilter],
        pydantic.Field(alias="filter"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filters the email notifications by ticket, comment, or notification id.

    """

    per_page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The number of records to return per page"""

    sort: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The field to sort the list.  Possible values are \"created_at\", \"updated_at\" (ascending order) or \"-created_at\", \"-updated_at\" (descending order)"""

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


class ListEmailNotificationsResponseTypedDict(TypedDict):
    result: EmailNotificationsResponseTypedDict


class ListEmailNotificationsResponse(BaseModel):
    next: Callable[[], Optional[ListEmailNotificationsResponse]]

    result: EmailNotificationsResponse
