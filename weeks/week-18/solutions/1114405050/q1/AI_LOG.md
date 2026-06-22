# AI 協作日誌

## 2026-06-22 任務：第一題 資料清理 (D=2)

### 0. 五項檢查表 (開工前規劃)
1. **函式簽名**: `clean_data(n: int, arr: List[int], d: int) -> List[int]`。
2. **輸入邊界**: $n \le 10^5$，數值 $\le 10^9$，讀到 $n=0$ 結束。
3. **例外處理**: 若輸入非整數應回報格式錯誤（目前假設輸入皆合法）。
4. **edge case**: $n=0$ (回傳 `[]`)、全部數字都不能被 $D$ 整除 (回傳 `NONE`)。
5. **驗收標準**: 順序正確（去重保留首現）、需排序。學號末碼 0 -> $D=2$。

### 1. 需求分析
- 目標：去除重複、保留能被 D=2 整除的數、由小到大排序。
- 學號末碼：0 (D=2)。

### 2. TDD 流程紀錄
- **測試案例設計 (Test Cases)**:
    - `test_sample_case`: 範例資料 `[4, 7, 4, 2, 9, 2, 6, 7]` -> `[2, 4, 6]`
    - `test_none_case`: 無法整除 `[1, 3, 5]` -> `[]` (輸出應顯示 `NONE`)
    - `test_edge_case_empty`: `n=0` 或空數組 -> `[]`
    - `test_negative_numbers`: 負數處理 `[-4, -2, -1, 0, 2, 4]` -> `[-4, -2, 0, 2, 4]`
- **紅燈階段**: 建立 `test_solution.py` 與 `solution.py` (空實作)，運行測試確認全數失敗。 
- **Git Commit**: `docs: add test cases for TDD red light stage`
- **綠燈階段**: 實作 `clean_data` 邏輯，使用 `dict.fromkeys()` 去重以保留順序，列表推導式過濾，並調用 `.sort()`。
- **測試結果**: 4 項測試全數通過。
- **Git Commit**: `feat: implement data cleaning logic for TDD green light stage`

### 3. 最終驗證
- 使用 `D=2` 計算 Sample Input:
    - 第一組: `2 4 6`
    - 第二組: `NONE`
