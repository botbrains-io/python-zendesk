"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL


class SessionObjectTypedDict(TypedDict):
    id: int
    r"""Automatically assigned when the session is created"""
    authenticated_at: NotRequired[Nullable[str]]
    r"""When the session was created"""
    last_seen_at: NotRequired[Nullable[str]]
    r"""The last approximate time this session was seen. This does not update on every request."""
    url: NotRequired[Nullable[str]]
    r"""The API URL of this session"""
    user_id: NotRequired[Nullable[int]]
    r"""The id of the user"""


class SessionObject(BaseModel):
    id: int
    r"""Automatically assigned when the session is created"""

    authenticated_at: OptionalNullable[str] = UNSET
    r"""When the session was created"""

    last_seen_at: OptionalNullable[str] = UNSET
    r"""The last approximate time this session was seen. This does not update on every request."""

    url: OptionalNullable[str] = UNSET
    r"""The API URL of this session"""

    user_id: OptionalNullable[int] = UNSET
    r"""The id of the user"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["authenticated_at", "last_seen_at", "url", "user_id"]
        nullable_fields = ["authenticated_at", "last_seen_at", "url", "user_id"]
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
