import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("q4_binary_search_eval.py")
RADAR = Path(__file__).with_name("assets") / "radar.png"


class TestQ4BinarySearchEval(unittest.TestCase):
    def test_search_results(self):
        from q4_binary_search_eval import ARR, K, binary_search, linear_search

        self.assertEqual(linear_search(ARR, K), (True, 139, 140))
        self.assertEqual(binary_search(ARR, K), (True, 139, 17))

    def test_not_found_format(self):
        from q4_binary_search_eval import format_search_result

        self.assertEqual(
            format_search_result((False, -1, 5)),
            "NOT FOUND cmp=5",
        )

    def test_program_outputs_radar_png(self):
        if RADAR.exists():
            RADAR.unlink()

        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            text=True,
            capture_output=True,
            check=True,
        )

        self.assertIn("FOUND idx=139 cmp=140", completed.stdout)
        self.assertIn("FOUND idx=139 cmp=17", completed.stdout)
        self.assertIn("=> binary faster", completed.stdout)
        self.assertTrue(RADAR.exists())
        self.assertGreater(RADAR.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()
