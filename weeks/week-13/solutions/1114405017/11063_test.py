import io
import sys

# --- 這裡放你剛剛寫好、要測試的解題程式 (稍微包裝成函式) ---
def run_solution(input_string):
    """
    這個函式負責模擬系統輸入，並抓取程式的標準輸出。
    """
    # 備份原本的系統輸入與輸出
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    
    # 用 StringIO 模擬輸入與攔截輸出
    sys.stdin = io.StringIO(input_string.strip())
    sys.stdout = io.StringIO()
    
    try:
        # ---- 這裡就是你原本的解題程式碼內容 ----
        data = sys.stdin.read().split()
        if data:
            n = int(data[0])
            total_pixels = n * n
            sum_y = 0.0
            inputs = iter(data[1:])
            
            for _ in range(total_pixels):
                r = float(next(inputs))
                g = float(next(inputs))
                b = float(next(inputs))
                
                x = 0.5149 * r + 0.3244 * g + 0.1607 * b
                y = 0.2654 * r + 0.6704 * g + 0.0642 * b
                z = 0.0248 * r + 0.1248 * g + 0.8504 * b
                
                sum_y += y
                print(f"{x:.4f} {y:.4f} {z:.4f}")
                
            print(f"The average of Y is {sum_y / total_pixels:.4f}")
        # ----------------------------------------
        
        # 抓取程式印出來的所有內容
        result = sys.stdout.getvalue()
    finally:
        # 測試完畢，把系統的輸入輸出還原
        sys.stdin = old_stdin
        sys.stdout = old_stdout
        
    return result.strip()


# --- 自動化測試主程式 ---
def main():
    # 準備測試題目給的範例，以及我們自己設計的極端狀況
    test_cases = [
        {
            "name": "範例測資 (2x2 影像)",
            "input": """
                2
                255 3 192 0 0 0
                128 128 128 255 255 255
            """,
            "expected": (
                "162.1323 69.8966 221.5476\n"
                "0.0000 0.0000 0.0000\n"
                "128.0000 128.0000 128.0000\n"
                "255.0000 255.0000 255.0000\n"
                "The average of Y is 113.2241"
            )
        },
        {
            "name": "邊界測試 (全黑 1x1)",
            "input": """
                1
                0 0 0
            """,
            "expected": (
                "0.0000 0.0000 0.0000\n"
                "The average of Y is 0.0000"
            )
        }
    ]
    
    print("=" * 40)
    print("開始執行自動化測試...")
    print("=" * 40)
    
    all_pass = True
    for i, case in enumerate(test_cases, 1):
        print(f"測試項目 {i}: {case['name']}")
        
        # 執行程式拿到實際輸出
        actual = run_solution(case["input"])
        expected = case["expected"].strip()
        
        # 比對結果
        if actual == expected:
            print("  👉 狀態: [ 成功 PASS ]")
        else:
            print("  👉 狀態: [ 失敗 FAIL ] ❌")
            print(f"  -- 預期輸出 --\n{expected}")
            print(f"  -- 你的輸出 --\n{actual}")
            all_pass = False
        print("-" * 40)
        
    if all_pass:
        print("🎉 太棒了！所有測試全部通過！")
    else:
        print("⚠️ 有些測資沒過，再檢查看看公式或空白格式喔！")

if __name__ == "__main__":
    main()