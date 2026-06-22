from pathlib import Path

from search_performance import (
    TARGET,
    linear_search,
    binary_search,
    benchmark_search,
    make_radar_chart,
    solve,
)


def test_target_value():
    assert TARGET == 114


def test_linear_search_found():
    arr = [3, 5, 7, 9, 20, 50, 100, 114]

    found, index, cmp_count = linear_search(arr, TARGET)

    assert found is True
    assert index == 7
    assert cmp_count == 8


def test_linear_search_not_found():
    arr = [3, 5, 7, 9, 20, 50, 100]

    found, index, cmp_count = linear_search(arr, TARGET)

    assert found is False
    assert index == -1
    assert cmp_count == len(arr)


def test_binary_search_found():
    arr = [3, 5, 7, 9, 20, 50, 100, 114]

    found, index, cmp_count = binary_search(arr, TARGET)

    assert found is True
    assert arr[index] == TARGET
    assert cmp_count > 0
    assert cmp_count <= 4


def test_binary_search_not_found():
    arr = [3, 5, 7, 9, 20, 50, 100]

    found, index, cmp_count = binary_search(arr, TARGET)

    assert found is False
    assert index == -1
    assert cmp_count > 0


def test_binary_search_empty_array():
    arr = []

    found, index, cmp_count = binary_search(arr, TARGET)

    assert found is False
    assert index == -1
    assert cmp_count == 0


def test_binary_search_single_element_found():
    arr = [114]

    found, index, cmp_count = binary_search(arr, TARGET)

    assert found is True
    assert index == 0
    assert cmp_count == 1


def test_binary_search_single_element_not_found():
    arr = [100]

    found, index, cmp_count = binary_search(arr, TARGET)

    assert found is False
    assert index == -1
    assert cmp_count == 1


def test_binary_search_with_duplicates_returns_valid_index():
    arr = [3, 5, 114, 114, 114, 200]

    found, index, cmp_count = binary_search(arr, TARGET)

    assert found is True
    assert arr[index] == TARGET
    assert cmp_count > 0


def test_solve_sorts_array_and_searches_target():
    input_text = """8
5 114 20 7 9 100 3 50
"""

    output = solve(input_text, TARGET)

    assert "FOUND" in output
    assert "index=7" in output
    assert "linear_cmp=8" in output
    assert "binary_cmp=" in output


def test_solve_target_not_found():
    input_text = """7
5 20 7 9 100 3 50
"""

    output = solve(input_text, TARGET)

    assert "NOT FOUND" in output
    assert "index=-1" in output
    assert "linear_cmp=7" in output
    assert "binary_cmp=" in output


def test_solve_accepts_numbers_across_multiple_lines():
    input_text = """8
5 114
20 7
9 100 3
50
"""

    output = solve(input_text, TARGET)

    assert "FOUND" in output
    assert "index=7" in output


def test_benchmark_search_returns_time_metrics():
    arr = list(range(1000))

    metrics = benchmark_search(arr, TARGET, repeat=10)

    assert "linear_time" in metrics
    assert "binary_time" in metrics
    assert metrics["linear_time"] >= 0
    assert metrics["binary_time"] >= 0


def test_make_radar_chart_creates_png_file(tmp_path):
    metrics = {
        "linear_time": 0.01,
        "binary_time": 0.001,
        "linear_cmp": 100,
        "binary_cmp": 7,
    }
    output_path = tmp_path / "radar.png"

    make_radar_chart(metrics, output_path)

    assert output_path.exists()
    assert output_path.stat().st_size > 0