# AI_LOG — 排序效能實驗室

## Stage 1 — timeit 裝飾器

> **我問 AI 什麼：**
> 「請幫我補完 test_timing.py 的測試，涵蓋回傳值、metadata、時間記錄、例外傳播、不 print。」

> **AI 給了什麼：**
> 給了 5 個測試案例，包含 test_returns_original_result、test_preserves_function_metadata、test_records_elapsed_time、test_exception_propagates、test_does_not_print。

> **我改了什麼：**
> 與 AI 討論後確認 edge case 初始化值為 f.last_elapsed = None、f.records = []，空殼 stub 需回傳可呼叫的 wrapper 才不會噴 ImportError。

## Stage 2 — 排序正確性測試

> **我問 AI 什麼：**
> 「請幫我補完 test_sorts.py，三個排序共用 subTest，涵蓋空 list、單一元素、已排序、反序、全部相同、含重複、含負數、隨機比對、不可修改輸入、禁用內建 sorted。」

> **AI 給了什麼：**
> 給了 11 個測試方法，使用 SORT_FUNCTIONS 清單 + subTest 共用同一組測試邏輯，包含 AST 靜態分析檢查有無使用 sorted()/list.sort()。

> **我改了什麼：**
> 確認了 edge case 清單（含重複元素、負數與零、大量資料）與例外行為（非 list 拋 TypeError、元素無法比較讓 Python 自己拋）。

## Stage 3 — 加速驗證

> **我問 AI 什麼：**
> 「請幫我實作 quick_sort_fast（in-place partitioning + tail recursion）與 merge_sort_fast（iterative bottom-up），以及 benchmark.py。」

> **AI 給了什麼：**
> 給了 quick_sort_fast 使用 Hoare partition + tail recursion optimization，merge_sort_fast 使用 iterative bottom-up merge，以及 benchmark.py 含 make_data/run_benchmark/print_table 與 results.json 輸出。

> **我改了什麼：**
> 加速幅度：quick_sort_fast 約快 1.6x、merge_sort_fast 差異不大（因已為 O(n log n)）。演算法優化策略為 in-place 操作減少記憶體配置與 GC 負擔、tail recursion 控制遞迴深度、iterative merge 避免遞迴開銷。

## Stage 4 — 繪圖

> **我問 AI 什麼：**
> 「請幫我寫 plot.py，讀 results.json 畫 log scale 折線圖輸出到 assets/benchmark.png。」

> **AI 給了什麼：**
> 給了一個 generate_plot(input_path, output_path) 函式，使用 matplotlib.use("Agg")、y 軸 log scale、marker="o"、自動建立輸出目錄。

> **我改了什麼：**
> 與 AI 討論了例外行為策略（FileNotFoundError/json.JSONDecodeError/KeyError 往上拋，腳本入口 try-except 捕捉）以及 edge case（空 dict 拋 ValueError、單一資料點靠 marker 顯示、水平線加 padding、舊圖直接覆蓋）。

## Stage 5 — 安全性自掃

> **我問 AI 什麼：**
> 「請依 OpenSSF Secure Coding Guide for Python 掃描 Stage 1–4 程式碼，找出安全問題並寫成 test_security.py。」

> **AI 給了什麼：**
> 掃出 2 個可修補問題：(1) quick_sort 接受非 list 輸入（tuple/string 可通過 list comprehension），(2) make_data 接受負數 n。依 pyscg-0034 (Check for None) 與 pyscg-0018 (Validate Numeric Data) 修補。另掃到 5 項不適用條目（OS Command Injection、Deserialization、Format String、Assertions in Production、Random Values）各附理由。

> **我改了什麼：**
> 加入 `_require_list(data)` 統一型別檢查至所有公開排序函式；make_data 加入 n 的型別與非負檢查。共修補 2 項程式問題。
