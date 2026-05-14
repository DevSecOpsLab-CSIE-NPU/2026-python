"""U01-timeit-decorator.py 的單元測試。"""

from __future__ import annotations

import contextlib
import io
import unittest

from support import load_module


class TestU01TimeitDecorator(unittest.TestCase):
    """確認裝飾器與格式速度比較範例可被驗證。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("U01-timeit-decorator.py")

    def test_timeit_preserves_metadata_and_returns_result(self):
        @self.module.timeit
        def add(a, b):
            """回傳兩數相加。"""
            return a + b

        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            result = add(3, 4)

        self.assertEqual(7, result)
        self.assertEqual("add", add.__name__)
        self.assertIn("add", stream.getvalue())

    def test_readers_parse_same_number_of_rows(self):
        csv_data, json_data, xml_data = self.module.build_sample_datasets(3)

        csv_rows = self.module.read_csv_raw(csv_data)
        json_rows = self.module.read_json_raw(json_data)
        xml_rows = self.module.read_xml_raw(xml_data)

        self.assertEqual(3, len(csv_rows))
        self.assertEqual(3, len(json_rows))
        self.assertEqual(3, len(xml_rows))

    def test_benchmark_returns_non_negative_average_times(self):
        csv_data, json_data, xml_data = self.module.build_sample_datasets(10)
        averages = self.module.benchmark_readers(csv_data, json_data, xml_data, runs=2)

        self.assertEqual({"CSV", "JSON", "XML"}, set(averages))
        for value in averages.values():
            self.assertGreaterEqual(value, 0.0)


if __name__ == "__main__":
    unittest.main()
