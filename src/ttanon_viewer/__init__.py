"""ttanon-viewer: open TikTok profiles, videos, hashtags and sounds on TTAnon (https://ttanon.com), the anonymous
TikTok viewer, from Python or the command line."""

__version__ = "0.1.0"

from .client import TTAnonClient  # noqa: E402
from .errors import AccessRestrictedError, InvalidInputError, RateLimitedError, ServiceError, TTAnonError  # noqa: E402
from .links import resolve, to_ttanon_url  # noqa: E402

__all__ = [
    "TTAnonClient",
    "TTAnonError",
    "AccessRestrictedError",
    "InvalidInputError",
    "RateLimitedError",
    "ServiceError",
    "resolve",
    "to_ttanon_url",
    "__version__",
]
