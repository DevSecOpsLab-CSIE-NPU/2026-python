# 題目 10062

**題名**: UVA 10062

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a055)
- [Yui Huang 題解](https://yuihuang.com/zj-a055/)

## 題目敘述

有 N 頭（2 ≤ N ≤ 80,000）乳牛，每頭乳牛都有一個在 1 到 N 範圍內的獨特編號。
牠們在晚餐前去附近的「飲水站」喝了太多啤酒，一時判斷失準。
排隊吃晚飯時，牠們沒有依照編號從小到大的正確順序排列。
不幸的是，農夫 FJ 無法直接幫牠們排序，而且他的觀察能力也不太好。
他沒有記錄每頭乳牛的編號，而是統計了一個奇怪的數據：對於隊伍中的每頭乳牛，他知道在該乳牛前面、編號比它小的乳牛有幾頭。
請根據這份資料，告訴 FJ 乳牛的正確排列順序。

## 輸入說明

- 第 1 行：一個整數 N。
- 第 2 至 N 行：共 N-1 行，每行描述該位置的乳牛前面、編號比它小的乳牛數量。
  第一頭乳牛前面沒有任何乳牛，因此不列出。
  第 2 行描述第 2 個位置的乳牛前面編號較小的牛數；第 3 行描述第 3 個位置的情形，以此類推。

## 輸出說明

- 共 N 行，每行輸出該位置乳牛的編號。
  第 1 行為隊伍第 1 個位置的乳牛編號，第 2 行為第 2 個位置，以此類推。

---

## 解題思路

這題本質上是「由前綴資訊還原排列」的問題。做法是先把每個位置對應的數字看成一個需要被放回去的位置，接著從大到小放入數字。

1. 先建立一個長度為 N 的陣列，記錄每個數字前面有多少個比較小的數字。
2. 從 N 開始往 1 依序處理，因為較大的數字不會影響較小數字的相對順序。
3. 用 Fenwick Tree（BIT）維護目前還空著的位置。
4. 對於目前數字 x，找到第 k 個空位，其中 k = 前面較小數字數量 + 1。
5. 把 x 放到那個位置，並把該位置從 BIT 中移除。

Fenwick Tree 可以在 O(log N) 時間內完成「找第 k 個空位」與「更新位置」，因此總時間複雜度是 O(N log N)。

## 解題代碼

```python
import sys


class FenwickTree:
  def __init__(self, size: int) -> None:
    self.size = size
    self.tree = [0] * (size + 1)

  def add(self, index: int, delta: int) -> None:
    while index <= self.size:
      self.tree[index] += delta
      index += index & -index

  def kth(self, k: int) -> int:
    index = 0
    bit_mask = 1 << (self.size.bit_length() - 1)
    while bit_mask:
      next_index = index + bit_mask
      if next_index <= self.size and self.tree[next_index] < k:
        k -= self.tree[next_index]
        index = next_index
      bit_mask >>= 1
    return index + 1


def main() -> None:
  data = sys.stdin.read().split()
  if not data:
    return

  n = int(data[0])
  smaller_before = [0] * (n + 1)
  for i in range(2, n + 1):
    smaller_before[i] = int(data[i - 1])

  bit = FenwickTree(n)
  for position in range(1, n + 1):
    bit.add(position, 1)

  answer = [0] * (n + 1)
  for value in range(n, 0, -1):
    position = bit.kth(smaller_before[value] + 1)
    answer[position] = value
    bit.add(position, -1)

  sys.stdout.write("\n".join(map(str, answer[1:])))


if __name__ == "__main__":
  main()
```

## 測試用例

輸入：

```text
5
1
2
3
4
```

輸出：

```text
1
2
3
4
5
```
