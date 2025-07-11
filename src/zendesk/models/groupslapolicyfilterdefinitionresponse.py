"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL


class GroupSLAPolicyFilterDefinitionResponseOperatorTypedDict(TypedDict):
    title: NotRequired[str]
    value: NotRequired[str]


class GroupSLAPolicyFilterDefinitionResponseOperator(BaseModel):
    title: Optional[str] = None

    value: Optional[str] = None


class GroupSLAPolicyFilterDefinitionResponseListTypedDict(TypedDict):
    title: NotRequired[str]
    value: NotRequired[Nullable[int]]


class GroupSLAPolicyFilterDefinitionResponseList(BaseModel):
    title: Optional[str] = None

    value: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["title", "value"]
        nullable_fields = ["value"]
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


class GroupSLAPolicyFilterDefinitionResponseValuesTypedDict(TypedDict):
    list: NotRequired[List[GroupSLAPolicyFilterDefinitionResponseListTypedDict]]
    type: NotRequired[str]


class GroupSLAPolicyFilterDefinitionResponseValues(BaseModel):
    list: Optional[List[GroupSLAPolicyFilterDefinitionResponseList]] = None

    type: Optional[str] = None


class GroupSLAPolicyFilterDefinitionResponseAllTypedDict(TypedDict):
    group: NotRequired[str]
    operators: NotRequired[
        List[GroupSLAPolicyFilterDefinitionResponseOperatorTypedDict]
    ]
    title: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[GroupSLAPolicyFilterDefinitionResponseValuesTypedDict]


class GroupSLAPolicyFilterDefinitionResponseAll(BaseModel):
    group: Optional[str] = None

    operators: Optional[List[GroupSLAPolicyFilterDefinitionResponseOperator]] = None

    title: Optional[str] = None

    value: Optional[str] = None

    values: Optional[GroupSLAPolicyFilterDefinitionResponseValues] = None


class GroupSLAPolicyFilterDefinitionResponseDefinitionsTypedDict(TypedDict):
    all: NotRequired[List[GroupSLAPolicyFilterDefinitionResponseAllTypedDict]]


class GroupSLAPolicyFilterDefinitionResponseDefinitions(BaseModel):
    all: Optional[List[GroupSLAPolicyFilterDefinitionResponseAll]] = None


class GroupSLAPolicyFilterDefinitionResponseTypedDict(TypedDict):
    definitions: NotRequired[GroupSLAPolicyFilterDefinitionResponseDefinitionsTypedDict]


class GroupSLAPolicyFilterDefinitionResponse(BaseModel):
    definitions: Optional[GroupSLAPolicyFilterDefinitionResponseDefinitions] = None
