import unittest
from collections import Counter

class TestCounter(unittest.TestCase):
    def test_counter_creation(self):
        words = ['look', 'into', 'my', 'eyes', 'look']
        word_counts = Counter(words)
        
        self.assertEqual(word_counts['look'], 2)
        self.assertEqual(word_counts['into'], 1)
        self.assertEqual(word_counts['eyes'], 1)
        self.assertEqual(word_counts['my'], 1)
    
    def test_counter_most_common(self):
        words = ['look', 'into', 'my', 'eyes', 'look']
        word_counts = Counter(words)
        top_3 = word_counts.most_common(3)
        
        self.assertEqual(len(top_3), 3)
        self.assertEqual(top_3[0][0], 'look')
        self.assertEqual(top_3[0][1], 2)
    
    def test_counter_most_common_single(self):
        words = ['a', 'b', 'a', 'c', 'a']
        word_counts = Counter(words)
        top_1 = word_counts.most_common(1)
        
        self.assertEqual(top_1[0], ('a', 3))
    
    def test_counter_update(self):
        words = ['look', 'into', 'my', 'eyes', 'look']
        word_counts = Counter(words)
        
        self.assertEqual(word_counts['eyes'], 1)
        word_counts.update(['eyes', 'eyes'])
        self.assertEqual(word_counts['eyes'], 3)
    
    def test_counter_update_multiple(self):
        c = Counter(['a', 'b'])
        c.update(['a', 'c', 'c'])
        
        self.assertEqual(c['a'], 2)
        self.assertEqual(c['b'], 1)
        self.assertEqual(c['c'], 2)
    
    def test_counter_from_dict(self):
        c = Counter({'red': 4, 'blue': 2})
        self.assertEqual(c['red'], 4)
        self.assertEqual(c['blue'], 2)
    
    def test_counter_arithmetic_add(self):
        c1 = Counter(a=3, b=1)
        c2 = Counter(a=1, b=2)
        result = c1 + c2
        
        self.assertEqual(result['a'], 4)
        self.assertEqual(result['b'], 3)
    
    def test_counter_arithmetic_subtract(self):
        c1 = Counter(a=3, b=2)
        c2 = Counter(a=1, b=1)
        result = c1 - c2
        
        self.assertEqual(result['a'], 2)
        self.assertEqual(result['b'], 1)
    
    def test_counter_most_common_all(self):
        c = Counter(['x', 'y', 'x', 'z'])
        all_elements = c.most_common()
        
        self.assertEqual(len(all_elements), 3)
        self.assertEqual(all_elements[0], ('x', 2))
    
    def test_counter_elements(self):
        c = Counter(a=3, b=1)
        elements = list(c.elements())
        
        self.assertIn('a', elements)
        self.assertEqual(elements.count('a'), 3)
        self.assertEqual(elements.count('b'), 1)

if __name__ == '__main__':
    unittest.main()
