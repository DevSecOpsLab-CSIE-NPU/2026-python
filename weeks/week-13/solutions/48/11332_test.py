"""
UVA 11332 Mirrors Visibility 測試程式
"""

def cross(o, a, b):
    """叉積 (a-o) × (b-o)"""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def is_visible(mirror_idx, mirrors):
    """Check if mirror is visible"""
    s, e = mirrors[mirror_idx]
    
    for t in [0, 0.25, 0.5, 0.75, 1.0]:
        px = s[0] + t * (e[0] - s[0])
        py = s[1] + t * (e[1] - s[1])
        p = (px, py)
        
        blocked = False
        dist_p = px * px + py * py
        
        for j in range(len(mirrors)):
            if mirror_idx == j:
                continue
            
            s2, e2 = mirrors[j]
            
            cross_s2 = cross((0, 0), p, s2)
            cross_e2 = cross((0, 0), p, e2)
            
            if cross_s2 * cross_e2 <= 0 and (cross_s2 != 0 or cross_e2 != 0):
                dist_s2 = s2[0] * s2[0] + s2[1] * s2[1]
                dist_e2 = e2[0] * e2[0] + e2[1] * e2[1]
                
                if min(dist_s2, dist_e2) < dist_p:
                    blocked = True
                    break
        
        if not blocked:
            return True
    
    return False

def solve_test(test_cases):
    """運行測試的求解函數"""
    lines = [line.strip() for line in test_cases.strip().split('\n') if line.strip()]
    line_idx = 0
    results = []
    
    while line_idx < len(lines):
        n = int(lines[line_idx])
        line_idx += 1
        
        if n == 0:
            break
        
        mirrors = []
        for _ in range(n):
            sx, sy, ex, ey = map(int, lines[line_idx].split())
            line_idx += 1
            mirrors.append(((sx, sy), (ex, ey)))
        
        result = []
        for i in range(n):
            result.append('1' if is_visible(i, mirrors) else '0')
        
        results.append(''.join(result))
    
    return '\n'.join(results)


# 測試用例
test_input = """3
5 5 10 5
0 10 10 10
5 0 5 10
2
1 1 2 2
3 3 4 4
0
"""

print("=" * 60)
print("UVA 11332 Mirrors Visibility - 測試程式")
print("=" * 60)
print("\n【測試 1: 3個鏡子】")
print("【測試輸入】")
print(test_input)
print("\n【實際輸出】")
output = solve_test(test_input)
print(output)

# 測試 2
test_input2 = """1
1 0 1 1
0
"""

print("\n" + "=" * 60)
print("【測試 2: 單個鏡子】")
print("=" * 60)
print("【測試輸入】")
print(test_input2)
print("\n【實際輸出】")
output2 = solve_test(test_input2)
print(output2)
