import unittest

from ttanon_viewer import InvalidInputError, to_ttanon_url


class LinkTests(unittest.TestCase):
    def test_tiktok_links(self):
        cases = {
            "https://www.tiktok.com/@Khaby.Lame": "https://ttanon.com/@khaby.lame",
            "https://www.tiktok.com/@khaby.lame?lang=en": "https://ttanon.com/@khaby.lame",
            "tiktok.com/@khaby.lame/video/7212345678901234567?is_from_webapp=1": "https://ttanon.com/@khaby.lame/video/7212345678901234567",
            "https://www.tiktok.com/@user/photo/7300000000000000001": "https://ttanon.com/@user/photo/7300000000000000001",
            "https://m.tiktok.com/v/7212345678901234567.html": "https://ttanon.com/@/video/7212345678901234567",
            "https://www.tiktok.com/tag/BookTok": "https://ttanon.com/tag/booktok",
            "https://www.tiktok.com/music/original-sound-7016547803243022337": "https://ttanon.com/music/original-sound-7016547803243022337",
            "https://www.tiktok.com/discover/easy-recipes": "https://ttanon.com/discover/easy-recipes",
            "https://www.tiktok.com/search?q=cat%20videos": "https://ttanon.com/search?q=cat%20videos",
            "https://www.tiktok.com/": "https://ttanon.com/",
            "https://ttanon.com/@khaby.lame": "https://ttanon.com/@khaby.lame",
        }
        for value, want in cases.items():
            with self.subTest(value=value):
                self.assertEqual(to_ttanon_url(value), want)

    def test_shorthands(self):
        self.assertEqual(to_ttanon_url("@charlidamelio"), "https://ttanon.com/@charlidamelio")
        self.assertEqual(to_ttanon_url("charlidamelio"), "https://ttanon.com/@charlidamelio")
        self.assertEqual(to_ttanon_url("khaby.lame"), "https://ttanon.com/@khaby.lame")
        self.assertEqual(to_ttanon_url("#FYP"), "https://ttanon.com/tag/fyp")
        self.assertEqual(to_ttanon_url("7212345678901234567"), "https://ttanon.com/@/video/7212345678901234567")

    def test_rejected(self):
        for value in ("", "https://vm.tiktok.com/ZMabc123/", "https://www.tiktok.com/t/ZTabc/", "https://example.com/@x",
                      "@" + "a" * 31, "#", "https://www.tiktok.com/@x/video/abc", "https://www.tiktok.com/upload"):
            with self.subTest(value=value):
                with self.assertRaises(InvalidInputError):
                    to_ttanon_url(value)


if __name__ == "__main__":
    unittest.main()
