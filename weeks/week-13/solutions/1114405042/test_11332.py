import unittest
import math

eps = 1e-9

def solve_mirrors(n, segments):
    angles = []
    for sx, sy, ex, ey in segments:
        ang1 = math.atan2(sy, sx)
        ang2 = math.atan2(ey, ex)
        angles.extend([ang1, ang2, ang1 - eps, ang1 + eps, ang2 - eps, ang2 + eps])
        
    visible = [0] * n
    
    for angle in angles:
        dx = math.cos(angle)
        dy = math.sin(angle)
        
        min_dist = float('inf')
        closest = -1
        
        for i, (sx, sy, ex, ey) in enumerate(segments):
            A = dx
            B = -(ex - sx)
            C = dy
            D = -(ey - sy)
            
            det = A * D - B * C
            if abs(det) < eps: continue
                
            t = (sx * D - sy * B) / det
            u = (A * sy - C * sx) / det
            
            if t > eps and -eps <= u <= 1 + eps:
                if t < min_dist:
                    min_dist = t
                    closest = i
                    
        if closest != -1:
            visible[closest] = 1
            
    return visible

class Test11332(unittest.TestCase):
    def test_mirrors_1(self):
        """
        測試鏡子互相遮蔽的情況
        """
        n = 2
        # 第一面鏡子在前面
        # 第二面鏡子在後面，被第一面完全遮住
        segments = [
            (1, 1, 1, -1),
            (2, 2, 2, -2)
        ]
        result = solve_mirrors(n, segments)
        self.assertEqual(result, [1, 0])

if __name__ == '__main__':
    unittest.main()
