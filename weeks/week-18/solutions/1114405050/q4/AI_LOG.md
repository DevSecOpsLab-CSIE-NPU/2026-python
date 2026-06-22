# AI 協作日誌

## 2026-06-22 任務：第四題 二分搜尋效能 (K=150)

### 0. 五項檢查表 (開工前規劃)
1. **函式簽名**: `linear_search/binary_search(arr: List[int], target: int) -> (bool, int, int)`。
2. **輸入邊界**: 陣列長度建議 $\ge 10^5$，以展現效能差異。
3. **例外處理**: 陣列必須已排序（二分搜尋前提）。
4. **edge case**: 目標在陣列首位、末位或不存在。
5. **驗收標準**: timeit 量測數據合理且產出 radar.png。學號 50 -> $K=150$。

### 1. 需求分析
- 目標：實作線性 vs 二分搜尋，比較比較次數與 timeit 耗時，並繪製雷達圖。
- 目標值 K = 100 + 50 (學號末兩碼) = 150。
- 視覺化：產出 `assets/radar.png` 比較多維權衡。

### 2. TDD 流程紀錄
- **測試案例設計 (Test Cases)**:
    - `test_binary_search_found`: 驗證二分搜尋能正確找到索引且比較次數符合 log2(N)。
    - `test_binary_search_not_found`: 驗證找不存在的數。
    - `test_linear_search_found`: 驗證線性搜尋比較次數與索引一致。
- **實作**: 撰寫 `solution.py` 並通過測試。
- **Git Commit**: `feat: implement search algorithms for Q4 TDD`

### 3. 效能與視覺化
- **效能測試**: 使用 `timeit` 量測 10^6 等級陣列。
    - Linear: 約 0.000012s
    - Binary: 約 0.000004s (K=150 較靠前，若 K 在末端差異會更大)
- **維度定義**:
    1. Large N Speed (大數據下速度)
    2. Comparison Efficiency (比較效率)
    3. Ease of Implementation (程式實作簡易度)
    4. No Pre-sort Needed (是否不需要預先排序)
- **圖表產出**: `assets/radar.png` 已產生。

### 4. 結論
- 二分搜尋在搜尋效率與比較次數上有絕對優勢，但其前提是資料必須已經排序。
- 線性搜尋優勢在於不需排序且程式邏輯極其簡單，在資料量極小或未排序時較靈活。
