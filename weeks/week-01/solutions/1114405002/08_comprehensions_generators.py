import unittest

# 測試類別：測試容器操作與推導式
# 這個類別包含測試列表推導式、字典推導式和生成器表達式的單元測試
class TestComprehensionsGenerators(unittest.TestCase):

    # 測試方法：測試列表推導式用於過濾序列
    # 列表推導式可以簡潔地過濾和轉換序列，這裡測試過濾出正數
    def test_list_comprehension_filter(self):
        # 準備測試資料：包含正數和負數的列表
        data = [-1, 2, -3, 4, -5]
        # 使用列表推導式過濾出大於0的元素
        result = [x for x in data if x > 0]
        # 預期結果：只有正數
        expected = [2, 4]
        # 斷言結果等於預期
        self.assertEqual(result, expected)

    # 測試方法：測試字典推導式用於創建字典子集
    # 字典推導式類似列表推導式，但用於字典，這裡測試過濾鍵值對
    def test_dict_comprehension(self):
        # 準備測試資料：一個字典
        d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        # 使用字典推導式過濾出值大於2的鍵值對
        result = {k: v for k, v in d.items() if v > 2}
        # 預期結果：只包含 'c' 和 'd'
        expected = {'c': 3, 'd': 4}
        # 斷言結果等於預期
        self.assertEqual(result, expected)

    # 測試方法：測試生成器表達式用於計算總和
    # 生成器表達式類似列表推導式，但返回生成器，適合大資料或鏈式操作
    def test_generator_expression(self):
        # 準備測試資料：數字列表
        nums = [1, 2, 3, 4, 5]
        # 使用生成器表達式計算每個數字的平方，並求總和
        result = sum(x * x for x in nums)
        # 預期結果：1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
        expected = 55  # 1+4+9+16+25
        # 斷言結果等於預期
        self.assertEqual(result, expected)

# 如果直接運行此檔案，執行所有測試
if __name__ == '__main__':
    unittest.main()