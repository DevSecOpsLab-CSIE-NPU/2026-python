# AI_LOG.md — 資料清理程式

## 5 步驟流程記錄

| 步驟 | 說明 | 狀態 |
|------|------|------|
| ① 設計測試 | 設計 3 組測試（一般、無偶數 NONE、單一負偶數邊界） | ✅ |
| ② 寫程式並跑測試 | 寫出 `D2_easy.py` 並通過 3 組測試 | ✅ |
| ③ 加中文註解 | `D2_easy.py` 每行關鍵邏輯加上中文註解 | ✅ |
| ④ 製作簡易版 | 產出 `D2-easy.py`（邏輯乾淨、變數直覺、`dict.fromkeys` 去重） | ✅ |
| ⑤ 加詳細註解 | 加入 docstring、時間 O(N log N)／空間 O(N) 複雜度說明 | ✅ |

## 手打版

`D2-handwritten.py` — 變數名稱與迴圈改為 basic 風格，無註解，通過全部測試。

## TDD 紅綠燈 Commit（最終版，以原始考卷測資為準）

```
508f2be test: add failing tests for Data Cleaning  ← 紅燈（3 FAILED）
65ddfad feat: implement Data Cleaning               ← 綠燈（3 passed）
```

Sample Input 1：`8\n4 7 4 2 9 2 6 7` → 預期輸出 `2 4 6` ✅

## 面試訪談摘要

| 提問 | 學生回答 | 如何填入檢查清單 |
|------|----------|------------------|
| 函式簽名與回傳型別 | 無特定要求，stdin/stdout | 簽名 ✅ |
| 輸入範圍與邊界 | n=1~10^5, ai=-10^9~10^9, n=0結束 | 邊界 ✅ |
| 例外行為 | 無特別例外處理 | 例外 ❌ |
| 邊界案例 | 無偶數輸出 NONE | 驗收 ✅ |

## 檔案清單

- `D2_easy.py` — 步驟②+③：簡易版含中文註解
- `D2-easy.py` — 步驟④+⑤：AI 簡易版含詳細註解與複雜度
- `D2-handwritten.py` — 手打版（無註解）
- `test_D2.py` — 測試程式（3 cases）
- `test_D2.log` — pytest LOG
- `test_D2-handwritten.log` — 手打版測試 LOG
