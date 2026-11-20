#!/usr/bin/env python3
"""
Unit Test Suite for Student Workshop Twitter Thread
"""

import unittest
from thread_content import TWEETS
from verify_thread import verify_all_tweets

class TestStudentWorkshopThread(unittest.TestCase):
    def test_compliance(self):
        res = verify_all_tweets()
        self.assertTrue(res["valid"], f"Thread validation failed: {res['errors']}")
        self.assertGreaterEqual(res["total_tweets"], 8)
        self.assertLessEqual(res["total_tweets"], 12)

    def test_character_limits(self):
        for t in TWEETS:
            self.assertLessEqual(
                len(t["content"]), 280, 
                f"Tweet {t['index']} is {len(t['content'])} chars (max 280)"
            )

    def test_tags_present(self):
        all_text = " ".join([t["content"] for t in TWEETS])
        self.assertIn("@SuperteamUKR", all_text)
        self.assertIn("@dev3pack", all_text)

    def test_key_programs_mentioned(self):
        all_text = " ".join([t["content"] for t in TWEETS])
        self.assertIn("Instagrants", all_text)
        self.assertIn("Bridge Accelerator", all_text)
        self.assertIn("Colosseum", all_text)
        self.assertIn("Solana", all_text)

if __name__ == "__main__":
    unittest.main()
