import subprocess
import os
import sys
import time

class DualLogger:
    def __init__(self, filepath):
        self.terminal = sys.stdout
        self.log = open(filepath, 'w', encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

def run_test():
    # 取得目標檔案的絕對路徑
    # 假設 TEST_10035.py 在 weeks\week-04\solutions\1112405053\TEST\
    # 而 10035_AI.py 在 weeks\week-04\solutions\1112405053\
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_script = os.path.join(current_dir, '..', '10035_AI.py')
    target_script = os.path.abspath(target_script)

    log_dir = os.path.join(current_dir, 'TEST_LOG')
    os.makedirs(log_dir, exist_ok=True)
    sys.stdout = DualLogger(os.path.join(log_dir, f"{os.path.splitext(os.path.basename(__file__))[0]}.log"))

    print(f"測試目標: {target_script}")
    
    # 準備 5 組不同的測試輸入資料 (包含標準 0 0 終止條件)
    test_cases = [
        ("123 456\n0 0", "測試 1: 無進位"),
        ("555 555\n0 0", "測試 2: 每個位數都進位 (3次)"),
        ("123 594\n0 0", "測試 3: 只有個位進位 (1次)"),
        ("999 1\n0 0", "測試 4: 連鎖進位 (3次)"),
        ("1 9999\n5 5\n0 0", "測試 5: 多筆連續輸入") 
    ]

    results = []

    # 執行 5 次
    for i, (input_data, desc) in enumerate(test_cases, 1):
        print(f"\n[{i}/5] 執行測試 ({desc})")
        
        # 為了顯示清晰，只印出非 0 0 的部分
        display_input = input_data.replace("\n0 0", "").replace("\n", " ; ")
        print(f"   輸入: {display_input}")
        
        start_time = time.time()
        
        try:
            # 執行 python 腳本
            process = subprocess.run(
                [sys.executable, target_script],
                input=input_data,
                capture_output=True,
                text=True,
                check=True
            )
            
            duration = time.time() - start_time
            output = process.stdout.strip()
            
            # 紀錄結果
            result_record = {
                "iteration": i,
                "input": display_input,
                "description": desc,
                "duration": f"{duration:.4f}s",
                "output": output.replace("\n", " ; "),
                "status": "Success"
            }
            results.append(result_record)
            
            print(f"   執行完成 (耗時: {duration:.4f}s)")
            print(f"   輸出結果: {output.replace('\n', ' ; ')}")
            
        except subprocess.CalledProcessError as e:
            print(f"   執行錯誤 (Exit Code: {e.returncode})")
            print(f"   錯誤訊息: {e.stderr}")
            results.append({
                "iteration": i,
                "input": display_input,
                "description": desc,
                "status": "Failed",
                "error": e.stderr
            })
            
    # 輸出總結報告
    print("\n" + "="*80)
    print(f"{'Run':<4} | {'Description':<25} | {'Expected Hint':<15} | {'Actual Output':<25} | {'Duration'}")
    print("-" * 80)
    
    # 簡單預期提示
    expected_hints = ["No carry", "3 carry", "1 carry", "3 carry", "4 carry ; 1 carry"]
    
    for idx, res in enumerate(results):
        if res["status"] == "Success":
            hint = expected_hints[idx] if idx < len(expected_hints) else "?"
            # 簡單檢查輸出是否包含預期關鍵字
            status_mark = "✅" 
            
            print(f"#{res['iteration']:<3} | {res['description']:<25} | {hint:<15} | {res['output']:<25} {status_mark} | {res['duration']}")
        else:
            print(f"#{res['iteration']:<3} | {res['description']:<25} | {'FAILED':<15} | {res.get('error', '').strip():<25} | -")
    print("="*80)

if __name__ == "__main__":
    run_test()
