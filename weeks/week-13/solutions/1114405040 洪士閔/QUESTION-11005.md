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

思路：

- 題目要求計算在不同進位制（2~36）下，將十進位整數 N 表示成該進位的各位字元後，依照每個字元的印刷成本求和，找出總成本最低的所有進位制。
- 關鍵在於：對每個查詢的 N，走訪所有 base=2..36，將 N 依序取餘數得到每一位的值（digit = N % base），利用給定的成本陣列累加；特殊情況 N==0 時，其表示為單一字元 '0'，成本為 costs[0]。
- 輸入格式上每組有 36 個成本值（分成 4 行各 9 個整數），為方便解析可把所有 token 讀入再逐個取用。
- 時間複雜度：每個查詢要做 35 個進位的模與除運算，N 最大到 2e9，位數上限約 32 位元（實際更少），因此效能足夠。整體為 O(T * Q * 35 * log_base(N))，在題目限制下可接受。

實作策略：

- 寫一個小函式 `cost_in_base(n, base, costs)`，回傳在該進位下的總成本。
- 主程式從標準輸入讀取所有整數 token，逐組解析並輸出格式化結果。


## 解題代碼

```python
#!/usr/bin/env python3
"""
UVA 11005 - Cheapest Base

此為可直接執行的參考解答，輸入由標準輸入讀入，輸出符合題目敘述格式。
繁體中文註解以利教學。
"""

import sys
from typing import List


def cost_in_base(n: int, base: int, costs: List[int]) -> int:
  """計算 n 在 base 下的印刷成本總和。

  n: 非負整數
  base: 2..36
  costs: 長度 36 的整數列表
  """
  # 特殊情況：數值 0 在任何進位下都只會以一個字元 '0' 表示
  if n == 0:
    return costs[0]

  total = 0
  x = n
  # 利用除餘法把數字拆成各位（從低位到高位）
  # 每個位元的數值 range 為 0..(base-1)，直接當作索引讀取 costs
  while x > 0:
    digit = x % base
    total += costs[digit]
    x //= base
  return total


def cheapest_bases_for_number(costs: List[int], n: int) -> List[int]:
  """回傳使成本最小的所有進位（升序）。"""
  min_cost = None
  best = []
  for b in range(2, 37):
    # 計算在進位 b 下的總印刷成本
    c = cost_in_base(n, b, costs)
    if min_cost is None or c < min_cost:
      min_cost = c
      best = [b]
    elif c == min_cost:
      best.append(b)
  return best


def main():
  data = sys.stdin.read().strip().split()
  if not data:
    return
  it = iter(data)
  try:
    t = int(next(it))
  except StopIteration:
    return

  out_lines = []
  for case in range(1, t + 1):
    # 讀 36 個成本值
    costs = []
    for _ in range(36):
      costs.append(int(next(it)))

    q = int(next(it))
    out_lines.append(f"Case {case}:")
    for _ in range(q):
      n = int(next(it))
      best = cheapest_bases_for_number(costs, n)
      bases_str = ' '.join(str(b) for b in best)
      out_lines.append(f"Cheapest base(s) for number {n}: {bases_str}")

    # 測資之間空一行（題目要求）
    if case != t:
      out_lines.append("")

  sys.stdout.write('\n'.join(out_lines))


if __name__ == '__main__':
  main()

```

## 測試用例

*測試輸入與預期輸出*
