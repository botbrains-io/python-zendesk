"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .twitterchannelobject import TwitterChannelObject, TwitterChannelObjectTypedDict
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict
from zendesk.types import BaseModel


class TwitterChannelsResponseTypedDict(TypedDict):
    monitored_twitter_handles: NotRequired[List[TwitterChannelObjectTypedDict]]


class TwitterChannelsResponse(BaseModel):
    monitored_twitter_handles: Optional[List[TwitterChannelObject]] = None
