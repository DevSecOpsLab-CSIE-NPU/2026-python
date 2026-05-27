import datetime
import subprocess
import sys
import unittest
from pathlib import Path


def run_program(filename: str, input_data: str) -> str:
    program = Path(__file__).with_name(filename)
    result = subprocess.run(
        [sys.executable, str(program)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class TestQuestion12019(unittest.TestCase):
    def test_fixed_dates(self) -> None:
        input_data = """3
1 1
2 29
12 25
"""
        expected = """Sunday
Wednesday
Tuesday"""
        self.assertEqual(run_program("question_12019.py", input_data), expected)

    def test_batch_dates(self) -> None:
        dates = [(3, 14), (6, 1), (10, 31), (11, 7)]
        parts = [str(len(dates))]
        for m, d in dates:
            parts.append(f"{m} {d}")
        input_data = "\n".join(parts) + "\n"

        expected = "\n".join(
            datetime.date(2012, m, d).strftime("%A") for m, d in dates
        )
        self.assertEqual(run_program("question_12019.py", input_data), expected)


if __name__ == "__main__":
    unittest.main()
