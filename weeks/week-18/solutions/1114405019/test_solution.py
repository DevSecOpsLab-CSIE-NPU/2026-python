"""
凱薩位移密碼測試（SHIFT=10）
每個測試案例都驗證「為什麼」這個行為重要，而不只是斷言輸出值。
"""
import io
import pytest

from solution import shift_char, shift_line, main

SHIFT = 10


def test_shift_char_basic():
    """基本位移公式要正確，對應 Sample 驗算 H→R, e→o"""
    assert shift_char("H", SHIFT) == "R"
    assert shift_char("e", SHIFT) == "o"


def test_shift_char_uppercase_wrap():
    """大寫位移超出 Z 時要循環回 A-Z 開頭，而不是跳出 ASCII 範圍變成其他符號"""
    assert shift_char("Q", SHIFT) == "A"


def test_shift_char_lowercase_wrap():
    """小寫同理要循環回 a-z 開頭，避免把大寫公式誤套用在小寫字元上的常見 bug"""
    assert shift_char("q", SHIFT) == "a"


def test_shift_char_non_alpha_unchanged():
    """非英文字母字元（標點、空白、數字）必須原樣保留，不能被誤位移或吃掉"""
    assert shift_char(",", SHIFT) == ","
    assert shift_char(" ", SHIFT) == " "
    assert shift_char("!", SHIFT) == "!"
    assert shift_char("3", SHIFT) == "3"


def test_shift_line_sample1():
    """整行集成測試，對應 Sample 驗算：Hello, NPU! → Rovvy, XZE!"""
    assert shift_line("Hello, NPU!", SHIFT) == "Rovvy, XZE!"


def test_shift_line_sample2():
    """整行集成測試，含混合大小寫與循環邊界 X,Y,Z：abc XYZ → klm HIJ"""
    assert shift_line("abc XYZ", SHIFT) == "klm HIJ"


def test_shift_line_empty():
    """空白行（長度 0）要原樣輸出空字串，不能因為長度 0 而出錯"""
    assert shift_line("", SHIFT) == ""


def test_shift_line_all_non_alpha():
    """整行都沒有字母時，不應觸發任何位移錯誤，原樣保留"""
    assert shift_line("123, !!!", SHIFT) == "123, !!!"


def test_shift_line_mixed_case_digit_punct():
    """混合大小寫、數字、標點同一行：驗證各字元類型互不干擾"""
    assert shift_line("Ab3, c!", SHIFT) == "Kl3, m!"


def test_main_eof_termination(monkeypatch, capsys):
    """
    驗證讀取迴圈是「讀到 EOF 結束」，而非讀到某個終止值（跟第一題的 n=0 不同）。
    用 io.StringIO 模擬多行輸入，最後一行沒有換行符也要正確輸出並結束迴圈。
    """
    fake_stdin = io.StringIO("Hello, NPU!\nabc XYZ\n")
    monkeypatch.setattr("sys.stdin", fake_stdin)
    main()
    captured = capsys.readouterr()
    assert captured.out == "Rovvy, XZE!\nklm HIJ\n"
