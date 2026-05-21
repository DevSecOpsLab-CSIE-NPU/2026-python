import subprocess
import sys
import unittest
from pathlib import Path

"""
測試檔：TestQuestion11321

透過黑箱測試 `solution_11321.py`，驗證逐步放置陷阱時的接受/拒絕輸出行為，
特別測試被拒絕後系統狀態仍維持正確性。
"""


class TestQuestion11321(unittest.TestCase):
    def run_solution(self, input_data: str) -> str:
        # 黑箱測試：直接執行同層的 solution_11321.py。
        # 題目是一步一步放陷阱，所以輸出也要逐步比對每一次的結果。
        solution_path = Path(__file__).with_name("solution_11321.py")
        completed = subprocess.run(
            [sys.executable, str(solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout.strip()

    def test_trap_wall(self) -> None:
        # 前兩個陷阱不會封死，第三個會形成從上到下的障礙，第四個再確認被拒絕後仍可繼續放。
        # 這組測資可以同時驗證：正常放置、形成阻隔、以及被拒絕後狀態沒有壞掉。
        input_data = """3 3 4
0 1
1 1
2 1
1 0
"""
        expected = "\n".join(["<(_ _)>", "<(_ _)>", ">_<", "<(_ _)>"])
        # 每一步的輸出都要和預期完全一致。
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()