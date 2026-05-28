"""UVA 11005 easy 版單元測試。"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("11005-easy.py")


def run_program(input_text: str) -> str:
    """執行 easy 版程式並回傳輸出。"""
    result = subprocess.run(
        [sys.executable, str(SCRIPT_PATH)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


class TestUVA11005Easy(unittest.TestCase):
    def test_all_costs_are_one(self) -> None:
        # 所有成本相同時，0 會在每個進位都同分。
        costs = " ".join(["1"] * 36)
        all_bases = " ".join(str(base) for base in range(2, 37))

        input_text = f"""1
{costs}
1
0
"""

        expected_output = (
            "Case 1:\n"
            f"Cheapest base(s) for number 0: {all_bases}"
        )

        self.assertEqual(run_program(input_text), expected_output)

    def test_simple_tie(self) -> None:
        # 讓 2 與 3 進位對數字 3 成本相同。
        costs = [1, 1] + [100] * 34
        cost_text = " ".join(str(cost) for cost in costs)

        input_text = f"""1
{cost_text}
1
3
"""

        expected_output = (
            "Case 1:\n"
            "Cheapest base(s) for number 3: 2 3"
        )

        self.assertEqual(run_program(input_text), expected_output)


if __name__ == "__main__":
    unittest.main()