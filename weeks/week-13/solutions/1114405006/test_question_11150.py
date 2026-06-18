"""
單元測試：UVA 11150 — 獨木橋與討厭的石子

此測試檔包含：
- 一個暴力但可正確解題的參考實作 `min_stones_bruteforce`（採 Dijkstra），
  適合用於小型測資的單元測試驗證。
- 數個代表性測試案例，並以繁體中文註解說明測試意圖。

注意：題目中 L 可能很大（最高 1e9），此暴力參考實作不適合處理極大 L，
但它足以驗證小型測資與演算法邏輯。
"""

import unittest
import heapq
from typing import List, Set
from question_11150 import min_stones


def min_stones_bruteforce(L: int, S: int, T: int, stones: List[int]) -> int:
    """
    參考暴力解：使用 Dijkstra（最小化踩到石子的次數）。

    節點：整數位置 pos（從 0 起），邊：pos -> pos + step (step in [S,T])。
    權重：若 landing_pos 在 stones 中且 landing_pos < = L-1，則權重為 1（踩石子），否則 0。

    注意：當 landing_pos >= L 時代表已跳出橋，視為成功（不會踩到橋外的石子）。

    此函式僅用於小規模 L 的正確性驗證。
    """
    stone_set: Set[int] = set(stones)

    # 使用 Dijkstra：狀態為位置 pos，值為至該位置踩到的最少石子數
    # 我們只會探索 pos <= L-1 (在橋上) 以及可直接越過 L 的跳躍
    INF = 10**9
    dist = {}
    pq = []  # (cost, pos)
    heapq.heappush(pq, (0, 0))
    dist[0] = 0

    best_finish = INF

    while pq:
        cost, pos = heapq.heappop(pq)
        if cost != dist.get(pos, INF):
            continue

        # 從 pos 嘗試各種跳躍
        for step in range(S, T+1):
            newpos = pos + step
            if newpos >= L:
                # 跳出橋，完成；不會另外踩到石子（題目保證終點無石）
                if cost < best_finish:
                    best_finish = cost
                continue

            # 否則落在橋內某位置，若該位置是石子，成本 +1
            add = 1 if newpos in stone_set else 0
            newcost = cost + add
            # 若新的成本比已知更好，放入優先佇列
            if newcost < dist.get(newpos, INF):
                dist[newpos] = newcost
                # 若 newpos 本身已經超過某個合理上界也可以剪枝，但此處為暴力實作
                heapq.heappush(pq, (newcost, newpos))

    return best_finish if best_finish != INF else -1


class TestQuestion11150(unittest.TestCase):
    """包含數個容易推理的測資以驗證演算法正確性"""

    def test_no_stones_easy(self):
        """
        沒有石子的情況：理論最少踩石子數為 0。
        範例：L=10, S=3, T=4, 無石子
        """
        self.assertEqual(min_stones_bruteforce(10, 3, 4, []), 0)

    def test_fixed_step_all_stones(self):
        """
        固定步長且每個踏點剛好都是石子時，需踩到所有中間石子。
        例：L=10, S=T=2, 石子在 2,4,6,8 -> 每步必經，需踩 4 個石子
        """
        self.assertEqual(min_stones_bruteforce(10, 2, 2, [2, 4, 6, 8]), 4)

    def test_example_with_choice_zero(self):
        """
        有選擇時可完全避開石子：
        L=10, S=3, T=4, 石子在 4,7。由於可選擇連續跳 3，路徑 0->3->6->9->12 可避開石子。
        所以最少為 0。
        """
        self.assertEqual(min_stones_bruteforce(10, 3, 4, [4, 7]), 0)

    def test_two_stones_fixed3(self):
        """
        固定步長 3，兩顆石子在每次著地點上，理論需要踩兩次。
        例：L=9, S=T=3, 石子 3,6
        """
        self.assertEqual(min_stones_bruteforce(9, 3, 3, [3, 6]), 2)

    def test_optimized_matches_bruteforce_small(self):
        """
        比較暴力解與優化解在小型測資上的結果是否一致。
        這裡限定 L 不大（<=30），以免暴力解超時。
        """
        import random
        random.seed(0)

        for L in [10, 20, 25]:
            for S in [1, 2, 3]:
                for T in range(S, min(S + 3, 6)):
                    # 產生一些隨機但可重覆的石子配置
                    for _ in range(10):
                        M = random.randint(0, min(6, max(0, L - 1)))
                        stones = random.sample(range(1, L), M)
                        bf = min_stones_bruteforce(L, S, T, stones)
                        opt = min_stones(L, S, T, stones)
                        self.assertEqual(bf, opt, msg=f"Mismatch L={L} S={S} T={T} stones={stones}")


if __name__ == "__main__":
    unittest.main()

