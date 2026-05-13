"""
測試 10812_hand.py 的簡單測試腳本，會把輸出寫入 10812_log.txt
使用 subprocess 執行手寫程式並傳入範例輸入。
"""
import subprocess
import sys
import os

def run_test():
    sample_input = """2
40 20
20 40
"""
    module_path = os.path.dirname(__file__)
    script = os.path.join(module_path, '10812_hand.py')
    proc = subprocess.run([sys.executable, script], input=sample_input, text=True, capture_output=True)
    out = proc.stdout.strip()
    log_path = os.path.join(module_path, '10812_log.txt')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(out + '\n')
    print('Wrote', log_path)

if __name__ == '__main__':
    run_test()
