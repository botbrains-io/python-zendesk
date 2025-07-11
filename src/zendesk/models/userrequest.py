"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .userinput import UserInput, UserInputTypedDict
from typing_extensions import TypedDict
from zendesk.types import BaseModel


class UserRequestTypedDict(TypedDict):
    user: UserInputTypedDict


class UserRequest(BaseModel):
    user: UserInput
