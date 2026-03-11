"""
test_q299_hand_typed.py — 測試 q299-Hand-typed.py
"""
import importlib.util, pathlib, unittest

# 動態載入含連字號的檔名
_path = pathlib.Path(__file__).parent / "q299-Hand-typed.py"
_spec = importlib.util.spec_from_file_location("q299_hand_typed", _path)
_mod  = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

min_swaps = _mod.min_swaps
solve     = _mod.solve


class TestMinSwaps(unittest.TestCase):
    def test_already_sorted(self):
        self.assertEqual(min_swaps([1, 2, 3]), 0)

    def test_reverse_sorted(self):
        self.assertEqual(min_swaps([3, 2, 1]), 3)

    def test_single_element(self):
        self.assertEqual(min_swaps([5]), 0)

    def test_two_elements_sorted(self):
        self.assertEqual(min_swaps([1, 2]), 0)

    def test_two_elements_reversed(self):
        self.assertEqual(min_swaps([2, 1]), 1)

    def test_example_case(self):
        self.assertEqual(min_swaps([3, 1, 2]), 2)

    def test_four_elements(self):
        self.assertEqual(min_swaps([4, 3, 2, 1]), 6)

    def test_five_elements(self):
        self.assertEqual(min_swaps([1, 5, 4, 3, 2]), 6)

    def test_duplicate_values(self):
        self.assertEqual(min_swaps([2, 2, 1]), 2)

    def test_all_same(self):
        self.assertEqual(min_swaps([3, 3, 3]), 0)

    def test_no_modification_to_input(self):
        original = [3, 1, 2]
        wagons = original[:]
        min_swaps(wagons)
        self.assertEqual(wagons, original)


class TestSolve(unittest.TestCase):
    def test_L_zero(self):
        inp = "1\n0\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 0 swaps.")

    def test_L_one(self):
        inp = "1\n1\n5\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 0 swaps.")

    def test_example_single(self):
        inp = "1\n3\n3 1 2\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 2 swaps.")

    def test_example_sorted(self):
        inp = "1\n3\n1 2 3\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 0 swaps.")

    def test_example_reverse(self):
        inp = "1\n3\n3 2 1\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 3 swaps.")

    def test_multiple_cases(self):
        inp = "3\n3\n1 2 3\n3\n3 2 1\n3\n3 1 2\n"
        expected = (
            "Optimal train swapping takes 0 swaps.\n"
            "Optimal train swapping takes 3 swaps.\n"
            "Optimal train swapping takes 2 swaps."
        )
        self.assertEqual(solve(inp), expected)

    def test_output_format(self):
        result = solve("1\n2\n2 1\n")
        self.assertIn("Optimal train swapping takes", result)
        self.assertIn("swaps.", result)

    def test_large_input(self):
        wagons = list(range(50, 0, -1))
        inp = f"1\n50\n{' '.join(map(str, wagons))}\n"
        result = solve(inp)
        self.assertIn("Optimal train swapping takes 1225 swaps.", result)

    def test_extra_blank_lines(self):
        inp = "\n1\n\n3\n3 1 2\n\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 2 swaps.")

    def test_two_cases_output_lines(self):
        inp = "2\n1\n1\n2\n2 1\n"
        lines = solve(inp).splitlines()
        self.assertEqual(len(lines), 2)

    def test_four_elements_reverse(self):
        inp = "1\n4\n4 3 2 1\n"
        self.assertEqual(solve(inp), "Optimal train swapping takes 6 swaps.")


if __name__ == "__main__":
    unittest.main()
