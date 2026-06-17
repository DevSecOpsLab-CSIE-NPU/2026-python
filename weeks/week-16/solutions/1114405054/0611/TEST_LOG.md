# TEST_LOG — 排序效能實驗室

## 測試結果（全部 13 組）

```
.............
----------------------------------------------------------------------
Ran 13 tests in 0.376s
OK
```

## 各階段測試

| Stage | 測試檔 | 測試數 | 結果 |
|-------|--------|--------|------|
| 1 | test_timing.py | 4 | OK |
| 2 | test_sorts.py | 3 | OK |
| 3 | test_sorts.py（含 fast 版） | 3 | OK |
| 4 | test_plot.py | 3 | OK |
| 5 | test_security.py | 3 | OK |

## git log

```
test: stage1 timeit 裝飾器測試
feat: stage1 實作 timeit 裝飾器
test: stage2 排序正確性測試
feat: stage2 實作三種排序與 benchmark
test: stage3 加速版共用正確性測試
feat: stage3 加速版與量測數據
test: stage4 繪圖輸出測試
feat: stage4 實驗結果圖表與報告
test: stage5 安全性規則測試
feat: stage5 修正安全性問題
```
