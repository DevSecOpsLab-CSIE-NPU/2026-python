import unittest
from benchmark import make_data


class TestSecurity(unittest.TestCase):
    def test_make_data_rejects_negative(self):
        # 測試 make_data 是否拒絕負數 size，預期拋出 ValueError
        with self.assertRaises(ValueError):
            make_data(-10)

    def test_make_data_rejects_huge_size(self):
        # 測試 make_data 是否拒絕過大的 size (安全閾值 100000)，預期拋出 ValueError
        with self.assertRaises(ValueError):
            make_data(200000)

    def test_make_data_rejects_invalid_seed_type(self):
        # 測試 make_data 是否限制 seed 必須為整數以確保安全與可重現性，預期拋出 TypeError
        with self.assertRaises(TypeError):
            make_data(10, seed="invalid_seed")


if __name__ == "__main__":
    unittest.main()
