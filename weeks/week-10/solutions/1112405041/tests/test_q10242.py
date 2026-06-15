import unittest
import subprocess
import sys
import os

class TestQ10242(unittest.TestCase):
    def run_solve(self, input_str):
        script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "q10242_hand.py")
        process = subprocess.Popen(
            [sys.executable, script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_str)
        return stdout

    def test_sample_graph(self):
        """測試題目描述中的 6 節點範例"""
        # 1-2-4-1 (SCC1), 2-3 (SCC2), 3-5 (SCC3), 1-2...
        # 簡化版輸入：
        # 1-2, 2-4, 4-1 (環)
        # 2-3, 3-5
        # 點錢：1:10, 2:10, 3:10, 4:10, 5:7
        # 起點 1, 酒吧 5
        # 路徑 1-2-4-1-2-3-5 = 10+10+10+10+7 = 47
        input_data = (
            "6 7\n"
            "1 2\n"
            "2 4\n"
            "4 1\n"
            "2 3\n"
            "3 5\n"
            "5 6\n" # 5-6 也是一條路
            "1 2\n" # 重複邊
            "10\n10\n10\n10\n7\n0\n" # 各點金額 (1-6)
            "1 1\n" # 起點 1, 1 個酒吧
            "5\n"   # 酒吧編號 5
        )
        output = self.run_solve(input_data)
        self.assertEqual(output.strip(), "47")

    def test_no_reachable_bar(self):
        """測試無法到達酒吧的情況"""
        input_data = (
            "2 1\n"
            "1 2\n"
            "10\n10\n"
            "1 1\n"
            "3\n" # 酒吧 3 不存在
        )
        output = self.run_solve(input_data)
        self.assertEqual(output.strip(), "0")

if __name__ == "__main__":
    unittest.main()
