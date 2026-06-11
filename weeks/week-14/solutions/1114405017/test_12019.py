import subprocess
import sys


def run(input_data):  # 本測試檔為示範用，會啟動 uva_12019_doomsday_full.py 並列印輸出
    p = subprocess.Popen([sys.executable, 'uva_12019_doomsday_full.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(input_data)
    return out.strip()


if __name__ == '__main__':
    # basic smoke test（3 個樣例）
    inp = '3\n1 1\n3 14\n12 25\n'
    print(run(inp))
