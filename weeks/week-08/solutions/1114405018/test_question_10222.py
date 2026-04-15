import os
import random
import subprocess
import sys
import unittest
from pathlib import Path
import importlib.util


class TestQuestion10222(unittest.TestCase):
    """題目 10222（Decode the Mad man）單元測試。"""

    @classmethod
    def setUpClass(cls):
        # 預設測試同資料夾下的 10222.py，可用 TARGET_FILE 覆蓋
        this_dir = Path(__file__).resolve().parent
        default_target = this_dir / "10222.py"
        target_from_env = os.environ.get("TARGET_FILE", "").strip()
        cls.target_file = Path(target_from_env).resolve() if target_from_env else default_target

        if not cls.target_file.exists():
            raise unittest.SkipTest(
                f"找不到被測試檔案：{cls.target_file}。請建立 10222.py，或設定 TARGET_FILE。"
            )

        cls.target_module = cls._try_load_module(cls.target_file)

    @staticmethod
    def _try_load_module(file_path: Path):
        # 先嘗試直接匯入，方便測試已封裝成函式的版本
        try:
            spec = importlib.util.spec_from_file_location("target_10222", file_path)
            if spec is None or spec.loader is None:
                return None
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception:
            return None

    @staticmethod
    def _keyboard_map():
        # 以題目中的 QWERTY 鍵盤為基準，建立「左邊一格」對照表
        rows = [
            "`1234567890-=",
            "qwertyuiop[]\\",
            "asdfghjkl;'",
            "zxcvbnm,./",
        ]

        mapping = {" ": " "}
        for row in rows:
            for i in range(1, len(row)):
                mapping[row[i]] = row[i - 1]
        return mapping

    @staticmethod
    def _build_input(lines):
        # lines 格式：['encoded line 1', 'encoded line 2', ...]
        return "\n".join(lines) + "\n"

    @classmethod
    def _reference_decode(cls, lines):
        # 逐字元做鍵盤對照，這就是題目的核心規則
        mapping = cls._keyboard_map()
        decoded_lines = []
        for line in lines:
            decoded_lines.append("".join(mapping.get(ch, ch) for ch in line))
        return "\n".join(decoded_lines) + "\n"

    @staticmethod
    def _parse_output(text):
        # 題目是純文字輸出，直接保留換行比較最準
        if text == "":
            raise AssertionError("輸出為空，預期應輸出解碼後的文字")
        return text

    def _run_target(self, lines):
        input_data = self._build_input(lines)
        module = self.target_module

        # 優先測試常見函式名稱；若沒有，就改走標準輸入輸出模式
        if module is not None:
            for fn_name in ("solve", "decode", "decode_mad_man", "solve_case"):
                if hasattr(module, fn_name):
                    fn = getattr(module, fn_name)
                    try:
                        result = fn(lines)
                    except TypeError:
                        result = fn(input_data)

                    if isinstance(result, str):
                        return result
                    if result is not None:
                        return str(result)

            if hasattr(module, "main"):
                fn = getattr(module, "main")
                try:
                    result = fn()
                except TypeError:
                    result = fn(input_data)

                if isinstance(result, str):
                    return result
                if result is not None:
                    return str(result)

        completed = subprocess.run(
            [sys.executable, str(self.target_file)],
            input=input_data,
            text=True,
            capture_output=True,
            check=True,
        )
        return self._parse_output(completed.stdout)

    def test_sample_like_case(self):
        # 用幾個常見字元組成的句子，確認基本位移與空白都正確
        lines = [
            "rty uio",
            "123 456",
            "sdf ghj",
        ]
        expected = self._reference_decode(lines)
        got = self._run_target(lines)
        self.assertEqual(got, expected)

    def test_punctuation_case(self):
        # 標點符號與數字一起測，避免只寫字母卻漏掉符號對照
        lines = [
            "=]\\ /.,",
            "90- p[]",
        ]
        expected = self._reference_decode(lines)
        got = self._run_target(lines)
        self.assertEqual(got, expected)

    def test_full_row_mix(self):
        # 把每一排的可解碼字元都拼起來，快速驗證整張鍵盤的映射
        lines = [
            "1234567890-=",
            "wertyuiop[]\\",
            "sdfghjkl;'",
            "xcvbnm,./",
        ]
        expected = self._reference_decode(lines)
        got = self._run_target(lines)
        self.assertEqual(got, expected)

    def test_randomized_against_reference(self):
        # 小範圍隨機對拍：用參考鍵盤映射比對，抓出字元表寫錯的情況
        random.seed(10222)
        mapping = self._keyboard_map()
        alphabet = [ch for ch in mapping.keys() if ch != " "]

        for _ in range(80):
            line_count = random.randint(1, 5)
            lines = []
            for _line in range(line_count):
                length = random.randint(0, 40)
                line = "".join(random.choice(alphabet + [" "]) for _ in range(length))
                lines.append(line)

            expected = self._reference_decode(lines)
            got = self._run_target(lines)
            self.assertEqual(got, expected, msg=f"failed lines={lines}")


if __name__ == "__main__":
    unittest.main(verbosity=2)