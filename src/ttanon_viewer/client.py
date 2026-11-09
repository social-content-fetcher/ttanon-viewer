"""Data client for TTAnon.

TTAnon (https://ttanon.com) is a website for people, not a data API. The data endpoints this client speaks are closed:

* without an access key (``api_key=`` or the ``TTANON_API_KEY`` environment variable) every data call raises
  :class:`~ttanon_viewer.errors.AccessRestrictedError` before any request is sent;
* with a key, the request is sent and the service's refusal (401, 403, 404) is raised as the same error.

Every :class:`AccessRestrictedError` carries ``web_url``: the same profile, video, hashtag or sound on ttanon.com, which
anyone can open in a browser without an account. That is the supported way to view TikTok through TTAnon.
"""

from __future__ import annotations

import json
import os
from typing import Any, Callable, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from . import __version__, links
from .errors import AccessRestrictedError, InvalidInputError, RateLimitedError, ServiceError
from .models import Hashtag, Page, Profile, Sound, Video

API_PATH = "/api/v1"
ENV_KEY = "TTANON_API_KEY"

_CLOSED = (
    "TTAnon has no open data API, so this request was not sent. "
    "Open the page in your browser instead (no account needed): {url}"
)
_REFUSED = "TTAnon refused the data request (HTTP {status}). Open the page in your browser instead: {url}"

Opener = Callable[..., Any]


class TTAnonClient:
    """Typed access to TTAnon pages; see the module docstring for what works without an access key (only links)."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = links.DEFAULT_BASE_URL,
        timeout: float = 15.0,
        opener: Optional[Opener] = None,
    ) -> None:
        self.api_key = api_key if api_key is not None else os.environ.get(ENV_KEY) or None
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._open = opener or urlopen

    # -- links: always available, no network ---------------------------------------------------------------------

    def url_for(self, value: str) -> str:
        """The TTAnon page of a TikTok link, ``@handle``, ``#hashtag`` or video id."""
        return links.to_ttanon_url(value, self.base_url)

    # -- data: needs an access key ---------------------------------------------------------------------------------

    def profile(self, username: str) -> Profile:
        t = links.profile(username)
        return Profile.from_dict(self._get(f"/users/{quote(t.handle or '')}", t))

    def user_videos(self, username: str, cursor: Optional[str] = None) -> Page:
        t = links.profile(username)
        return Page.from_dict(self._get(f"/users/{quote(t.handle or '')}/videos", t, {"cursor": cursor}))

    def video(self, link_or_id: str) -> Video:
        t = links.resolve(link_or_id)
        if t.kind not in ("video", "photo"):
            raise InvalidInputError(f"not a TikTok video or photo post: {link_or_id!r}")
        return Video.from_dict(self._get(f"/videos/{t.id}", t))

    def hashtag(self, name: str) -> Hashtag:
        t = links.tag(name)
        return Hashtag.from_dict(self._get(f"/tags/{quote(t.name or '', safe='')}", t))

    def sound(self, sound_id: str, title_slug: str = "sound") -> Sound:
        t = links.music(sound_id, title_slug)
        return Sound.from_dict(self._get(f"/music/{t.id}", t))

    def search(self, query: str, cursor: Optional[str] = None) -> Page:
        t = links.search(query)
        return Page.from_dict(self._get("/search", t, {"q": t.name, "cursor": cursor}))

    def trending(self) -> Page:
        t = links.trending()
        return Page.from_dict(self._get("/trending", t))

    # -- transport ---------------------------------------------------------------------------------------------------

    def _get(self, path: str, target: links.Target, params: Optional[Dict[str, Optional[str]]] = None) -> Dict[str, Any]:
        web_url = target.url(self.base_url)
        if not self.api_key:
            raise AccessRestrictedError(_CLOSED.format(url=web_url), web_url=web_url)

        query = urlencode({k: v for k, v in (params or {}).items() if v})
        url = f"{self.base_url}{API_PATH}{path}" + (f"?{query}" if query else "")
        req = Request(
            url,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "User-Agent": f"ttanon-viewer/{__version__}",
            },
        )
        try:
            with self._open(req, timeout=self.timeout) as resp:
                body = resp.read()
        except HTTPError as e:
            if e.code in (401, 403, 404):
                raise AccessRestrictedError(_REFUSED.format(status=e.code, url=web_url), web_url=web_url, status=e.code) from None
            if e.code == 429:
                retry = e.headers.get("Retry-After") if e.headers else None
                raise RateLimitedError("TTAnon asked to slow down (HTTP 429)", int(retry) if retry and retry.isdigit() else None) from None
            raise ServiceError(f"TTAnon answered HTTP {e.code}") from None
        except URLError as e:
            raise ServiceError(f"could not reach TTAnon: {e.reason}") from None

        try:
            data = json.loads(body)
        except ValueError:
            raise ServiceError("TTAnon's answer was not JSON") from None
        if not isinstance(data, dict):
            raise ServiceError("TTAnon's answer was not a JSON object")
        return data
