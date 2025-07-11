"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL


class SLAPolicyFilterDefinitionResponseAllOperatorTypedDict(TypedDict):
    title: NotRequired[str]
    value: NotRequired[str]


class SLAPolicyFilterDefinitionResponseAllOperator(BaseModel):
    title: Optional[str] = None

    value: Optional[str] = None


class SLAPolicyFilterDefinitionResponseAllListTypedDict(TypedDict):
    title: NotRequired[str]
    value: NotRequired[Nullable[str]]


class SLAPolicyFilterDefinitionResponseAllList(BaseModel):
    title: Optional[str] = None

    value: OptionalNullable[str] = UNSET

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


class SLAPolicyFilterDefinitionResponseAllValuesTypedDict(TypedDict):
    list: NotRequired[List[SLAPolicyFilterDefinitionResponseAllListTypedDict]]
    type: NotRequired[str]


class SLAPolicyFilterDefinitionResponseAllValues(BaseModel):
    list: Optional[List[SLAPolicyFilterDefinitionResponseAllList]] = None

    type: Optional[str] = None


class SLAPolicyFilterDefinitionResponseAllTypedDict(TypedDict):
    group: NotRequired[str]
    operators: NotRequired[List[SLAPolicyFilterDefinitionResponseAllOperatorTypedDict]]
    target: NotRequired[Nullable[str]]
    title: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[SLAPolicyFilterDefinitionResponseAllValuesTypedDict]


class SLAPolicyFilterDefinitionResponseAll(BaseModel):
    group: Optional[str] = None

    operators: Optional[List[SLAPolicyFilterDefinitionResponseAllOperator]] = None

    target: OptionalNullable[str] = UNSET

    title: Optional[str] = None

    value: Optional[str] = None

    values: Optional[SLAPolicyFilterDefinitionResponseAllValues] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["group", "operators", "target", "title", "value", "values"]
        nullable_fields = ["target"]
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


class AnyOperatorTypedDict(TypedDict):
    title: NotRequired[str]
    value: NotRequired[str]


class AnyOperator(BaseModel):
    title: Optional[str] = None

    value: Optional[str] = None


class AnyListTypedDict(TypedDict):
    title: NotRequired[str]
    value: NotRequired[Nullable[str]]


class AnyList(BaseModel):
    title: Optional[str] = None

    value: OptionalNullable[str] = UNSET

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


class AnyValuesTypedDict(TypedDict):
    list: NotRequired[List[AnyListTypedDict]]
    type: NotRequired[str]


class AnyValues(BaseModel):
    list: Optional[List[AnyList]] = None

    type: Optional[str] = None


class SLAPolicyFilterDefinitionResponseAnyTypedDict(TypedDict):
    group: NotRequired[str]
    operators: NotRequired[List[AnyOperatorTypedDict]]
    target: NotRequired[Nullable[str]]
    title: NotRequired[str]
    value: NotRequired[str]
    values: NotRequired[AnyValuesTypedDict]


class SLAPolicyFilterDefinitionResponseAny(BaseModel):
    group: Optional[str] = None

    operators: Optional[List[AnyOperator]] = None

    target: OptionalNullable[str] = UNSET

    title: Optional[str] = None

    value: Optional[str] = None

    values: Optional[AnyValues] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["group", "operators", "target", "title", "value", "values"]
        nullable_fields = ["target"]
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


class SLAPolicyFilterDefinitionResponseDefinitionsTypedDict(TypedDict):
    all: NotRequired[List[SLAPolicyFilterDefinitionResponseAllTypedDict]]
    any: NotRequired[List[SLAPolicyFilterDefinitionResponseAnyTypedDict]]


class SLAPolicyFilterDefinitionResponseDefinitions(BaseModel):
    all: Optional[List[SLAPolicyFilterDefinitionResponseAll]] = None

    any: Optional[List[SLAPolicyFilterDefinitionResponseAny]] = None


class SLAPolicyFilterDefinitionResponseTypedDict(TypedDict):
    definitions: NotRequired[SLAPolicyFilterDefinitionResponseDefinitionsTypedDict]


class SLAPolicyFilterDefinitionResponse(BaseModel):
    definitions: Optional[SLAPolicyFilterDefinitionResponseDefinitions] = None
