import unittest

class TestNamedSlice(unittest.TestCase):
    def test_slice_creation(self):
        SHARES = slice(20, 23)
        self.assertEqual(SHARES.start, 20)
        self.assertEqual(SHARES.stop, 23)
        self.assertIsNone(SHARES.step)
    
    def test_slice_access(self):
        record = '....................100 .......513.25 ..........'
        SHARES = slice(20, 23)
        PRICE = slice(31, 37)
        
        shares_str = record[SHARES]
        price_str = record[PRICE]
        
        self.assertEqual(shares_str, '100')
        self.assertEqual(price_str, '513.25')
    
    def test_slice_calculation(self):
        record = '....................100 .......513.25 ..........'
        SHARES = slice(20, 23)
        PRICE = slice(31, 37)
        
        cost = int(record[SHARES]) * float(record[PRICE])
        self.assertAlmostEqual(cost, 51325.0, places=1)
    
    def test_slice_with_step(self):
        s = slice(0, 10, 2)
        result = 'abcdefghij'[s]
        self.assertEqual(result, 'acegi')
    
    def test_slice_negative_indices(self):
        s = slice(-5, -1)
        result = 'abcdefghij'[s]
        self.assertEqual(result, 'fghi')
    
    def test_slice_string_extraction(self):
        data = 'NAME:John;AGE:30;CITY:NYC'
        name_slice = slice(5, 9)
        age_slice = slice(14, 16)
        
        self.assertEqual(data[name_slice], 'John')
        self.assertEqual(data[age_slice], '30')
    
    def test_slice_list(self):
        items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        s = slice(2, 7)
        self.assertEqual(items[s], [2, 3, 4, 5, 6])
    
    def test_slice_object_equality(self):
        s1 = slice(10, 20)
        s2 = slice(10, 20)
        self.assertEqual(s1, s2)
    
    def test_slice_reusable(self):
        data1 = 'abcdefghij'
        data2 = '0123456789'
        s = slice(2, 5)
        
        self.assertEqual(data1[s], 'cde')
        self.assertEqual(data2[s], '234')
    
    def test_slice_empty_result(self):
        s = slice(5, 5)
        result = 'abcdefghij'[s]
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()
