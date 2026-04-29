"""UVA 10268 的單元測試。

這份測試假設正式解答會提供一個可直接呼叫的函式：
    minimum_trials(k, n)

契約如下：
- k：水球數量
- n：建築物樓層數
- 回傳值：最少試驗次數
- 若答案超過 63 次，則回傳 None

如果你的實作函式名稱不同，只要把下方的匯入位置改掉即可。
"""

from __future__ import annotations

import unittest


def _load_solver():
    """載入正式解答函式。

    這裡先保留彈性，方便你之後把解答檔接進來。
    預設會嘗試從 solution_10268 匯入 minimum_trials。
    """

    try:
        from solution_10268 import minimum_trials  # type: ignore

        return minimum_trials
    except Exception as exc:  # pragma: no cover - 測試檔骨架期允許失敗提示
        raise RuntimeError(
            "找不到 solution_10268.minimum_trials。請將正式解答檔名或匯入路徑調整一致。"
        ) from exc


class TestUVA10268(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 在類別層級先載入一次，避免每個測試方法都重複匯入模組。
        cls.solve = staticmethod(_load_solver())

    def test_one_egg_simple_cases(self):
        # 只有 1 顆水球時，只能一層一層往上試，答案會等於樓層數。
        self.assertEqual(self.solve(1, 1), 1)
        self.assertEqual(self.solve(1, 10), 10)
        self.assertEqual(self.solve(1, 63), 63)

    def test_small_classic_examples(self):
        # 這些是經典的小型範例，用來驗證遞推轉移是否正確。
        self.assertEqual(self.solve(2, 1), 1)
        self.assertEqual(self.solve(2, 3), 2)
        self.assertEqual(self.solve(2, 6), 3)
        self.assertEqual(self.solve(3, 14), 4)

    def test_boundary_within_63_trials(self):
        # 63 次試驗的上限內，應該回傳正確數值，不可提早判成超過上限。
        self.assertEqual(self.solve(2, 2016), 63)
        self.assertEqual(self.solve(3, 41664), 63)

    def test_over_63_trials(self):
        # 一旦最少試驗次數會超過 63，就應該回傳 None，對應題目的輸出格式。
        self.assertIsNone(self.solve(1, 64))
        self.assertIsNone(self.solve(2, 2017))

    def test_zero_floor_or_degenerate_case(self):
        # 題目正式輸入不會給 0 樓，但這個案例可用來檢查函式的健壯性。
        # 若你不想支援此情況，可以把這個測試刪掉。
        self.assertEqual(self.solve(10, 1), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)