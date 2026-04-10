# main.py
import os
import sys

# 確保 Python 能找到資料夾模組
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.app import BigTwoApp

if __name__ == "__main__":
    app = BigTwoApp()
    app.run()