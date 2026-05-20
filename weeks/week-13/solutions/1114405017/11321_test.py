import subprocess
import sys

# 這裡定義好幾個不同的測試用例，包含基本、斜向、極端狀況
TEST_CASES = [
    {
        "name": "範例 1：直線阻斷測試",
        "input": """3 3 3
0 1
2 1
1 1""",
        "expected": """<(_ _)>
<(_ _)>
>_<"""
    },
    {
        "name": "範例 2：斜向（階梯式）阻斷測試",
        "input": """3 3 3
0 0
2 2
1 1""",
        "expected": """<(_ _)>
<(_ _)>
>_<"""
    },
    {
        "name": "範例 3：極端狀況 N=1（任何陷阱都會斷路）",
        "input": """1 5 2
0 2
0 4""",
        "expected": """>_<
>_<"""
    },
    {
        "name": "範例 4：繞道測試（陷阱沒完全封死）",
        "input": """4 4 4
0 0
1 1
2 2
2 3""",
        "expected": """<(_ _)>
<(_ _)>
<(_ _)>
<(_ _)>"""  # 雖然一路斜上去，但因為最上面 N-1(也就是3) 還沒被放陷阱，人還可以從最上面走過去
    }
]

def run_test():
    target_script = "solution.py"  # 請確保您的主程式檔名是這個
    all_passed = True
    
    print("=" * 50)
    print(" 開始執行自動測試 ")
    print("=" * 50)
    
    for i, case in enumerate(TEST_CASES, 1):
        print(f"運行測試 {i}: {case['name']}...")
        
        try:
            # 執行主程式，並將 input 餵進去
            process = subprocess.Popen(
                [sys.executable, target_script],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate(input=case["input"])
            
            # 清理輸出結尾的換行符號，方便比對
            actual_output = stdout.strip()
            expected_output = case["expected"].strip()
            
            if actual_output == expected_output:
                print("Result: ✅ 通過 (PASSED)")
            else:
                all_passed = False
                print("Result: ❌ 失敗 (FAILED)")
                print(f"--- 預期輸出 ---\n{expected_output}")
                print(f"--- 實際輸出 ---\n{actual_output}")
                if stderr:
                    print(f"--- 錯誤訊息 ---\n{stderr}")
                    
        except FileNotFoundError:
            print(f"❌ 錯誤：找不到主程式檔案 '{target_script}'，請檢查檔名是否正確。")
            return
            
        print("-" * 50)
        
    if all_passed:
        print("🎉 恭喜！所有測試用例皆順利通過！")
    else:
        print("⚠️ 有部分測試未通過，請檢查程式邏輯。")

if __name__ == "__main__":
    run_test()