import pytest

from data_cleaning import clean_sequence, format_result


def test_dedup_filter_sort_sample1():
    # 對齊題目自算範例：去重保序 -> 篩選 D=3 -> 升冪排序
    assert clean_sequence([4, 7, 4, 2, 9, 2, 6, 7], 3) == [6, 9]


def test_dedup_filter_sort_sample2():
    assert clean_sequence([1, 3, 5], 3) == [3]


def test_no_match_returns_empty():
    # 篩選後沒有任何數字符合，必須回傳空 list（NONE 是輸出層的事）
    assert clean_sequence([1, 2, 4, 5], 3) == []


def test_single_element():
    # 長度為 1 時去重/排序邏輯不能因為切片或比較而出錯
    assert clean_sequence([3], 3) == [3]


def test_negative_divisible():
    # Python 的 % 對負數的整除判斷依數學定義為真（-9 % 3 == 0），
    # 這是題目特別點名的風險點，必須用實際斷言鎖住行為
    assert clean_sequence([-9, -3, 2], 3) == [-9, -3]


def test_duplicates_preserve_first_then_filter():
    # 專門驗證「去重要在篩選之前發生，且保留第一次出現的順序」
    # 而不是先篩選再去重（雖然這組資料兩種順序的最終結果相同，
    # 但測的是去重保序這個中間步驟本身有沒有做對）
    assert clean_sequence([6, 3, 6, 9, 3], 3) == [3, 6, 9]


def test_format_empty_is_NONE():
    assert format_result([]) == "NONE"


def test_format_nonempty_joins_with_space():
    assert format_result([6, 9]) == "6 9"
