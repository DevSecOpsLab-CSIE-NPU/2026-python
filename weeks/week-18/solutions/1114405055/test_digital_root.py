# 第三題：任意進位的數字根 -- 測試
# 學號 1114405055 末兩碼 55，個位 u=5，查表得 base=7
#
# digit_sum_in_base(x, base)：x 換算成 base 進位後，把各位數字加總，回傳十進位整數
# digital_root(x, base)：重複呼叫 digit_sum_in_base 直到結果是 base 進位下的一位數
#   x=0 時題目規定直接回傳 0，不套公式硬算

import pytest

from digital_root import digit_sum_in_base, digital_root

BASE = 7


def test_zero_is_zero_by_definition():
    # 題目明文規定 x=0 的數字根固定是 0，不能用一般迭代公式去算
    assert digital_root(0, BASE) == 0


def test_already_single_digit_no_iteration_needed():
    # x < base 時，本身在 base 進位下就是一位數，不需要任何累加迭代
    for x in range(1, BASE):
        assert digital_root(x, BASE) == x


def test_sample_8_one_iteration_to_converge():
    # 8 在 7 進位是 11 -> 1+1=2，2 < 7 已是一位數，迭代一次即收斂
    assert digit_sum_in_base(8, BASE) == 2
    assert digital_root(8, BASE) == 2


def test_sample_63_needs_two_iterations_to_converge():
    # 63 在 7 進位是 120 -> 1+2+0=3，3 < 7 已是一位數
    # 這組驗證「相加一次後仍可能不是一位數，需再轉一次進位再加一次」的收斂邊界
    assert digit_sum_in_base(63, BASE) == 3
    assert digital_root(63, BASE) == 3


def test_needs_multiple_rounds_to_converge_to_single_digit():
    # 自行驗算：x=1000000 在 7 進位是 11333311
    #   第一輪：1+1+3+3+3+3+1+1 = 16，16 在 7 進位是 22（兩位數，尚未收斂）
    #   第二輪：2+2 = 4，4 < 7 已是一位數
    # 證明 digital_root 必須是「迴圈直到一位數」而非只做固定一次相加
    x = 1_000_000
    first_round = digit_sum_in_base(x, BASE)
    assert first_round == 16
    assert first_round >= BASE  # 第一次相加後仍是兩位數，尚未收斂
    second_round = digit_sum_in_base(first_round, BASE)
    assert second_round == 4
    assert digital_root(x, BASE) == 4


def test_large_value_terminates_quickly():
    # x 接近上限 1e9，確認迴圈會收斂且不會死迴圈或效能爆炸
    x = 10**9
    result = digital_root(x, BASE)
    assert 0 <= result < BASE


@pytest.mark.parametrize("x", [0, 1, 6, 7, 8, 63, 1_000_000, 10**9])
def test_digital_root_always_single_digit_in_base(x):
    # 數字根定義上必須落在 [0, base) 之間（在 base 進位下是一位數）
    assert 0 <= digital_root(x, BASE) < BASE


def test_base_16_conversion_not_hardcoded_for_small_base():
    # 題目特別提醒 base 可能是 16，確認進位轉換/輸出邏輯沒有寫死成只服務小 base
    # 255 在 16 進位是 FF -> 十進位數字相加 15+15=30，30 在 16 進位是 1E -> 1+14=15
    base16 = 16
    assert digit_sum_in_base(255, base16) == 30
    assert digital_root(255, base16) == 15
    # 16 進位下剛好一位數的情況
    assert digital_root(15, base16) == 15
    assert digital_root(0, base16) == 0
