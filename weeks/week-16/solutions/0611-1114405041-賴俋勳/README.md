# Week 16 - 1114405041 - 賴俋勳

## 專題摘要

本專題整合 `@timeit`、三種排序、效能基準測試、加速方案與視覺化，並加入安全自掃修補。
加速策略採用 quick sort 的 median-of-three 以及小區間 insertion sort。

## 方法

- Stage 1：`timing.py` 實作 `timeit`，保留回傳值與 metadata
- Stage 2：`sorts.py` 實作 bubble / quick / merge，且不修改輸入
- Stage 3：`benchmark.py` 納入 `sorted_builtin` baseline 與 `quick_sort_median`
- Stage 4：`plot.py` 將 `results.json` 繪製成 `assets/benchmark.png`
- Stage 5：以 OpenSSF 思路檢查輸入驗證與資料載入安全性，補上對應測試

## 效能數據與加速比

| 演算法 | 500 | 1000 | 2000 | 4000 |
|---|---:|---:|---:|---:|
| bubble_sort | 0.015651 | 0.080616 | 0.336209 | 1.372417 |
| quick_sort | 0.001224 | 0.002335 | 0.004496 | 0.010615 |
| merge_sort | 0.001868 | 0.002779 | 0.005535 | 0.013120 |
| quick_sort_median | 0.000872 | 0.001644 | 0.004387 | 0.007996 |
| sorted_builtin | 0.000052 | 0.000133 | 0.000277 | 0.000481 |

解讀：

- `sorted_builtin` 仍是最快，符合 C 實作 baseline 的預期。
- `bubble_sort` 在 n=4000 時 1.372417 秒，成長趨勢最陡，符合 O(n^2)。
- `quick_sort_median` 相對 `quick_sort` 在 n=4000 時由 0.010615 秒降到 0.007996 秒，約 1.33x 加速。
- `quick_sort_median` 相對 `bubble_sort` 在 n=4000 時約 171.64x 加速。

## 圖表

![benchmark](assets/benchmark.png)

## 安全自掃紀錄（OpenSSF 對應）

| 條目 | 檢查結果 | 處理方式 |
|---|---|---|
| 08 Coding Standards / 輸入邊界 | `make_data` 原先接受負值（已修） | `n < 0` 時拋 `ValueError` |
| 05 Exception Handling / 具體例外 | `load_results` 解析錯誤需明確處理（已修） | 捕捉 `json.JSONDecodeError` 並轉 `ValueError` |
| 04 Neutralization / CWE-502 | 結果檔載入僅允許 JSON（已修） | 非 `.json` 副檔名直接拒絕 |

不適用項：benchmark 的亂數資料生成非資安敏感流程，因此使用 `random` 即可。
