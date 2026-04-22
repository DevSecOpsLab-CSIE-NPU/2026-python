import subprocess
import sys
import unittest
from pathlib import Path


class TestZeroJudgeA235(unittest.TestCase):
    def run_program(self, filename, input_data):
        file_path = Path(__file__).resolve().parent / filename
        result = subprocess.run(
            [sys.executable, str(file_path)],
            input=input_data,
            text=True,
            capture_output=True
        )

        self.assertEqual(
            result.returncode,
            0,
            msg=f"{filename} 執行失敗：\nSTDERR:\n{result.stderr}"
        )

        return result.stdout.strip()

    def check_all_versions(self, input_data, expected_output):
        for filename in ["main.py", "main-easy.py", "main-handwritten.py"]:
            actual_output = self.run_program(filename, input_data)
            self.assertEqual(
                actual_output,
                expected_output,
                msg=f"{filename} 輸出錯誤"
            )

    def test_sample(self):
        input_data = """6 7
1 2
2 3
3 5
2 4
4 1
2 6
6 5
10
12
8
16
1
5
1 4
3 5 6
"""
        expected_output = "47"
        self.check_all_versions(input_data, expected_output)

    def test_single_node_bar(self):
        input_data = """1 0
7
1 1
1
"""
        expected_output = "7"
        self.check_all_versions(input_data, expected_output)

    def test_simple_chain(self):
        input_data = """3 2
1 2
2 3
5
10
20
1 1
3
"""
        expected_output = "35"
        self.check_all_versions(input_data, expected_output)

    def test_one_scc_then_path(self):
        input_data = """4 4
1 2
2 1
2 3
3 4
5
6
7
8
1 1
4
"""
        expected_output = "26"
        self.check_all_versions(input_data, expected_output)

    def test_multiple_sccs(self):
        input_data = """5 6
1 2
2 1
2 3
3 4
4 3
4 5
10
20
30
40
50
1 1
5
"""
        expected_output = "150"
        self.check_all_versions(input_data, expected_output)

    def test_choose_better_bar(self):
        input_data = """5 5
1 2
2 3
1 4
4 5
5 4
5
100
1
20
30
1 2
3 5
"""
        expected_output = "55"
        self.check_all_versions(input_data, expected_output)


if __name__ == "__main__":
    unittest.main()