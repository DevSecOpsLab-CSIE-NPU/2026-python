import io
import sys
import unittest

# 這裡導入你原本寫好的解題函式
# 假設原本的解題函式命名為 solve()
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    num_cases = int(next(iterator))
    
    for case_idx in range(1, num_cases + 1):
        print(f"Case {case_idx}:")
        costs = [int(next(iterator)) for _ in range(36)]
        num_queries = int(next(iterator))
        
        for _ in range(num_queries):
            target_num = int(next(iterator))
            base_costs = {}
            
            for base in range(2, 37):
                current_cost = 0
                temp_num = target_num
                
                if temp_num == 0:
                    current_cost = costs[0]
                else:
                    while temp_num > 0:
                        remainder = temp_num % base
                        current_cost += costs[remainder]
                        temp_num //= base
                
                base_costs[base] = current_cost
            
            min_cost = min(base_costs.values())
            cheapest_bases = [str(b) for b in range(2, 37) if base_costs[b] == min_cost]
            print(f"Cheapest base(s) for number {target_num}: {' '.join(cheapest_bases)}")
            
        if case_idx < num_cases:
            print()

# ================= 測試案例開始 =================

class TestCheapestBase(unittest.TestCase):

    def run_solve_with_input(self, input_string):
        """輔助函式：模擬輸入並擷取輸出結果"""
        saved_stdin = sys.stdin
        saved_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(input_string.strip())
            sys.stdout = io.StringIO()
            solve()
            return sys.stdout.getvalue()
        finally:
            sys.stdin = saved_stdin
            sys.stdout = saved_stdout

    def test_sample_case(self):
        """測試範例測資：包含基本數字、0 與邊界值"""
        sample_input = """
2
10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
3
0
5
35

1 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
1
10
        """
        
        expected_output = (
            "Case 1:\n"
            "Cheapest base(s) for number 0: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
            "Cheapest base(s) for number 5: 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
            "Cheapest base(s) for number 35: 36\n"
            "\n"
            "Case 2:\n"
            "Cheapest base(s) for number 10: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
        )
        
        result = self.run_solve_with_input(sample_input)
        self.assertEqual(result, expected_output)

    def test_single_cheapest_base(self):
        """測試案例：設計特定成本，讓某個進位制具有絕對優勢"""
        # 讓 '0' 的成本極高(100)，其餘為 10，但 'A'(索引10) 的成本極低(1)
        # 當查詢數字為 10 時，在 11 進位以上會被寫成 'A'，成本只需 1
        custom_input = """
1
100 10 10 10 10 10 10 10 10 10 1 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10
1
10
        """
        # 在 11 進位（含）以上，10 頂多佔用 1 個字元 'A'，花費成本為 1。
        # 在 10 進位以下，10 會變成 '10'，成本為 10 + 100 = 110。
        # 因此 11~36 進位都會是最低成本
        expected_output = (
            "Case 1:\n"
            "Cheapest base(s) for number 10: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
        )
        result = self.run_solve_with_input(custom_input)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()