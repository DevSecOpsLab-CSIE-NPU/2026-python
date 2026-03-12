import unittest
from operator import itemgetter

class TestItemGetter(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {'fname': 'Brian', 'uid': 1003, 'lname': 'Jones'},
            {'fname': 'John', 'uid': 1001, 'lname': 'Doe'},
            {'fname': 'Alice', 'uid': 1002, 'lname': 'Smith'}
        ]
    
    def test_itemgetter_single_key(self):
        sorted_rows = sorted(self.rows, key=itemgetter('fname'))
        self.assertEqual(sorted_rows[0]['fname'], 'Alice')
        self.assertEqual(sorted_rows[1]['fname'], 'Brian')
        self.assertEqual(sorted_rows[2]['fname'], 'John')
    
    def test_itemgetter_by_uid(self):
        sorted_rows = sorted(self.rows, key=itemgetter('uid'))
        self.assertEqual(sorted_rows[0]['uid'], 1001)
        self.assertEqual(sorted_rows[1]['uid'], 1002)
        self.assertEqual(sorted_rows[2]['uid'], 1003)
    
    def test_itemgetter_multiple_keys(self):
        rows = [
            {'lname': 'Smith', 'fname': 'John'},
            {'lname': 'Smith', 'fname': 'Alice'},
            {'lname': 'Doe', 'fname': 'John'}
        ]
        sorted_rows = sorted(rows, key=itemgetter('lname', 'fname'))
        
        self.assertEqual(sorted_rows[0]['lname'], 'Doe')
        self.assertEqual(sorted_rows[1]['lname'], 'Smith')
        self.assertEqual(sorted_rows[1]['fname'], 'Alice')
        self.assertEqual(sorted_rows[2]['fname'], 'John')
    
    def test_itemgetter_reverse(self):
        sorted_rows = sorted(self.rows, key=itemgetter('uid'), reverse=True)
        self.assertEqual(sorted_rows[0]['uid'], 1003)
        self.assertEqual(sorted_rows[2]['uid'], 1001)
    
    def test_itemgetter_on_list(self):
        data = [('John', 30), ('Alice', 25), ('Bob', 35)]
        sorted_data = sorted(data, key=itemgetter(1))
        
        self.assertEqual(sorted_data[0], ('Alice', 25))
        self.assertEqual(sorted_data[1], ('John', 30))
        self.assertEqual(sorted_data[2], ('Bob', 35))
    
    def test_itemgetter_callable(self):
        getter = itemgetter('fname')
        result = getter(self.rows[0])
        self.assertEqual(result, 'Brian')
    
    def test_itemgetter_multiple_keys_callable(self):
        getter = itemgetter('uid', 'fname')
        result = getter(self.rows[0])
        self.assertEqual(result, (1003, 'Brian'))
    
    def test_itemgetter_with_max(self):
        row = max(self.rows, key=itemgetter('uid'))
        self.assertEqual(row['fname'], 'Brian')
        self.assertEqual(row['uid'], 1003)
    
    def test_itemgetter_with_min(self):
        row = min(self.rows, key=itemgetter('uid'))
        self.assertEqual(row['fname'], 'John')
        self.assertEqual(row['uid'], 1001)
    
    def test_itemgetter_missing_key(self):
        with self.assertRaises(KeyError):
            sorted(self.rows, key=itemgetter('missing_key'))

if __name__ == '__main__':
    unittest.main()
