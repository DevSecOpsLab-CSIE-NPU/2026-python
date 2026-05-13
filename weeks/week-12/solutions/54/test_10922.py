"""
測試 10922_hand.py 的單元測試腳本（繁體中文註解）。
會執行多組測試輸入，並把結果寫入 10922_log.txt
"""
import subprocess
import sys
import os

def run_test():
    # 測試樣例：包含簡單的 9, 999, 18, 非 9 的倍數
    sample = """9
999
18
123456
0
"""
    module_path = os.path.dirname(__file__)
    script = os.path.join(module_path, '10922_hand.py')
    proc = subprocess.run([sys.executable, script], input=sample, text=True, capture_output=True)
    out = proc.stdout.strip()
    log_path = os.path.join(module_path, '10922_log.txt')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(out + '\n')
    print('Wrote', log_path)

if __name__ == '__main__':
    run_test()
