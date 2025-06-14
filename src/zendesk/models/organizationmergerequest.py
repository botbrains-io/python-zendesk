"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class OrganizationMergeRequestOrganizationMergeTypedDict(TypedDict):
    winner_id: NotRequired[int]
    r"""The id of the winning organization."""


class OrganizationMergeRequestOrganizationMerge(BaseModel):
    winner_id: Optional[int] = None
    r"""The id of the winning organization."""


class OrganizationMergeRequestTypedDict(TypedDict):
    organization_merge: NotRequired[OrganizationMergeRequestOrganizationMergeTypedDict]


class OrganizationMergeRequest(BaseModel):
    organization_merge: Optional[OrganizationMergeRequestOrganizationMerge] = None
