"""``ttanon-viewer`` command line.

    ttanon-viewer link https://www.tiktok.com/@user/video/123   # print the TTAnon address
    ttanon-viewer open @user                                    # open it in your browser
    ttanon-viewer profile user                                  # data call: needs an access key
"""

from __future__ import annotations

import argparse
import json
import sys
import webbrowser
from dataclasses import asdict
from typing import List, Optional

from . import __version__
from .client import TTAnonClient
from .errors import AccessRestrictedError, TTAnonError


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ttanon-viewer", description="Open TikTok content on TTAnon (https://ttanon.com) without an account.")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    p.add_argument("--base-url", default="https://ttanon.com", help=argparse.SUPPRESS)
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("link", help="print the TTAnon address of a TikTok link, @handle, #hashtag or video id")
    s.add_argument("value", nargs="+")
    s = sub.add_parser("open", help="open the TTAnon page in your default browser")
    s.add_argument("value")

    for name, arg, help_ in (
        ("profile", "username", "profile data of a public account"),
        ("videos", "username", "a public account's videos"),
        ("video", "link_or_id", "data of a video or photo post"),
        ("tag", "name", "a hashtag and its popular videos"),
        ("sound", "sound_id", "a sound and its videos"),
        ("search", "query", "search results"),
    ):
        s = sub.add_parser(name, help=f"{help_} (needs an access key)")
        s.add_argument(arg)
        s.add_argument("--open", action="store_true", help="open the TTAnon page when the data call is refused")
    s = sub.add_parser("trending", help="trending videos (needs an access key)")
    s.add_argument("--open", action="store_true", help="open the TTAnon page when the data call is refused")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    args = _parser().parse_args(argv)
    client = TTAnonClient(base_url=args.base_url)
    try:
        if args.command == "link":
            for v in args.value:
                print(client.url_for(v))
            return 0
        if args.command == "open":
            url = client.url_for(args.value)
            print(url)
            webbrowser.open(url)
            return 0

        calls = {
            "profile": lambda: client.profile(args.username),
            "videos": lambda: client.user_videos(args.username),
            "video": lambda: client.video(args.link_or_id),
            "tag": lambda: client.hashtag(args.name),
            "sound": lambda: client.sound(args.sound_id),
            "search": lambda: client.search(args.query),
            "trending": lambda: client.trending(),
        }
        print(json.dumps(asdict(calls[args.command]()), ensure_ascii=False, indent=2))
        return 0
    except AccessRestrictedError as e:
        print(f"ttanon-viewer: {e}", file=sys.stderr)
        if getattr(args, "open", False) and e.web_url:
            webbrowser.open(e.web_url)
        return 3
    except TTAnonError as e:
        print(f"ttanon-viewer: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
