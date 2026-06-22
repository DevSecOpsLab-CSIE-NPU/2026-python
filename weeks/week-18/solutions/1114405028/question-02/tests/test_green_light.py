from solver import caesar_cipher


def test_caesar_cipher_shift_9_hello_npu():
    assert caesar_cipher('Hello, NPU!', 9) == 'Qnuux, WYD!'


def test_caesar_cipher_shift_9_wraps_around():
    assert caesar_cipher('xyz XYZ', 9) == 'ghi GHI'
