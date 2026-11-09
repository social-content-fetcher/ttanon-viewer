# Python client reference

```python
import ttanon_viewer
```

## Links (always available, no network)

### `to_ttanon_url(value, base_url="https://ttanon.com") -> str`

The TTAnon address of a TikTok link, `@username`, `username`, `#hashtag` or bare video id. Raises `InvalidInputError`
for anything else, including short links (`vm.tiktok.com`, `vt.tiktok.com`, `tiktok.com/t/…`), which only TikTok can
expand.

```python
to_ttanon_url("https://www.tiktok.com/@user/video/7212345678901234567")
# 'https://ttanon.com/@user/video/7212345678901234567'
to_ttanon_url("#BookTok")
# 'https://ttanon.com/tag/booktok'
```

### `resolve(value) -> Target`

The same input as a `Target(kind, path, handle, id, name)`; `kind` is one of `profile`, `video`, `photo`, `tag`,
`music`, `topic`, `search`, `trending`, `home`. `Target.url(base_url)` gives the full address.

## Data client (closed)

### `TTAnonClient(api_key=None, base_url="https://ttanon.com", timeout=15.0)`

| Method | Returns |
|---|---|
| `url_for(value)` | `str`, same as `to_ttanon_url` (works without a key) |
| `profile(username)` | `Profile` |
| `user_videos(username, cursor=None)` | `Page` of `Video` |
| `video(link_or_id)` | `Video` |
| `hashtag(name)` | `Hashtag` |
| `sound(sound_id, title_slug="sound")` | `Sound` |
| `search(query, cursor=None)` | `Page` of `Video` |
| `trending()` | `Page` of `Video` |

TTAnon has no open data API. The data methods behave as follows:

- **No key** (`api_key` unset and no `TTANON_API_KEY` in the environment): `AccessRestrictedError` is raised and **no
  request is sent**.
- **With a key**: the request is sent; a refusal (HTTP 401, 403, 404) raises `AccessRestrictedError` with `status` set.

`AccessRestrictedError.web_url` is the same content on ttanon.com:

```python
from ttanon_viewer import TTAnonClient, AccessRestrictedError
import webbrowser

try:
    TTAnonClient().hashtag("booktok")
except AccessRestrictedError as e:
    webbrowser.open(e.web_url)  # https://ttanon.com/tag/booktok
```

## Errors

| Exception | When |
|---|---|
| `TTAnonError` | Base class |
| `InvalidInputError` (also a `ValueError`) | Input is not a link, handle, hashtag, sound or video id this package understands |
| `AccessRestrictedError` | Data access refused; see `web_url` |
| `RateLimitedError` | HTTP 429; `retry_after` in seconds when given |
| `ServiceError` | Network error, other HTTP error, or a body that is not a JSON object |

## Command line

| Command | Does |
|---|---|
| `ttanon-viewer link VALUE...` | Print TTAnon addresses |
| `ttanon-viewer open VALUE` | Open the TTAnon page in the default browser |
| `ttanon-viewer profile USERNAME [--open]` | Data call (exit code 3 when refused; `--open` opens the page instead) |
| `ttanon-viewer videos USERNAME [--open]` | 〃 |
| `ttanon-viewer video LINK_OR_ID [--open]` | 〃 |
| `ttanon-viewer tag NAME [--open]` | 〃 |
| `ttanon-viewer sound SOUND_ID [--open]` | 〃 |
| `ttanon-viewer search QUERY [--open]` | 〃 |
| `ttanon-viewer trending [--open]` | 〃 |

Exit codes: `0` success, `2` invalid input or other error, `3` data access refused.
