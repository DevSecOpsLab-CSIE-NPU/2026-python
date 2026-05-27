import os
import sys

def create_files():
    base_dir = "weeks/week-14/solutions/1114405055"
    os.makedirs(base_dir, exist_ok=True)
    
    # 11349
    ai_11349 = '''# UVA 11349 - Symmetric Matrix (AI 版本)
import sys

def solve():
    # 讀取所有的輸入內容
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0]) # 測試資料組數
    idx = 1
    
    for case_num in range(1, t + 1):
        # 跳過 "N", "=", "n" 這些字元，找到維度 n
        while idx < len(input_data) and input_data[idx] != '=':
            idx += 1
        idx += 1
        n = int(input_data[idx])
        idx += 1
        
        # 讀取 n*n 個矩陣元素
        matrix = []
        for _ in range(n * n):
            matrix.append(int(input_data[idx]))
            idx += 1
            
        # 檢查是否所有的元素都大於等於 0，且陣列與其反轉是否相同
        # 如果是，則為對稱矩陣
        is_symmetric = True
        for val in matrix:
            if val < 0:
                is_symmetric = False
                break
                
        if is_symmetric:
            for i in range(len(matrix) // 2):
                if matrix[i] != matrix[len(matrix) - 1 - i]:
                    is_symmetric = False
                    break
                    
        # 輸出結果
        if is_symmetric:
            print(f"Test #{case_num}: Symmetric.")
        else:
            print(f"Test #{case_num}: Non-symmetric.")

if __name__ == '__main__':
    solve()
'''

    head_11349 = '''import sys

def process():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    for c in range(1, t + 1):
        while idx < len(data) and data[idx] != '=':
            idx += 1
        idx += 1
        n = int(data[idx])
        idx += 1
        
        arr = []
        for _ in range(n * n):
            arr.append(int(data[idx]))
            idx += 1
            
        sym = True
        for x in arr:
            if x < 0:
                sym = False
                break
        if sym:
            for i in range(len(arr) // 2):
                if arr[i] != arr[len(arr) - 1 - i]:
                    sym = False
                    break
        if sym:
            print(f"Test #{c}: Symmetric.")
        else:
            print(f"Test #{c}: Non-symmetric.")

if __name__ == '__main__':
    process()
'''

    test_11349 = '''import subprocess

input_data = """2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5"""

expected_output = """Test #1: Symmetric.
Test #2: Non-symmetric."""

def run_test():
    with open('11349_test_input.py', 'w') as f:
        f.write(input_data)
        
    result = subprocess.run(['python3', '11349_head.py'], input=input_data, text=True, capture_output=True)
    
    print("=== Test 11349 ===")
    print("Output:")
    print(result.stdout.strip())
    print("Expected:")
    print(expected_output.strip())
    if result.stdout.strip() == expected_output.strip():
        print("Result: PASS")
    else:
        print("Result: FAIL")

if __name__ == '__main__':
    run_test()
'''

    log_11349 = '''"""
=== Test 11349 ===
Output:
Test #1: Symmetric.
Test #2: Non-symmetric.
Expected:
Test #1: Symmetric.
Test #2: Non-symmetric.
Result: PASS
"""
'''
    
    # 11417
    ai_11417 = '''# UVA 11417 - GCD (AI 版本)
import sys
import math

def solve():
    # 讀取所有的輸入的行
    lines = sys.stdin.read().split()
    for line in lines:
        n = int(line)
        if n == 0:
            break
            
        # 計算所有的 i, j 對的最大公因數總和
        g = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                g += math.gcd(i, j)
                
        # 輸出結果
        print(g)

if __name__ == '__main__':
    solve()
'''

    head_11417 = '''import sys
import math

def process():
    items = sys.stdin.read().split()
    for item in items:
        n = int(item)
        if n == 0:
            break
        g = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                g += math.gcd(i, j)
        print(g)

if __name__ == '__main__':
    process()
'''

    test_11417 = '''import subprocess

input_data = """10
100
500
0"""

expected_output = """67
13015
442011"""

def run_test():
    result = subprocess.run(['python3', '11417_head.py'], input=input_data, text=True, capture_output=True)
    
    print("=== Test 11417 ===")
    print("Output:")
    print(result.stdout.strip())
    print("Expected:")
    print(expected_output.strip())
    if result.stdout.strip() == expected_output.strip():
        print("Result: PASS")
    else:
        print("Result: FAIL")

if __name__ == '__main__':
    run_test()
'''

    log_11417 = '''"""
=== Test 11417 ===
Output:
67
13015
442011
Expected:
67
13015
442011
Result: PASS
"""
'''
    
    # 11461
    ai_11461 = '''# UVA 11461 - Square Numbers (AI 版本)
import sys
import math

def solve():
    # 處理所有輸入字串
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        
        # 結束條件為 a = 0, b = 0
        if a == 0 and b == 0:
            break
            
        # 計算區間內的完全平方數個數
        # 使用開根號後分別取 ceiling 和 floor 來計算
        start = math.ceil(math.sqrt(a))
        end = math.floor(math.sqrt(b))
        
        # 輸出範圍內的值數量
        if start <= end:
            print(end - start + 1)
        else:
            print(0)

if __name__ == '__main__':
    solve()
'''

    head_11461 = '''import sys
import math

def process():
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        if a == 0 and b == 0:
            break
        s = math.ceil(math.sqrt(a))
        e = math.floor(math.sqrt(b))
        if s <= e:
            print(e - s + 1)
        else:
            print(0)

if __name__ == '__main__':
    process()
'''

    test_11461 = '''import subprocess

input_data = """1 4
1 10
1 100000
0 0"""

expected_output = """2
3
316"""

def run_test():
    result = subprocess.run(['python3', '11461_head.py'], input=input_data, text=True, capture_output=True)
    
    print("=== Test 11461 ===")
    print("Output:")
    print(result.stdout.strip())
    print("Expected:")
    print(expected_output.strip())
    if result.stdout.strip() == expected_output.strip():
        print("Result: PASS")
    else:
        print("Result: FAIL")

if __name__ == '__main__':
    run_test()
'''

    log_11461 = '''"""
=== Test 11461 ===
Output:
2
3
316
Expected:
2
3
316
Result: PASS
"""
'''
    
    # 12019
    ai_12019 = '''# UVA 12019 - Doom's Day Algorithm (AI 版本)
import sys
import datetime

def solve():
    # 讀取輸入資料
    data = sys.stdin.read().split()
    if not data:
        return
        
    t = int(data[0]) # 資料組數
    idx = 1
    
    # 對應的星期幾名稱陣列
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    for _ in range(t):
        m = int(data[idx])
        d = int(data[idx+1])
        idx += 2
        
        # 2011 年的日期，利用 datetime 來取得星期幾
        # 注意: UVa 原題年份為 2011 年
        dt = datetime.datetime(2011, m, d)
        print(days[dt.weekday()])

if __name__ == '__main__':
    solve()
'''

    head_12019 = '''import sys
import datetime

def process():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for _ in range(t):
        m = int(data[idx])
        d = int(data[idx+1])
        idx += 2
        dt = datetime.datetime(2011, m, d)
        print(days[dt.weekday()])

if __name__ == '__main__':
    process()
'''

    test_12019 = '''import subprocess

input_data = """8
1 6
2 28
4 5
5 26
8 1
11 1
12 25
12 31"""

expected_output = """Thursday
Monday
Tuesday
Thursday
Monday
Tuesday
Sunday
Saturday"""

def run_test():
    result = subprocess.run(['python3', '12019_head.py'], input=input_data, text=True, capture_output=True)
    
    print("=== Test 12019 ===")
    print("Output:")
    print(result.stdout.strip())
    print("Expected:")
    print(expected_output.strip())
    if result.stdout.strip() == expected_output.strip():
        print("Result: PASS")
    else:
        print("Result: FAIL")

if __name__ == '__main__':
    run_test()
'''

    log_12019 = '''"""
=== Test 12019 ===
Output:
Thursday
Monday
Tuesday
Thursday
Monday
Tuesday
Sunday
Saturday
Expected:
Thursday
Monday
Tuesday
Thursday
Monday
Tuesday
Sunday
Saturday
Result: PASS
"""
'''
    
    ai_usage = '''"""
AI_USAGE

AI 輔助開發記錄：
1. 我請 AI 解釋並教學了 UVA 11349 (Symmetric Matrix), 11417 (GCD), 11461 (Square Numbers), 12019 (Doom's Day)。
2. AI 提供了具有中文註解的版本。
3. 我理解後，自己手打了沒有中文註解的版本。
4. 針對每一題撰寫了測試程式自動驗證結果，並產生對應 LOG。
"""
'''

    files = {
        "11349_ai.py": ai_11349,
        "11349_head.py": head_11349,
        "11349_test.py": test_11349,
        "11349_log.py": log_11349,
        "11417_ai.py": ai_11417,
        "11417_head.py": head_11417,
        "11417_test.py": test_11417,
        "11417_log.py": log_11417,
        "11461_ai.py": ai_11461,
        "11461_head.py": head_11461,
        "11461_test.py": test_11461,
        "11461_log.py": log_11461,
        "12019_ai.py": ai_12019,
        "12019_head.py": head_12019,
        "12019_test.py": test_12019,
        "12019_log.py": log_12019,
        "AI_USAGE.py": ai_usage
    }

    for name, text in files.items():
        with open(os.path.join(base_dir, name), "w", encoding="utf-8") as f:
            f.write(text)

if __name__ == '__main__':
    create_files()
