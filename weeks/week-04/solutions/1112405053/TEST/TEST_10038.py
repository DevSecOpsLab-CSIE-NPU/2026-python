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
    # 假設 TEST_10038.py 在 weeks\week-04\solutions\1112405053\TEST\
    # 而 10038_AI.py 在 weeks\week-04\solutions\1112405053\
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_script = os.path.join(current_dir, '..', '10038_AI.py')
    target_script = os.path.abspath(target_script)

    log_dir = os.path.join(current_dir, 'TEST_LOG')
    os.makedirs(log_dir, exist_ok=True)
    sys.stdout = DualLogger(os.path.join(log_dir, f"{os.path.splitext(os.path.basename(__file__))[0]}.log"))

    print(f"測試目標: {target_script}")
    
    # 準備 5 組不同的測試輸入資料
    test_cases = [
        ("4 1 4 2 3", "測試 1: 4 1 4 2 3 (Jolly)"),
        ("5 1 4 2 -1 6", "測試 2: 5 1 4 2 -1 6 (Not jolly)"),
        ("3 1 2 4", "測試 3: 差值包含 1, 2 (Jolly)"),
        ("2 1 5", "測試 4: 差值 4, 應為 1 (Not jolly)"),
        ("1 100", "測試 5: 單元素序列 (Jolly)")
    ]

    results = []

    # 執行 5 次
    for i, (input_data, desc) in enumerate(test_cases, 1):
        print(f"\n[{i}/5] 執行測試 ({desc})")
        print(f"   輸入: {input_data}")
        
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
                "input": input_data,
                "description": desc,
                "duration": f"{duration:.4f}s",
                "output": output,
                "status": "Success"
            }
            results.append(result_record)
            
            print(f"   執行完成 (耗時: {duration:.4f}s)")
            print(f"   輸出結果: {output}")
            
        except subprocess.CalledProcessError as e:
            print(f"   執行錯誤 (Exit Code: {e.returncode})")
            print(f"   錯誤訊息: {e.stderr}")
            results.append({
                "iteration": i,
                "input": input_data,
                "description": desc,
                "status": "Failed",
                "error": e.stderr
            })
            
    # 輸出總結報告
    print("\n" + "="*80)
    print(f"{'Run':<4} | {'Input':<20} | {'Output':<15} | {'Duration'}")
    print("-" * 80)
    
    for res in results:
        if res["status"] == "Success":
            print(f"#{res['iteration']:<3} | {res['input']:<20} | {res['output']:<15} | {res['duration']}")
        else:
            print(f"#{res['iteration']:<3} | {res['input']:<20} | {'FAILED':<15} | -")
    print("="*80)

if __name__ == "__main__":
    run_test()
