"""
Week-09 綜合測試程式 - 學號 1114405001
涵蓋所有7個範例檔案的單元測試

測試目標：
1. R01：檔案讀寫與逐行迭代
2. R02：路徑操作與檔案搜尋
3. U03：編碼轉換與二進位操作
4. U04：StringIO 記憶體檔案與行處理
5. U_02：itertools 各函數
6. A05：檔案模式與目錄統計
7. A06：gzip、tempfile、pickle
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import io
import csv
import gzip
import pickle
from itertools import islice, dropwhile, takewhile, chain, permutations, combinations


class TestR01FileIO(unittest.TestCase):
    """R01 - 文本 I/O 基本式"""
    
    def setUp(self):
        """建立暫存目錄"""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
    
    def tearDown(self):
        """清理暫存目錄"""
        shutil.rmtree(self.temp_dir)
    
    def test_write_and_read_text_file(self):
        """測試：寫入和讀取文本檔"""
        test_file = self.temp_path / "test.txt"
        
        # 寫入
        with open(test_file, "wt", encoding="utf-8") as f:
            f.write("你好，Python\n")
            f.write("第二行\n")
        
        # 讀取
        with open(test_file, "rt", encoding="utf-8") as f:
            content = f.read()
        
        self.assertEqual(content, "你好，Python\n第二行\n")
    
    def test_line_by_line_read(self):
        """測試：逐行讀取檔案"""
        test_file = self.temp_path / "test.txt"
        
        # 寫入多行
        with open(test_file, "wt", encoding="utf-8") as f:
            f.write("line1\nline2\nline3\n")
        
        # 逐行讀取並計數
        count = 0
        with open(test_file, "rt", encoding="utf-8") as f:
            for line in f:
                count += 1
        
        self.assertEqual(count, 3)
    
    def test_print_to_file(self):
        """測試：print 函數導向檔案"""
        test_file = self.temp_path / "log.txt"
        
        with open(test_file, "wt", encoding="utf-8") as f:
            print("登入成功", file=f)
            print("使用者:", "alice", file=f)
        
        content = test_file.read_text(encoding="utf-8")
        self.assertIn("登入成功", content)
        self.assertIn("使用者:", content)
    
    def test_separator_and_line_ending(self):
        """測試：分隔符與行終止符"""
        test_file = self.temp_path / "data.csv"
        
        fruits = ["apple", "banana", "cherry"]
        with open(test_file, "wt", encoding="utf-8") as f:
            print(*fruits, sep=",", file=f)
        
        content = test_file.read_text(encoding="utf-8")
        self.assertEqual(content.strip(), "apple,banana,cherry")


class TestR02PathAndListing(unittest.TestCase):
    """R02 - 路徑操作與目錄列舉"""
    
    def setUp(self):
        """建立測試目錄結構"""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
        
        # 建立測試檔案
        (self.temp_path / "file1.py").touch()
        (self.temp_path / "file2.txt").touch()
        (self.temp_path / "subdir").mkdir()
        (self.temp_path / "subdir" / "file3.py").touch()
    
    def tearDown(self):
        """清理暫存目錄"""
        shutil.rmtree(self.temp_dir)
    
    def test_path_composition(self):
        """測試：路徑組合"""
        base = Path("weeks") / "week-09"
        self.assertEqual(base.name, "week-09")
        self.assertEqual(base.parent.name, "weeks")
    
    def test_file_properties(self):
        """測試：檔案屬性"""
        f = Path("hello.txt")
        self.assertEqual(f.stem, "hello")
        self.assertEqual(f.suffix, ".txt")
    
    def test_exists_check(self):
        """測試：存在判定"""
        test_file = self.temp_path / "file1.py"
        self.assertTrue(test_file.exists())
        self.assertTrue(test_file.is_file())
        
        missing = self.temp_path / "nonexistent.txt"
        self.assertFalse(missing.exists())
    
    def test_glob_files(self):
        """測試：當層檔案搜尋"""
        py_files = list(self.temp_path.glob("*.py"))
        self.assertEqual(len(py_files), 1)
        self.assertEqual(py_files[0].name, "file1.py")
    
    def test_rglob_recursive(self):
        """測試：遞迴檔案搜尋"""
        py_files = list(self.temp_path.rglob("*.py"))
        self.assertEqual(len(py_files), 2)  # file1.py 和 subdir/file3.py


class TestU03BytesAndEncoding(unittest.TestCase):
    """U03 - 文字 vs 位元組、編碼觀念"""
    
    def setUp(self):
        """建立暫存目錄"""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
    
    def tearDown(self):
        """清理暫存目錄"""
        shutil.rmtree(self.temp_dir)
    
    def test_encode_decode(self):
        """測試：編碼轉換"""
        s = "你好"
        b = s.encode("utf-8")
        
        self.assertIsInstance(b, bytes)
        self.assertEqual(b.decode("utf-8"), s)
    
    def test_binary_file_write_read(self):
        """測試：二進位檔案讀寫"""
        magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
        test_file = self.temp_path / "test.bin"
        
        # 寫入
        test_file.write_bytes(magic)
        
        # 讀回
        with open(test_file, "rb") as f:
            head = f.read(8)
        
        self.assertEqual(head, magic)
    
    def test_encoding_error_handling(self):
        """測試：編碼錯誤"""
        test_file = self.temp_path / "zh.txt"
        
        # 用 UTF-8 寫入中文
        test_file.write_text("中文測試\n", encoding="utf-8")
        
        # 用 UTF-8 正常讀取
        content = test_file.read_text(encoding="utf-8")
        self.assertEqual(content, "中文測試\n")
        
        # 用 big5 讀取會錯誤
        with self.assertRaises(UnicodeDecodeError):
            test_file.read_text(encoding="big5")


class TestU04StringIOAndLines(unittest.TestCase):
    """U04 - 類檔案物件 StringIO 與逐行處理"""
    
    def test_stringio_write_and_read(self):
        """測試：StringIO 寫入與讀取"""
        buf = io.StringIO()
        print("第一行", file=buf)
        print("第二行", file=buf)
        print("第三行", file=buf)
        
        text = buf.getvalue()
        self.assertIn("第一行", text)
        self.assertIn("第二行", text)
        self.assertIn("第三行", text)
    
    def test_stringio_line_iteration(self):
        """測試：StringIO 逐行迭代"""
        buf = io.StringIO("line1\nline2\nline3\n")
        lines = list(buf)
        self.assertEqual(len(lines), 3)
    
    def test_csv_in_memory(self):
        """測試：記憶體中的 CSV 操作"""
        mem = io.StringIO()
        writer = csv.writer(mem)
        writer.writerow(["name", "score"])
        writer.writerow(["alice", 90])
        
        content = mem.getvalue()
        self.assertIn("name,score", content)
        self.assertIn("alice,90", content)
    
    def test_line_numbering(self):
        """測試：逐行處理與行號加工"""
        buf = io.StringIO("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n")
        
        lines = []
        n = 0
        for line in buf:
            line = line.rstrip()
            if not line:
                continue
            n += 1
            lines.append(f"{n:02d}. {line}")
        
        self.assertEqual(len(lines), 4)
        self.assertTrue(lines[0].startswith("01."))


class TestU02Itertools(unittest.TestCase):
    """U_02 - itertools 工具函數"""
    
    def test_islice(self):
        """測試：islice 切片"""
        def count(n):
            i = n
            while True:
                yield i
                i += 1
        
        c = count(0)
        result = list(islice(c, 5, 10))
        self.assertEqual(result, [5, 6, 7, 8, 9])
    
    def test_dropwhile(self):
        """測試：dropwhile 條件跳過"""
        nums = [1, 3, 5, 2, 4, 6]
        result = list(dropwhile(lambda x: x < 5, nums))
        self.assertEqual(result, [5, 2, 4, 6])
    
    def test_takewhile(self):
        """測試：takewhile 條件取用"""
        nums = [1, 3, 5, 2, 4, 6]
        result = list(takewhile(lambda x: x < 5, nums))
        self.assertEqual(result, [1, 3])
    
    def test_chain(self):
        """測試：chain 串聯"""
        a = [1, 2]
        b = [3, 4]
        c = [5]
        result = list(chain(a, b, c))
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_permutations_full(self):
        """測試：permutations 全排列"""
        items = ["a", "b"]
        result = list(permutations(items))
        self.assertEqual(len(result), 2)
        self.assertIn(("a", "b"), result)
        self.assertIn(("b", "a"), result)
    
    def test_permutations_partial(self):
        """測試：permutations 部分排列"""
        items = ["a", "b", "c"]
        result = list(permutations(items, 2))
        self.assertEqual(len(result), 6)
    
    def test_combinations(self):
        """測試：combinations 組合"""
        items = ["a", "b", "c"]
        result = list(combinations(items, 2))
        self.assertEqual(len(result), 3)
        self.assertIn(("a", "b"), result)


class TestA05FileOperations(unittest.TestCase):
    """A05 - 綜合應用：檔案操作"""
    
    def setUp(self):
        """建立暫存目錄"""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
    
    def tearDown(self):
        """清理暫存目錄"""
        shutil.rmtree(self.temp_dir)
    
    def test_exclusive_create_mode(self):
        """測試：獨占建立模式 'x'"""
        diary = self.temp_path / "test.txt"
        
        # 第一次建立成功
        with open(diary, "x", encoding="utf-8") as f:
            f.write("內容\n")
        
        # 第二次建立會失敗
        with self.assertRaises(FileExistsError):
            with open(diary, "x", encoding="utf-8") as f:
                f.write("新內容\n")
    
    def test_count_py_files(self):
        """測試：計算 .py 檔案行數"""
        # 建立測試檔案
        py_file = self.temp_path / "test.py"
        py_file.write_text("# 註解\ndef foo():\n    pass\n\nprint('hello')\n", encoding="utf-8")
        
        # 計算行數
        total, nonblank, defs = 0, 0, 0
        for p in self.temp_path.glob("*.py"):
            with open(p, "rt", encoding="utf-8", errors="replace") as f:
                for line in f:
                    total += 1
                    s = line.strip()
                    if s:
                        nonblank += 1
                    if s.startswith("def "):
                        defs += 1
        
        self.assertEqual(total, 5)
        self.assertEqual(nonblank, 4)
        self.assertEqual(defs, 1)


class TestA06GzipAndTempfile(unittest.TestCase):
    """A06 - 壓縮檔、臨時資料夾、物件序列化"""
    
    def setUp(self):
        """建立暫存目錄"""
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
    
    def tearDown(self):
        """清理暫存目錄"""
        shutil.rmtree(self.temp_dir)
    
    def test_gzip_write_read(self):
        """測試：gzip 壓縮檔讀寫"""
        gz_file = self.temp_path / "test.txt.gz"
        
        # 寫入壓縮檔
        with gzip.open(gz_file, "wt", encoding="utf-8") as f:
            f.write("第一行筆記\n")
            f.write("第二行筆記\n")
        
        # 讀回壓縮檔
        with gzip.open(gz_file, "rt", encoding="utf-8") as f:
            lines = f.readlines()
        
        self.assertEqual(len(lines), 2)
        self.assertIn("筆記", lines[0])
    
    def test_temporary_directory(self):
        """測試：臨時資料夾自動清理"""
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            self.assertTrue(tmp.exists())
            
            # 在裡面建立檔案
            (tmp / "test.txt").write_text("test", encoding="utf-8")
            self.assertTrue((tmp / "test.txt").exists())
        
        # 離開 with 後應該被刪除
        self.assertFalse(tmp.exists())
    
    def test_pickle_serialization(self):
        """測試：pickle 物件序列化"""
        data = {"name": "alice", "scores": [90, 85, 88]}
        pickle_file = self.temp_path / "data.pkl"
        
        # 序列化
        with open(pickle_file, "wb") as f:
            pickle.dump(data, f)
        
        # 反序列化
        with open(pickle_file, "rb") as f:
            loaded = pickle.load(f)
        
        self.assertEqual(loaded, data)


def run_tests():
    """執行所有測試"""
    # 建立測試套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 加入所有測試類別
    suite.addTests(loader.loadTestsFromTestCase(TestR01FileIO))
    suite.addTests(loader.loadTestsFromTestCase(TestR02PathAndListing))
    suite.addTests(loader.loadTestsFromTestCase(TestU03BytesAndEncoding))
    suite.addTests(loader.loadTestsFromTestCase(TestU04StringIOAndLines))
    suite.addTests(loader.loadTestsFromTestCase(TestU02Itertools))
    suite.addTests(loader.loadTestsFromTestCase(TestA05FileOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestA06GzipAndTempfile))
    
    # 執行測試
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == "__main__":
    result = run_tests()
    
    # 列印總結
    print("\n" + "="*70)
    print("測試總結")
    print("="*70)
    print(f"執行測試數：{result.testsRun}")
    print(f"成功數：{result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"失敗數：{len(result.failures)}")
    print(f"錯誤數：{len(result.errors)}")
    print(f"成功率：{((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
