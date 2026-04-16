"""UVA 118（Mutant Flatworld Explorers）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 118.py
   - question_118.py
   - uva118.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_118.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測的 stdin / stdout 互動。
- 先驗證官方範例，再驗證 LOST、scent（氣味標記）與轉向邏輯。
- 若找不到受測檔案，會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["118.py", "question_118.py", "uva118.py", "main.py"]


class TestUVA118(unittest.TestCase):
    """針對 UVA 118 題意核心規則進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在所有測試前先定位受測解答檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            candidate = cls.test_dir / filename
            if candidate.exists() and candidate.is_file():
                cls.solver_path = candidate
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 UVA 118 解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式，回傳標準輸出（去除尾端空白）。

        設計重點：
        - 使用 sys.executable 確保以目前 Python 環境執行。
        - 若程式非正常結束，會帶出 stdout/stderr 方便除錯。
        """
        proc = subprocess.run(
            [sys.executable, str(self.solver_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
            cwd=str(self.test_dir),
        )

        if proc.returncode != 0:
            self.fail(
                "受測程式執行失敗（return code != 0）。\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}"
            )

        return proc.stdout.strip()

    def test_official_sample(self) -> None:
        """驗證 UVA 118 常見官方範例輸入輸出。"""
        input_data = "\n".join(
            [
                "5 3",
                "1 1 E",
                "RFRFRFRF",
                "3 2 N",
                "FRRFLLFFRRFLL",
                "0 3 W",
                "LLFFFLFLFL",
                "",
            ]
        )

        expected = "\n".join(
            [
                "1 1 E",
                "3 3 N LOST",
                "2 3 S",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_lost_adds_scent_and_next_robot_ignores_same_fall(self) -> None:
        """第一台機器人在邊界掉落後，第二台在同點同方向前進應忽略該危險指令。"""
        input_data = "\n".join(
            [
                "2 2",
                "2 2 N",
                "F",        # 會掉出地圖，在 (2,2) 留下 scent
                "2 2 N",
                "F",        # 因 scent 存在，這一步應被忽略，不可再 LOST
                "",
            ]
        )

        expected = "\n".join(
            [
                "2 2 N LOST",
                "2 2 N",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_turning_only_no_movement(self) -> None:
        """純轉向指令（L/R）不應改變座標，只改方向。"""
        input_data = "\n".join(
            [
                "4 4",
                "1 2 N",
                "LLRRR",
                "",
            ]
        )

        # N -> L:W -> L:S -> R:W -> R:N -> R:E
        expected = "1 2 E"

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_multiple_robots_processed_in_order(self) -> None:
        """驗證多台機器人會依序執行，且前者留下的 scent 影響後者。"""
        input_data = "\n".join(
            [
                "1 1",
                "0 0 E",
                "FF",       # 第一步到 (1,0)，第二步掉落，於 (1,0) 留 scent
                "1 0 E",
                "F",        # 同點同方向會掉落，應被 scent 阻止
                "0 1 N",
                "F",        # 會掉落，於 (0,1) 留 scent
                "0 1 N",
                "F",        # 再次同點同方向，應被忽略
                "",
            ]
        )

        expected = "\n".join(
            [
                "1 0 E LOST",
                "1 0 E",
                "0 1 N LOST",
                "0 1 N",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
