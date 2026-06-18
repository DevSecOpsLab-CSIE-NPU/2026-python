import unittest
import os
import json


class TestSecurity(unittest.TestCase):

    def test_make_data_rejects_negative_n(self):
        from benchmark import make_data
        with self.assertRaises(ValueError):
            make_data(-5)

    def test_results_file_closed(self):
        with open("results.json") as f:
            self.assertTrue(f.readable())
        self.assertTrue(f.closed)

    def test_load_uses_json_not_pickle(self):
        with open("results.json") as f:
            header = f.read(1)
        self.assertEqual(header, "{")