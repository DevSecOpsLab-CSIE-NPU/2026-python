import unittest

# 導入解答程式
# from solution_10931 import solve_10931

class TestParity(unittest.TestCase):
    """
    測試 UVA 10931 - Parity
    測試計算二進位中 1 的個數（奇偶性）
    """
    
    def get_binary_and_parity(self, num):
        """
        將數字轉換為二進位，返回二進位字符串和 1 的個數
        """
        binary = bin(num)[2:]  # 移除 '0b' 前綴
        parity = binary.count('1')
        return binary, parity
    
    def test_one(self):
        """測試 1：二進位 1，1 的個數為 1"""
        binary, parity = self.get_binary_and_parity(1)
        self.assertEqual(binary, "1")
        self.assertEqual(parity, 1)
    
    def test_two(self):
        """測試 2：二進位 10，1 的個數為 1"""
        binary, parity = self.get_binary_and_parity(2)
        self.assertEqual(binary, "10")
        self.assertEqual(parity, 1)
    
    def test_ten(self):
        """測試 10：二進位 1010，1 的個數為 2"""
        binary, parity = self.get_binary_and_parity(10)
        self.assertEqual(binary, "1010")
        self.assertEqual(parity, 2)
    
    def test_twenty_one(self):
        """測試 21：二進位 10101，1 的個數為 3"""
        binary, parity = self.get_binary_and_parity(21)
        self.assertEqual(binary, "10101")
        self.assertEqual(parity, 3)
    
    def test_seven(self):
        """測試 7：二進位 111，1 的個數為 3"""
        binary, parity = self.get_binary_and_parity(7)
        self.assertEqual(binary, "111")
        self.assertEqual(parity, 3)
    
    def test_fifteen(self):
        """測試 15：二進位 1111，1 的個數為 4"""
        binary, parity = self.get_binary_and_parity(15)
        self.assertEqual(binary, "1111")
        self.assertEqual(parity, 4)
    
    def test_max_value(self):
        """測試最大值 2147483647，計算 1 的個數"""
        binary, parity = self.get_binary_and_parity(2147483647)
        # 2147483647 的二進位為 1111111111111111111111111111111 (31個1)
        self.assertEqual(parity, 31)

if __name__ == '__main__':
    unittest.main()
