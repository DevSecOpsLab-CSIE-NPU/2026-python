import subprocess
import os
import unittest

BASE = os.path.dirname(os.path.abspath(__file__))


def run(script, input_data):
    result = subprocess.run(
        ['python', os.path.join(BASE, script)],
        input=input_data, capture_output=True, text=True, timeout=30
    )
    return result.stdout.strip()


class TestWeek08Hand(unittest.TestCase):

    def test_10189_minesweeper(self):
        data = "4 4\n*...\n....\n.*..\n....\n3 5\n**...\n.....\n.*...\n0 0\n"
        out = run('10189-hand.py', data)
        expected = (
            "Field #1:\n"
            "*100\n"
            "2210\n"
            "1*10\n"
            "1110\n"
            "\n"
            "Field #2:\n"
            "**100\n"
            "33200\n"
            "1*100"
        )
        self.assertEqual(out, expected)

    def test_10190_rain(self):
        data = "2 10 5 3\n0 3 2\n5 4 1\n"
        out = run('10190-hand.py', data)
        self.assertEqual(out, '62.50')

    def test_10193_arctan(self):
        # a=1 -> N=2, d1=1, d2=2 -> b+c = 2+3 = 5
        out = run('10193-hand.py', '1\n')
        self.assertEqual(out, '5')

    def test_10221_satellites(self):
        data = "500 30 deg\n700 60 min\n200 45 deg\n"
        out = run('10221-hand.py', data)
        lines = out.split('\n')
        self.assertEqual(len(lines), 3)
        # 500 30 deg: r=6940, arc=r*(pi/6), chord=2r*sin(pi/12)
        parts = lines[0].split()
        self.assertAlmostEqual(float(parts[0]), 3633.775503, places=2)
        self.assertAlmostEqual(float(parts[1]), 3592.408346, places=2)

    def test_10222_keyboard(self):
        # 'tyuy' 是 'were' 往右偏移 3 格的結果，解碼應還原為 'were'
        out = run('10222-hand.py', 'tyuy\n')
        self.assertEqual(out, 'were')


if __name__ == '__main__':
    unittest.main(verbosity=2)
