from pathlib import Path
import runpy

"""
優化說明：
- easy 包裝版直接執行主版本程式。
- 避免維護兩份獨立 DP 實作。
"""


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("10268.py")), run_name="__main__")