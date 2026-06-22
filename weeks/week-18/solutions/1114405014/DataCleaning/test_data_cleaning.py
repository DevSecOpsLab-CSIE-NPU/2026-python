import pytest

from data_cleaning import clean_sequence, solve


D = 2


def test_sample_case():
    input_text = """8
4 7 4 2 9 2 6 7
3
1 3 5
0
"""
    expected = """2 4 6
NONE"""
    assert solve(input_text, D) == expected


def test_remove_duplicates_keep_first_then_sort():
    numbers = [8, 2, 8, 4, 2, 6]

    result = clean_sequence(numbers, D)

    assert result == [2, 4, 6, 8]


def test_no_number_divisible_by_d_returns_empty_list():
    numbers = [1, 3, 5, 7]

    result = clean_sequence(numbers, D)

    assert result == []


def test_no_number_divisible_by_d_outputs_none():
    input_text = """4
1 3 5 7
0
"""
    expected = "NONE"

    assert solve(input_text, D) == expected


def test_negative_numbers():
    numbers = [-4, -3, -2, -4, 1, 2]

    result = clean_sequence(numbers, D)

    assert result == [-4, -2, 2]


def test_all_duplicates():
    numbers = [6, 6, 6, 6]

    result = clean_sequence(numbers, D)

    assert result == [6]


def test_zero_terminates_input():
    input_text = """0
"""

    assert solve(input_text, D) == ""


def test_multiple_cases():
    input_text = """5
10 5 10 4 3
6
9 8 7 6 5 4
4
1 1 1 1
0
"""
    expected = """4 10
4 6 8
NONE"""

    assert solve(input_text, D) == expected


def test_large_order_and_sorting_behavior():
    numbers = [100, 2, 50, 100, 3, 2, 8, 7, 50]

    result = clean_sequence(numbers, D)

    assert result == [2, 8, 50, 100]