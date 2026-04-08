from __future__ import annotations

import io
import pathlib
import sys
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent
LOG_PATH = BASE_DIR / "unit_test_record.txt"


def main() -> int:
    """
    這支腳本會：
    1. 自動探索目前資料夾內所有 test_*.py。
    2. 執行 unittest。
    3. 把完整紀錄寫入 unit_test_record.txt，方便保留作業證明。
    """
    loader = unittest.defaultTestLoader
    suite = loader.discover(str(BASE_DIR), pattern="test_*.py")
    buffer = io.StringIO()
    runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
    result = runner.run(suite)

    report_lines = [
        "Python unittest 測試紀錄",
        f"總測試數量: {result.testsRun}",
        f"失敗數量: {len(result.failures)}",
        f"錯誤數量: {len(result.errors)}",
        "",
        buffer.getvalue().rstrip(),
        "",
        f"整體結果: {'PASS' if result.wasSuccessful() else 'FAIL'}",
    ]
    LOG_PATH.write_text("\n".join(report_lines).rstrip() + "\n", encoding="utf-8")
    sys.stdout.write(LOG_PATH.read_text(encoding="utf-8"))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())