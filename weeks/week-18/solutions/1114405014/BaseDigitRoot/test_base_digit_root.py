import pytest

from base_digit_root import to_base_digits, digit_root_in_base, solve


BASE = 5


def test_to_base_digits_zero():
    assert to_base_digits(0, BASE) == [0]


def test_to_base_digits_single_digit():
    assert to_base_digits(4, BASE) == [4]


def test_to_base_digits_base_value():
    assert to_base_digits(5, BASE) == [1, 0]


def test_to_base_digits_multiple_digits():
    assert to_base_digits(24, BASE) == [4, 4]


def test_digit_root_zero():
    assert digit_root_in_base(0, BASE) == 0


def test_digit_root_number_less_than_base():
    assert digit_root_in_base(4, BASE) == 4


def test_digit_root_equal_to_base():
    assert digit_root_in_base(5, BASE) == 1


def test_digit_root_requires_repeated_sum():
    # 24 = 44(base 5)
    # 4 + 4 = 8
    # 8 = 13(base 5)
    # 1 + 3 = 4
    assert digit_root_in_base(24, BASE) == 4


def test_digit_root_power_of_base():
    # 25 = 100(base 5)
    # 1 + 0 + 0 = 1
    assert digit_root_in_base(25, BASE) == 1


def test_digit_root_larger_number():
    # 124 = 444(base 5)
    # 4 + 4 + 4 = 12
    # 12 = 22(base 5)
    # 2 + 2 = 4
    assert digit_root_in_base(124, BASE) == 4


def test_solve_multiple_lines():
    input_text = """0
4
5
24
25
124
"""
    expected = """0
4
1
4
1
4"""

    assert solve(input_text, BASE) == expected


def test_solve_space_separated_input():
    input_text = "0 4 5 24 25 124"
    expected = """0
4
1
4
1
4"""

    assert solve(input_text, BASE) == expected


def test_invalid_negative_number_raises_value_error():
    with pytest.raises(ValueError):
        digit_root_in_base(-1, BASE)


def test_invalid_base_less_than_two_raises_value_error():
    with pytest.raises(ValueError):
        digit_root_in_base(10, 1)