import importlib.util
import subprocess
import sys
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("10922-easy.py")


def load_module():
    """依檔案位置載入主程式。"""
    spec = importlib.util.spec_from_file_location("u10922_easy", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestEasyVersion(unittest.TestCase):
    """簡易版功能測試。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def test_digit_sum(self):
        """基本加總測試。"""
        self.assertEqual(self.module.digit_sum("12345"), 15)

    def test_not_multiple_of_nine(self):
        """不是 9 的倍數時要回傳 0。"""
        self.assertEqual(self.module.degree_of_nine("1234"), 0)

    def test_single_nine(self):
        """單一 9 的深度是 1。"""
        self.assertEqual(self.module.degree_of_nine("9"), 1)

    def test_degree_two(self):
        """999999 -> 54 -> 9，所以深度是 2。"""
        self.assertEqual(self.module.degree_of_nine("999999"), 2)

    def test_degree_three(self):
        """111 個 9 需要三次加總才會到 9。"""
        self.assertEqual(self.module.degree_of_nine("9" * 111), 3)

    def test_main_output(self):
        """主程式輸出要與題目格式一致。"""
        input_data = """18
1234
999999
0
"""

        expected_output = """9-degree of 18 is 1.
1234 is not a multiple of 9.
9-degree of 999999 is 2.
"""

        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), expected_output.strip())


if __name__ == "__main__":
    unittest.main(verbosity=2)