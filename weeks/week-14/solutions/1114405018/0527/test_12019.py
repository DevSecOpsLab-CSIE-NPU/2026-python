"""12019 單元測試：驗證 2012 年日期對應星期幾。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("12019.py")


def run_input(input_text: str) -> str:
    # 透過 subprocess 模擬正式評測環境。
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class Test12019(unittest.TestCase):
    def test_sample_dates(self) -> None:
        input_text = "3\n1 11\n1 12\n12 12\n"
        self.assertEqual(run_input(input_text), "\n".join(["Wednesday", "Thursday", "Wednesday"]))

    def test_more_dates(self) -> None:
        # 2012/2/29 是閏年日期，應為 Wednesday。
        input_text = "2\n2 29\n6 6\n"
        self.assertEqual(run_input(input_text), "\n".join(["Wednesday", "Wednesday"]))


if __name__ == "__main__":
    unittest.main()