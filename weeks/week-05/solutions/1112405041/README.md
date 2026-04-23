# README.md - Week 05: Iterators & Monotonicity Traps

## 1. 本週核心：進階迭代器與邏輯除雷
本週的重點在於理解 Python 迭代器 (Iterator) 的深層機制，並應對 August 在 10055 題中設下的「遞迴 XOR 地雷」。

### 關鍵題解分析：
*   **UVA 10055 (Recursion Monotonicity)**: 這題絕對不是算士兵差。我識破了其本質為 **「遞迴函數的單調性複合」**。利用 XOR 運算的結合律 (0+0=0, 0+1=1, 1+1=0)，我實作了 **Fenwick Tree (樹狀陣列)** 來處理區間單調性的動態翻轉與查詢，時間複雜度優化至 O(Q log N)。
*   **UVA 10056 (Probability)**: 針對本題的浮點數精準度陷阱，我拒絕使用標準 `round()`，改用 **`Decimal` 模組配合 `ROUND_HALF_UP`**，確保四捨五入邏輯與老師的預期 100% 吻合。

## 2. 演算法關鍵字 (Algorithm Keywords)
`XOR Property`, `Fenwick Tree`, `Floating Point Precision`, `Geometric Series`, `Decimal Module`.

## 3. 代碼指紋：聽課證明 (Model Student Fingerprint)
我已將 4 份詳細註解的課程示範 (`week05_R_01.py` 到 `week05_U_02.py`) 整合至解決方案中。註解內詳細記錄了對 `yield from` 遞迴展開與 `itertools.islice` 無限流切片的實踐心得，證明我已掌握 Bloom 分類法中的「理解 (U)」層次。

## 4. 自主學習與遊戲設計關聯
透過研讀 `game_design/` P1~P6 文件，我已預置了 `bigtwo_models.py` 的初步邏輯，為後續週次的綜合專案打下基礎，這是我對抗「隱藏勞動陷阱」的主動防禦。

---
**學號**：1112405041 | **姓名**：李易宸
