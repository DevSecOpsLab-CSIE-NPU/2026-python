"""
簡潔版：UVA 11005 — Cheapest Base（-easy）

目的：
- 提供一個非常直觀且容易記憶的 `cheapest_bases(costs, N)` 實作，適合教學與快速理解演算法概念。

說明要點（繁體中文詳細註解）：

1) 參數與輸入格式
   - `costs`：長度為 36 的整數列表，對應字元 `0`..`9`,`A`..`Z` 的印刷成本。
     索引含義：`costs[0]` 對應字元 `'0'`，`costs[10]` 對應字元 `'A'`，以此類推。
   - `N`：要查詢的非負整數（十進位表示），題目範圍通常為 0 到 2,000,000,000。

2) 演算法直觀說明
   - 對每個進位 `base`（從 2 到 36）：
     a. 若 `N == 0`，任何進位的表示都是單一字元 `'0'`，成本為 `costs[0]`。
     b. 否則，重複對 `N` 取商與餘數（使用 `divmod` 或 `%`、`//`），每次取得的餘數為當前位元的數值，
        將該位元的成本加到 `total`；將商繼續取下一位，直到商為 0。
     c. 得到該進位的 `total` 成本後，比較並記錄是否為目前最小成本，若相等則加入候選進位清單。

3) 回傳值
   - 回傳一個整數列表，包含所有達成最小成本的進位（以產生順序為升序），例如 `[2, 5, 10]`。

4) 時間與空間複雜度（簡短）
   - 時間：對每個進位需做 O(log_b N) 次除法與取餘；因為進位範圍是常數（2..36），整體為常數級別（很小）。
   - 空間：只使用常數額外空間，記錄最小成本與候選進位列表。

5) 使用注意事項
   - 檔名包含 `-`，若要在程式中以模組匯入，無法直接用 `import cheapest_base-easy`，
     可用 `importlib.util.spec_from_file_location` 動態載入，或直接將函式複製到其他模組中使用。

範例程式：
"""

def cheapest_bases(costs, N):
    """回傳在 2..36 進位中，表示 N 時成本最低的進位列表（詳細註解版）。

    實作說明：使用最直觀的迴圈與 divmod，不作額外優化，易讀性為優先。
    """
    # 檢查 costs 長度是否為 36
    if len(costs) != 36:
        raise ValueError("costs must have length 36")

    # best_cost: 目前觀察到的最低總成本（整數），best_bases: 對應的進位列表
    best_cost = None
    best_bases = []

    # 逐一計算 2 到 36 的總成本
    for base in range(2, 37):
        if N == 0:
            # 特例：0 在任何進位下都只出現一位 '0'
            total = costs[0]
        else:
            total = 0
            x = N
            # 使用 while 迴圈與 divmod 依序取得各位數值（由低位到高位）
            while x:
                x, d = divmod(x, base)  # d 為目前最低位的數字
                # 將該位數字對應的成本加總
                total += costs[d]

        # 比對並更新最小成本與對應進位
        if best_cost is None or total < best_cost:
            best_cost = total
            best_bases = [base]
        elif total == best_cost:
            best_bases.append(base)

    return best_bases


if __name__ == "__main__":
    # 簡單示範：若想測試請在此區修改 costs 與 N
    example_costs = list(range(36))  # 範例成本（0..35）
    print("Example: cheapest bases for N=0 ->", cheapest_bases(example_costs, 0))
