# Week 03 解題報告

**學號**：1114405056  
**姓名**：尤靖崵

---

## 題目清單

| 題號 | 題目名稱 | 演算法 | 狀態 |
|------|----------|--------|------|
| UVA 100 | The 3n+1 Problem | Collatz 序列 + 記憶化 | ✅ |
| UVA 118 | Mutant Flatworld Explorers | 機器人路徑模擬 | ✅ |
| UVA 272 | TeX Quotes | 字串替換 | ✅ |
| UVA 299 | Train Swapping | 逆序對計數 (O(n²)) | ✅ |
| UVA 490 | Rotating Sentences | 矩陣順時針旋轉 90° | ✅ |

---

## 檔案說明

| 檔案 | 說明 |
|------|------|
| `uva100-easy.py` | UVA 100 AI 教學版（含詳細中文註解） |
| `uva100-hand.py` | UVA 100 手打版（模擬 CPE 考場） |
| `uva100.py` | UVA 100 精簡版 |
| `uva118-easy.py` | UVA 118 AI 教學版 |
| `uva118-hand.py` | UVA 118 手打版 |
| `uva272-easy.py` | UVA 272 AI 教學版 |
| `uva272-hand.py` | UVA 272 手打版 |
| `uva299-easy.py` | UVA 299 AI 教學版 |
| `uva299-hand.py` | UVA 299 手打版 |
| `uva490-easy.py` | UVA 490 AI 教學版 |
| `uva490-hand.py` | UVA 490 手打版 |
| `test_uva100.py` | UVA 100 單元測試 |
| `test_uva118.py` | UVA 118 單元測試 |
| `test_uva272.py` | UVA 272 單元測試 |
| `test_uva299.py` | UVA 299 單元測試 |
| `test_uva490.py` | UVA 490 單元測試 |
| `TEST_CASES.md` | 測試案例文件 |
| `TEST_LOG.md` | 測試執行結果日誌 |
| `AI_USAGE.md` | AI 使用說明 |

---

## 執行方式

```bash
# 執行解題程式（以 UVA 100 為例）
python uva100.py < input.txt

# 執行單元測試
python -m pytest test_uva100.py -v
# 或
python test_uva100.py
```

---

## 題目說明

### UVA 100 - The 3n+1 Problem
計算兩數之間所有數字的 Collatz 序列長度最大值。
- 使用記憶化 (memoization) 加速遞迴計算
- 注意輸入順序可能為 `i > j`，需取 min/max

### UVA 118 - Mutant Flatworld Explorers
機器人在矩形格子上依指令移動，墜落邊緣後留下氣味。
- 若前方位置有其他機器人留下的氣味，忽略會墜落的指令
- 使用 `set` 記錄有氣味的格子

### UVA 272 - TeX Quotes
將文字中的雙引號 `"` 依奇偶順序轉換為 TeX 格式（`` `` `` 和 `''`）。
- 全文統一計數，不以行為單位重置

### UVA 299 - Train Swapping
計算相鄰車廂交換次數最少化，等同於逆序對個數。
- 使用 O(n²) 巢狀迴圈計數逆序對

### UVA 490 - Rotating Sentences
將輸入文字矩陣順時針旋轉 90 度輸出。
- 補齊各行至相同長度
- 從右至左逐列取字元形成新的輸出行
