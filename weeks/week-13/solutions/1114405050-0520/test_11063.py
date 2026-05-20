import unittest

def rgb_to_xyz(r, g, b):
    """
    將像素的 RGB 數值根據題目給定的公式轉換為 XYZ 數值
    
    參數:
    r, g, b (int): 像素的紅綠藍顏色值，介於 0~255
    
    回傳:
    tuple: 包含三個浮點數的 tuple，分別代表 X, Y, Z
    """
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z

def calculate_average_y(y_list):
    """
    計算影像中所有像素的平均亮度 (Y)
    
    參數:
    y_list (list): 包含所有像素 Y 數值的串列
    
    回傳:
    float: Y 的平均值
    """
    if not y_list:
        return 0.0
    return sum(y_list) / len(y_list)

class TestImageConversion(unittest.TestCase):
    def test_rgb_to_xyz_zero(self):
        # 測試案例 1：全黑像素 (0, 0, 0)
        x, y, z = rgb_to_xyz(0, 0, 0)
        self.assertAlmostEqual(x, 0.0, places=4, msg="全黑像素 X 轉換錯誤")
        self.assertAlmostEqual(y, 0.0, places=4, msg="全黑像素 Y 轉換錯誤")
        self.assertAlmostEqual(z, 0.0, places=4, msg="全黑像素 Z 轉換錯誤")

    def test_rgb_to_xyz_max(self):
        # 測試案例 2：全白像素 (255, 255, 255)
        x, y, z = rgb_to_xyz(255, 255, 255)
        # 公式中各項係數總和為 1.0，因此 255 轉換後依然為 255
        self.assertAlmostEqual(x, 255.0, places=4, msg="全白像素 X 轉換錯誤")
        self.assertAlmostEqual(y, 255.0, places=4, msg="全白像素 Y 轉換錯誤")
        self.assertAlmostEqual(z, 255.0, places=4, msg="全白像素 Z 轉換錯誤")
        
    def test_rgb_to_xyz_custom(self):
        # 測試案例 3：針對題目敘述中提到的數值做測試 (255, 3, 192)
        x, y, z = rgb_to_xyz(255, 3, 192)
        self.assertAlmostEqual(x, 163.1271, places=4)
        self.assertAlmostEqual(y, 82.0146, places=4)
        self.assertAlmostEqual(z, 169.9752, places=4)

    def test_average_y(self):
        # 測試案例 4：測試平均亮度的計算
        self.assertAlmostEqual(calculate_average_y([10.0, 20.0, 30.0]), 20.0, places=4)

if __name__ == '__main__':
    unittest.main()