import subprocess
import sys


# 測試 UVA 11349 的 sample，啟動 full 版本並比對輸出
def run(input_data):
    p = subprocess.Popen([sys.executable, 'uva_11349_symmetric_full.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(input_data)
    return out.strip()


def test_sample():
    inp = '''2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
'''
    expected = 'Test #1: Symmetric.\nTest #2: Non-symmetric.'
    assert run(inp) == expected


if __name__ == '__main__':
    test_sample()
    print('11349 sample passed')
