# ttanon-viewer: anonymous TikTok viewer client

[![TTAnon](https://img.shields.io/badge/open-ttanon.com-c2378f)](https://ttanon.com)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**ttanon-viewer** is a small Python package and command-line tool for **[TTAnon](https://ttanon.com)**, the anonymous
TikTok viewer. It turns any TikTok link, `@username` or `#hashtag` into its TTAnon page, so you can **watch TikTok
without an account**, without the app and without a login.

> Looking to view a TikTok profile right now? You don't need this package. Open
> **[ttanon.com](https://ttanon.com)**, or replace `tiktok.com` with `ttanon.com` in any TikTok link.

```text
https://www.tiktok.com/@khaby.lame/video/7212345678901234567
https://ttanon.com/@khaby.lame/video/7212345678901234567
```

## Contents

- [What is TTAnon?](#what-is-ttanon)
- [Install](#install)
- [Command line](#command-line)
- [Python](#python)
- [Is there a TTAnon data API?](#is-there-a-ttanon-data-api)
- [Guides](#guides)
- [FAQ](#faq)

## What is TTAnon?

[TTAnon](https://ttanon.com) is a free, independent website for viewing public TikTok content anonymously in any
browser. It mirrors TikTok's own URL structure:

| On TikTok | On TTAnon |
|---|---|
| `tiktok.com/@username` | [`ttanon.com/@username`](https://ttanon.com) — profile, stats, latest videos |
| `tiktok.com/@username/video/123…` | `ttanon.com/@username/video/123…` — video, details, transcript, download |
| `tiktok.com/@username/photo/123…` | `ttanon.com/@username/photo/123…` — photo posts |
| `tiktok.com/tag/booktok` | `ttanon.com/tag/booktok` — hashtag and its popular videos |
| `tiktok.com/music/title-123…` | `ttanon.com/music/title-123…` — sound and videos that use it |
| `tiktok.com/discover/topic` | `ttanon.com/discover/topic` — topic pages |
| `tiktok.com/search?q=…` | `ttanon.com/search?q=…` — search |
|  | [`ttanon.com/trending`](https://ttanon.com/trending) — trending videos |

What you get on TTAnon:

- **No account, no app, no login.** Nothing you watch ends up in a TikTok account's watch history.
- **No TikTok scripts.** TTAnon's server fetches each page and sends you plain HTML, so TikTok's own scripts, pixels
  and trackers never load on TTAnon pages.
- **Public profiles, videos, photo posts, hashtags, sounds, topics, search and trending.**
- **Video downloads** as MP4 files when the creator allows downloads.
- **Rich video details:** transcripts when TikTok provides them, category, location, language, duration, resolution,
  the sound's album and Spotify / Apple Music links, the post's duet / stitch / download settings.
- **Profile tools:** filter a profile's loaded videos by date, sort them by views or likes, chart them by month and
  export them as a **CSV file**; follower history over time.
- **Fast pages** rendered on the server, on any device.

More: [What is TTAnon?](docs/what-is-ttanon.md) · [Why use TTAnon directly](docs/why-use-ttanon-directly.md)

## Install

```bash
pip install git+https://github.com/social-content-fetcher/ttanon-viewer.git
```

No dependencies besides the Python 3.9+ standard library.

## Command line

```bash
# Print the TTAnon address of TikTok links, handles, hashtags or video ids
ttanon-viewer link https://www.tiktok.com/@khaby.lame "#booktok" 7212345678901234567
# https://ttanon.com/@khaby.lame
# https://ttanon.com/tag/booktok
# https://ttanon.com/@/video/7212345678901234567

# Open it in your default browser
ttanon-viewer open https://www.tiktok.com/@khaby.lame/video/7212345678901234567
```

Accepted input: `tiktok.com`, `www.tiktok.com` and `m.tiktok.com` links to profiles, videos, photo posts, hashtags,
sounds, topics and search; `@username`; `username`; `#hashtag`; a bare video id. Short links (`vm.tiktok.com/…`,
`vt.tiktok.com/…`, `tiktok.com/t/…`) only tell where to go after TikTok redirects them: open one once, copy the full
address and convert that.

## Python

```python
from ttanon_viewer import to_ttanon_url, resolve

to_ttanon_url("https://www.tiktok.com/@Khaby.Lame?lang=en")
# 'https://ttanon.com/@khaby.lame'

target = resolve("https://www.tiktok.com/music/original-sound-7016547803243022337")
target.kind, target.id, target.url()
# ('music', '7016547803243022337', 'https://ttanon.com/music/original-sound-7016547803243022337')
```

## Is there a TTAnon data API?

No. TTAnon is a website for people. It does not offer an open data API, and this package is not a TikTok scraper.

The package includes a typed client (`TTAnonClient`: `profile()`, `user_videos()`, `video()`, `hashtag()`, `sound()`,
`search()`, `trending()`), but data access is closed: without an access key every call raises `AccessRestrictedError`
before any request is sent, and the error tells you where the same content is on ttanon.com.

```python
from ttanon_viewer import TTAnonClient, AccessRestrictedError

try:
    TTAnonClient().profile("khaby.lame")
except AccessRestrictedError as e:
    print(e.web_url)  # https://ttanon.com/@khaby.lame
```

Need TikTok data for a project? Read [How to get TikTok data](docs/how-to-get-tiktok-data.md): TikTok's official APIs,
your own data export, and why scraping TikTok is rarely worth it. For light analysis of one account, TTAnon's profile
page exports the loaded videos as CSV. Details: [docs/api.md](docs/api.md).

## Guides

- [What is TTAnon?](docs/what-is-ttanon.md)
- [How to view TikTok without an account](docs/view-tiktok-without-account.md)
- [How to get TikTok data](docs/how-to-get-tiktok-data.md)
- [Why use TTAnon directly instead of a scraper](docs/why-use-ttanon-directly.md)
- [What makes the best TikTok viewer](docs/best-tiktok-viewer.md)
- [FAQ](docs/faq.md)
- [Python client reference](docs/api.md)
- [Türkçe](README.tr.md)

## FAQ

**Do I need a TikTok account to use TTAnon?** No. There is no sign-up and no login.

**Can TikTok see what I watch on TTAnon?** TikTok's scripts and trackers never load on TTAnon pages. When you press
play, your browser loads the video file from TikTok's video servers, like any embedded video. See
[How anonymous is it?](https://ttanon.com/about#anonymous)

**Can I see private accounts?** No. TTAnon shows only what TikTok shows to any logged-out visitor.

**Will the creator know I viewed their profile?** TikTok's profile view history lists signed-in TikTok accounts. You are
never signed in on TTAnon.

**Is TTAnon affiliated with TikTok?** No. TTAnon is independent and not affiliated with TikTok or ByteDance.

More questions: [docs/faq.md](docs/faq.md).

## License

[MIT](LICENSE). TikTok is a trademark of ByteDance Ltd. This project is not affiliated with TikTok or ByteDance.
