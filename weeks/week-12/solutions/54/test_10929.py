"""
測試 10929_hand.py 的腳本（繁體中文註解）。
會執行幾個範例並把輸出寫入 10929_log.txt
"""
import subprocess
import sys
import os

def run_test():
    sample = """1
11
121
123456789
0
"""
    module_path = os.path.dirname(__file__)
    script = os.path.join(module_path, '10929_hand.py')
    proc = subprocess.run([sys.executable, script], input=sample, text=True, capture_output=True)
    out = proc.stdout.strip()
    log_path = os.path.join(module_path, '10929_log.txt')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(out + '\n')
    print('Wrote', log_path)

if __name__ == '__main__':
    run_test()
