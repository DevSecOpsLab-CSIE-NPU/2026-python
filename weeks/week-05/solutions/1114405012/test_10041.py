import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10041(unittest.TestCase):
    """針對 UVA 10041（Vito's Family）的單元測試。"""

    # 依常見命名習慣，嘗試自動找到待測解答檔案
    CANDIDATE_FILES = [
        "solution.py",
        "10041.py",
        "main.py",
        "QUESTION-10041.py",
        "uva10041.py",
    ]

    @classmethod
    def setUpClass(cls):
        # 測試檔所在資料夾（也就是學號資料夾）
        cls.base_dir = Path(__file__).resolve().parent

        # 從候選檔名中找出第一個存在的檔案
        cls.solution_file = None
        for name in cls.CANDIDATE_FILES:
            p = cls.base_dir / name
            if p.exists():
                cls.solution_file = p
                break

    def run_solution(self, input_data: str):
        """執行待測程式，回傳標準輸出（每行去除前後空白）。"""
        if self.solution_file is None:
            self.fail(
                "找不到待測解答檔案。\n"
                "請在同資料夾建立下列任一檔名："
                f"{', '.join(self.CANDIDATE_FILES)}"
            )

        # 使用目前 Python 直譯器執行，避免環境不一致
        completed = subprocess.run(
            [sys.executable, str(self.solution_file)],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=str(self.base_dir),
            check=False,
        )

        # 若程式非正常結束，直接顯示 stderr 幫助除錯
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"程式執行失敗，return code={completed.returncode}\n"
            f"stderr:\n{completed.stderr}",
        )

        # 只保留有內容的行，避免結尾多一個換行導致比對失敗
        return [line.strip() for line in completed.stdout.splitlines() if line.strip()]

    @staticmethod
    def expected_min_total_distance(addresses):
        """用中位數法計算最小總距離（UVA 10041 核心性質）。"""
        sorted_addresses = sorted(addresses)
        median = sorted_addresses[len(sorted_addresses) // 2]
        return sum(abs(x - median) for x in sorted_addresses)

    def test_single_case_basic(self):
        # 單一測資：最基本功能測試
        input_data = "1\n2 2 4\n"
        output = self.run_solution(input_data)
        self.assertEqual(output, ["2"])

    def test_multiple_cases_with_duplicates(self):
        # 多組測資 + 重複門牌，檢查解析與計算都正確
        cases = [
            [2, 4, 6, 8, 10],      # 期望 12
            [1, 1, 1, 100, 100],    # 期望 198
            [5, 5, 5],              # 期望 0
            [10, 20, 30, 40],       # 偶數筆，任一中位區間都可達最小值
        ]

        lines = [str(len(cases))]
        for arr in cases:
            lines.append(f"{len(arr)} " + " ".join(map(str, arr)))
        input_data = "\n".join(lines) + "\n"

        expected = [str(self.expected_min_total_distance(arr)) for arr in cases]
        output = self.run_solution(input_data)
        self.assertEqual(output, expected)

    def test_many_generated_cases(self):
        # 產生多組可預期測資，確保程式在多樣輸入下穩定
        generated_cases = []
        for n in range(1, 9):
            # 這裡不使用隨機，避免測試不穩定；用規律序列即可覆蓋多種分布
            arr = [((i * 7 + n * 3) % 50) + 1 for i in range(n + 2)]
            generated_cases.append(arr)

        lines = [str(len(generated_cases))]
        for arr in generated_cases:
            lines.append(f"{len(arr)} " + " ".join(map(str, arr)))
        input_data = "\n".join(lines) + "\n"

        expected = [str(self.expected_min_total_distance(arr)) for arr in generated_cases]
        output = self.run_solution(input_data)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
