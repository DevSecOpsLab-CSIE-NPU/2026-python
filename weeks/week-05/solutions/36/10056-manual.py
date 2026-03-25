import unittest

class ProbabilityCalculator:

    @staticmethod
    def solve(n, p, i):
        if p == 0:
            return 0.0000
        
        q = 1 - p
        result = (q**(i-1) * p) / (1 - q**n)
        return round(result, 4)

class TestProbability(unittest.TestCase):
    def test_sample_cases(self):
        calc = ProbabilityCalculator()
        self.assertAlmostEqual(calc.solve(2, 0.1666, 1), 0.5455, places=4)
        self.assertAlmostEqual(calc.solve(2, 0.1666, 2), 0.4545, places=4)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)