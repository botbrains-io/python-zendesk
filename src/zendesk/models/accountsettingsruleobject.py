"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class AccountSettingsRuleObjectTypedDict(TypedDict):
    r"""Rules settings for triggers, macros, views, and automations. See [Rules](#rules)"""

    macro_most_used: NotRequired[bool]
    macro_order: NotRequired[str]
    skill_based_filtered_views: NotRequired[List[Dict[str, Any]]]
    using_skill_based_routing: NotRequired[bool]


class AccountSettingsRuleObject(BaseModel):
    r"""Rules settings for triggers, macros, views, and automations. See [Rules](#rules)"""

    macro_most_used: Optional[bool] = None

    macro_order: Optional[str] = None

    skill_based_filtered_views: Optional[List[Dict[str, Any]]] = None

    using_skill_based_routing: Optional[bool] = None
