"""
測試 10931_hand.py，將範例輸出寫入 10931_log.txt
"""
import subprocess
import sys
import os

def run_test():
    sample_input = """1
2
10
21
0
"""
    module_path = os.path.dirname(__file__)
    script = os.path.join(module_path, '10931_hand.py')
    proc = subprocess.run([sys.executable, script], input=sample_input, text=True, capture_output=True)
    out = proc.stdout.strip()
    log_path = os.path.join(module_path, '10931_log.txt')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(out + '\n')
    print('Wrote', log_path)

if __name__ == '__main__':
    run_test()
