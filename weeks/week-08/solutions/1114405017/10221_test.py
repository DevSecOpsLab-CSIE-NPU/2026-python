import math
import io
import sys

# 這是原本的計算邏輯函式
def calculate(s, a, unit):
    r = 6440 + s
    if unit == 'min':
        a /= 60.0
    if a > 180:
        a = 360 - a
    
    rad = a * math.pi / 180.0
    arc_length = r * rad
    chord_distance = 2 * r * math.sin(rad / 2.0)
    
    return f"{arc_length:.6f} {chord_distance:.6f}"

# 測試執行器
def run_test():
    test_cases = [
        {"input": (500, 30, 'deg'), "expected": "3633.775503 3592.408346"},
        {"input": (700, 60, 'min'), "expected": "124.616509 124.614927"},
        {"input": (200, 45, 'deg'), "expected": "5215.043805 5082.035982"},
    ]
    
    print(f"{'測試狀態':<10} | {'計算結果':<40} | {'預期結果'}")
    print("-" * 80)
    
    for i, case in enumerate(test_cases):
        res = calculate(*case["input"])
        status = "✅ 通過" if res == case["expected"] else "❌ 失敗"
        print(f"測試 {i+1} {status} | {res} | {case['expected']}")

if __name__ == "__main__":
    run_test()