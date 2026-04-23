# 主題 05：索引與切片 - 正式版

def string_indexing():
    """展示字串索引和切片"""
    text = 'abcdefg'
    return {
        'full': text,
        'first': text[0],
        'last': text[-1],
        'mid': text[2:5]
    }

def list_slicing():
    """展示 list 切片"""
    nums = [10, 20, 30, 40, 50]
    return {
        'full': nums,
        'first': nums[0],
        'last_two': nums[-2:],
        'first_three': nums[:3],
        'every_other': nums[::2]
    }

if __name__ == '__main__':
    print("字串:", string_indexing())
    print("列表:", list_slicing())
