# How to view TikTok without an account

TikTok's website shows a few videos to logged-out visitors, then asks you to log in or open the app. To keep watching
public TikTok content without an account, use an anonymous TikTok viewer such as **[TTAnon](https://ttanon.com)**.

## View a TikTok profile without an account

1. Open **[ttanon.com](https://ttanon.com)**.
2. Type the username (with or without `@`) in the search box, or go straight to `ttanon.com/@username`.
3. The profile opens with its bio, follower / like / video counts and newest videos. Tap a video to watch it.

## Watch a TikTok video someone sent you

1. Copy the TikTok link, e.g. `https://www.tiktok.com/@username/video/7212345678901234567`.
2. Replace `tiktok.com` with `ttanon.com`: `https://ttanon.com/@username/video/7212345678901234567`.
3. Open it. No login prompt, no app banner.

Short links (`vm.tiktok.com/…`) need one extra step: open the short link once, copy the full address it lands on
(`tiktok.com/@…/video/…`) and swap the domain in that one.

From a terminal:

```bash
ttanon-viewer open https://www.tiktok.com/@username/video/7212345678901234567
```

## Browse hashtags, sounds and trends

- Hashtag: `ttanon.com/tag/booktok`
- Sound: `ttanon.com/music/title-ID` (same address as on TikTok)
- Topics: [ttanon.com/discover](https://ttanon.com/discover)
- Trending: [ttanon.com/trending](https://ttanon.com/trending)
- Search: the search box on every page

## Download a TikTok video

On a video page, use the download button to save the video as an MP4 file. The button appears when the creator allows
downloads; photo posts and videos whose creator turned downloads off have no download button.

## Does it work on iPhone and Android?

Yes. TTAnon is a website: it works in Safari, Chrome, Firefox or any other browser on phones, tablets and computers.
Nothing to install.

## Is it anonymous?

You never sign in, and TikTok's scripts and trackers never load on TTAnon pages. When you press play, your browser
loads the video file from TikTok's video servers. Details: [How anonymous is it?](https://ttanon.com/about#anonymous)

## See also

- [What is TTAnon?](what-is-ttanon.md)
- [FAQ](faq.md)
