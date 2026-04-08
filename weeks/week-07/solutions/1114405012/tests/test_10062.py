"""UVA 10062 的單元測試。

這份測試以黑箱方式驗證命令列程式。
預設尋找同層的 solution.py；如果未來改成 main.py、10062.py 或 easy 版本檔名，也會自動嘗試找到。
"""

from pathlib import Path
import subprocess
import sys
import unittest


class TestUVA10062(unittest.TestCase):
    """驗證依據前方較小編號數量，是否能還原正確隊伍順序。"""

    def setUp(self):
        # 每個測試都先定位待測程式，避免檔名不同時不好排查。
        # 這樣可同時支援正式版與 easy 版檔名。
        self.root = Path(__file__).resolve().parents[1]
        self.script = self._find_script()

    def _find_script(self):
        # 依照常見提交檔名依序尋找，讓學生後續實作時比較好接上。
        candidates = [
            self.root / "solution.py",
            self.root / "main.py",
            self.root / "10062.py",
            self.root / "10062_easy.py",
            self.root / "10062-easy.py",
        ]
        for candidate in candidates:
            if candidate.exists():
                return candidate

        self.fail("找不到可執行程式，請先建立 solution.py 或 main.py。")

    def _run_case(self, input_data, expected_output):
        # 這裡用 subprocess 模擬正式評測環境，
        # 從標準輸入餵資料、比對標準輸出，確保 I/O 行為符合題目要求。
        completed = subprocess.run(
            [sys.executable, str(self.script)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"程式執行失敗\nSTDERR:\n{completed.stderr}",
        )
        # 用 strip() 忽略最後換行差異，聚焦在內容正確性。
        self.assertEqual(completed.stdout.strip(), expected_output.strip())

    def test_case_01_two_cows_descending(self):
        # 最小邊界：N=2，而且第二頭前面沒有較小編號，結果應該是 2,1。
        self._run_case(
            "2\n0\n",
            "2\n1",
        )

    def test_case_02_two_cows_ascending(self):
        # 最小邊界的另一種情況：N=2，而且第二頭前面有 1 頭較小編號。
        self._run_case(
            "2\n1\n",
            "1\n2",
        )

    def test_case_03_three_cows_all_zero(self):
        # 全零代表每一步都沒有較小編號在前面，排列會是完全遞減。
        self._run_case(
            "3\n0\n0\n",
            "3\n2\n1",
        )

    def test_case_04_three_cows_middle_case(self):
        # 這組可以檢查中間位置的重建是否正確。
        self._run_case(
            "3\n0\n1\n",
            "3\n1\n2",
        )

    def test_case_05_three_cows_another_mix(self):
        # 這組可驗證不是單純遞增或遞減時，程式是否仍能還原正確順序。
        self._run_case(
            "3\n1\n0\n",
            "2\n3\n1",
        )

    def test_case_06_four_cows_prefix_zero(self):
        # 前半段都沒有較小編號，最後一頭才出現 1，常見於插入位置計算錯誤。
        self._run_case(
            "4\n0\n0\n1\n",
            "4\n3\n1\n2",
        )

    def test_case_07_four_cows_mixed(self):
        # 混合型案例，確認不同位置的計數能同時滿足。
        self._run_case(
            "4\n0\n1\n1\n",
            "4\n1\n3\n2",
        )

    def test_case_08_five_cows_ascending(self):
        # 逐步遞增的計數，對應到第一頭放最大值、後面依序遞增的排列。
        self._run_case(
            "5\n0\n1\n2\n3\n",
            "5\n1\n2\n3\n4",
        )

    def test_case_09_five_cows_nontrivial(self):
        # 這組是較完整的非平凡案例，用來檢查多次插入是否都正確。
        self._run_case(
            "5\n0\n0\n1\n2\n",
            "5\n4\n1\n2\n3",
        )


if __name__ == "__main__":
    unittest.main()
