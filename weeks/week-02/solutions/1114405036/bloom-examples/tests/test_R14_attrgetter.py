import unittest
from operator import attrgetter

class User:
    def __init__(self, user_id, name=None, age=None):
        self.user_id = user_id
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"User({self.user_id}, {self.name}, {self.age})"

class TestAttrGetter(unittest.TestCase):
    def setUp(self):
        self.users = [User(23, 'Alice', 30), User(3, 'Bob', 25), User(99, 'Charlie', 35)]
    
    def test_attrgetter_single_attr(self):
        sorted_users = sorted(self.users, key=attrgetter('user_id'))
        self.assertEqual(sorted_users[0].user_id, 3)
        self.assertEqual(sorted_users[1].user_id, 23)
        self.assertEqual(sorted_users[2].user_id, 99)
    
    def test_attrgetter_by_name(self):
        sorted_users = sorted(self.users, key=attrgetter('name'))
        self.assertEqual(sorted_users[0].name, 'Alice')
        self.assertEqual(sorted_users[1].name, 'Bob')
        self.assertEqual(sorted_users[2].name, 'Charlie')
    
    def test_attrgetter_by_age(self):
        sorted_users = sorted(self.users, key=attrgetter('age'))
        self.assertEqual(sorted_users[0].age, 25)
        self.assertEqual(sorted_users[1].age, 30)
        self.assertEqual(sorted_users[2].age, 35)
    
    def test_attrgetter_multiple_attrs(self):
        users = [
            User(1, 'Charlie', 30),
            User(2, 'Alice', 30),
            User(3, 'Bob', 25)
        ]
        sorted_users = sorted(users, key=attrgetter('age', 'name'))
        
        self.assertEqual(sorted_users[0].user_id, 3)
        self.assertEqual(sorted_users[1].user_id, 2)
        self.assertEqual(sorted_users[2].user_id, 1)
    
    def test_attrgetter_reverse(self):
        sorted_users = sorted(self.users, key=attrgetter('user_id'), reverse=True)
        self.assertEqual(sorted_users[0].user_id, 99)
        self.assertEqual(sorted_users[2].user_id, 3)
    
    def test_attrgetter_callable(self):
        getter = attrgetter('user_id')
        result = getter(self.users[0])
        self.assertEqual(result, 23)
    
    def test_attrgetter_multiple_attrs_callable(self):
        getter = attrgetter('user_id', 'name')
        result = getter(self.users[0])
        self.assertEqual(result, (23, 'Alice'))
    
    def test_attrgetter_with_max(self):
        user = max(self.users, key=attrgetter('user_id'))
        self.assertEqual(user.user_id, 99)
    
    def test_attrgetter_with_min(self):
        user = min(self.users, key=attrgetter('user_id'))
        self.assertEqual(user.user_id, 3)
    
    def test_attrgetter_missing_attr(self):
        with self.assertRaises(AttributeError):
            sorted(self.users, key=attrgetter('missing_attr'))

if __name__ == '__main__':
    unittest.main()
