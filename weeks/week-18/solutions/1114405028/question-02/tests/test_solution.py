import pytest
from solver import caesar_cipher


def test_caesar_cipher_basic():
    assert caesar_cipher('Hello, World!') == 'Khoor, Zruog!'


def test_caesar_cipher_wrap():
    assert caesar_cipher('XYZ xyz') == 'ABC abc'


def test_caesar_cipher_nonalpha():
    assert caesar_cipher('123 !?') == '123 !?'


def test_caesar_cipher_jkl_GHI():
    assert caesar_cipher('jkl GHI') == 'mno JKL'
