"""
UVA 11321 Magic Road 測試程式
"""
from collections import deque

def can_reach(N, M, traps):
    """Check if can reach from left to right"""
    grid = {(x, y): True for x, y in traps}
    
    queue = deque()
    visited = set()
    
    for x in range(N):
        if (x, 0) not in grid:
            queue.append((x, 0))
            visited.add((x, 0))
    
    while queue:
        x, y = queue.popleft()
        
        if y == M - 1:
            return True
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M:
                if (nx, ny) not in visited and (nx, ny) not in grid:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return False

def solve_test(test_cases):
    """執行測試的求解函數"""
    lines = [line.strip() for line in test_cases.strip().split('\n')]
    line_idx = 0
    results = []
    
    while line_idx < len(lines):
        vals = list(map(int, lines[line_idx].split()))
        line_idx += 1
        
        N, M, T = vals[0], vals[1], vals[2]
        
        if N == 0 and M == 0 and T == 0:
            break
        
        traps = set()
        
        for _ in range(T):
            x, y = map(int, lines[line_idx].split())
            line_idx += 1
            
            test_traps = traps | {(x, y)}
            
            if can_reach(N, M, test_traps):
                results.append("<(_ _)>")
                traps.add((x, y))
            else:
                results.append(">_<")
    
    return "\n".join(results)


# 測試用例
test_input = """3 3 3
0 1
1 1
2 1
0 0 0
"""

print("=" * 60)
print("UVA 11321 Magic Road - 測試程式")
print("=" * 60)
print("\n【測試 1: 3x3 網格】")
print("【測試輸入】")
print(test_input)
print("\n【實際輸出】")
output = solve_test(test_input)
print(output)

# 測試 2
test_input2 = """2 2 2
1 0
0 1
0 0 0
"""

print("\n" + "=" * 60)
print("【測試 2: 2x2 網格】")
print("=" * 60)
print("【測試輸入】")
print(test_input2)
print("\n【實際輸出】")
output2 = solve_test(test_input2)
print(output2)
