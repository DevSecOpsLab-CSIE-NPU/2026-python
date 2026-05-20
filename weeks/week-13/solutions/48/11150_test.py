"""
UVA 11150 Frog Bridge 測試程式
"""
from collections import deque

def solve_test(test_cases):
    """運行測試的求解函數"""
    lines = [line.strip() for line in test_cases.strip().split('\n')]
    line_idx = 0
    results = []
    
    while line_idx < len(lines):
        vals = list(map(int, lines[line_idx].split()))
        line_idx += 1
        
        L, S, T, M = vals[0], vals[1], vals[2], vals[3]
        
        if L == 0 and S == 0 and T == 0 and M == 0:
            break
        
        stones = set()
        if M > 0:
            stones = set(map(int, lines[line_idx].split()))
            line_idx += 1
        
        # BFS
        queue = deque([(0, 0)])
        visited = {0: 0}
        ans = float('inf')
        
        while queue:
            pos, cnt = queue.popleft()
            
            if pos + S >= L:
                ans = min(ans, cnt)
                continue
            
            for jump in range(S, T + 1):
                nxt = pos + jump
                
                if nxt >= L:
                    ans = min(ans, cnt)
                else:
                    ncnt = cnt + (1 if nxt in stones else 0)
                    if nxt not in visited or visited[nxt] > ncnt:
                        visited[nxt] = ncnt
                        queue.append((nxt, ncnt))
        
        results.append(str(ans))
    
    return "\n".join(results)


# 測試用例
test_input = """10 1 2 3
2 4 5
20 2 3 4
5 10 15 20
0 0 0 0
"""

print("=" * 60)
print("UVA 11150 Frog Bridge - 測試程式")
print("=" * 60)
print("\n【測試輸入】")
print(test_input)
print("\n【實際輸出】")
output = solve_test(test_input)
print(output)

# 測試 2
test_input2 = """100 5 10 5
10 20 30 40 50
0 0 0 0
"""

print("\n" + "=" * 60)
print("【測試 2: 較大規模】")
print("=" * 60)
print("\n【測試輸入】")
print(test_input2)
print("\n【實際輸出】")
output2 = solve_test(test_input2)
print(output2)
