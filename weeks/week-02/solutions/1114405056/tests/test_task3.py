"""tests/test_task3.py — Task 3: Log Summary 的單元測試"""
import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from task3_log_summary import log_summary


def run_log_summary(lines: list[str]) -> list[str]:
    """執行 log_summary 並收集所有 print 輸出為字串列表。"""
    outputs = []
    with patch("builtins.print", side_effect=lambda *args: outputs.append(" ".join(str(a) for a in args))):
        log_summary(lines)
    return outputs


class TestLogSummaryNormal(unittest.TestCase):
    """一般情況的測試。"""

    def test_example_case(self):
        """HOMEWORK.md 提供的範例測資。"""
        lines = [
            "8",
            "alice login",
            "bob login",
            "alice view",
            "alice logout",
            "bob view",
            "bob view",
            "chris login",
            "bob logout",
        ]
        output = run_log_summary(lines)
        self.assertEqual(output[0], "bob 4")
        self.assertEqual(output[1], "alice 3")
        self.assertEqual(output[2], "chris 1")
        self.assertIn("login", output[3])
        self.assertIn("3", output[3])

    def test_top_action_in_output(self):
        """確認最後一行包含 top_action 關鍵字。"""
        lines = ["2", "u1 login", "u2 login"]
        output = run_log_summary(lines)
        self.assertTrue(output[-1].startswith("top_action:"))


class TestLogSummaryEdge(unittest.TestCase):
    """邊界情況的測試。"""

    def test_empty_input(self):
        """m=0 時應能正常輸出，不崩潰。"""
        output = run_log_summary(["0"])
        self.assertEqual(len(output), 1)
        self.assertIn("none", output[0].lower())

    def test_single_event(self):
        """只有一筆紀錄。"""
        lines = ["1", "alice login"]
        output = run_log_summary(lines)
        self.assertEqual(output[0], "alice 1")
        self.assertIn("login", output[1])


class TestLogSummaryTieBreak(unittest.TestCase):
    """同數排序的測試。"""

    def test_tie_sorted_by_name(self):
        """相同事件數時，使用者依名稱升冪排列。"""
        lines = ["2", "bob view", "alice login"]
        output = run_log_summary(lines)
        self.assertEqual(output[0], "alice 1")
        self.assertEqual(output[1], "bob 1")

    def test_multiple_users_same_count(self):
        """三位使用者同數時，依名稱排序。"""
        lines = ["3", "charlie x", "alice y", "bob z"]
        output = run_log_summary(lines)
        names = [line.split()[0] for line in output[:-1]]
        self.assertEqual(names, ["alice", "bob", "charlie"])


if __name__ == "__main__":
    unittest.main()
