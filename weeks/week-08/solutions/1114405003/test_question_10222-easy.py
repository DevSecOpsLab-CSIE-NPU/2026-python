import os
import subprocess
import sys
import unittest
from pathlib import Path


# ============================================================
# 10222 好記版：
# - 直接跑解答程式，驗證輸出是否等於預期解碼結果
# - 再用一個參考解碼函式交叉驗證
# ============================================================


def find_target_script() -> Path:
    """找 10222 解答檔，找不到就跳過。"""
    custom_path = os.environ.get("TARGET_10222")
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p

    folder = Path(__file__).resolve().parent
    names = [
        "QUESTION-10222-手打.py",
        "QUESTION-10222.py",
        "question_10222.py",
        "uva10222.py",
        "10222.py",
        "solution_10222.py",
    ]
    for name in names:
        p = folder / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10222 解答檔，請放同資料夾或設定 TARGET_10222")


def run_program(input_text: str) -> str:
    """執行目標程式並回傳輸出。"""
    script = find_target_script()
    result = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def decode_reference(text: str) -> str:
    """參考解碼器（依 UVA 常見做法：字元映射到鍵盤左兩格）。"""
    keyboard = "`1234567890-=WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./"
    table = {}
    for i in range(2, len(keyboard)):
        table[keyboard[i]] = keyboard[i - 2]

    out = []
    for ch in text:
        up = ch.upper()
        if up in table:
            out.append(table[up])
        else:
            out.append(ch)
    return "".join(out)


class Test10222Easy(unittest.TestCase):
    """UVA 10222（Decode the Mad man）好記版測試。"""

    def test_known_sentence(self):
        # 這組是常見示例，能快速確認映射方向正確。
        input_text = "O S, GOMR YPFSU/\n"
        expected = "I AM FINE TODAY.\n"
        actual = run_program(input_text)
        self.assertEqual(actual, expected)

    def test_simple_word(self):
        # 使用參考函式產生預期答案，降低手算錯字風險。
        input_text = "YHOO\n"
        expected = decode_reference(input_text)
        actual = run_program(input_text)
        self.assertEqual(actual, expected)

    def test_with_punctuation(self):
        # 測試空白與標點是否一併正確處理。
        input_text = "Jr;;p Ept;f\n"
        expected = decode_reference(input_text)
        actual = run_program(input_text)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
