import unittest
import io
import sys
import math

# ==========================================
# 這是我們剛剛寫好的解題核心邏輯
# ==========================================
def run_visibility_logic(input_string):
    """將原本 sys.stdin.read() 的邏輯封裝，方便測試"""
    input_data = input_string.split()
    if not input_data:
        return ""
    
    iterator = iter(input_data)
    output_lines = []
    
    while True:
        try:
            n = int(next(iterator))
        except StopIteration:
            break
        
        segments = []
        angles = set()
        
        for i in range(n):
            sx, sy, ex, ey = [int(next(iterator)) for _ in range(4)]
            segments.append((sx, sy, ex, ey, i))
            angles.add(math.atan2(sy, sx))
            angles.add(math.atan2(ey, ex))
        
        sorted_angles = sorted(list(angles))
        
        mid_angles = []
        for i in range(len(sorted_angles) - 1):
            mid_angles.append((sorted_angles[i] + sorted_angles[i+1]) / 2)
        if sorted_angles:
            mid_angles.append((sorted_angles[-1] + sorted_angles[0] + 2 * math.pi) / 2)
        
        visible = [0] * n
        
        def get_distance(ang, x1, y1, x2, y2):
            rx, ry = math.cos(ang), math.sin(ang)
            dx, dy = x2 - x1, y2 - y1
            denom = rx * dy - ry * dx
            if abs(denom) < 1e-9: 
                return float('inf')
            
            t = (x1 * dy - y1 * dx) / denom
            u = (x1 * ry - y1 * rx) / denom
            
            if t > 0 and 0 <= u <= 1:
                return t
            return float('inf')

        for ang in mid_angles:
            min_dist = float('inf')
            closest_idx = -1
            
            for sx, sy, ex, ey, idx in segments:
                dist = get_distance(ang, sx, sy, ex, ey)
                if dist < min_dist:
                    min_dist = dist
                    closest_idx = idx
            
            if closest_idx != -1:
                visible[closest_idx] = 1
                
        output_lines.append(" ".join(map(str, visible)))
        
    return "\n".join(output_lines)


# ==========================================
# 自動化測試單元
# ==========================================
class TestMirrorVisibility(unittest.TestCase):

    def test_case_1_basic(self):
        """測試案例 1：基本交錯鏡子與完全遮擋"""
        # 第一組：三個鏡子互相交錯，但各自都有部分露出
        # 第二組：第二個鏡子完全被第一個鏡子擋在正後方
        test_input = """3
1 2 3 2
2 1 2 3
0 3 3 0
2
-1 1 -2 2
-2 2 -3 3"""
        
        expected_output = """1 1 1
1 0"""
        
        result = run_visibility_logic(test_input)
        self.assertEqual(result, expected_output)

    def test_case_2_partial_blocking(self):
        """測試案例 2：部分遮擋（大鏡子後面躲一個更長但露出一點點的鏡子）"""
        # 第一個鏡子在前方擋住部分視線
        # 第二個鏡子比較遠，但它很長，兩端會露出來
        test_input = """2
-2 2 2 2
-4 4 4 4"""
        
        expected_output = """1 1""" # 兩個都應該看得到
        
        result = run_visibility_logic(test_input)
        self.assertEqual(result, expected_output)

    def test_case_3_no_mirrors(self):
        """測試案例 3：邊界條件，沒有鏡子或輸入為空"""
        test_input = ""
        expected_output = ""
        
        result = run_visibility_logic(test_input)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    # 執行測試
    unittest.main()