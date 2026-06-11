## 我問 AI 什麼
「請依 0611-sort-lab.md Stage 1 規格，幫我寫 @timeit 裝飾器的 unittest，至少 3 個測試，含 edge case。」 「請幫我實作 timing.py 的 timeit 裝飾器：保留回傳值、用 functools.wraps、記錄 last_elapsed 和 records、不准 print。」 「依 Stage 2 規格，用 subTest 寫三種排序共用的正確性測試：基本案例、隨機資料對照 sorted()、輸入不被修改、edge case 大數值。」 「請用 Python 實作 bubble_sort、quick_sort、merge_sort，不可用 sorted()/list.sort()，回傳新 list。」 「Stage 3：請幫我寫加速版 quick sort（median-of-three pivot + 小區間切換 insertion sort），並寫測試驗證正確性。」 「Stage 4：請寫 plot.py 的 load_results、plot_results，y 軸 log scale，輸出 assets/benchmark.png。」 「Stage 5：請依 OpenSSF Secure Coding Guide 寫 test_security.py，至少 3 條檢查（無 bare except、用 json 非 pickle、檔案用 with、無 assert 做驗證）」
## AI給了甚麼
Stage 1：給了 4 個測試（回傳值不變、metadata 保留、elapsed time 記錄、edge case 無參數回傳 None），但 last_elapsed 初值設 0.0 而非 None。 Stage 1 實作：用 perf_counter() 計時，裝飾器把 last_elapsed、records 掛在 wrapper 上。

Stage 2：給了 4 個測試方法用 subTest 跨三種排序，含基本案例、隨機對照、輸入不變、大數值。 Stage 2 實作：三種排序遞迴/迴圈寫完，quick_sort 用中間 pivot、merge_sort 分 _merge。

Stage 3：給了 quick_sort_fast（median-of-three + ≤16 切 insertion sort）與測試，且 test_sorts.py 的 SORT_FUNCTIONS 共用測試。 

Stage 4：給了 load_results（自動把 JSON key 轉 int）與 plot_results（log scale、Agg backend）。

Stage 5：給了 4 條安全測試（無 bare except、json 非 pickle、benchmark.py 用 with、無 assert），但 benchmark.py 尚未存在導致一紅。
## 我改了什麼
Stage 1：保留 AI 測試結構，修正 last_elapsed 初值為 0.0、records 為 []；實作改用 functools.wraps 包裝並在 wrapper 上掛屬性，符合規格。

Stage 2：AI 給的測試漏了「已排序」與「反序」case，我補入 test_basic_cases；實作 quick_sort 原本用第一元素 pivot，改為中間值避免退化；merge_sort 獨立 _merge 避免重複切片。 

Stage 3：AI 給的測試只針對 quick_sort_fast，我改為在 test_sorts.py 的 SORT_FUNCTIONS 加入它，三種排序+加速版共用同一組測試；實作加上 insertion sort 小區間優化並驗證通過。 

Stage 4：AI 的 load_results 會把 JSON key 留成字串，我改為字典解析式自動轉 int；plot_results 加上 matplotlib.use("Agg") 且空 dict 也能出圖不報錯。

Stage 5：test_benchmark_py_uses_with_for_files 原本 AST 會誤判 with open 為違規，我改寫成收集 With 節點內的 open 再排除；補寫 benchmark.py 並在寫 results.json 時用 with open 確保關檔；確認全專案無 bare except、無 pickle、無 assert 做驗證。

(1) 加速多少百分比
quick_sort_fast 比 quick_sort 快約 30%（1000 筆資料：0.00127s vs 0.00159s）。median-of-three pivot + 小區間 insertion sort 明顯提升了 nlogn 類演算法的常數因子。

(2) 演算法優化的策略為何
策略：median-of-three pivot 選 pivot + 小於等於 16 筆切 insertion sort。median-of-three 降低退化機率，insertion sort 減少遞迴開銷，適合現代 CPU 記憶體階層。

(3) 依 Python 安全程式原則，修補幾項程式問題
修補 1 項：

benchmark.py 原本未建立 → 安全測試 test_benchmark_py_uses_with_for_files 會紅 → 建立 benchmark.py 並在寫 results.json 時用 with open 確保關檔，符合 OpenSSF 08 Coding Standards。