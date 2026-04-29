# 題目 10226

**題名**: UVA 10226

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a219)
- [Yui Huang 題解](https://yuihuang.com/zj-a219/)

## 題目敘述

小光的 DFS 剪枝技巧在這個暑假進步了一些些，但仍然無法通過 DP 的噩夢。
現在給你 N 個人，編號分別是 A, B, ... Z，接著總是會有人不想排哪裡。
請你把所有可能的排列依字典順序列出來，但若新的排列跟上次相同的部分就不輸出，僅輸出不同的部分。

## 輸入說明

有多筆測資，每筆第一行有一個正整數 N（1 ≦ N ≦ 15）。
接下來會有 N 行，第 i 行代表第 i 個人不想排的位置，以 0 代表結束。

## 輸出說明

請把所有可能的排列依字典順序列出來。
與上次相同的部分就不輸出，僅輸出不同的部分。

---

## 解題思路

**核心概念**：DFS + 回溯 + 位掩碼

使用深度優先搜尋配合回溯法產生所有可能排列，同時剪枝掉違反限制的分支。

**步驟**：
1. **位掩碼記錄使用狀態**：用整數的每個 bit 表示某人是否已被放置
   - `mask & (1 << i)` = 1：第 i 人已使用
   - `mask | (1 << i)`：標記第 i 人為已用
   
2. **DFS 遍歷各位置**：對每個位置，嘗試放置尚未使用且符合限制的人
   
3. **剪枝優化**：直接跳過違反限制的人選（人 i 無法在位置 j）
   
4. **字典序輸出**：先將所有排列放入列表，然後排序
   
5. **去重輸出**：與上次排列比較，僅輸出不同部分

**時間複雜度**: O(N! × N)
**空間複雜度**: O(N × N!)

## 解題代碼

```python
def generate_permutations(n: int, restrictions: List[Set[int]]) -> List[List[str]]:
    """使用 DFS + 位掩碼生成所有有效排列"""
    people = [chr(ord('A') + i) for i in range(n)]
    result = []
    
    def dfs(position: int, used: int, current: List[str]) -> None:
        """DFS 遞迴：position=當前位置, used=位掩碼, current=當前排列"""
        if position == n:
            result.append(current[:])
            return
        
        for i in range(n):
            # 跳過已使用的人
            if used & (1 << i):
                continue
            # 跳過該人避免的位置
            if position in restrictions[i]:
                continue
            
            # 放置第 i 人，遞迴到下一位置
            current.append(people[i])
            dfs(position + 1, used | (1 << i), current)
            current.pop()  # 回溯
    
    dfs(0, 0, [])
    result.sort()
    return result
```

## 測試用例

**樣本輸入**:
```
3
0
0
0
```
（3 人，都無限制）

**預期輸出**:
```
A B C
B C
A C
```

**解釋**：
- 第一排列 ABC：完全輸出
- 第二排列 ACB：與 ABC 不同從位置 1 開始，所以輸出「B C」錯誤
- 第二排列 ACB：與 ABC 從位置 1 不同（C vs B），輸出「C B」
- 第三排列 BAC：與 ACB 從位置 0 不同（B vs A），輸出「B A C」

更多測試詳見 `TEST_LOG_10226.md`
