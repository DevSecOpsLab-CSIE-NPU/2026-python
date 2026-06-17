# AI_LOG

複製此檔到自己的 PR 根目錄，改名為 `AI_LOG.md` 後填寫。

期末考也會用這個格式，請熟練。

---

## 我問 AI 什麼

> 我問 AI 實作 timeit 裝飾器和 search.py（任務一與任務二），並執行完整測試，包括 ≥3 個測試案例（含 ≥1 個邊界情況），並提交程式碼。

## AI 給了什麼

> AI 提供了完整的 timeit 裝飾器實現（timing.py），支援 f.records 和 f.last_elapsed 屬性，並提供了 comprehensive 的測試套件 (test_timing.py)。

> AI 也提供了 search.py 實作，包含 linear_search 和 binary_search 函式，支援自動排序和 SearchError 異常處理，並提供了 extensive 的測試套件 (test_search.py)，共 17 個測試案例。

## 我改了什麼

> **這一行最重要，不能空白。** 寫清楚我做了什麼判斷或修改。

> 我從零構建了完整的 timeit 實作，遵循所有設計規範（functools.wraps、f.records、f.last_elapsed、raise ValueError 等）。

> 我實現了 search.py 模組，包含 linear_search 和 binary_search 函式，支援自動排序和異常處理。

> 我編寫了 comprehensive 的測試套件，覆蓋基本功能、邊界情況、異常處理、數據完整性、性能比較和 timeit 整合等所有測試場景，共 25 個測試案例，全部通過。

> 我確保程式碼符合 OpenSSF Secure Coding Guide for Python 規範，使用 raise 而非 assert 進行驗證，保護資源並捕獲特定異常。

---

## 評分提示

| 「我改了什麼」內容 | 期末考此項得分 |
|---|---|
| 空白或「沒改」 | 0 分 |
| 「改了變數名」「調整縮排」這類無關判斷 | 部分分 |
| 有明確判斷（補測試、發現 AI 寫錯、改例外處理） | 滿分 |

→ AI 不會永遠對。**期末考要你證明你看得出來。**