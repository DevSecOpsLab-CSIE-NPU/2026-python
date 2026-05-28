"""UVA 11005 單元測試。

這裡用整支程式的標準輸入/輸出來驗證，
比較接近實際交作業時的執行方式。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("11005.py")


def run_program(input_text: str) -> str:
    """執行解題程式並回傳標準輸出。"""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


class TestUVA11005(unittest.TestCase):
    def test_all_costs_are_one(self) -> None:
        # 當所有字元成本都一樣時，0 會在所有進位制下成本相同。
        # 31 則會偏好可以用單一位數表示的 32 進位以上。
        costs = " ".join(["1"] * 36)
        all_bases = " ".join(str(base) for base in range(2, 37))
        high_bases = " ".join(str(base) for base in range(32, 37))

        input_text = f"""1
{costs}
2
0
31
"""

        expected_output = (
            "Case 1:\n"
            f"Cheapest base(s) for number 0: {all_bases}\n"
            f"Cheapest base(s) for number 31: {high_bases}"
        )

        self.assertEqual(run_program(input_text), expected_output)

    def test_custom_costs_with_unique_and_tie_results(self) -> None:
        # 這組成本故意讓 2 進位較便宜，並讓 2 與 3 進位出現平手。
        costs = [1, 1] + [100] * 34
        cost_text = " ".join(str(cost) for cost in costs)

        input_text = f"""1
{cost_text}
2
2
3
"""

        expected_output = (
            "Case 1:\n"
            "Cheapest base(s) for number 2: 2\n"
            "Cheapest base(s) for number 3: 2 3"
        )

        self.assertEqual(run_program(input_text), expected_output)


if __name__ == "__main__":
    unittest.main()