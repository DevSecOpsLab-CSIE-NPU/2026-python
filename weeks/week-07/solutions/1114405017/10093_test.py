import io
import sys

# --- 核心演算法函數 ---
def max_artillery(input_string):
    input_data = input_string.split()
    if not input_data: return 0
    
    N = int(input_data[0])
    M = int(input_data[1])
    grid = input_data[2:]

    # 1. 預處理合法狀態
    valid_states = []
    for s in range(1 << M):
        if not (s & (s << 1)) and not (s & (s << 2)):
            valid_states.append((s, bin(s).count('1')))

    # 2. 地形遮罩
    row_masks = []
    for r in range(N):
        mask = 0
        for c in range(M):
            if grid[r][c] == 'H': mask |= (1 << (M - 1 - c))
        row_masks.append(mask)

    # 3. DP 初始化
    num_states = len(valid_states)
    dp = [[-1] * num_states for _ in range(num_states)]
    
    for j, (s_curr, cnt) in enumerate(valid_states):
        if not (s_curr & row_masks[0]):
            dp[j][0] = cnt

    # 4. DP 轉移
    for i in range(1, N):
        new_dp = [[-1] * num_states for _ in range(num_states)]
        for j, (s_curr, cnt) in enumerate(valid_states):
            if s_curr & row_masks[i]: continue
            for k, (s_prev, _) in enumerate(valid_states):
                if s_curr & s_prev: continue
                max_val = -1
                for l, (s_pprev, _) in enumerate(valid_states):
                    if (s_curr & s_pprev) or (dp[k][l] == -1): continue
                    if dp[k][l] > max_val: max_val = dp[k][l]
                if max_val != -1:
                    new_dp[j][k] = max_val + cnt
        dp = new_dp

    ans = 0
    for r in dp:
        ans = max(ans, max(r))
    return ans

# --- 測試程式 ---
def run_tests():
    test_cases = [
        {
            "name": "範例測資",
            "input": "5 4\nPHPP\nPPHH\nPPPP\nPHPP\nPHHP",
            "expected": 6
        },
        {
            "name": "全平原 (1x1)",
            "input": "1 1\nP",
            "expected": 1
        },
        {
            "name": "全山地 (3x3)",
            "input": "3 3\nHHH\nHHH\nHHH",
            "expected": 0
        },
        {
            "name": "窄長條 (1x10)",
            "input": "1 10\nPPPPPPPPPP",
            "expected": 4 # 1001001001 (最多4個，間隔2格)
        },
        {
            "name": "垂直密集 (3x1)",
            "input": "3 1\nP\nP\nP",
            "expected": 1 # 縱向也會互相攻擊，所以只能放1個
        }
    ]

    print(f"{'測試名稱':<15} | {'預期':<5} | {'實際':<5} | {'結果'}")
    print("-" * 50)

    for case in test_cases:
        result = max_artillery(case["input"])
        status = "✅ 通過" if result == case["expected"] else "❌ 失敗"
        print(f"{case['name']:<15} | {case['expected']:<5} | {result:<5} | {status}")

if __name__ == "__main__":
    run_tests()