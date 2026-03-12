import unittest

class TestDedupe(unittest.TestCase):
    def test_dedupe_basic(self):
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
        
        result = list(dedupe([1, 5, 2, 1, 9, 1, 5, 10]))
        self.assertEqual(result, [1, 5, 2, 9, 10])
    
    def test_dedupe_strings(self):
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
        
        result = list(dedupe(['look', 'into', 'look', 'my', 'into']))
        self.assertEqual(result, ['look', 'into', 'my'])
    
    def test_dedupe_order_preserved(self):
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
        
        result = list(dedupe(['z', 'a', 'z', 'b', 'a']))
        self.assertEqual(result, ['z', 'a', 'b'])
    
    def test_dedupe_with_key(self):
        def dedupe2(items, key=None):
            seen = set()
            for item in items:
                val = item if key is None else key(item)
                if val not in seen:
                    yield item
                    seen.add(val)
        
        result = list(dedupe2(['a', 'B', 'c', 'A'], key=str.lower))
        self.assertEqual(result, ['a', 'B', 'c'])
    
    def test_dedupe_with_key_on_dicts(self):
        def dedupe2(items, key=None):
            seen = set()
            for item in items:
                val = item if key is None else key(item)
                if val not in seen:
                    yield item
                    seen.add(val)
        
        items = [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}, {'id': 1, 'name': 'c'}]
        result = list(dedupe2(items, key=lambda d: d['id']))
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'a')
        self.assertEqual(result[1]['name'], 'b')
    
    def test_dedupe_empty(self):
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
        
        result = list(dedupe([]))
        self.assertEqual(result, [])
    
    def test_dedupe_single_element(self):
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
        
        result = list(dedupe([42]))
        self.assertEqual(result, [42])
    
    def test_dedupe_all_same(self):
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
        
        result = list(dedupe([1, 1, 1, 1]))
        self.assertEqual(result, [1])
    
    def test_dedupe_no_duplicates(self):
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
        
        result = list(dedupe([1, 2, 3, 4, 5]))
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_dedupe_generator_lazy(self):
        def dedupe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)
        
        gen = dedupe([1, 2, 1, 3])
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)

if __name__ == '__main__':
    unittest.main()
