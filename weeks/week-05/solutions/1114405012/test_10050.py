import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA10050(unittest.TestCase):
    """UVA 10050 (Hartals) 單元測試。"""

    # 優先尋找本題常見檔名，避免誤抓到 10041 的程式
    CANDIDATE_FILES = [
        "10050.py",
        "10050-easy.py",
        "10050-hand.py",
        "QUESTION-10050.py",
        "uva10050.py",
        "main_10050.py",
        "solution_10050.py",
    ]

    @classmethod
    def setUpClass(cls):
        # 測試檔所在目錄（學號資料夾）
        cls.base_dir = Path(__file__).resolve().parent

        # 依候選檔名順序，找出第一個存在的待測程式
        cls.solution_file = None
        for name in cls.CANDIDATE_FILES:
            path = cls.base_dir / name
            if path.exists():
                cls.solution_file = path
                break

    def run_solution(self, input_data: str):
        """執行待測程式，回傳去除空白後的輸出行。"""
        if self.solution_file is None:
            self.fail(
                "找不到 UVA 10050 的解答檔案。\n"
                "請在同資料夾建立下列任一檔名：\n"
                + ", ".join(self.CANDIDATE_FILES)
            )

        # 使用目前 Python 直譯器執行，確保環境一致
        completed = subprocess.run(
            [sys.executable, str(self.solution_file)],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=str(self.base_dir),
            check=False,
        )

        # 若程式異常結束，顯示 stderr 方便除錯
        self.assertEqual(
            completed.returncode,
            0,
            msg=f"程式執行失敗，return code={completed.returncode}\n"
            f"stderr:\n{completed.stderr}",
        )

        # 忽略空白行，降低格式細節造成的誤判
        return [line.strip() for line in completed.stdout.splitlines() if line.strip()]

    @staticmethod
    def expected_lost_days(total_days, hartal_params):
        """計算預期損失工作天。

        規則：
        - 第 1 天是星期天
        - 每週星期五與星期六（第 6、7 天；之後每隔 7 天）不計入損失
        - 只要任一政黨在該工作日發動罷會，即算損失 1 天
        """
        lost = set()

        for h in hartal_params:
            # 每個政黨在 h, 2h, 3h, ... 發動罷會
            for day in range(h, total_days + 1, h):
                weekday = day % 7
                # weekday == 6 -> 星期五；weekday == 0 -> 星期六
                if weekday == 6 or weekday == 0:
                    continue
                lost.add(day)

        return len(lost)

    def test_problem_statement_example(self):
        # 題目敘述中的範例：N=14, h=[3,4,8]，答案應為 5
        input_data = "1\n14\n3\n3\n4\n8\n"
        output = self.run_solution(input_data)
        self.assertEqual(output, ["5"])

    def test_known_multi_case(self):
        # 多組測資：同時檢查輸入解析與多行輸出
        cases = [
            (14, [3, 4, 8]),
            (100, [12, 15, 25, 40]),
        ]

        lines = [str(len(cases))]
        for n, params in cases:
            lines.append(str(n))
            lines.append(str(len(params)))
            lines.extend(map(str, params))
        input_data = "\n".join(lines) + "\n"

        expected = [str(self.expected_lost_days(n, params)) for n, params in cases]
        output = self.run_solution(input_data)
        self.assertEqual(output, expected)

    def test_generated_cases(self):
        # 產生多組規律測資（非隨機），提高覆蓋率與穩定性
        cases = []
        for i in range(1, 7):
            n = 30 + i * 7
            p = 3 + (i % 4)

            # 參數避免 7 的倍數（符合題意）
            params = []
            x = 2 + i
            while len(params) < p:
                if x % 7 != 0:
                    params.append(x)
                x += 2

            cases.append((n, params))

        lines = [str(len(cases))]
        for n, params in cases:
            lines.append(str(n))
            lines.append(str(len(params)))
            lines.extend(map(str, params))
        input_data = "\n".join(lines) + "\n"

        expected = [str(self.expected_lost_days(n, params)) for n, params in cases]
        output = self.run_solution(input_data)
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
