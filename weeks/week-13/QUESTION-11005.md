# 題目 11005

**題名**: UVA 11005 — Cheapest Base

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a998)
- [UVA Online Judge](https://uva.onlinejudge.org/external/11005.pdf)

## 題目敘述

印刷數字需要墨水，不同的字元（`0`–`9`、`A`–`Z`）各有不同的**印刷成本**。

一個數字在不同的**進位制**（2 到 36 進位）下，其表示方式不同，**總成本**為各位數字成本之和。

給定每個字元的成本以及若干查詢數字，請找出印刷該數字**成本最低**的進位制。

若有多個進位制成本相同，全部輸出（升序）。

## 輸入說明

- 第一行為測試資料組數（< 25）。
- 每組測試資料：前 4 行各 9 個整數，共 **36 個整數**，依序表示字元 `0`–`9`、`A`–`Z` 的印刷成本。
- 接著一行為查詢數量，每行一個**十進位正整數**（**0 ≤ N ≤ 2,000,000,000**）。

## 輸出說明

- 每組測試資料先輸出 `Case X:`（X 為組號）。
- 每個查詢輸出一行：
  ```
  Cheapest base(s) for number Y: b1 b2 ...
  ```
  其中 b1, b2, … 為成本最低的進位制（**升序排列**，以空格分隔）。
- 測試資料之間空一行。

---

## 解題思路

*請填入你的解題思路*

## 解題代碼

思路：

- 對於每個進位 b（2 到 36），把輸入的十進位整數 N 轉換成 base-b 的各位數字，
  並將每個位元對應的印刷成本相加，得到該進位的總成本。
- 對所有進位計算後，找出總成本的最小值，並回傳所有達到該最小值的進位（升序）。

實作細節：

- 若 N == 0，任何進位的表示皆為單一字元 '0'，因此總成本為 costs[0]。
- 轉換過程可使用不斷對 base 取餘數與整除直到 x==0 的方式取得各位數字。
- 因為進位範圍固定（2..36），時間與空間複雜度可視為常數級，足以在題目限制內執行。


# 你的代碼這裡
```

# 範例：使用剛才撰寫的 cheapest_bases 函式
from cheapest_base import cheapest_bases

def process_case(costs, queries):
    """處理一組測資：costs 為長度 36 的成本列表，queries 為要查詢的整數列表。"""
    results = []
    for n in queries:
        bases = cheapest_bases(costs, n)
        results.append((n, bases))
    return results

# 範例使用（讀入輸入時請依題目格式處理）：
# costs = [...]  # 36 個整數
# queries = [0, 10, 100000]
# for n, bases in process_case(costs, queries):
#     print(f"Cheapest base(s) for number {n}:", ' '.join(map(str, bases)))

*測試輸入與預期輸出*
