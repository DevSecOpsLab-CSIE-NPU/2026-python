import unittest

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

class TestHartals(unittest.TestCase):
    def test_sample_case_1(self):
        calc = HartalCalculator()
        result = calc.count_lost_days(14, [3, 4, 8])
        print(f"測試 1 結果: {result}")
        self.assertEqual(result, 5)
    
    def test_sample_case_2(self):
        calc = HartalCalculator()
        result = calc.count_lost_days(100, [3, 4, 8])
        print(f"測試 2 結果: {result}")
        self.assertEqual(result, 28)

if __name__ == '__main__':
    print("=== 開始執行 Hartals 單元測試 ===")
    unittest.main(argv=[''], exit=False)