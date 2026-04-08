import sys
import io

# 增加遞迴深度限制，這對處理 N=80,000 的線段樹至關重要
sys.setrecursionlimit(200000)

def solve(input_string):
    """
    這是核心邏輯函式，接收一個字串作為輸入，並回傳結果清單。
    """
    data = input_string.split()
    if not data:
        return []
    
    n = int(data[0])
    # 建立「前面比我小的數量」數組，補上第一頭牛的 0
    pre_smaller = [0] * n
    for i in range(1, n):
        pre_smaller[i] = int(data[i])
    
    # 線段樹：儲存區間內剩餘可用編號的數量
    tree = [0] * (4 * n)
    
    def build(node, start, end):
        if start == end:
            tree[node] = 1
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query_and_update(node, start, end, k):
        tree[node] -= 1  # 找到目標的路徑上，可用數量都減 1
        if start == end:
            return start
        
        mid = (start + end) // 2
        left_available = tree[2 * node]
        
        if k <= left_available:
            return query_and_update(2 * node, start, mid, k)
        else:
            return query_and_update(2 * node + 1, mid + 1, end, k - left_available)

    # 執行流程
    build(1, 1, n)
    ans = [0] * n
    # 從最後一頭牛逆推
    for i in range(n - 1, -1, -1):
        rank = pre_smaller[i] + 1
        ans[i] = query_and_update(1, 1, n, rank)
    
    return ans

# --- 測試區塊 ---

def run_test(test_id, input_str, expected_output):
    """ 輔助函式：執行單一測試案例並比對結果 """
    print(f"--- 測試案例 {test_id} ---")
    result = solve(input_str)
    
    if result == expected_output:
        print("✅ 測試通過！")
        print(f"結果: {result}")
    else:
        print("❌ 測試失敗！")
        print(f"預期結果: {expected_output}")
        print(f"實際結果: {result}")
    print("-" * 20)

if __name__ == "__main__":
    # 測試案例 1：題目提供的範例
    case1_input = "5 1 2 1 0"
    case1_expected = [2, 4, 5, 3, 1]
    
    # 測試案例 2：由小到大排列 (1, 2, 3, 4, 5)
    # 輸入應該是：2前面有1個, 3前面有2個...
    case2_input = "5 1 2 3 4"
    case2_expected = [1, 2, 3, 4, 5]

    # 測試案例 3：由大到小排列 (5, 4, 3, 2, 1)
    # 輸入應該是：4前面有0個, 3前面有0個...
    case3_input = "5 0 0 0 0"
    case3_expected = [5, 4, 3, 2, 1]

    run_test(1, case1_input, case1_expected)
    run_test(2, case2_input, case2_expected)
    run_test(3, case3_input, case3_expected)
    
    print("\n💡 提示：如果要在 ZeroJudge 執行，請使用 sys.stdin.read() 的版本！")