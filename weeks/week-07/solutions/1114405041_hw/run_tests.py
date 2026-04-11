from __future__ import annotations

import io
import pathlib
import sys
import unittest


BASE_DIR = pathlib.Path(__file__).resolve().parent
LOG_PATH = BASE_DIR / "TEST_LOG.md"


def main() -> int:
    loader = unittest.defaultTestLoader
    suite = loader.discover(str(BASE_DIR), pattern="test_chibi.py")
    buffer = io.StringIO()
    runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
    result = runner.run(suite)

    report_lines = [
        "# 赤壁戰役 - 測試執行日誌",
        "",
        f"- 測試時間：由 run_tests.py 自動產生",
        f"- 總測試數量：{result.testsRun}",
        f"- 失敗數量：{len(result.failures)}",
        f"- 錯誤數量：{len(result.errors)}",
        "",
        "```text",
        buffer.getvalue().rstrip(),
        "```",
        "",
        f"整體結果：{'PASS' if result.wasSuccessful() else 'FAIL'}",
    ]
    LOG_PATH.write_text("\n".join(report_lines).rstrip() + "\n", encoding="utf-8")
    sys.stdout.write(LOG_PATH.read_text(encoding="utf-8"))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())