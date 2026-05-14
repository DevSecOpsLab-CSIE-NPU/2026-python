"""R01-csv-basic.py 的單元測試。"""

from __future__ import annotations

import unittest

from support import load_module


class TestR01CsvBasic(unittest.TestCase):
    """確認 CSV 讀寫範例已整理成可重複驗證的函式。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("R01-csv-basic.py")

    def test_reader_can_split_header_and_rows(self):
        headers, rows = self.module.read_csv_rows(self.module.RAW_CSV)

        self.assertEqual(
            ["Symbol", "Price", "Date", "Time", "Change", "Volume"],
            headers,
        )
        self.assertEqual(["AA", "39.48", "6/11/2007", "9:36am", "-0.18", "181800"], rows[0])
        self.assertEqual(3, len(rows))

    def test_dict_reader_keeps_named_fields(self):
        rows = self.module.read_csv_dict_rows(self.module.RAW_CSV)

        self.assertEqual("AIG", rows[1]["Symbol"])
        self.assertEqual("-0.46", rows[2]["Change"])

    def test_writer_outputs_expected_csv_text(self):
        csv_text = self.module.write_csv_text(
            [
                ["AA", 39.48, -0.18],
                ["AIG", 71.38, -0.15],
            ]
        )

        expected = (
            "Symbol,Price,Change\r\n"
            "AA,39.48,-0.18\r\n"
            "AIG,71.38,-0.15\r\n"
        )
        self.assertEqual(expected, csv_text)

    def test_dict_writer_outputs_expected_csv_text(self):
        csv_text = self.module.write_dict_csv_text(
            [
                {"Symbol": "AA", "Price": 39.48, "Change": -0.18},
                {"Symbol": "AIG", "Price": 71.38, "Change": -0.15},
            ]
        )

        expected = (
            "Symbol,Price,Change\r\n"
            "AA,39.48,-0.18\r\n"
            "AIG,71.38,-0.15\r\n"
        )
        self.assertEqual(expected, csv_text)


if __name__ == "__main__":
    unittest.main()
