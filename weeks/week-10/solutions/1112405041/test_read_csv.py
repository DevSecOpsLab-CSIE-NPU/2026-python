import unittest
import tempfile
import os
from pathlib import Path
from task1_csv_to_json import read_csv

DATA_FILE = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data" / "113年新生資料庫.csv"

class TestReadCSV(unittest.TestCase):

    def test_read_csv_normal(self):
        result = read_csv(str(DATA_FILE))
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        for row in result:
            self.assertIsInstance(row, dict)

    def test_read_csv_empty_file(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8-sig') as f:
            f.write("")
            tmp = f.name
        try:
            result = read_csv(tmp)
            self.assertEqual(result, [])
        finally:
            os.unlink(tmp)

    def test_read_csv_header_only(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8-sig') as f:
            f.write("學號,系所名稱,入學方式,郵遞區號,畢業學校,前畢業科系\n")
            tmp = f.name
        try:
            result = read_csv(tmp)
            self.assertEqual(result, [])
        finally:
            os.unlink(tmp)

    def test_read_csv_missing_field(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8-sig') as f:
            f.write("學號,系所名稱,入學方式,郵遞區號,畢業學校,前畢業科系\n")
            f.write("1131234001,電機工程系,聯合登記分發,880,,\n")
            tmp = f.name
        try:
            result = read_csv(tmp)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0]["畢業學校"], "")
        finally:
            os.unlink(tmp)

    def test_read_csv_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_csv("不存在_檔案.csv")
