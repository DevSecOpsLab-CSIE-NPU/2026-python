"""Stage 5 — 安全性自掃測試

對照 OpenSSF Secure Coding Guide for Python:
  03 Numbers / 04 Neutralization / 05 Exception Handling / 08 Coding Standards
"""

import unittest

from timing import timeit
from search import linear_search, binary_search, set_search


class TestSecurity(unittest.TestCase):

    # pyscg-0011: Prevent Type Confusion (04 Neutralization)
    def test_search_rejects_non_list_data(self):
        for func in (linear_search, binary_search, set_search):
            with self.subTest(func=func.__name__):
                with self.assertRaises(TypeError):
                    func("not_a_list", 42)

    # pyscg-0004: Use Integer Loop Counters (03 Numbers)
    def test_timeit_rejects_bool_repeat(self):
        with self.assertRaises(TypeError):
            @timeit(repeat=True)
            def dummy():
                pass

    # pyscg-0035: Complete Resource Cleanup (08 Coding Standards)
    def test_plot_closes_figure(self):
        import plot
        import matplotlib.pyplot as plt
        self.assertEqual(len(plt.get_fignums()), 0,
                         "plot.py did not close its figure")


if __name__ == "__main__":
    unittest.main()
