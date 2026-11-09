import io
import os
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock
from urllib.error import HTTPError

from ttanon_viewer import AccessRestrictedError, TTAnonClient
from ttanon_viewer.cli import main


def _refusing_opener(code):
    calls = []

    def opener(req, timeout):
        calls.append(req)
        raise HTTPError(req.full_url, code, "refused", hdrs=None, fp=None)

    return opener, calls


class ClientTests(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.dict(os.environ, {}, clear=False)
        patcher.start()
        os.environ.pop("TTANON_API_KEY", None)
        self.addCleanup(patcher.stop)

    def test_no_key_sends_nothing(self):
        opener, calls = _refusing_opener(200)
        client = TTAnonClient(opener=opener)
        for call, want in (
            (lambda: client.profile("Khaby.Lame"), "https://ttanon.com/@khaby.lame"),
            (lambda: client.video("https://www.tiktok.com/@a/video/7212345678901234567"), "https://ttanon.com/@a/video/7212345678901234567"),
            (lambda: client.hashtag("#booktok"), "https://ttanon.com/tag/booktok"),
            (lambda: client.trending(), "https://ttanon.com/trending"),
        ):
            with self.assertRaises(AccessRestrictedError) as ctx:
                call()
            self.assertEqual(ctx.exception.web_url, want)
        self.assertEqual(calls, [])

    def test_refused_with_key(self):
        for code in (401, 403, 404):
            opener, calls = _refusing_opener(code)
            client = TTAnonClient(api_key="k", opener=opener)
            with self.assertRaises(AccessRestrictedError) as ctx:
                client.profile("someone")
            self.assertEqual(ctx.exception.status, code)
            self.assertEqual(ctx.exception.web_url, "https://ttanon.com/@someone")
            self.assertEqual(calls[0].full_url, "https://ttanon.com/api/v1/users/someone")

    def test_url_for(self):
        self.assertEqual(TTAnonClient().url_for("https://www.tiktok.com/@x"), "https://ttanon.com/@x")


class CliTests(unittest.TestCase):
    def test_link(self):
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(main(["link", "https://www.tiktok.com/@x", "#cats"]), 0)
        self.assertEqual(out.getvalue().split(), ["https://ttanon.com/@x", "https://ttanon.com/tag/cats"])

    def test_data_command_points_to_site(self):
        err = io.StringIO()
        with mock.patch.dict(os.environ, {"TTANON_API_KEY": ""}), redirect_stderr(err):
            self.assertEqual(main(["profile", "x"]), 3)
        self.assertIn("https://ttanon.com/@x", err.getvalue())


if __name__ == "__main__":
    unittest.main()
