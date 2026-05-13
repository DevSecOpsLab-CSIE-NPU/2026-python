"""
測試 10908_hand.py，會使用題目提供的範例輸入，並把輸出寫入 10908_log.txt
（繁體中文註解）
"""
import subprocess
import sys
import os

def run_test():
    # 來自題目範例的輸入
    sample = """1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2
"""
    module_path = os.path.dirname(__file__)
    script = os.path.join(module_path, '10908_hand.py')
    proc = subprocess.run([sys.executable, script], input=sample, text=True, capture_output=True)
    out = proc.stdout.strip()
    log_path = os.path.join(module_path, '10908_log.txt')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(out + '\n')
    print('Wrote', log_path)

if __name__ == '__main__':
    run_test()
