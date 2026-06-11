import subprocess
import sys
import os


# run_all_tests.py：逐一執行本資料夾內的 test_*.py 文件，方便本地快速驗證
HERE = os.path.dirname(__file__)

TESTS = ['test_11349.py', 'test_11417.py', 'test_11461.py', 'test_12019.py']


if __name__ == '__main__':
    for t in TESTS:
        print('Running', t)
        # 在此資料夾下執行測試檔，並捕獲 stdout/stderr
        p = subprocess.Popen([sys.executable, t], cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, err = p.communicate()
        print(out)
        if err:
            print('ERR:', err)
