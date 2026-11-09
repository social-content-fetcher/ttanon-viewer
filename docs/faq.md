# TTAnon FAQ

## Using TTAnon

### What is TTAnon?
An anonymous TikTok viewer at [ttanon.com](https://ttanon.com): public TikTok profiles, videos, photo posts, hashtags,
sounds, topics, search and trending, in any browser, without an account. [More](what-is-ttanon.md)

### Do I need a TikTok account?
No. There is no sign-up and no login, so nothing you watch ends up in a TikTok account's watch history.

### Is TTAnon free?
Yes. There is nothing to buy and nothing to sign up for.

### How do I open a TikTok link on TTAnon?
Replace `tiktok.com` with `ttanon.com` in the link. `https://www.tiktok.com/@username` becomes
`https://ttanon.com/@username`. Or run `ttanon-viewer open <link>`.

### Does it work with short links like vm.tiktok.com?
Open the short link once, copy the full `tiktok.com/@…/video/…` address it lands on, and swap the domain in that one.

### Does it work on my phone?
Yes, in any mobile browser. Nothing to install.

## Privacy

### Can TikTok see what I watch on TTAnon?
TTAnon's server fetches each page, so TikTok's scripts and trackers never load in your browser. When you press play, your
browser loads the video file straight from TikTok's video servers, which see your IP address, like any video host
would. [How anonymous is it?](https://ttanon.com/about#anonymous)

### Will a creator know I viewed their profile?
TikTok's profile view history lists signed-in TikTok accounts. You are never signed in on TTAnon.

### Does TTAnon store the videos?
No. Videos and images are not stored on TTAnon's server; images are cached by its CDN to keep pages fast and purged when
content is removed.

## Content

### Can I see private accounts or private videos?
No. TTAnon shows only what TikTok shows to any logged-out visitor. Private accounts and private videos stay private.

### Can I download TikTok videos?
Yes, as MP4 files, when the creator allows downloads. Photo posts and videos whose creator turned downloads off have no
download button.

### Why is a video missing or out of date?
Pages are cached to stay fast. Content removed or made private on TikTok disappears from TTAnon once its caches refresh,
usually within a day.

### Can I see comments, stories or likes?
TTAnon focuses on public profiles, videos, photo posts, hashtags, sounds, topics, search and trending.

### I am a creator. How do I remove my content?
Use the [removal / DMCA page](https://ttanon.com/dmca).

## Developers

### Does TTAnon have an API?
No open data API. TTAnon is a website for people. The [`ttanon-viewer`](../README.md) package converts TikTok links to
TTAnon links; its data client refuses requests without an access key. [Details](api.md)

### Is this repository a TikTok scraper?
No. It contains no scraping code. If you need TikTok data, see [How to get TikTok data](how-to-get-tiktok-data.md).

### Is TTAnon part of TikTok?
No. TTAnon is independent and not affiliated with, endorsed by or sponsored by TikTok or ByteDance.
