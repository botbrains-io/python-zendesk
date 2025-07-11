"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class ConditionsAllOperatorTypedDict(TypedDict):
    terminal: NotRequired[bool]
    title: NotRequired[str]
    value: NotRequired[str]


class ConditionsAllOperator(BaseModel):
    terminal: Optional[bool] = None

    title: Optional[str] = None

    value: Optional[str] = None


class ConditionsAllValueTypedDict(TypedDict):
    enabled: NotRequired[bool]
    title: NotRequired[str]
    value: NotRequired[str]


class ConditionsAllValue(BaseModel):
    enabled: Optional[bool] = None

    title: Optional[str] = None

    value: Optional[str] = None


class DefinitionsResponseConditionsAllTypedDict(TypedDict):
    group: NotRequired[str]
    nullable: NotRequired[bool]
    operators: NotRequired[List[ConditionsAllOperatorTypedDict]]
    repeatable: NotRequired[bool]
    subject: NotRequired[str]
    title: NotRequired[str]
    type: NotRequired[str]
    values: NotRequired[List[ConditionsAllValueTypedDict]]


class DefinitionsResponseConditionsAll(BaseModel):
    group: Optional[str] = None

    nullable: Optional[bool] = None

    operators: Optional[List[ConditionsAllOperator]] = None

    repeatable: Optional[bool] = None

    subject: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None

    values: Optional[List[ConditionsAllValue]] = None


class ConditionsAnyOperatorTypedDict(TypedDict):
    terminal: NotRequired[bool]
    title: NotRequired[str]
    value: NotRequired[str]


class ConditionsAnyOperator(BaseModel):
    terminal: Optional[bool] = None

    title: Optional[str] = None

    value: Optional[str] = None


class ConditionsAnyValueTypedDict(TypedDict):
    enabled: NotRequired[bool]
    title: NotRequired[str]
    value: NotRequired[str]


class ConditionsAnyValue(BaseModel):
    enabled: Optional[bool] = None

    title: Optional[str] = None

    value: Optional[str] = None


class DefinitionsResponseConditionsAnyTypedDict(TypedDict):
    group: NotRequired[str]
    nullable: NotRequired[bool]
    operators: NotRequired[List[ConditionsAnyOperatorTypedDict]]
    repeatable: NotRequired[bool]
    subject: NotRequired[str]
    title: NotRequired[str]
    type: NotRequired[str]
    values: NotRequired[List[ConditionsAnyValueTypedDict]]


class DefinitionsResponseConditionsAny(BaseModel):
    group: Optional[str] = None

    nullable: Optional[bool] = None

    operators: Optional[List[ConditionsAnyOperator]] = None

    repeatable: Optional[bool] = None

    subject: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None

    values: Optional[List[ConditionsAnyValue]] = None


class DefinitionsResponseDefinitionsTypedDict(TypedDict):
    conditions_all: NotRequired[List[DefinitionsResponseConditionsAllTypedDict]]
    conditions_any: NotRequired[List[DefinitionsResponseConditionsAnyTypedDict]]


class DefinitionsResponseDefinitions(BaseModel):
    conditions_all: Optional[List[DefinitionsResponseConditionsAll]] = None

    conditions_any: Optional[List[DefinitionsResponseConditionsAny]] = None


class DefinitionsResponseTypedDict(TypedDict):
    definitions: NotRequired[DefinitionsResponseDefinitionsTypedDict]


class DefinitionsResponse(BaseModel):
    definitions: Optional[DefinitionsResponseDefinitions] = None
