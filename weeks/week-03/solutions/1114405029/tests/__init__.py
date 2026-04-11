# 這個檔案讓 Python 將 tests 資料夾視為一個 package
# 確保在執行單元測試時，模組導入路徑能正確被識別

import os
import sys

# 為了方便測試腳本直接運行，這裡可以確保根目錄被加入 sys.path
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_path not in sys.path:
    sys.path.append(root_path)