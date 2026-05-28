"""
針對 `in_class/R03-profile-basic.py` 的單元測試

說明：
- 測試 `timed` 裝飾器會正確回傳函式結果並輸出時間訊息。
- 使用 patch 模擬 `timeit.timeit`，避免耗時實際跑 benchmark。
- 模擬 `cProfile.Profile` 與 `pstats.Stats` 以驗證 `bench_cprofile` 的列印流程。

執行：
    python -m unittest test_R03_profile_basic.py
或：
    python -m unittest discover
"""
import os
import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch, MagicMock


# 動態載入原始模組（以免改動 in_class 原檔）
HERE = os.path.dirname(__file__)
SRC_PATH = os.path.normpath(os.path.join(HERE, '..', 'in_class', 'R03-profile-basic.py'))
spec = importlib.util.spec_from_file_location('r03_module', SRC_PATH)
r03 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r03)


class TestTimedDecorator(unittest.TestCase):
    """測試 `timed` 裝飾器：回傳值與輸出格式"""

    def test_sum_of_squares_returns_correct_result_and_prints_timing(self):
        # 對小輸入驗證回傳值，並捕捉 stdout 以檢查有無 timing 訊息
        buf = io.StringIO()
        with redirect_stdout(buf):
            res = r03.sum_of_squares(10)
        self.assertEqual(res, sum(i * i for i in range(10)))
        out = buf.getvalue()
        # timing 訊息應包含函式名稱
        self.assertIn('[timed] sum_of_squares:', out)


class TestBenchTimeit(unittest.TestCase):
    """測試 bench_timeit 會使用 timeit.timeit 並列印結果（模擬 timeit）"""

    def test_bench_timeit_prints_mocked_results(self):
        # 讓第一次與第二次 timeit 返回固定值，驗證輸出中包含該數值
        with patch.object(r03.timeit, 'timeit', side_effect=[0.123, 0.456]):
            buf = io.StringIO()
            with redirect_stdout(buf):
                r03.bench_timeit()
            out = buf.getvalue()
            self.assertIn('genexp =', out)
            self.assertIn('map+lambda =', out)


class TestCProfileBench(unittest.TestCase):
    """測試 bench_cprofile 能夠執行並呼叫 pstats.Stats 的列印流程（模擬 cProfile 與 pstats）"""

    def test_bench_cprofile_uses_profile_and_stats(self):
        # 模擬 Profile 類別與 pstats.Stats，並模擬 workload 避免實際大量計算
        with patch.object(r03, 'workload', return_value=42) as mock_workload:
            with patch.object(r03.cProfile, 'Profile') as mock_profile_cls:
                mock_pr = mock_profile_cls.return_value
                # pstats.Stats(pr).sort_stats(...).print_stats(5) 應被呼叫
                with patch.object(r03.pstats, 'Stats') as mock_stats_cls:
                    mock_stats = MagicMock()
                    mock_stats.sort_stats.return_value = mock_stats
                    mock_stats.print_stats.return_value = None
                    mock_stats_cls.return_value = mock_stats

                    buf = io.StringIO()
                    with redirect_stdout(buf):
                        r03.bench_cprofile()
                    out = buf.getvalue()
                    # 應該會列印表頭文字
                    self.assertIn('[cProfile] 前 5 名：', out)
                    mock_profile_cls.assert_called_once()
                    mock_stats_cls.assert_called_once_with(mock_pr)


class TestWorkload(unittest.TestCase):
    """簡單驗證 workload 回傳數值類型與可計算性"""

    def test_workload_returns_number(self):
        val = r03.workload()
        self.assertIsInstance(val, float)


if __name__ == '__main__':
    unittest.main()
