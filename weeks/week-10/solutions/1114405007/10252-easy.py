from pathlib import Path
import runpy

"""
優化說明：
- easy 檔案僅作為主版本的輕量啟動器。
- 在避免重複程式碼的同時，確保正確性一致。
"""


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("10252.py")), run_name="__main__")