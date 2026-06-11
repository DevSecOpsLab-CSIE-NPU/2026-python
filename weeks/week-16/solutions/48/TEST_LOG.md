# TEST_LOG — 排序效能實驗室

## 最終測試結果

```text
$ python -m unittest discover -p "test_*.py"
................................
----------------------------------------------------------------------
Ran 32 tests in 0.471s
OK
```

## 各階段測試數量

| Stage | 測試檔 | 測試數 | 說明 |
|-------|--------|--------|------|
| 1 | test_timing.py | 5 | timeit 裝飾器功能 |
| 2 | test_sorts.py | 11 | bubble/quick/merge 排序正確性 |
| 3 | test_acceleration.py | 10 | 加速版正確性 + 效能 + benchmark 輸出 |
| 4 | test_plot.py | 3 | PNG 產生與非空驗證 |
| 5 | test_security.py | 3 | 型別驗證與輸入範圍安全 |

## Commit 歷史

```
a022033 feat: stage5 修補型別驗證與輸入範圍安全問題
73e24e9 test: stage5 安全性自掃測試
2a5249e feat: stage4 繪製 benchmark 折線圖
17c647d test: stage4 繪圖功能測試
53ec5ae feat: stage3 排序加速與 benchmark
e767a19 test: stage3 加速驗證測試
66624ee feat: stage2 實作三種排序演算法
5deceb6 test: stage2 排序正確性測試
74cbc36 feat: stage1 實作 timeit 裝飾器
0d2542e test: stage1 timeit 裝飾器測試
```
