# 主題 08：容器操作與推導式 - 正式版

def filter_positive(numbers):
    """篩選出正數"""
    return [n for n in numbers if n > 0]

def double_values(numbers):
    """將所有數值乘以 2"""
    return [n * 2 for n in numbers]

def create_dict_from_pairs(pairs):
    """從鍵值對建立字典"""
    return {k: v for k, v in pairs}

def invert_dict(d):
    """反轉字典的鍵值"""
    return {v: k for k, v in d.items()}

def unique_squares(numbers):
    """計算不重複的平方值"""
    return {n * n for n in numbers}

def sum_of_squares(numbers):
    """計算平方和（使用生成器）"""
    return sum(n * n for n in numbers)

def replace_negative_with_zero(numbers):
    """將負數替換為 0"""
    return [n if n > 0 else 0 for n in numbers]

if __name__ == '__main__':
    nums = [1, -2, 3, -4]
    print("正數:", filter_positive(nums))
    print("雙倍:", double_values(nums))
    print("平方和:", sum_of_squares(nums))
    print("替換:", replace_negative_with_zero(nums))
