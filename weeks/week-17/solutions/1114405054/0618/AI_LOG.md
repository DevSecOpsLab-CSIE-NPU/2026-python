## 🔍 我問 AI 什麼

> 詢問「先排序再二分搜尋（Sort + Binary Search）」在 $n$ 多大時效能會超越「線性搜尋（Linear Search）」，要求給出直覺預測，並輸出符合 `docs:` 規範的 Commit 訊息與 README 段落。

---

##  AI 給了什麼

* **直覺預測：** 在多次搜尋的前提下，交叉點約在 $n \approx 40 \sim 80$。
* **分析原因：** 小數據時 Linear Search 具備 Cache Locality 優勢；大數據時排序的 $O(n \log n)$ 攤提成本才會小於 Linear 的 $O(n^2)$。
* **產出物：** 符合規格的 Git Commit 訊息與 README.md 效能預測段落。

---

##  我改了什麼

> **修正了 AI 原先忽略「單次與多次查詢」邊界條件的邏輯漏洞，並將其實作範例中的內建 `sort()` 調整為自訂的 `Merge Sort` 以符合實驗控制變因。**

---

## 🔁 AI 反問我什麼 / 我怎麼回答

### ⏱️ Stage 1 — timeit（從零實作）

* **AI 問：** `@timeit` 和 `@timeit(repeat=N)` 都支援？
* **我答：** 兩者都要支援。


* **AI 問：** `repeat` 合法值？
* **我答：** $\ge 1$ 正整數；傳入 `float` 則拋出 `TypeError`。


* **AI 問：** 例外行為處理？
* **我答：** $<1$ 拋出 `ValueError`；被裝飾的函式若拋出例外則原樣傳遞。


* **AI 問：** Edge case 考慮？
* **我答：** 注意 `repeat=1`、`records` 紀錄重置，以及 `classmethod` / `staticmethod` 的相容性。


* **AI 問：** 驗收標準？
* **我答：** 回傳值被修改、殘留 `print`、或殘留 `self.fail` 皆視為紅燈不通過。



### 🔍 Stage 2 — 三種搜尋

* **AI 問：** 共用測試時，如何處理回傳型別不一致？
* **我答：** 使用 `_found()` 統一轉換為 `bool` 再進行斷言（Assert）。


* **AI 問：** Binary Search 收到未排序的 data 怎麼辦？
* **我答：** 直接回傳 `-1`，並在 docstring 中明確寫明前置條件。


* **AI 問：** data 非 `list` 型別時？
* **我答：** 拋出 `TypeError`。


* **AI 問：** 重複元素時，Binary Search 回傳哪一個？
* **我答：** 演算法第一個碰到的那一個。



###  Stage 3 — 加速實驗 + 交叉點

* **AI 問：** 預測的交叉點 $n$ 是多少？
* **我答：** $40 \sim 80$。


* **AI 問：** 實際量測的交叉點？
* **我答：** 單次查詢永不交叉；但在 100 次查詢時，交叉點約在 $n \approx 20$。


* **AI 問：** AI 前期預測錯在哪？
* **我答：** 盲目認為「binary 一定比 linear 快」，忽略了「需要先排序且只查一次」時，排序開銷會讓二分搜尋完敗。



###  Stage 4 — 雷達圖

* **AI 問：** 效能評比包含哪些維度？
* **我答：** Time (100/1000/10000/100000 數據量)、Scalability（擴展性）、Simplicity（程式碼複雜度）。


* **AI 問：** 數據如何進行正規化（Normalization）？
* **我答：** 使用 Min-max 映射至 $[0, 1]$ 區間，時間維度需倒轉計算（耗時越小，得分越高）。



###  Stage 5 — 安全自掃

* **AI 問：** 找到哪些適用的安全檢查條目？
* **我答：** `make_data` 負數無檢查（防禦 03 Numbers）、`open()` 未指定 `encoding`（防禦 08 Coding）、使用 `assert` 代替常規業務檢查。


* **AI 問：** 哪些條目不適用？
* **我答：** 無 `with` 關檔（程式碼已全用 with）、`pickle` 污染（已正確使用 json）、`random` 預測漏洞（非安全敏感場景，不需密碼級亂數）。