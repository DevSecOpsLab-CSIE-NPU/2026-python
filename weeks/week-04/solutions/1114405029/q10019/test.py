import sys
from io import StringIO

# 1. 定義題目給的測試輸入 (範例)
sample_input = """10 12
100 200
10 1
"""

# 2. 定義預期的標準輸出
expected_output = """2
100
9
"""

def run_test(filename):
    print(f"【開始測試檔案: {filename}】")
    
    # 備份原本的系統輸入輸出
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    
    # 模擬輸入與攔截輸出
    sys.stdin = StringIO(sample_input)
    output_buffer = StringIO()
    sys.stdout = output_buffer
    
    try:
        # 執行程式碼
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
            # 模擬執行程式，環境設定為 __main__
            exec(code, {'__name__': '__main__'})
        
        # 取得執行後的結果
        actual_output = output_buffer.getvalue()
        
        # 還原輸出，準備印出比對結果
        sys.stdout = original_stdout
        
        # 去掉頭尾空白進行比對
        if actual_output.strip() == expected_output.strip():
            print("✅ 測試結果：完全正確 (PASS)")
        else:
            print("❌ 測試結果：錯誤 (FAIL)")
            print(f"--- 預期內容 ---\n{expected_output}")
            print(f"--- 實際內容 ---\n{actual_output}")
            
    except Exception as e:
        sys.stdout = original_stdout
        print(f"💥 執行時發生錯誤: {e}")
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout
    print("-" * 30)

if __name__ == "__main__":
    # 一次測試三個版本
    files_to_test = ["main.py", "main-easy.py", "main-handwritten.py"]
    for file in files_to_test:
        run_test(file)