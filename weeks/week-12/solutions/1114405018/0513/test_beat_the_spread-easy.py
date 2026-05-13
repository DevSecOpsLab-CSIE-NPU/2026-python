"""
UVA 10812 — Beat the Spread! 簡易版測試

簡單易懂的測試方式
"""

import subprocess
import sys


def test_case(S, D, expected):
    """
    測試單個案例
    
    參數:
        S: 分數之和
        D: 分數之差
        expected: 預期輸出
    """
    # 建立輸入
    input_data = f"1\n{S} {D}\n"
    
    # 執行程式
    result = subprocess.run(
        [sys.executable, "10812beat_the_spread-easy.py"],
        input=input_data,
        capture_output=True,
        text=True
    )
    
    # 取得輸出（去掉換行符）
    output = result.stdout.strip()
    
    # 檢查結果
    passed = output == expected
    status = "✓" if passed else "✗"
    
    print(f"{status} S={S}, D={D}: {output} (期望: {expected})")
    
    return passed


# 執行所有測試
print("=" * 50)
print("UVA 10812 — Beat the Spread! 簡易測試")
print("=" * 50)
print()

test_results = []

# 正常情況
print("【正常情況】")
test_results.append(test_case(40, 20, "30 10"))
test_results.append(test_case(100, 50, "75 25"))
test_results.append(test_case(10, 4, "7 3"))

# 邊界情況
print("\n【邊界情況】")
test_results.append(test_case(0, 0, "0 0"))
test_results.append(test_case(20, 20, "20 0"))
test_results.append(test_case(50, 0, "25 25"))

# 無解情況
print("\n【無解情況】")
test_results.append(test_case(20, 40, "impossible"))
test_results.append(test_case(15, 10, "impossible"))
test_results.append(test_case(5, 15, "impossible"))

# 統計結果
print()
print("=" * 50)
passed_count = sum(test_results)
total_count = len(test_results)
print(f"測試結果: {passed_count}/{total_count} 通過")
print("=" * 50)

if passed_count == total_count:
    print("✓ 全部測試通過！")
    sys.exit(0)
else:
    print("✗ 有測試失敗")
    sys.exit(1)
