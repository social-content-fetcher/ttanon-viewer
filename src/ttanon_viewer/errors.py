"""Exceptions raised by ttanon-viewer."""

from __future__ import annotations

from typing import Optional


class TTAnonError(Exception):
    """Base class for every error this package raises."""


class InvalidInputError(TTAnonError, ValueError):
    """The input is not a TikTok/TTAnon link, handle, hashtag, sound or video id this package understands."""


class AccessRestrictedError(TTAnonError):
    """TTAnon refused a data request.

    TTAnon has no open data API: requests without an access key are refused before they leave your machine, and
    requests with a key the service does not accept are refused by the service. ``web_url`` is the same content on
    ttanon.com, which anyone can open in a browser.
    """

    def __init__(self, message: str, web_url: Optional[str] = None, status: Optional[int] = None) -> None:
        super().__init__(message)
        self.web_url = web_url
        self.status = status


class RateLimitedError(TTAnonError):
    """The service asked the client to slow down (HTTP 429)."""

    def __init__(self, message: str, retry_after: Optional[int] = None) -> None:
        super().__init__(message)
        self.retry_after = retry_after


class ServiceError(TTAnonError):
    """Any other failure: a network error, a 5xx answer or a body that is not the JSON the client expects."""
