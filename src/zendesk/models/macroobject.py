"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .actionobject import ActionObject, ActionObjectTypedDict
from datetime import datetime
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL


class MacroObjectTypedDict(TypedDict):
    actions: List[ActionObjectTypedDict]
    r"""Each action describes what the macro will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)"""
    title: str
    r"""The title of the macro"""
    active: NotRequired[bool]
    r"""Useful for determining if the macro should be displayed"""
    created_at: NotRequired[datetime]
    r"""The time the macro was created"""
    default: NotRequired[bool]
    r"""If true, the macro is a default macro"""
    description: NotRequired[Nullable[str]]
    r"""The description of the macro"""
    id: NotRequired[int]
    r"""The id automatically assigned when a macro is created"""
    position: NotRequired[int]
    r"""The position of the macro"""
    restriction: NotRequired[Nullable[Dict[str, Any]]]
    r"""Access to this macro. A null value allows unrestricted access for all users in the account"""
    updated_at: NotRequired[datetime]
    r"""The time of the last update of the macro"""
    url: NotRequired[str]
    r"""A URL to access the macro's details"""
    app_installation: NotRequired[Nullable[str]]
    r"""The app installation that requires each macro, if present"""
    categories: NotRequired[Nullable[str]]
    r"""The macro categories"""
    permissions: NotRequired[Nullable[str]]
    r"""Permissions for each macro"""
    usage_1h: NotRequired[int]
    r"""The number of times each macro has been used in the past hour"""
    usage_7d: NotRequired[int]
    r"""The number of times each macro has been used in the past week"""
    usage_24h: NotRequired[int]
    r"""The number of times each macro has been used in the past day"""
    usage_30d: NotRequired[int]
    r"""The number of times each macro has been used in the past thirty days"""


class MacroObject(BaseModel):
    actions: List[ActionObject]
    r"""Each action describes what the macro will do. See [Actions reference](/documentation/ticketing/reference-guides/actions-reference)"""

    title: str
    r"""The title of the macro"""

    active: Optional[bool] = None
    r"""Useful for determining if the macro should be displayed"""

    created_at: Optional[datetime] = None
    r"""The time the macro was created"""

    default: Optional[bool] = None
    r"""If true, the macro is a default macro"""

    description: OptionalNullable[str] = UNSET
    r"""The description of the macro"""

    id: Optional[int] = None
    r"""The id automatically assigned when a macro is created"""

    position: Optional[int] = None
    r"""The position of the macro"""

    restriction: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Access to this macro. A null value allows unrestricted access for all users in the account"""

    updated_at: Optional[datetime] = None
    r"""The time of the last update of the macro"""

    url: Optional[str] = None
    r"""A URL to access the macro's details"""

    app_installation: OptionalNullable[str] = UNSET
    r"""The app installation that requires each macro, if present"""

    categories: OptionalNullable[str] = UNSET
    r"""The macro categories"""

    permissions: OptionalNullable[str] = UNSET
    r"""Permissions for each macro"""

    usage_1h: Optional[int] = None
    r"""The number of times each macro has been used in the past hour"""

    usage_7d: Optional[int] = None
    r"""The number of times each macro has been used in the past week"""

    usage_24h: Optional[int] = None
    r"""The number of times each macro has been used in the past day"""

    usage_30d: Optional[int] = None
    r"""The number of times each macro has been used in the past thirty days"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "active",
            "created_at",
            "default",
            "description",
            "id",
            "position",
            "restriction",
            "updated_at",
            "url",
            "app_installation",
            "categories",
            "permissions",
            "usage_1h",
            "usage_7d",
            "usage_24h",
            "usage_30d",
        ]
        nullable_fields = [
            "description",
            "restriction",
            "app_installation",
            "categories",
            "permissions",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
