import sys
from io import StringIO

# 這裡放入你寫好的解題邏輯
def solve():
    # 為了測試，我們將 sys.stdin 替換為我們模擬的輸入源
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    field_count = 1
    
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        if n == 0 and m == 0:
            break
        
        grid = []
        for i in range(n):
            grid.append(list(input_data[idx]))
            idx += 1
            
        if field_count > 1:
            print()
            
        print(f"Field #{field_count}:")
        
        for r in range(n):
            row_result = ""
            for c in range(m):
                if grid[r][c] == '*':
                    row_result += '*'
                else:
                    mine_count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0: continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < m:
                                if grid[nr][nc] == '*':
                                    mine_count += 1
                    row_result += str(mine_count)
            print(row_result)
        field_count += 1

# --- 測試專用區塊 ---
def run_test(test_input, expected_output):
    # 模擬輸入
    sys.stdin = StringIO(test_input.strip())
    # 捕捉輸出
    captured_output = StringIO()
    sys.stdout = captured_output
    
    solve()
    
    # 取得結果
    result = captured_output.getvalue().strip()
    expected = expected_output.strip()
    
    print("-" * 30)
    if result == expected:
        print("✅ 測試通過 (PASSED)")
    else:
        print("❌ 測試失敗 (FAILED)")
        print("\n[預期輸出]:")
        print(expected)
        print("\n[實際輸出]:")
        print(result)
    print("-" * 30)

# 準備測試資料
test_cases = [
    {
        "input": """
4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
""",
        "expected": """
Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100
"""
    }
]

if __name__ == "__main__":
    # 執行測試
    for i, case in enumerate(test_cases):
        print(f"執行測試案例 {i+1}...")
        run_test(case["input"], case["expected"])
    
    # 測試完畢後恢復標準輸出，否則在 IDE 裡看不到東西
    sys.stdout = sys.__stdout__