"""
第二題：凱撒密碼測試用例
SHIFT = 15
"""

import sys
sys.path.insert(0, '.')
from question_2_solution import caesar_cipher


def test_example_case():
    """測試基本範例"""
    # 利用 SHIFT=15 進行測試
    # A -> P, B -> Q, ... Z -> O (循環)
    # a -> p, b -> q, ... z -> o (循環)
    
    text = "Hello, World!"
    result = caesar_cipher(text, 15)
    # H->W, e->t, l->a, l->a, o->d, space, W->L, o->d, r->g, l->a, d->s, ! unchanged
    # "Wtaad, Ldgas!"
    expected = "Wtaad, Ldgas!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ 基本範例通過")


def test_uppercase():
    """測試全大寫"""
    text = "ABCXYZ"
    result = caesar_cipher(text, 15)
    # A->P, B->Q, C->R, X->M, Y->N, Z->O
    expected = "PQRMNО"
    assert result == "PQRMNО", f"Expected 'PQRMNО', got '{result}'"
    print("✓ 全大寫測試通過")


def test_lowercase():
    """測試全小寫"""
    text = "abcxyz"
    result = caesar_cipher(text, 15)
    # a->p, b->q, c->r, x->m, y->n, z->o
    expected = "pqrmno"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ 全小寫測試通過")


def test_mixed_case():
    """測試大小寫混合"""
    text = "Python"
    result = caesar_cipher(text, 15)
    # P->E, y->n, t->i, h->w, o->d, n->c
    expected = "EniWdc"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ 大小寫混合通過")


def test_with_numbers():
    """測試包含數字"""
    text = "ABC123XYZ"
    result = caesar_cipher(text, 15)
    # A->P, B->Q, C->R, 1->1, 2->2, 3->3, X->M, Y->N, Z->O
    expected = "PQR123MNO"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ 包含數字測試通過")


def test_with_punctuation():
    """測試包含標點"""
    text = "Hello, World!"
    result = caesar_cipher(text, 15)
    # H->W, e->t, l->a, l->a, o->d, ,->comma, space, W->L, o->d, r->g, l->a, d->s, !->!
    expected = "Wtaad, Ldgas!"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ 包含標點測試通過")


def test_empty_string():
    """測試空字串"""
    text = ""
    result = caesar_cipher(text, 15)
    expected = ""
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ 空字串測試通過")


def test_only_spaces():
    """測試只有空格"""
    text = "   "
    result = caesar_cipher(text, 15)
    expected = "   "
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ 只有空格測試通過")


def test_shift_wrapping():
    """測試 Z/z 回環"""
    text = "XYZ"
    result = caesar_cipher(text, 15)
    # X->M, Y->N, Z->O
    expected = "MNO"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ Z回環測試通過")


def test_shift_wrapping_lowercase():
    """測試 z/z 回環"""
    text = "xyz"
    result = caesar_cipher(text, 15)
    # x->m, y->n, z->o
    expected = "mno"
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ z回環測試通過")


def test_special_characters():
    """測試特殊字符"""
    text = "!@#$%^&*()"
    result = caesar_cipher(text, 15)
    expected = "!@#$%^&*()"  # 全部保持不變
    assert result == expected, f"Expected '{expected}', got '{result}'"
    print("✓ 特殊字符測試通過")


if __name__ == "__main__":
    print("開始測試第二題解決方案...\n")
    
    test_example_case()
    test_uppercase()
    test_lowercase()
    test_mixed_case()
    test_with_numbers()
    test_with_punctuation()
    test_empty_string()
    test_only_spaces()
    test_shift_wrapping()
    test_shift_wrapping_lowercase()
    test_special_characters()
    
    print("\n✅ 所有測試都通過了！")
