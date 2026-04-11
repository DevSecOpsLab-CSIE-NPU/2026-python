import sys
from io import StringIO

# 1. 模擬題目提供的範例輸入
sample_input = """3
This is a test.
Hello World!
Good stuff.
"""

# 2. 預期的標準輸出結果 (根據範例統計)
# 注意：這裡只列出前幾名作為比對基準
expected_output = """S 4
T 4
O 3
D 2
E 2
H 2
L 2
I 2
A 1
F 1
G 1
R 1
U 1
W 1
"""

def run_test(filename):
    print(f"【測試檔案: {filename}】")
    
    # 備份原本的輸入輸出
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    
    # 設定模擬環境
    sys.stdin = StringIO(sample_input)
    output_buffer = StringIO()
    sys.stdout = output_buffer
    
    try:
        # 讀取並執行目標檔案
        with open(filename, "r", encoding="utf-8") as f:
            exec(f.read(), {'__name__': '__main__'})
        
        # 獲取程式輸出的內容
        actual_output = output_buffer.getvalue()
        
        # 還原輸出到螢幕
        sys.stdout = original_stdout
        
        # 進行比對 (忽略前後空白)
        if actual_output.strip() == expected_output.strip():
            print("✅ 測試通過 (PASS)")
        else:
            print("❌ 測試失敗 (FAIL)")
            print(f"--- 預期輸出 ---\n{expected_output}")
            print(f"--- 實際輸出 ---\n{actual_output}")
            
    except Exception as e:
        sys.stdout = original_stdout
        print(f"💥 發生錯誤: {e}")
    finally:
        sys.stdin = original_stdin
        sys.stdout = original_stdout
    print("-" * 30)

if __name__ == "__main__":
    # 自動跑遍三個主程式檔案
    target_files = ["main.py", "main-easy.py", "main-handwritten.py"]
    for file in target_files:
        run_test(file)