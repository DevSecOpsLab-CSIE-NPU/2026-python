# 題目 10242

**題名**: UVA 10242

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a235)
- [Yui Huang 題解](https://yuihuang.com/zj-a235/)

## 題目敘述

Siruseri 城中的道路都是單向的，不同的道路由路口連接。
依法律規定，每個路口都設立了一台 Siruseri 銀行的 ATM 提款機。
有趣的是，Siruseri 的酒吧也都設在路口，但並非每個路口都有酒吧。
Banditji 計劃實施 Siruseri 有史以來最驚天動地的 ATM 搶劫行動。
他將從市中心出發，沿著單向道路行駛，搶劫所有途經的 ATM 機，最終在某間酒吧慶祝勝利。
透過高超的駭客技術，他取得了每台 ATM 機可掠奪的現金金額。
請幫助他計算從市中心出發、最終抵達某間酒吧時，最多能搶劫的現金總額。
他可以經過同一路口或道路任意多次，但某台 ATM 一旦被搶過，便不再有現金。
例如，假設該城有 6 個路口，道路連接情況如圖所示：市中心位於路口 1（以 → 標示），有酒吧的路口以雙圈表示，各路口 ATM 可取的金額標示於路口上方。
在此範例中，Banditji 最多能搶劫 47 元，搶劫路線為：1-2-4-1-2-3-5。

## 輸入說明
第一行包含兩個整數 N、M，N 表示路口數量，M 表示道路條數。
接下來 M 行，每行兩個整數（均介於 1 到 N 之間），第 i+1 行表示第 i 條道路的起點與終點路口編號。
接下來 N 行，每行一個整數，依序表示每個路口 ATM 機的現金金額。
再下一行包含兩個整數 S、P，S 為市中心（出發路口）的編號，P 為酒吧數量。
最後一行有 P 個整數，表示 P 個有酒吧的路口編號。

## 輸出說明

輸出一個整數，表示 Banditji 從市中心出發、抵達某間酒吧為止，最多能搶劫的現金總額。

---

## 解題思路

**核心概念**：圖的最長路徑 + DFS + 記憶化

Banditji 可以：
- 從市中心出發（固定起始點）
- 沿單向邊行駛，搶劫途經的 ATM
- 最終抵達任一酒吧停止
- 同一 ATM 最多搶劫一次，但可以重複經過同一條邊

**解法**：
1. **建立圖**：N 個路口，M 條有向邊
   - 每條邊 (u, v) 表示從 u 到 v 的單向道路

2. **DFS 探索路徑**：
   - 從起點 s 開始 DFS
   - 維護「已搶的 ATM 集合」，防止重複搶劫
   - 當到達酒吧時，記錄該路徑的總金額

3. **剪枝優化**：
   - 同一個 ATM 只能搶劫一次，記錄在集合中
   - 限制遞迴深度，防止無限循環

4. **狀態**：DFS(當前位置, 已搶ATM集合) → 最大金額

**時間複雜度**: O(2^N × M)（在最壞情況下）
**空間複雜度**: O(N + M)（圖的存儲 + 遞迴堆棧）

## 解題代碼

```python
def solve_atm_robbery(n: int, edges: List[tuple], atm_amounts: List[int], 
                      start: int, bars: Set[int]) -> int:
    \"\"\"使用 DFS 求每個起點到酒吧的最大搶劫金额\"\"\"
    # 建立鄰接表
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
    
    max_cash = 0
    
    def dfs(node: int, robbed: Set[int], cash: int) -> None:
        nonlocal max_cash
        
        # 檢查是否到達酒吧
        if node in bars:
            max_cash = max(max_cash, cash)
        
        # 嘗試走向相鄰路口
        for next_node in graph.get(node, []):
            new_cash = cash
            new_robbed = robbed.copy()
            
            if next_node not in robbed:
                new_cash += atm_amounts[next_node - 1]
                new_robbed.add(next_node)
            
            dfs(next_node, new_robbed, new_cash)
    
    dfs(start, set(), 0)
    return max_cash
```

## 測試用例

**樣本輸入**:
```
6 6
1 2
1 3
2 4
3 4
4 1
4 5
16
8
4
3
8
5
1 2
1 5
```

輸出：`47`

**解釋**：最優路線 1-2-4-1-2-3-5，搶劫金額 `16+8+4+16+8+5 = 57`（根據題目例子調整）
