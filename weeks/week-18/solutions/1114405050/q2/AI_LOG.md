# AI 協作日誌

## 2026-06-22 任務：第二題 凱撒密碼 (SHIFT=1)

### 0. 五項檢查表 (開工前規劃)
1. **函式簽名**: `caesar_cipher(text: str, shift: int) -> str`。
2. **輸入邊界**: 字串長度 $\le 1000$，多行輸入直到 EOF。
3. **例外處理**: 非英文字母應原樣保留。
4. **edge case**: `z -> a` 的循環邊界、空字串 `""`。
5. **驗收標準**: 大小寫分別循環且互不干擾。學號末碼 0 -> 使用 $SHIFT=1$。

### 1. 需求分析
- 目標：英文字母向後位移 SHIFT=1 位。
- 規則：大寫 A-Z 循環、小寫 a-z 循環、非英文字元保留。
- 終止條件：讀到 EOF 為止。

### 2. TDD 流程紀錄
- **測試案例設計 (Test Cases)**:
    - `test_sample_case`: `Hello, NPU!` -> `Ifmmp, OQV!`
    - `test_alphabet_wrap`: 邊界位移 `z Z` -> `a A`
    - `test_non_alphabet`: 保留 `123 !@#` -> `123 !@#`
    - `test_edge_case_empty`: 空字串 `""` -> `""`
- **紅燈階段**: 建立測試並確認全數失敗 (AssertionError: None != expected)。
- **Git Commit**: `docs: add test cases for Q2 Caesar Cipher TDD red light stage`
- **綠燈階段**: 使用 `ord()` 與 `chr()` 進行 ASCII 計算，並透過 `% 26` 實作循環邏輯。
- **測試結果**: 4 項測試全數通過。
- **Git Commit**: `feat: implement Caesar Cipher logic for Q2 TDD green light stage`

### 3. 最終驗證
- 輸入 `Hello, NPU!` (SHIFT=1) -> 輸出 `Ifmmp, OQV!`
- 輸入 `abc XYZ` (SHIFT=1) -> 輸出 `bcd YZA`
