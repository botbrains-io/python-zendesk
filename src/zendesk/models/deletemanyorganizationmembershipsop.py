"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict
from zendesk.types import BaseModel
from zendesk.utils import FieldMetadata, QueryParamMetadata


class DeleteManyOrganizationMembershipsRequestTypedDict(TypedDict):
    ids: NotRequired[List[int]]
    r"""The IDs of the organization memberships to delete"""


class DeleteManyOrganizationMembershipsRequest(BaseModel):
    ids: Annotated[
        Optional[List[int]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The IDs of the organization memberships to delete"""
