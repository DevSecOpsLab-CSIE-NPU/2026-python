import sys
import os
import unittest

# 讓 tests/ 能 import 上層目錄的模組
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from task1_csv_to_json import filter_by_admission, count_by_dept


class TestFilterByAdmission(unittest.TestCase):

    def _sample_rows(self):
        return [
            {"入學方式": "聯合登記分發", "系所名稱": "電機工程系"},
            {"入學方式": "甄選入學",     "系所名稱": "資訊工程系"},
            {"入學方式": "繁星推甄",     "系所名稱": "機械工程系"},
            {"入學方式": "聯合登記分發", "系所名稱": "資訊工程系"},
        ]

    # 正常：過濾後只保留目標入學方式
    def test_filter_keeps_correct_rows(self):
        result = filter_by_admission(self._sample_rows(), "聯合登記分發")
        self.assertEqual(len(result), 2)
        for r in result:
            self.assertEqual(r["入學方式"], "聯合登記分發")

    # 正常：其他入學方式不出現在結果中
    def test_filter_removes_others(self):
        result = filter_by_admission(self._sample_rows(), "聯合登記分發")
        for r in result:
            self.assertNotEqual(r["入學方式"], "甄選入學")
            self.assertNotEqual(r["入學方式"], "繁星推甄")

    # 邊界：空 list 輸入回傳空 list
    def test_filter_empty_input(self):
        result = filter_by_admission([], "聯合登記分發")
        self.assertEqual(result, [])

    # 反例：找不到的方式回傳空 list
    def test_filter_nonexistent_method(self):
        result = filter_by_admission(self._sample_rows(), "不存在方式")
        self.assertEqual(result, [])

    # 邊界：大小寫完全相符才算（不做模糊比對）
    def test_filter_case_sensitive(self):
        result = filter_by_admission(self._sample_rows(), "聯合登記")
        self.assertEqual(result, [])


class TestCountByDept(unittest.TestCase):

    # 正常：已知資料的統計結果正確
    def test_count_by_dept_correct(self):
        rows = [
            {"系所名稱": "電機工程系"},
            {"系所名稱": "資訊工程系"},
            {"系所名稱": "電機工程系"},
        ]
        result = count_by_dept(rows)
        self.assertEqual(result["電機工程系"], 2)
        self.assertEqual(result["資訊工程系"], 1)

    # 邊界：空輸入回傳空 dict
    def test_count_by_dept_empty(self):
        result = count_by_dept([])
        self.assertEqual(result, {})

    # 邊界：只有一個系所
    def test_count_by_dept_single(self):
        rows = [{"系所名稱": "電機工程系"}] * 5
        result = count_by_dept(rows)
        self.assertEqual(result, {"電機工程系": 5})

    # 正常：回傳值為 dict 型態
    def test_count_returns_dict(self):
        rows = [{"系所名稱": "資訊工程系"}]
        result = count_by_dept(rows)
        self.assertIsInstance(result, dict)

    # 反例：有缺少系所名稱欄位的列，應以空字串計入而非 KeyError
    def test_count_missing_dept_key(self):
        rows = [{"入學方式": "聯合登記分發"}]  # 無 '系所名稱' 欄位
        try:
            result = count_by_dept(rows)
            # 有 "" 鍵或有值都可接受，重點是不拋出例外
            self.assertIsInstance(result, dict)
        except KeyError:
            self.fail("count_by_dept 不應因缺少欄位而拋出 KeyError")


if __name__ == "__main__":
    unittest.main(verbosity=2)
