# 單元測試：主題 11（Hello World）

import unittest
import importlib

# 動態導入 11_formal 模組
formal_11 = importlib.import_module('11_formal')
hello_world = formal_11.hello_world
hello_with_name = formal_11.hello_with_name

class TestHelloWorld(unittest.TestCase):
    
    def test_hello_world(self):
        """測試 Hello World"""
        result = hello_world()
        self.assertEqual(result, 'Hello, World!')
    
    def test_hello_with_name(self):
        """測試帶名字的問候"""
        result = hello_with_name('Alice')
        self.assertEqual(result, 'Hello, Alice!')

if __name__ == '__main__':
    unittest.main()
