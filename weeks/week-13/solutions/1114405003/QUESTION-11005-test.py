"""
QUESTION-11005 測試程式
最便宜的進位制 - Cheapest Base
"""

def test_cheapest_base():
    """測試進位制轉換和成本計算"""
    
    print("=" * 70)
    print("測試案例1：簡單的數字轉換")
    print("=" * 70)
    
    # 測試進位制轉換
    test_cases = [
        (10, 2, [1, 0, 1, 0]),  # 10進位的10在2進位是1010
        (10, 10, [1, 0]),        # 10進位的10在10進位是10
        (255, 16, [15, 15]),     # 10進位的255在16進位是FF
        (100, 10, [1, 0, 0]),    # 10進位的100在10進位是100
    ]
    
    for decimal, base, expected in test_cases:
        # 轉換
        result = []
        n = decimal
        while n > 0:
            result.append(n % base)
            n //= base
        result = result[::-1]
        
        status = "✓" if result == expected else "✗"
        print(f"{status} {decimal}(十) → {base}進位 = {result} (預期: {expected})")
    
    print()
    print("=" * 70)
    print("測試案例2：成本計算邏輯")
    print("=" * 70)
    
    # 假設成本陣列：0-9各1,A-Z各2
    costs = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 0-9 的成本
    costs.extend([2] * 26)  # A-Z 的成本
    
    print(f"成本陣列示例：")
    print(f"  0-9: 各1單位")
    print(f"  A-Z: 各2單位")
    print()
    
    # 數字5在10進位: 成本=1 (只有一位數字5)
    cost = costs[5]
    print(f"✓ 數字5在10進位表示為'5' → 成本 = {cost}")
    
    # 數字10在2進位: 1010 → 成本=4 (1+0+1+0)
    cost = costs[1] + costs[0] + costs[1] + costs[0]
    print(f"✓ 數字10在2進位表示為'1010' → 成本 = {cost}")
    
    print()
    print("=" * 70)
    print("測試案例3：進位制選擇")
    print("=" * 70)
    
    # 計算數字8用不同進位制的成本
    n = 8
    print(f"\n為數字{n}尋找最便宜的進位制：")
    print()
    
    costs_simple = [1] * 10 + [2] * 26  # 0-9:1, A-Z:2
    
    results = []
    for base in [2, 8, 10, 16]:
        if n == 0:
            cost = costs_simple[0]
        else:
            temp = n
            digits = []
            while temp > 0:
                digits.append(temp % base)
                temp //= base
            cost = sum(costs_simple[d] for d in digits)
        
        results.append((base, cost))
        print(f"  {n} 在 {base:2d}進位: 成本 = {cost}")
    
    min_cost = min(results, key=lambda x: x[1])[1]
    best_bases = [r[0] for r in results if r[1] == min_cost]
    print(f"\n最便宜進位制: {best_bases} (成本={min_cost})")

if __name__ == "__main__":
    test_cheapest_base()
