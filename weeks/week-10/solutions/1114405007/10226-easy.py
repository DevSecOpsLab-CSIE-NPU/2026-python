from pathlib import Path
import runpy

"""
優化說明：
- easy 版本直接重用主版本實作。
- 這樣可以避免重複邏輯，並確保兩個版本行為一致。
"""


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("10226.py")), run_name="__main__")