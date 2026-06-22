# -*- coding: utf-8 -*-
"""
凱撒密碼測試（SHIFT = 6）
測試對象：caesar_cipher.py 內的 shift_char / encrypt_line / main
"""
import io
import sys

from caesar_cipher import shift_char, encrypt_line, main, SHIFT


def test_full_line_sample1():
    # 依使用者列出的逐字元位移規則：H->N, e->k, l->r, l->r, o->u；逗號/空白/驚嘆號不變
    # 注意：使用者原文手寫的最終結果字串是 "Nkeru"，與其自己列的逐字元規則 N-k-r-r-u 不符，
    # 視為手寫筆誤，測試以逐字元規則推出的 "Nkrru" 為準
    assert encrypt_line("Hello, NPU!", SHIFT) == "Nkrru, TVA!"


def test_full_line_sample2():
    # 第二組驗算範例：abc->ghi, XYZ->DEF（含大寫循環繞回開頭）
    assert encrypt_line("abc XYZ", SHIFT) == "ghi DEF"


def test_lowercase_wraps_around_boundary():
    # 'u' + 6 會超過 'z'，必須繞回字母表開頭變成 'a'，
    # 這裡專門測循環邊界，不能只測中間值（例如 a->g 那種不會碰到邊界的情況）
    assert shift_char('u', SHIFT) == 'a'


def test_uppercase_wraps_around_boundary():
    # 'U' + 6 同理應繞回 'A'，驗證大寫循環邏輯跟小寫一致
    assert shift_char('U', SHIFT) == 'A'


def test_non_alpha_chars_unchanged():
    # 標點、數字、空白都不是英文字母，規則要求原樣保留，不能被誤位移
    assert shift_char('!', SHIFT) == '!'
    assert shift_char('3', SHIFT) == '3'
    assert shift_char(' ', SHIFT) == ' '


def test_empty_line_stays_empty():
    # 長度為 0 的字串本身沒有任何字元可位移，預期輸出仍是空字串
    assert encrypt_line("", SHIFT) == ""


def test_line_with_only_non_alpha_chars():
    # 整行都沒有英文字母時，逐字元位移規則對每個字元都不生效，輸出應與輸入相同
    assert encrypt_line("123, !!?", SHIFT) == "123, !!?"


def test_mixed_case_digits_and_punctuation_in_one_line():
    # 同一行混合大寫、小寫、數字、標點，驗證三種字元各自的處理規則
    # 互不干擾：A->G, b->h, 3 不變(非字母), c->i, ! 不變(非字母)
    assert encrypt_line("Ab3, c!", SHIFT) == "Gh3, i!"


def test_main_reads_until_eof_not_until_sentinel_value():
    # 重點：這題的輸入結束條件是 EOF，不是像第一題那樣讀到某個終止值（如 n=0）才停。
    # 用兩行輸入（無終止標記）模擬 stdin，確認 main 會把兩行都處理完才結束，
    # 且輸出行數與輸入行數一致。
    fake_stdin = io.StringIO("Hello, NPU!\nabc XYZ\n")
    fake_stdout = io.StringIO()

    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = fake_stdin, fake_stdout
    try:
        main()
    finally:
        sys.stdin, sys.stdout = old_stdin, old_stdout

    output_lines = fake_stdout.getvalue().splitlines()
    assert output_lines == ["Nkrru, TVA!", "ghi DEF"]
