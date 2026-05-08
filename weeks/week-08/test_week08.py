import unittest
import io
import sys
import importlib.util

class TestWeek08Solutions(unittest.TestCase):

    def run_script(self, script_name, input_data):
        """輔助函式：動態載入並執行程式以捕獲輸出"""
        saved_stdin = sys.stdin
        saved_stdout = sys.stdout
        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()
        try:
            spec = importlib.util.spec_from_file_location("__main__", script_name)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            output = sys.stdout.getvalue()
        except Exception as e:
            output = sys.stdout.getvalue() + str(e)
        finally:
            sys.stdin = saved_stdin
            sys.stdout = saved_stdout
        return output

    def test_uva10189(self):
        input_data = "4 4\n*...\n....\n.*..\n....\n3 5\n**...\n.....\n.*...\n0 0\n"
        expected = "Field #1:\n*100\n2210\n1*10\n1110\n\nField #2:\n**100\n33200\n1*100\n"
        self.assertEqual(self.run_script("uva10189.py", input_data).strip(), expected.strip())

    def test_uva10190(self):
        input_data = "125 5\n30 3\n80 2\n81 3\n"
        expected = "125 25 5 1\nBoring!\nBoring!\n81 27 9 3 1\n"
        self.assertEqual(self.run_script("uva10190.py", input_data).strip(), expected.strip())

    def test_uva10193(self):
        input_data = "5\n11011\n11000\n11011\n11001\n111111\n100\n1000000000\n110\n1010\n100\n"
        expected = "Pair #1: All you need is love!\nPair #2: Love is not all you need!\nPair #3: Love is not all you need!\nPair #4: All you need is love!\nPair #5: All you need is love!\n"
        self.assertEqual(self.run_script("uva10193.py", input_data).strip(), expected.strip())

    def test_uva10221(self):
        input_data = "500 120 deg\n700 52.25 min\n"
        expected = "14535.102061 12020.252718\n108.536762 108.535492\n"
        self.assertEqual(self.run_script("uva10221.py", input_data).strip(), expected.strip())

    def test_uva10222(self):
        input_data = "k[r\\g\n"
        expected = "how a\n"
        self.assertEqual(self.run_script("uva10222.py", input_data).strip(), expected.strip())