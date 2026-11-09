# What is TTAnon?

**[TTAnon](https://ttanon.com)** is an anonymous TikTok viewer: a free website where you can watch public TikTok videos
and browse public profiles, hashtags, sounds and topics in any browser, **without a TikTok account, the app or a login
wall**.

The name says what it does: **TT** for TikTok, **Anon** for anonymous.

## How it works

When you open a page on TTAnon, TTAnon's server fetches the public content from TikTok and sends your browser a plain,
fast HTML page. Your browser talks to TTAnon, not to TikTok's website, so:

- TikTok's own scripts, tracking pixels and trackers never load on TTAnon pages;
- there is nothing to sign in to, so what you watch is not added to a TikTok account's watch history;
- the page works without the TikTok app and without TikTok's login prompts.

When you press play on a video, your browser loads the video file itself from TikTok's video servers, the same way an
embedded video loads from its host. Pages, images, sounds, captions and downloads come from TTAnon.
([How anonymous is it?](https://ttanon.com/about#anonymous))

## Same URLs as TikTok

TTAnon mirrors TikTok's address structure. To open any TikTok link on TTAnon, replace `tiktok.com` with `ttanon.com`:

```text
https://www.tiktok.com/@username            →  https://ttanon.com/@username
https://www.tiktok.com/@username/video/ID   →  https://ttanon.com/@username/video/ID
https://www.tiktok.com/tag/hashtag          →  https://ttanon.com/tag/hashtag
```

The [`ttanon-viewer`](../README.md) command does this for you: `ttanon-viewer open <tiktok link>`.

## What you can see

| Page | What it shows |
|---|---|
| **Profile** (`/@username`) | Name, bio, follower / like / video counts with their date, the newest videos (pinned first), follower history, join date |
| **Video** (`/@username/video/ID`) | The video, caption, stats, transcript when TikTok provides one, category, tagged location, language, duration · resolution · fps, repost count, the sound with album and Spotify / Apple Music links, duet / stitch / comment / download settings, related searches |
| **Photo post** (`/@username/photo/ID`) | Every photo of a slideshow post with its caption and stats |
| **Hashtag** (`/tag/name`) | TikTok's description of the hashtag and its popular videos |
| **Sound** (`/music/title-ID`) | The sound and public videos that use it |
| **Topic** (`/discover/topic`) | Videos about a topic, with related topics |
| **Search** (`/search?q=…`) | Creators and videos for a query |
| **Trending** (`/trending`) | Trending videos |
| **Creators** (`/creators`) | Popular creators |

## Tools

- **Download** a video as an MP4 file when its creator allows downloads.
- On a profile: **filter** the loaded videos by date, **sort** them by views or likes, **chart** them by month and
  **export a CSV file**.
- **Follower history**: how an account's follower count changed over time
  ([how stats are counted](https://ttanon.com/about/stats)).

## What TTAnon does not do

- It does not show private accounts or private videos: only what TikTok shows any logged-out visitor.
- It does not post, like, follow or comment: there is no account.
- It is not TikTok and is not affiliated with TikTok or ByteDance. Creators can ask for removal on the
  [removal / DMCA page](https://ttanon.com/dmca).

## See also

- [How to view TikTok without an account](view-tiktok-without-account.md)
- [Why use TTAnon directly](why-use-ttanon-directly.md)
- [FAQ](faq.md)
