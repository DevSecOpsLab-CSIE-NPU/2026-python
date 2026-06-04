## Summary（摘要）
新增 `count_squares` 的實作與對應單元測試，並附上 `AI_LOG.md`。所有本地 unittest 已通過（綠燈）。

## 變更檔案
- `weeks/week-15/solutions/fychao/0604/square_counter.py` — 實作 `count_squares(a, b)`
- `weeks/week-15/solutions/fychao/0604/test_square_counter.py` — unittest 測試（共 5 個測試，含 edge case 與例外情境）
- `weeks/week-15/solutions/fychao/0604/AI_LOG.md` — AI 互動記錄

## 為什麼要改（Why）
依據 6/4 TDD 課題：實作 UVA 11461 簡化版的平方數計數器，並示範 TDD 流程與 AI 使用記錄（AI_LOG）。

## 如何驗證（How to test）
在本地執行：
```powershell
cd d:\0604\2026-python\weeks\week-15\solutions\fychao\0604
python -m unittest -v
```
應看到全部通過（OK / GREEN）。

可選（將輸出儲存為檔案以便檢視）：
```powershell
python -m unittest -v > test_output.txt 2>&1
```

## 注意（Permissions）
我在本地已 commit 所有檔案。如果你沒有對上游 repo 的寫權，請 fork 並把分支推到你的 fork 後再發 PR；或把你的 fork URL 提供給我，我可以把遠端設為 `fork` 並幫你推分支。

## AI_LOG.md（已包含於 PR）
## 我問 AI 什麼
請幫我用 unittest 寫 `count_squares` 的測試，並指出還需要哪些 edge case 或例外處理。

## AI 給了什麼
提供了基本範例測試與部分 edge case，但沒有包含 `a > b` 應丟 `ValueError` 的例外測試。

## 我改了什麼
我補上了 `a > b` 應丟 `ValueError` 的測試，並實作 `count_squares`，所有本地 unittest 已通過（綠燈）。
