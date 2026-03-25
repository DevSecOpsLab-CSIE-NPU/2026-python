# weeks/week-04/solutions/Hartals.py

class HartalCalculator:
    
    @staticmethod
    def count_lost_days(n_days, hartal_params):

        lost_count = 0
        for day in range(1, n_days + 1):
            if day % 7 == 6 or day % 7 == 0:
                continue
            
            for h in hartal_params:
                if day % h == 0:
                    lost_count += 1
                    break 
        return lost_count

import unittest

class TestHartals(unittest.TestCase):
    def test_sample_case_1(self):
        calc = HartalCalculator()
        self.assertEqual(calc.count_lost_days(14, [3, 4, 8]), 5)

    def test_sample_case_2(self):
        calc = HartalCalculator()
        self.assertEqual(calc.count_lost_days(100, [12, 15]), 15)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)