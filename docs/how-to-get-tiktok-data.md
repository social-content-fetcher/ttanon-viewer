# How to get TikTok data

"How do I get TikTok data?" has a different answer depending on what you need. Most people asking only want to **look
at** a profile or video without the app; a few need **structured data** for research or a product. This page covers
both, starting with the simplest option.

## 1. You want to look at TikTok content → use a viewer

If the goal is to see a profile, a video, a hashtag or what is trending, you don't need data or code. Open it on
**[TTAnon](https://ttanon.com)**: replace `tiktok.com` with `ttanon.com` in any link, or search on the home page. No
account, no app, no login. See [How to view TikTok without an account](view-tiktok-without-account.md).

## 2. You want a quick table of one account's videos → TTAnon's CSV export

On a TTAnon profile page you can filter the loaded videos by date, sort them by views or likes, chart them by month and
**export them as a CSV file** you can open in Excel, Google Sheets or pandas. That covers most one-off questions
("which of this creator's recent videos did best?") without any scraping.

## 3. You want your own TikTok data → TikTok's data download

TikTok lets every account holder download their own data (videos, comments, watch history, likes and more) from the
app's settings (**Settings and privacy → Account → Download your data**). Developers can request the same with TikTok's
**Data Portability API**, with the user's consent.

## 4. You are building an app → TikTok's official APIs

TikTok for Developers ([developers.tiktok.com](https://developers.tiktok.com)) offers official, documented access:

| Product | For |
|---|---|
| **Embed / oEmbed** | Embedding a public video or profile on your site; the oEmbed endpoint returns the title, author and thumbnail of a public video link |
| **Login Kit + Display API** | Showing a signed-in user's own profile and videos in your app |
| **Content Posting API** | Posting to TikTok on a user's behalf |
| **Research API** | Public video, comment and account data for approved, non-commercial academic research |
| **Commercial Content API** | Ads and commercial content shown on TikTok in the EU |

These are the only routes TikTok supports for structured data, and they come with terms, review and rate limits.

## 5. "Can't I just scrape TikTok?"

Plenty of repositories promise a working TikTok scraper. In practice:

- **It breaks often.** TikTok changes its web app, request formats and protections regularly; scrapers that worked last
  month stop working without notice.
- **It is blocked.** Automated traffic meets captchas, challenges and blocked IP addresses. Keeping a scraper running
  means a constant fight against bot detection, and it gets more expensive the more you need.
- **It is against the terms.** TikTok's Terms of Service do not allow automated collection of its content without
  permission. Collecting personal data in bulk can also raise privacy-law obligations (GDPR, CCPA and others).
- **It costs more than it looks.** Servers, proxies and maintenance time add up quickly for data you could often get
  from an official API or not need at all.

This repository does not contain a TikTok scraper and TTAnon does not offer one: the [Python client](api.md) here only
converts links and points you to the TTAnon page.

## Which one should I use?

| You need… | Use |
|---|---|
| To watch a video, browse a profile or hashtag | [TTAnon](https://ttanon.com) |
| A spreadsheet of one creator's recent videos | TTAnon profile → CSV export |
| Your own account's data | TikTok's "Download your data" / Data Portability API |
| Embeds on your website | TikTok Embed / oEmbed |
| Academic research datasets | TikTok Research API |
| A product that shows users their own TikTok content | Login Kit + Display API |

## See also

- [Why use TTAnon directly instead of a scraper](why-use-ttanon-directly.md)
- [What is TTAnon?](what-is-ttanon.md)
