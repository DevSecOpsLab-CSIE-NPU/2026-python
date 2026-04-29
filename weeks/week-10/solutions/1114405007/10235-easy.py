from pathlib import Path
import runpy

"""
優化說明：
- easy 版本改為委派給主版本執行。
- 只保留一份核心邏輯，可避免兩份實作逐漸不一致。
"""


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("10235.py")), run_name="__main__")