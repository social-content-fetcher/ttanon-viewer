"""Typed records for TTAnon data responses."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


def _int(d: Dict[str, Any], key: str) -> int:
    try:
        return int(d.get(key) or 0)
    except (TypeError, ValueError):
        return 0


@dataclass(frozen=True)
class Profile:
    username: str
    nickname: str = ""
    bio: str = ""
    verified: bool = False
    private: bool = False
    followers: int = 0
    following: int = 0
    likes: int = 0
    videos: int = 0
    avatar_url: Optional[str] = None
    url: Optional[str] = None

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Profile":
        return cls(
            username=str(d.get("username", "")),
            nickname=str(d.get("nickname", "")),
            bio=str(d.get("bio", "")),
            verified=bool(d.get("verified", False)),
            private=bool(d.get("private", False)),
            followers=_int(d, "followers"),
            following=_int(d, "following"),
            likes=_int(d, "likes"),
            videos=_int(d, "videos"),
            avatar_url=d.get("avatar_url"),
            url=d.get("url"),
        )


@dataclass(frozen=True)
class Video:
    id: str
    author: str = ""
    caption: str = ""
    created_at: Optional[str] = None
    duration: int = 0
    views: int = 0
    likes: int = 0
    comments: int = 0
    shares: int = 0
    hashtags: List[str] = field(default_factory=list)
    sound_id: Optional[str] = None
    is_photo: bool = False
    url: Optional[str] = None

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Video":
        return cls(
            id=str(d.get("id", "")),
            author=str(d.get("author", "")),
            caption=str(d.get("caption", "")),
            created_at=d.get("created_at"),
            duration=_int(d, "duration"),
            views=_int(d, "views"),
            likes=_int(d, "likes"),
            comments=_int(d, "comments"),
            shares=_int(d, "shares"),
            hashtags=[str(t) for t in d.get("hashtags") or []],
            sound_id=d.get("sound_id"),
            is_photo=bool(d.get("is_photo", False)),
            url=d.get("url"),
        )


@dataclass(frozen=True)
class Hashtag:
    name: str
    description: str = ""
    views: int = 0
    videos: List[Video] = field(default_factory=list)
    url: Optional[str] = None

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Hashtag":
        return cls(
            name=str(d.get("name", "")),
            description=str(d.get("description", "")),
            views=_int(d, "views"),
            videos=[Video.from_dict(v) for v in d.get("videos") or []],
            url=d.get("url"),
        )


@dataclass(frozen=True)
class Sound:
    id: str
    title: str = ""
    author: str = ""
    duration: int = 0
    videos: List[Video] = field(default_factory=list)
    url: Optional[str] = None

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Sound":
        return cls(
            id=str(d.get("id", "")),
            title=str(d.get("title", "")),
            author=str(d.get("author", "")),
            duration=_int(d, "duration"),
            videos=[Video.from_dict(v) for v in d.get("videos") or []],
            url=d.get("url"),
        )


@dataclass(frozen=True)
class Page:
    """One page of a list (a profile's videos, search results, trending) and the cursor of the next one."""

    items: List[Video]
    cursor: Optional[str] = None
    has_more: bool = False

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Page":
        return cls(
            items=[Video.from_dict(v) for v in d.get("items") or []],
            cursor=d.get("cursor"),
            has_more=bool(d.get("has_more", False)),
        )
