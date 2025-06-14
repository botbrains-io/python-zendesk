"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .macrosresponse import MacrosResponse, MacrosResponseTypedDict
import pydantic
from typing import Callable, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, QueryParamMetadata


class ListMacrosRequestTypedDict(TypedDict):
    page_before: NotRequired[str]
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """
    page_after: NotRequired[str]
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """
    page_size: NotRequired[int]
    r"""Specifies how many records should be returned in the response. You can specify up to 100 records per page.

    """
    include: NotRequired[str]
    r"""A sideload to include in the response. See [Sideloads](#sideloads-2)"""
    access: NotRequired[str]
    r"""Filter macros by access. Possible values are \"personal\", \"agents\", \"shared\", or \"account\". The \"agents\" value returns all personal macros for the account's agents and is only available to admins."""
    active: NotRequired[bool]
    r"""Filter by active macros if true or inactive macros if false"""
    category: NotRequired[int]
    r"""Filter macros by category"""
    group_id: NotRequired[int]
    r"""Filter macros by group"""
    only_viewable: NotRequired[bool]
    r"""If true, returns only macros that can be applied to tickets. If false, returns all macros the current user can manage. Default is false"""
    sort_by: NotRequired[str]
    r"""Possible values are \"alphabetical\", \"created_at\", \"updated_at\", \"usage_1h\", \"usage_24h\", \"usage_7d\", or \"usage_30d\". Defaults to alphabetical"""
    sort_order: NotRequired[str]
    r"""One of \"asc\" or \"desc\". Defaults to \"asc\" for alphabetical and position sort, \"desc\" for all others"""


class ListMacrosRequest(BaseModel):
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

    include: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A sideload to include in the response. See [Sideloads](#sideloads-2)"""

    access: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter macros by access. Possible values are \"personal\", \"agents\", \"shared\", or \"account\". The \"agents\" value returns all personal macros for the account's agents and is only available to admins."""

    active: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter by active macros if true or inactive macros if false"""

    category: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter macros by category"""

    group_id: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter macros by group"""

    only_viewable: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""If true, returns only macros that can be applied to tickets. If false, returns all macros the current user can manage. Default is false"""

    sort_by: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Possible values are \"alphabetical\", \"created_at\", \"updated_at\", \"usage_1h\", \"usage_24h\", \"usage_7d\", or \"usage_30d\". Defaults to alphabetical"""

    sort_order: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""One of \"asc\" or \"desc\". Defaults to \"asc\" for alphabetical and position sort, \"desc\" for all others"""


class ListMacrosResponseTypedDict(TypedDict):
    result: MacrosResponseTypedDict


class ListMacrosResponse(BaseModel):
    next: Callable[[], Optional[ListMacrosResponse]]

    result: MacrosResponse
