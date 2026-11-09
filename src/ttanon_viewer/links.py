"""Turn TikTok links, handles and hashtags into their TTAnon page.

TTAnon mirrors TikTok's URL structure, so most links only need their host swapped::

    https://www.tiktok.com/@khaby.lame/video/7212345678901234567
    https://ttanon.com/@khaby.lame/video/7212345678901234567

Everything here is pure string handling: no network request is made.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional
from urllib.parse import parse_qs, quote, unquote, urlsplit

from .errors import InvalidInputError

DEFAULT_BASE_URL = "https://ttanon.com"

TIKTOK_HOSTS = {"tiktok.com", "www.tiktok.com", "m.tiktok.com"}
TTANON_HOSTS = {"ttanon.com", "www.ttanon.com"}
SHORT_LINK_HOSTS = {"vm.tiktok.com", "vt.tiktok.com"}

_HANDLE_RE = re.compile(r"^[a-z0-9._]{1,30}$")
_POST_HANDLE_RE = re.compile(r"^[a-z0-9._-]{0,64}$")
_ID_RE = re.compile(r"^\d{1,25}$")
_TAG_RE = re.compile(r"^\w{1,100}$", re.UNICODE)
_MUSIC_RE = re.compile(r"^(?P<slug>.*?)-?(?P<id>\d{1,25})$")


@dataclass(frozen=True)
class Target:
    """A page TTAnon serves: its kind and the canonical path on ttanon.com."""

    kind: str  # "profile", "video", "photo", "tag", "music", "topic", "search", "trending", "home"
    path: str
    handle: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

    def url(self, base_url: str = DEFAULT_BASE_URL) -> str:
        return base_url.rstrip("/") + self.path


def _handle(raw: str) -> str:
    h = unquote(raw).strip().lstrip("@").lower()
    if not _HANDLE_RE.match(h) or set(h) == {"."}:
        raise InvalidInputError(f"not a TikTok username: {raw!r}")
    return h


def _post_handle(raw: str) -> str:
    h = unquote(raw).strip().lstrip("@").lower()
    if not _POST_HANDLE_RE.match(h):
        raise InvalidInputError(f"not a TikTok username: {raw!r}")
    return h


def _tag(raw: str) -> str:
    t = unquote(raw).strip().lstrip("#").lower()
    if not _TAG_RE.match(t):
        raise InvalidInputError(f"not a TikTok hashtag: {raw!r}")
    return t


def _video_id(raw: str) -> str:
    s = raw.strip()
    if not _ID_RE.match(s) or not s.strip("0"):
        raise InvalidInputError(f"not a TikTok video id: {raw!r}")
    return s.lstrip("0")


def profile(handle: str) -> Target:
    h = _handle(handle)
    return Target("profile", f"/@{h}", handle=h)


def post(video_id: str, handle: str = "", photo: bool = False) -> Target:
    """A video or photo post. Without the author's handle TTAnon finds the author itself (``/@/video/{id}``)."""
    h = _post_handle(handle) if handle else ""
    vid = _video_id(video_id)
    kind = "photo" if photo else "video"
    return Target(kind, f"/@{h}/{kind}/{vid}", handle=h or None, id=vid)


def tag(name: str) -> Target:
    t = _tag(name)
    return Target("tag", f"/tag/{quote(t, safe='')}", name=t)


def music(sound_id: str, title_slug: str = "sound") -> Target:
    if not _ID_RE.match(sound_id):
        raise InvalidInputError(f"not a TikTok sound id: {sound_id!r}")
    slug = quote(title_slug.strip("-") or "sound", safe="-")
    return Target("music", f"/music/{slug}-{sound_id}", id=sound_id, name=title_slug)


def topic(slug: str) -> Target:
    s = unquote(slug).strip().strip("/")
    if not s:
        raise InvalidInputError("empty topic")
    return Target("topic", f"/discover/{quote(s, safe='-')}", name=s)


def search(query: str) -> Target:
    q = query.strip()
    if not q:
        raise InvalidInputError("empty search query")
    return Target("search", f"/search?q={quote(q, safe='')}", name=q)


def trending() -> Target:
    return Target("trending", "/trending")


def _from_path(path: str, query: str) -> Target:
    segs = [s for s in path.split("/") if s]
    if not segs:
        return Target("home", "/")
    first = unquote(segs[0]).lower()
    if first.startswith("@"):
        handle = first
        if len(segs) >= 3 and segs[1].lower() in ("video", "photo"):
            return post(segs[2], handle, photo=segs[1].lower() == "photo")
        return profile(handle)
    if first == "tag" and len(segs) >= 2:
        return tag(segs[1])
    if first == "music" and len(segs) >= 2:
        m = _MUSIC_RE.match(unquote(segs[1]))
        if not m:
            raise InvalidInputError(f"not a TikTok sound link: {path!r}")
        return music(m.group("id"), m.group("slug") or "sound")
    if first == "discover" and len(segs) >= 2:
        return topic(segs[1])
    if first == "search":
        q = parse_qs(query).get("q", [""])[0]
        return search(q)
    if first in ("trending", "foryou", "explore"):
        return trending()
    if first == "video" and len(segs) >= 2:
        return post(segs[1])
    if first == "v" and len(segs) >= 2:  # m.tiktok.com/v/{id}.html
        return post(segs[1].split(".")[0])
    if first == "t":
        raise InvalidInputError(_SHORT_LINK_HINT)
    raise InvalidInputError(f"no TTAnon page for this TikTok path: {path!r}")


_SHORT_LINK_HINT = (
    "short links (vm.tiktok.com, vt.tiktok.com, tiktok.com/t/...) only say where to go after TikTok redirects them: "
    "open the link once, copy the full tiktok.com/@user/video/... address and convert that one"
)


def resolve(value: str) -> Target:
    """Any TikTok or TTAnon link, ``@handle``, ``#hashtag``, bare video id or bare username → its TTAnon page.

    A bare number is read as a video id; write ``@123`` for a username made of digits only.
    """
    v = value.strip()
    if not v:
        raise InvalidInputError("empty input")
    if v.startswith("#"):
        return tag(v)
    if v.startswith("@") and "/" not in v:
        return profile(v)
    if _ID_RE.match(v):
        return post(v)
    known_hosts = TIKTOK_HOSTS | TTANON_HOSTS | SHORT_LINK_HOSTS
    if "/" not in v and "?" not in v and v.lower() not in known_hosts:
        return profile(v)
    parts = urlsplit(v if "://" in v else "https://" + v)
    host = (parts.hostname or "").lower()
    if host in SHORT_LINK_HOSTS:
        raise InvalidInputError(_SHORT_LINK_HINT)
    if host not in TIKTOK_HOSTS | TTANON_HOSTS:
        raise InvalidInputError(f"not a TikTok link: {value!r}")
    return _from_path(parts.path, parts.query)


def to_ttanon_url(value: str, base_url: str = DEFAULT_BASE_URL) -> str:
    """``https://www.tiktok.com/@user`` → ``https://ttanon.com/@user`` (see :func:`resolve` for accepted input)."""
    return resolve(value).url(base_url)
