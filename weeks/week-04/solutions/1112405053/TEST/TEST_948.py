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
    # 假設 TEST_948.py 在 weeks\week-04\solutions\1112405053\TEST\
    # 而 948_AI.py 在 weeks\week-04\solutions\1112405053\
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_script = os.path.join(current_dir, '..', '948_AI.py')
    target_script = os.path.abspath(target_script)

    log_dir = os.path.join(current_dir, 'TEST_LOG')
    os.makedirs(log_dir, exist_ok=True)
    sys.stdout = DualLogger(os.path.join(log_dir, f"{os.path.splitext(os.path.basename(__file__))[0]}.log"))

    print(f"測試目標: {target_script}")
    
    # 準備測試輸入資料 (來自 ZeroJudge c095 範例)
    input_data = """2

5 3
2 1 2 3 4
<
1 1 4
=
1 2 5
=

4 2
1 1 2
<
1 3 4
=
"""

    results = []

    # 執行 5 次
    for i in range(1, 6):
        print(f"\n[{i}/5] 正在執行測試...")
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
                "duration": f"{duration:.4f}s",
                "output": output,
                "status": "Success"
            }
            results.append(result_record)
            
            print(f"   執行完成 (耗時: {duration:.4f}s)")
            print(f"   輸出結果:\n{output}")
            
        except subprocess.CalledProcessError as e:
            print(f"   執行錯誤 (Exit Code: {e.returncode})")
            print(f"   錯誤訊息: {e.stderr}")
            results.append({
                "iteration": i,
                "status": "Failed",
                "error": e.stderr
            })
            
    # 輸出總結報告
    print("\n" + "="*40)
    print("測試總結報告")
    print("="*40)
    for res in results:
        if res["status"] == "Success":
            print(f"Run #{res['iteration']}: {res['status']} ({res['duration']})")
            # print(f"Output: {res['output']}") # 若輸出很長可省略
        else:
            print(f"Run #{res['iteration']}: {res['status']}")

if __name__ == "__main__":
    run_test()
