from __future__ import annotations

import itertools
import unittest

from test_support import run_script


def brute_force(grid: list[list[int]]) -> int:
    # 小尺寸暴力：枚舉所有邊集合，計算每個可用格度數是否皆為 2。
    row_count = len(grid)
    column_count = len(grid[0])
    vertices = [
        (row, column)
        for row in range(row_count)
        for column in range(column_count)
        if grid[row][column] == 1
    ]
    vertex_index = {vertex: index for index, vertex in enumerate(vertices)}

    edges: list[tuple[int, int]] = []
    for row in range(row_count):
        for column in range(column_count):
            if grid[row][column] == 0:
                continue
            for delta_row, delta_column in ((1, 0), (0, 1)):
                nxt_row = row + delta_row
                nxt_column = column + delta_column
                if 0 <= nxt_row < row_count and 0 <= nxt_column < column_count and grid[nxt_row][nxt_column] == 1:
                    edges.append((vertex_index[(row, column)], vertex_index[(nxt_row, nxt_column)]))

    answer = 0
    for mask in range(1 << len(edges)):
        degree = [0] * len(vertices)
        for edge_index, (left, right) in enumerate(edges):
            if mask & (1 << edge_index):
                degree[left] += 1
                degree[right] += 1
        if all(value == 2 for value in degree):
            answer += 1
    return answer


class Test10235(unittest.TestCase):
    def assert_case(self, grid: list[list[int]], expected: int) -> None:
        # 組成一筆 Case 輸入並驗證兩個版本輸出。
        row_count = len(grid)
        column_count = len(grid[0])
        input_lines = ["1", f"{row_count} {column_count}"]
        input_lines.extend(" ".join(map(str, row)) for row in grid)
        input_data = "\n".join(input_lines) + "\n"
        expected_output = f"Case 1: {expected}"
        self.assertEqual(run_script("10235.py", input_data), expected_output)
        self.assertEqual(run_script("10235-easy.py", input_data), expected_output)

    def test_sample_like_cases(self) -> None:
        # 基本案例：全開 2x2 與單格案例。
        self.assert_case([[1, 1], [1, 1]], 1)
        self.assert_case([[1]], 0)

    def test_bruteforce_small_grids(self) -> None:
        # 用暴力答案驗證 DP 在小板面下的正確性。
        grids = [
            [[1, 1], [1, 1]],
            [[1, 0], [1, 1]],
            [[1, 1, 1], [1, 1, 1]],
            [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        ]
        for grid in grids:
            with self.subTest(grid=grid):
                self.assert_case(grid, brute_force(grid))


if __name__ == "__main__":
    unittest.main(verbosity=2)