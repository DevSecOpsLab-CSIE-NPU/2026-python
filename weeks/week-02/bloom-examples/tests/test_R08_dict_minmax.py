"""
測試 R08: 字典運算 min/max/sorted + zip
驗證使用 zip, min, max, sorted 進行字典操作
"""

import unittest


class TestDictMinMax(unittest.TestCase):
    """字典 min/max 運算測試"""
    
    def setUp(self):
        """設定測試用的字典"""
        self.prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}
    
    def test_zip_values_keys(self):
        """測試 zip 價格和鍵"""
        zipped = list(zip(self.prices.values(), self.prices.keys()))
        
        # 應該得到 (價格, 鍵) 的元組
        self.assertEqual(len(zipped), 3)
        self.assertIn((45.23, 'ACME'), zipped)
        self.assertIn((612.78, 'AAPL'), zipped)
        self.assertIn((10.75, 'FB'), zipped)
    
    def test_min_price_and_key(self):
        """測試找最小價格及對應的鍵"""
        result = min(zip(self.prices.values(), self.prices.keys()))
        
        price, key = result
        self.assertEqual(price, 10.75)
        self.assertEqual(key, 'FB')
    
    def test_max_price_and_key(self):
        """測試找最大價格及對應的鍵"""
        result = max(zip(self.prices.values(), self.prices.keys()))
        
        price, key = result
        self.assertEqual(price, 612.78)
        self.assertEqual(key, 'AAPL')
    
    def test_sorted_by_price(self):
        """測試按價格排序"""
        sorted_result = sorted(zip(self.prices.values(), self.prices.keys()))
        
        # 應該按價格從小到大排序
        prices_only = [price for price, key in sorted_result]
        self.assertEqual(prices_only, [10.75, 45.23, 612.78])
        
        keys_only = [key for price, key in sorted_result]
        self.assertEqual(keys_only, ['FB', 'ACME', 'AAPL'])
    
    def test_min_key_by_value(self):
        """測試使用 key 參數找最小值對應的鍵"""
        result = min(self.prices, key=lambda k: self.prices[k])
        
        self.assertEqual(result, 'FB')
    
    def test_max_key_by_value(self):
        """測試使用 key 參數找最大值對應的鍵"""
        result = max(self.prices, key=lambda k: self.prices[k])
        
        self.assertEqual(result, 'AAPL')
    
    def test_sorted_keys_by_value(self):
        """測試按值排序鍵"""
        sorted_keys = sorted(self.prices, key=lambda k: self.prices[k])
        
        self.assertEqual(sorted_keys, ['FB', 'ACME', 'AAPL'])
    
    def test_empty_dict(self):
        """測試空字典"""
        empty = {}
        
        zipped = list(zip(empty.values(), empty.keys()))
        self.assertEqual(zipped, [])
    
    def test_single_entry(self):
        """測試單一條目的字典"""
        single = {'GOOG': 2800.50}
        
        result = min(zip(single.values(), single.keys()))
        self.assertEqual(result, (2800.50, 'GOOG'))
        
        result = max(zip(single.values(), single.keys()))
        self.assertEqual(result, (2800.50, 'GOOG'))
    
    def test_reverse_sort_by_price(self):
        """測試按價格反向排序"""
        sorted_result = sorted(
            zip(self.prices.values(), self.prices.keys()),
            reverse=True
        )
        
        prices_only = [price for price, key in sorted_result]
        self.assertEqual(prices_only, [612.78, 45.23, 10.75])
    
    def test_zip_different_structures(self):
        """測試 zip 不同長度的序列"""
        values = [1, 2, 3]
        keys = ['a', 'b']
        
        zipped = list(zip(values, keys))
        # zip 會截斷到最短的長度
        self.assertEqual(zipped, [(1, 'a'), (2, 'b')])
    
    def test_dict_comprehension_from_zip(self):
        """測試從 zip 創建新字典"""
        zipped = zip(self.prices.values(), self.prices.keys())
        new_dict = {key: price for price, key in zipped}
        
        # 應該是反向的字典（鍵變值，值變鍵）
        self.assertEqual(new_dict['ACME'], 45.23)
        self.assertEqual(new_dict['AAPL'], 612.78)


if __name__ == '__main__':
    unittest.main()
