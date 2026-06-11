import subprocess
import sys


# 測試 UVA 11461 的 sample，呼叫完整版本並比對輸出
def run(input_data):
    p = subprocess.Popen([sys.executable, 'uva_11461_squares_full.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(input_data)
    return out.strip()


def test_sample():
    inp = '1 4\n1 10\n1 100000\n0 0\n'
    expected = '2\n3\n316'
    assert run(inp) == expected


if __name__ == '__main__':
    test_sample()
    print('11461 sample passed')
