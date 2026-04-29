from pathlib import Path
import runpy

"""
優化說明：
- easy 包裝版直接執行主版本解法。
- 可避免重複維護圖演算法邏輯，降低維護成本。
"""


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("10242.py")), run_name="__main__")