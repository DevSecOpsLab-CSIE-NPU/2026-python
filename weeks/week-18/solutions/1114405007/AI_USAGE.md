# AI_USAGE.md

## 我問了哪些問題
1. 讀取 week-02 HOMEWORK.md 和 bloom 範例（R09, R10）
2. 實作 D=5 的整數數列處理（去重→篩選→排序）
3. 用 TDD 方式：先寫測試 → commit Red → 實作 → commit Green
4. 依 week-18 README 建立對應檔案
5. 補上多組測資與 edge case

## AI 給的建議我有採用
- 去重保序用 `set` + `list` 模式（參考 R10-dedupe.py）
- 測試架構用 `unittest`，符合作業要求
- `solve()` 設計成可接受字串輸入方便測試
- `get_D()` 公式：`(u % 4) + 2`（依題目說明修正）

## AI 給的建議我拒絕
- AI 最初用猜測的 mapping table 實作 `get_D()`，我改用題目給的正確公式

## AI 可能誤導但我自行修正的案例
- `solve()` 回傳結尾換行處理：AI 最初在空輸入時回傳 `"\n"`，我修正為有輸出才加換行
- `get_D()` 對照表：AI 沒找到參數頁而自創 mapping，我後來提供題目公式 `(u % 4) + 2` 修正
