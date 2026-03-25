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
    # 假設 TEST_10019.py 在 weeks\week-04\solutions\1112405053\TEST\
    # 而 10019_AI.py 在 weeks\week-04\solutions\1112405053\
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_script = os.path.join(current_dir, '..', '10019_AI.py')
    target_script = os.path.abspath(target_script)

    log_dir = os.path.join(current_dir, 'TEST_LOG')
    os.makedirs(log_dir, exist_ok=True)
    sys.stdout = DualLogger(os.path.join(log_dir, f"{os.path.splitext(os.path.basename(__file__))[0]}.log"))

    print(f"測試目標: {target_script}")
    
    # 準備 5 組不同的測試輸入資料 (每組一個字串，模擬一次執行)
    test_cases = [
        ("10 12", "範例 1: Hashmat < Enemy"),
        ("14 10", "範例 2: Hashmat > Enemy"),
        ("100 200", "測試 3: 差距較大"),
        ("5 5", "測試 4: 兩者相等"),
        ("0 1000000", "測試 5: 其中一方為 0")
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
    print(f"{'Run':<4} | {'Input':<15} | {'Expected Output':<20} | {'Actual Output':<15} | {'Duration'}")
    print("-" * 80)
    
    # 預期輸出簡單計算
    for res in results:
        if res["status"] == "Success":
            # 簡單計算預期結果以供比較
            try:
                nums = list(map(int, res['input'].split()))
                expected = str(abs(nums[0] - nums[1]))
            except:
                expected = "?"
                
            status_mark = "✅" if res['output'] == expected else "❌"
            
            print(f"#{res['iteration']:<3} | {res['input']:<15} | {expected:<20} | {res['output']:<15} {status_mark} | {res['duration']}")
        else:
            print(f"#{res['iteration']:<3} | {res['input']:<15} | {'FAILED':<20} | {res.get('error', '').strip():<15} | -")
    print("="*80)

if __name__ == "__main__":
    run_test()
