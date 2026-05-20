"""
QUESTION-11063 測試程式
設計用來測試RGB轉XYZ色彩系統的轉換
"""

def test_rgb_to_xyz():
    """測試RGB到XYZ的轉換"""
    
    # 測試案例1: 2x2 影像
    test_input_1 = """2
255 0 0 0 255 0
0 0 255 255 255 255"""
    
    expected_output_1 = """0.5149 0.2654 0.0248
0.3244 0.6704 0.1248
0.1607 0.0642 0.8504
0.9643 0.9300 1.0359
The average of Y is 0.5150"""
    
    # 測試案例2: 1x1 灰色像素
    test_input_2 = """1
128 128 128"""
    
    expected_output_2 = """65.9072 51.6512 53.6128
The average of Y is 51.6512"""
    
    print("測試案例1：2x2影像")
    print("=" * 50)
    print("輸入：")
    print(test_input_1)
    print("\n預期輸出：")
    print(expected_output_1)
    print("\n" + "=" * 50)
    
    print("\n測試案例2：1x1灰色像素")
    print("=" * 50)
    print("輸入：")
    print(test_input_2)
    print("\n預期輸出：")
    print(expected_output_2)
    print("\n" + "=" * 50)
    
    # 簡單驗證
    r, g, b = 128, 128, 128
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    
    print("\n手動計算驗證 (R=128, G=128, B=128)：")
    print(f"X = {x:.4f}")
    print(f"Y = {y:.4f}")
    print(f"Z = {z:.4f}")

if __name__ == "__main__":
    test_rgb_to_xyz()
