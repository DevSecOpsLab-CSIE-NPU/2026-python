import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_sample_case_with_my_parameter(self):
        """測試考卷範例，使用我學號對應的 SHIFT = 2 進行加密"""
        from caesar import caesar_cipher
        # H->J, e->g, l->n, l->n, o->q, N->O, P->R, U->W
        self.assertEqual(caesar_cipher("Hello, NPU!", shift=2), "Jgnnq, ORW!")
        self.assertEqual(caesar_cipher("abc XYZ", shift=2), "cde ZAB")

    def test_non_alpha_characters(self):
        """Edge Case: 非字母字元（數字、符號、空白）應保持不變"""
        from caesar import caesar_cipher
        self.assertEqual(caesar_cipher("123!@# ", shift=2), "123!@# ")

if __name__ == "__main__":
    unittest.main()