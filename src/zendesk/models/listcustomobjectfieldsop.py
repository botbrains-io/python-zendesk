"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customobjectfieldsresponse import (
    CustomObjectFieldsResponse,
    CustomObjectFieldsResponseTypedDict,
)
import pydantic
from typing import Callable, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class ListCustomObjectFieldsRequestTypedDict(TypedDict):
    custom_object_key: str
    r"""The key of a custom object"""
    page_before: NotRequired[str]
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """
    page_after: NotRequired[str]
    r"""A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.

    """
    page_size: NotRequired[int]
    r"""Specifies how many records should be returned in the response. You can specify up to 100 records per page.

    """
    include_standard_fields: NotRequired[bool]
    r"""Include standard fields if true. Exclude them if false"""


class ListCustomObjectFieldsRequest(BaseModel):
    custom_object_key: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The key of a custom object"""

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

    include_standard_fields: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Include standard fields if true. Exclude them if false"""


class ListCustomObjectFieldsResponseTypedDict(TypedDict):
    result: CustomObjectFieldsResponseTypedDict


class ListCustomObjectFieldsResponse(BaseModel):
    next: Callable[[], Optional[ListCustomObjectFieldsResponse]]

    result: CustomObjectFieldsResponse
