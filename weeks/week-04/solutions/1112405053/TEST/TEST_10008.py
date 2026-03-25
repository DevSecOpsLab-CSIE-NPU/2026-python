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
    # 假設 TEST_10008.py 在 weeks\week-04\solutions\1112405053\TEST\
    # 而 10008_AI.py 在 weeks\week-04\solutions\1112405053\
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_script = os.path.join(current_dir, '..', '10008_AI.py')
    target_script = os.path.abspath(target_script)

    log_dir = os.path.join(current_dir, 'TEST_LOG')
    os.makedirs(log_dir, exist_ok=True)
    sys.stdout = DualLogger(os.path.join(log_dir, f"{os.path.splitext(os.path.basename(__file__))[0]}.log"))

    print(f"測試目標: {target_script}")
    
    # 準備 5 組不同的測試輸入資料
    test_inputs = [
        "world",
        "C++",
        "Python",
        "ZeroJudge",
        "12345"
    ]

    results = []

    # 執行 5 次
    for i, input_str in enumerate(test_inputs, 1):
        print(f"\n[{i}/5] 測試輸入: {input_str}")
        start_time = time.time()
        
        try:
            # 執行 python 腳本
            process = subprocess.run(
                [sys.executable, target_script],
                input=input_str,
                capture_output=True,
                text=True,
                check=True
            )
            
            duration = time.time() - start_time
            output = process.stdout.strip()
            
            # 紀錄結果
            result_record = {
                "iteration": i,
                "input": input_str,
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
                "input": input_str,
                "status": "Failed",
                "error": e.stderr
            })
            
    # 輸出總結報告
    print("\n" + "="*50)
    print(f"{'Run':<5} | {'Input':<15} | {'Status':<10} | {'Duration':<10} | {'Output'}")
    print("-" * 50)
    for res in results:
        if res["status"] == "Success":
            print(f"#{res['iteration']:<4} | {res['input']:<15} | {res['status']:<10} | {res['duration']:<10} | {res['output']}")
        else:
            print(f"#{res['iteration']:<4} | {res['input']:<15} | {res['status']:<10} | {'-':<10} | Error: {res.get('error', '').strip()}")
    print("="*50)

if __name__ == "__main__":
    run_test()
