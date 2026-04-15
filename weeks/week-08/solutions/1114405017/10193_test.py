import math

# 這是你原本的解題函式，封裝起來以便測試
def calculate_min_bc(a):
    target = a * a + 1
    # 找最接近根號的因數對
    x = math.isqrt(target)
    while x > 0:
        if target % x == 0:
            y = target // x
            return x + y + 2 * a
        x -= 1
    return None

def run_test():
    # 測試資料清單：(輸入 a, 預期輸出 b+c)
    test_cases = [
        (1, 5),      # 1^2+1=2, 因數(1,2), 1+2+2=5
        (2, 9),      # 2^2+1=5, 因數(1,5), 1+5+4=9
        (3, 16),     # 3^2+1=10, 因數(2,5), 2+5+6=13 (更正: 3^2+1=10, 因數(2,5)最接近, 2+5+6=13)
                     # 注意：(1,10)和是11, (2,5)和是7, 所以取 (2,5)
        (10, 122),   # 10^2+1=101(質數), 因數(1,101), 1+101+20=122
    ]

    print(f"{'輸入 a':<10} | {'預期結果':<10} | {'實際結果':<10} | {'測試狀態'}")
    print("-" * 55)

    passed_count = 0
    for a, expected in test_cases:
        actual = calculate_min_bc(a)
        status = "✅ 通過" if actual == expected else "❌ 失敗"
        if actual == expected:
            passed_count += 1
        
        print(f"{a:<10} | {expected:<10} | {actual:<10} | {status}")

    print("-" * 55)
    print(f"測試完成！總共通過 {passed_count}/{len(test_cases)} 個案例。")

if __name__ == "__main__":
    run_test()