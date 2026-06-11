import subprocess
import sys


# 本測試檔會啟動完整版程式（uva_11417_gcd_full.py），將 sample 輸入傳入並比對輸出
def run(input_data):
    p = subprocess.Popen([sys.executable, 'uva_11417_gcd_full.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate(input_data)
    return out.strip()


def test_sample():
    # UVA 11417 的 sample 測資
    inp = '10\n100\n500\n0\n'
    expected = '67\n13015\n442011'
    assert run(inp) == expected


if __name__ == '__main__':
    test_sample()
    print('11417 sample passed')
