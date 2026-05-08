#!/usr/bin/env python3
import unittest
import sys
import os

# Ensure parent directory is in path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from uva10041 import process_input as process_10041
from uva10050 import process_input as process_10050
from uva10055 import process_input as process_10055
from uva10056 import process_input as process_10056
from uva10057 import process_input as process_10057


class TestWeek05Solutions(unittest.TestCase):
    def test_uva10041_sample(self):
        input_text = '2\n3 1 2 3\n4 2 4 5 6\n'
        expected = '2\n5'
        self.assertEqual(process_10041(input_text), expected)

    def test_uva10050_sample(self):
        input_text = '1\n14\n3\n3\n4\n8\n'
        expected = '5'
        self.assertEqual(process_10050(input_text), expected)

    def test_uva10055_sample(self):
        input_text = '4 4\n1 1\n1 2\n2 1 4\n2 2 3\n'
        expected = '0\n1'
        self.assertEqual(process_10055(input_text), expected)

    def test_uva10056_sample(self):
        input_text = '2\n3 0.50 1\n1 0.25 1\n'
        expected = '0.5714\n1.0000'
        self.assertEqual(process_10056(input_text), expected)

    def test_uva10057_sample(self):
        input_text = '5 1 2 3 4 5\n4 1 2 2 3\n'
        expected = '3 1 1\n2 2 1'
        self.assertEqual(process_10057(input_text), expected)


if __name__ == '__main__':
    unittest.main()
import unittest

from uva10041 import process_input as process_10041
from uva10050 import process_input as process_10050
from uva10055 import process_input as process_10055
from uva10056 import process_input as process_10056
from uva10057 import process_input as process_10057


class TestWeek05Solutions(unittest.TestCase):
    def test_uva10041_sample(self):
        input_text = '2\n3 1 2 3\n4 2 4 5 6\n'
        expected = '2\n5'
        self.assertEqual(process_10041(input_text), expected)

    def test_uva10050_sample(self):
        input_text = '1\n14\n3\n3\n4\n8\n'
        expected = '5'
        self.assertEqual(process_10050(input_text), expected)

    def test_uva10055_sample(self):
        input_text = '4 4\n1 1\n1 2\n2 1 4\n2 2 3\n'
        expected = '0\n1'
        self.assertEqual(process_10055(input_text), expected)

    def test_uva10056_sample(self):
        input_text = '2\n3 0.50 1\n1 0.25 1\n'
        expected = '0.5714\n1.0000'
        self.assertEqual(process_10056(input_text), expected)

    def test_uva10057_sample(self):
        input_text = '5 1 2 3 4 5\n4 1 2 2 3\n'
        expected = '3 1 1\n2 2 1'
        self.assertEqual(process_10057(input_text), expected)


if __name__ == '__main__':
    unittest.main()
import unittest

from uva10041 import process_input as process_10041
from uva10050 import process_input as process_10050
from uva10055 import process_input as process_10055
from uva10056 import process_input as process_10056
from uva10057 import process_input as process_10057


class TestWeek05Solutions(unittest.TestCase):
    def test_uva10041_sample(self):
        input_text = '2\n3 1 2 3\n4 2 4 5 6\n'
        expected = '2\n5'
        self.assertEqual(process_10041(input_text), expected)

    def test_uva10050_sample(self):
        input_text = '1\n14\n3\n3\n4\n8\n'
        expected = '5'
        self.assertEqual(process_10050(input_text), expected)

    def test_uva10055_sample(self):
        input_text = '4 4\n1 1\n1 2\n2 1 4\n2 2 3\n'
        expected = '0\n1'
        self.assertEqual(process_10055(input_text), expected)

    def test_uva10056_sample(self):
        input_text = '2\n3 0.50 1\n1 0.25 1\n'
        expected = '0.5714\n1.0000'
        self.assertEqual(process_10056(input_text), expected)

    def test_uva10057_sample(self):
        input_text = '5 1 2 3 4 5\n4 1 2 2 3\n'
        expected = '3 1 1\n2 2 1'
        self.assertEqual(process_10057(input_text), expected)


if __name__ == '__main__':
    unittest.main()
