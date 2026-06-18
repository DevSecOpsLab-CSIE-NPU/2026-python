# 0617 解答 — timeit + 搜尋效能評估（預演）

## 檔案結構

```
0617/
├── timing.py          任務一：timeit 裝飾器實作
├── test_timing.py     任務一：完整測試（9 個 test case）
├── search.py          任務二：linear_search / binary_search
├── test_search.py     任務二：搜尋測試（17 個 test case）
├── README.md          本文件（含效能評估）
└── AI_LOG.md          提示詞記錄與問答摘要
```

執行所有測試：

```bash
python3 -m unittest discover -v
```

---

## 任務二：效能評估結果

測試環境：N = 500,000、target 取中間值（保證找得到）、每次量測 repeat=5 取平均。

| 搜尋方式 | 平均耗時 |
|----------|---------|
| `linear_search` | ≈ 7.58 ms |
| `binary_search`（data 已排序） | ≈ 0.0039 ms |
| **加速比** | **~1,900×** |

### 1. 誰快？差多少？

`binary_search` 快了將近 **1,900 倍**。在 N=500,000 的情況下，linear 平均跑 ~7.6 ms，
binary 只要 ~0.004 ms，差距符合 O(n) vs O(log n) 的理論預期（log₂(500000) ≈ 19）。

### 2. 「排序 + binary」到底划不划算？（今日直覺）

對 N=500,000 的 unsorted data 量測：

- `sorted()` 成本：≈ **133 ms**
- `linear_search` 最壞情況：≈ **51 ms**

如果**只搜一次**，sort+binary（133 ms）比直接 linear（51 ms）還貴 2.6 倍——**不划算**。
直覺上：只有在「先排序、重複搜很多次」的場景，binary 的 O(log n) 優勢才能攤平 O(n log n)
的排序成本。**精確的交叉點（需要搜幾次才回本）明天 6/18 用數據量出來。**

### 3. 為什麼 repeat 取平均，而不取最小值？

取平均反映一般執行情況（含 OS 排程抖動）；取最小值反映最佳情況（cache 最熱）。
今天的目標是「粗略評估一般場景」，所以用平均。明天會討論兩種做法的適用情境。

---

## 課末自我檢測答案

1. **`last_elapsed`、`records` 為什麼掛在 wrapper 上，不用全域變數？**
   全域變數在多個被裝飾函式並存時會互相覆蓋；掛在 wrapper 上讓每個被裝飾函式
   各自持有獨立狀態，符合封裝原則。

2. **為什麼輸入驗證要 `raise` 不能 `assert`？**
   Python 以 `-O`（optimize）模式執行時，`assert` 陳述式整行被移除，
   驗證形同虛設；`raise ValueError` 不受最佳化旗標影響，永遠生效。

3. **`binary_search` 為什麼能比 `linear_search` 快？前提是什麼？**
   每次比較後排除一半的搜尋範圍，時間複雜度降為 O(log n)。
   前提：data 必須已升序排序，才能用大小關係決定往左或往右縮。

4. **「排序 + binary」在什麼情況下反而比 linear 慢？**
   只搜尋少數幾次（極端情況：只搜一次）時，O(n log n) 的排序成本比
   O(n) 的 linear 搜尋更貴——明天用數據找出精確的交叉點。
