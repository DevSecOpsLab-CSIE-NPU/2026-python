# AI_LOG.md - 0611 排序實驗室

## 🤖 提示詞記錄

### Stage 1: 裝飾器
> 我：請實作一個 `@timeit` 裝飾器，不准 print，結果存在 `f.last_elapsed`。

### Stage 2-3: 排序與優化
> 我：請實作三種排序，不准有 Side Effect。Quick Sort 必須包含優化機制避免極端情況，並加入 `sorted()` 作為 Baseline。

### Stage 4-5: 繪圖與安全
> 我：產出 Log Scale 的 matplotlib 效能圖，並對照 OpenSSF 指南寫出安全性測試。

---

## 🛠 我改了什麼

1. **編碼修復**：解決了 Windows 環境下 Non-UTF-8 的語法報錯。
2. **格式美化**：將原本混亂的 Markdown 表格重新排列，確保各平台閱讀體驗一致。
3. **邏輯強化**：修正了 `results.json` 寫入時的型別問題 (int key 轉為 string)。

