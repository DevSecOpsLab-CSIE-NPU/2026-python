import subprocess
import sys
import unittest
from pathlib import Path

"""
測試檔：TestQuestion11332

以黑箱測試執行 `solution_11332.py`，檢查基本可見性案例（單一線段可見，多段被遮擋）
以驗證極角掃描與 active set 在簡單情況下的正確性。
"""


class TestQuestion11332(unittest.TestCase):
    def run_solution(self, input_data: str) -> str:
        # 黑箱測試：直接執行同資料夾的 solution_11332.py。
        # 幾何題常常有邊界差異，所以直接驗證整段輸出最保險。
        solution_path = Path(__file__).with_name("solution_11332.py")
        completed = subprocess.run(
            [sys.executable, str(solution_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return completed.stdout.strip()

    def test_visibility_sample_like(self) -> None:
        # 第一組只有一面鏡子，一定可見；第二組兩面鏡子共線，遠的那面會被近的遮住。
        # 這樣可以檢查最基本的「可見」與「被遮住」兩種狀況。
        input_data = """1
    5 -5 5 5
    2
    1 1 2 2
    3 3 4 4
    """
        expected = "\n".join([
            "1",
            "1 0",
        ])
        # 輸出順序要和輸入的測資順序一致。
        self.assertEqual(self.run_solution(input_data), expected)


if __name__ == "__main__":
    unittest.main()