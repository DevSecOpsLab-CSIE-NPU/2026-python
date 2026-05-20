"""
UVA 11063 RGB to XYZ 測試程式
"""

def solve_test(input_data):
    """運行測試的求解函數"""
    lines = input_data.strip().split('\n')
    line_idx = 0
    
    n = int(lines[line_idx])
    line_idx += 1
    
    pixels = []
    total_y = 0
    
    for i in range(n):
        row = list(map(int, lines[line_idx].split()))
        line_idx += 1
        
        for j in range(n):
            r, g, b = row[j*3:j*3+3]
            
            # RGB to XYZ conversion
            x = 0.5149 * r + 0.3244 * g + 0.1607 * b
            y = 0.2654 * r + 0.6704 * g + 0.0642 * b
            z = 0.0248 * r + 0.1248 * g + 0.8504 * b
            
            pixels.append((x, y, z))
            total_y += y
    
    results = []
    # Output pixels
    for x, y, z in pixels:
        results.append(f"{x:.4f} {y:.4f} {z:.4f}")
    
    # Output average Y
    avg_y = total_y / (n * n)
    results.append(f"The average of Y is {avg_y:.4f}")
    
    return "\n".join(results)


# 測試用例 1: 2x2 影像
test_input1 = """2
255 0 0 0 255 0
0 0 255 255 255 255
"""

print("=" * 60)
print("UVA 11063 RGB to XYZ - 測試程式")
print("=" * 60)
print("\n【測試 1: 2x2 影像】")
print("【測試輸入】")
print(test_input1)
print("【實際輸出】")
output1 = solve_test(test_input1)
print(output1)

# 測試用例 2: 1x1 影像
test_input2 = """1
128 128 128
"""

print("\n" + "=" * 60)
print("【測試 2: 1x1 影像 (中性灰)】")
print("=" * 60)
print("【測試輸入】")
print(test_input2)
print("【實際輸出】")
output2 = solve_test(test_input2)
print(output2)
