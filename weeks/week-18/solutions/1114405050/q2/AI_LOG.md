# AI 協作日誌

## 2026-06-22 任務：第二題 凱撒密碼 (SHIFT=2)

### 1. 需求分析
- 目標：英文字母向後位移 SHIFT=2 位。
- 規則：大寫 A-Z 循環、小寫 a-z 循環、非英文字元保留。
- 終止條件：讀到 EOF 為止。

### 2. TDD 流程紀錄
- **測試案例設計 (Test Cases)**:
    - `test_sample_case`: `Hello, NPU!` -> `Jgnnq, PRW!`
    - `test_alphabet_wrap`: 邊界位移 `yz YZ` -> `ab AB`
    - `test_non_alphabet`: 保留 `123 !@#` -> `123 !@#`
    - `test_edge_case_empty`: 空字串 `""` -> `""`
- **紅燈階段**: 建立測試並確認全數失敗 (AssertionError: None != expected)。
- **Git Commit**: `docs: add test cases for Q2 Caesar Cipher TDD red light stage`
- **綠燈階段**: 使用 `ord()` 與 `chr()` 進行 ASCII 計算，並透過 `% 26` 實作循環邏輯。
- **測試結果**: 4 項測試全數通過。
- **Git Commit**: `feat: implement Caesar Cipher logic for Q2 TDD green light stage`

### 3. 最終驗證
- 輸入 `Hello, NPU!` (SHIFT=2) -> 輸出 `Jgnnq, PRW!`
- 輸入 `abc XYZ` (SHIFT=2) -> 輸出 `cde ZAB`
