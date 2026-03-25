import sys
from io import StringIO

def solve(input_str):
    """
    主要解題邏輯
    """
    input_data = input_str.split()
    if not input_data:
        return ""
    
    S = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(S):
        N = int(input_data[idx])
        p = float(input_data[idx+1])
        i = int(input_data[idx+2])
        idx += 3
        
        # 處理特殊情況：成功機率為 0 或失敗機率為 1
        if p == 0:
            results.append(f"{0.0000:.4f}")
            continue
            
        q = 1 - p
        # 公式：(p * q^(i-1)) / (1 - q^N)
        # 這是無窮等比級數求和的簡化結果
        ans = (p * (q**(i-1))) / (1 - (q**N))
        
        # 格式化輸出到小數點後四位
        results.append(f"{ans:.4f}")
    
    return "\n".join(results)

def run_test():
    """
    自動化測試工具
    """
    # 測試案例 1: 來自題目範例 (N=2, p=1/6, i=1 & 2)
    # 0.166667 趨近於 1/6
    test_input_1 = """2
2 0.166667 1
2 0.166667 2"""
    expected_1 = "0.5455\n0.4545"

    # 測試案例 2: 特殊情況 p=0
    test_input_2 = """1
10 0.0000 3"""
    expected_2 = "0.0000"

    # 執行測試
    cases = [(test_input_1, expected_1), (test_input_2, expected_2)]
    
    print("=== UVA 10056 測試開始 ===")
    for i, (inp, exp) in enumerate(cases, 1):
        actual = solve(inp)
        if actual.strip() == exp.strip():
            print(f"測試案例 {i}: 通過 (✅)")
        else:
            print(f"測試案例 {i}: 失敗 (❌)")
            print(f"  預期輸出:\n{exp}")
            print(f"  實際輸出:\n{actual}")
    print("==========================")

if __name__ == "__main__":
    # 執行測試
    run_test()
    
    # 如果你想手動輸入測試，可以取消下面這行的註解
    # print(solve(sys.stdin.read()))