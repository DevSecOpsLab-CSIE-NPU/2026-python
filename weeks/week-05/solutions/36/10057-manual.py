import unittest

class DreamSolver:
    
    @staticmethod
    def solve(numbers):
        n = len(numbers)
        numbers.sort()
        
        mid1 = numbers[(n - 1) // 2]
        mid2 = numbers[n // 2]
        
        min_median = mid1
        
        count_in_input = 0
        for x in numbers:
            if mid1 <= x <= mid2:
                count_in_input += 1
                
        possible_integers = mid2 - mid1 + 1
        
        return min_median, count_in_input, possible_integers

class TestDream(unittest.TestCase):
    def test_odd_elements(self):
        solver = DreamSolver()
        self.assertEqual(solver.solve([10, 10]), (10, 2, 1))

    def test_even_elements(self):
        solver = DreamSolver()
        self.assertEqual(solver.solve([1, 2, 3, 4]), (2, 2, 2))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)