import unittest

def get_cheapest_bases(costs, number):
    """
    計算指定數字在 2 到 36 進位制中的印刷成本，並回傳成本最低的進位制列表。
    
    參數:
    costs (list): 長度為 36 的整數列表，代表字元 0-9, A-Z 的印刷成本
    number (int): 要查詢的十進位整數
    
    回傳:
    list: 包含最低成本進位制（2到36）的列表，依升序排列
    """
    # 處理特殊情況：當數字為 0 時，無論哪個進位制都只顯示 '0'
    # 因此所有進位制的成本皆為 costs[0]，全都是最低成本
    if number == 0:
        return list(range(2, 37))

    min_cost = float('inf')  # 初始最低成本設為無限大
    best_bases = []          # 儲存最低成本的進位制

    # 遍歷 2 到 36 進位
    for base in range(2, 37):
        current_cost = 0
        temp = number
        
        # 將十進位數字轉換為該進位制，並同時累加該位數對應的成本
        while temp > 0:
            digit = temp % base
            current_cost += costs[digit]
            temp //= base

        # 判斷是否需要更新最低成本或是加入並列的進位制
        if current_cost < min_cost:
            min_cost = current_cost
            best_bases = [base]      # 找到更低的成本，重置列表
        elif current_cost == min_cost:
            best_bases.append(base)  # 成本相同，加入列表

    return best_bases


class TestUVA11005(unittest.TestCase):
    def test_zero_number(self):
        # 測試案例 1：測試目標數字為 0 的極端情況
        costs = [10] * 36  # 假設每個字元的成本都是 10
        result = get_cheapest_bases(costs, 0)
        self.assertEqual(result, list(range(2, 37)), "數字為 0 時，所有進位制（2~36）的成本應該都相同且為最低")

    def test_uniform_costs(self):
        # 測試案例 2：測試所有字元成本皆相同的情況
        costs = [1] * 36  # 所有字元成本都是 1
        # 對於數字 10，在 11~36 進位中只需一個位元 (成本為 1)
        # 但在 2~10 進位中需要多個位元 (成本 > 1)
        result = get_cheapest_bases(costs, 10)
        self.assertEqual(result, list(range(11, 37)), "所有字元成本相同時，進位制越大位數越少，總成本應越低")

    def test_example_cost(self):
        # 測試案例 3：測試特定的成本陣列
        # 假設我們將字母 A（值為 10）的成本設為極低，其餘非常高
        costs = [100] * 36
        costs[10] = 5  # 'A' 的成本為 5
        
        # 數字 10 在 11 進位以上會直接表示為 'A'（成本 5）
        # 在 10 進位會表示為 '10'（成本為 costs[1]+costs[0] = 200）
        result = get_cheapest_bases(costs, 10)
        self.assertEqual(result, list(range(11, 37)), "必須優先選擇對應字元成本總和最低的進位制")

if __name__ == '__main__':
    # 執行單元測試
    unittest.main()