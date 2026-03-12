import unittest
from collections import namedtuple

class TestNamedTuple(unittest.TestCase):
    def test_namedtuple_creation(self):
        Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
        sub = Subscriber('jonesy@example.com', '2012-10-19')
        
        self.assertEqual(sub.addr, 'jonesy@example.com')
        self.assertEqual(sub.joined, '2012-10-19')
    
    def test_namedtuple_access_by_index(self):
        Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
        sub = Subscriber('jonesy@example.com', '2012-10-19')
        
        self.assertEqual(sub[0], 'jonesy@example.com')
        self.assertEqual(sub[1], '2012-10-19')
    
    def test_namedtuple_unpacking(self):
        Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
        sub = Subscriber('jonesy@example.com', '2012-10-19')
        
        addr, joined = sub
        self.assertEqual(addr, 'jonesy@example.com')
        self.assertEqual(joined, '2012-10-19')
    
    def test_namedtuple_replace(self):
        Stock = namedtuple('Stock', ['name', 'shares', 'price'])
        s = Stock('ACME', 100, 123.45)
        
        s = s._replace(shares=75)
        self.assertEqual(s.shares, 75)
        self.assertEqual(s.name, 'ACME')
        self.assertEqual(s.price, 123.45)
    
    def test_namedtuple_immutable(self):
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(1, 2)
        
        with self.assertRaises(AttributeError):
            p.x = 5
    
    def test_namedtuple_iteration(self):
        Stock = namedtuple('Stock', ['name', 'shares', 'price'])
        s = Stock('ACME', 100, 123.45)
        
        values = list(s)
        self.assertEqual(values, ['ACME', 100, 123.45])
    
    def test_namedtuple_asdict(self):
        Point = namedtuple('Point', ['x', 'y'])
        p = Point(1, 2)
        
        d = p._asdict()
        self.assertEqual(d, {'x': 1, 'y': 2})
    
    def test_namedtuple_make(self):
        Stock = namedtuple('Stock', ['name', 'shares', 'price'])
        values = ('ACME', 100, 123.45)
        
        s = Stock._make(values)
        self.assertEqual(s.name, 'ACME')
        self.assertEqual(s.shares, 100)
    
    def test_namedtuple_multiple_replace(self):
        Person = namedtuple('Person', ['name', 'age', 'city'])
        p = Person('John', 30, 'NYC')
        
        p = p._replace(age=31, city='LA')
        self.assertEqual(p.name, 'John')
        self.assertEqual(p.age, 31)
        self.assertEqual(p.city, 'LA')
    
    def test_namedtuple_fields(self):
        Stock = namedtuple('Stock', ['name', 'shares', 'price'])
        self.assertEqual(Stock._fields, ('name', 'shares', 'price'))
    
    def test_namedtuple_defaults(self):
        Stock = namedtuple('Stock', ['name', 'shares', 'price'], defaults=[100, 50.0])
        s = Stock('ACME')
        
        self.assertEqual(s.name, 'ACME')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 50.0)
    
    def test_namedtuple_in_list(self):
        Point = namedtuple('Point', ['x', 'y'])
        points = [Point(0, 0), Point(1, 1), Point(2, 2)]
        
        self.assertEqual(len(points), 3)
        self.assertEqual(points[0].x, 0)
        self.assertEqual(points[2].y, 2)

if __name__ == '__main__':
    unittest.main()
