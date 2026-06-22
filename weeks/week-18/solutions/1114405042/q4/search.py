"""三种搜索算法实现

实现三个搜索函数，供第4题使用。
- linear_search: 线性搜索，从头到尾逐一比较
- binary_search: 二分搜索，要求输入数据已排序
- set_search: 哈希集合搜索，使用集合实现O(1)查找

注意事项：
1. 不可修改输入的data（保持原始数据不变）
2. 函数名和签名必须保持不变，否则测试会导入失败
3. 返回类型不同：linear/binary返回int（索引），set_search返回bool（存在性）
4. binary_search收到未排序的数据时的行为需要明确定义并写入docstring
"""

from typing import List, Any


def linear_search(data: List[Any], target: Any) -> int:
    """线性搜索

    从头到尾逐一比较数据，返回找到的元素索引，如果找不到返回-1。

    参数:
        data: 要搜索的数据列表
        target: 要查找的目标元素

    返回:
        找到的目标元素的索引，如果找不到返回-1
    """
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


def binary_search(data: List[Any], target: Any) -> int:
    """二分搜索

    前提：输入数据必须已排序（升序）。如果收到未排序的数据，
    将返回-1并提示呼叫者需要先对数据进行排序。

    参数:
        data: 已排序的数据列表
        target: 要查找的目标元素

    返回:
        找到的目标元素的索引，如果找不到返回-1
        如果输入数据未排序，返回-2
    """
    # 检查数据是否已排序
    for i in range(1, len(data)):
        if data[i] < data[i-1]:
            return -2  # 数据未排序

    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def set_search(data: List[Any], target: Any) -> bool:
    """哈希集合搜索

    将数据转换为集合，使用O(1)的哈希查找时间复杂度，
    返回目标元素是否存在。

    参数:
        data: 要搜索的数据列表
        target: 要查找的目标元素

    返回:
        True表示找到目标元素，False表示找不到
    """
    return target in set(data)


if __name__ == "__main__":
    # 简单的测试
    test_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7

    linear_result = linear_search(test_data, target)
    binary_result = binary_search(test_data, target)
    set_result = set_search(test_data, target)

    print(f"线性搜索结果: {linear_result}")
    print(f"二分搜索结果: {binary_result}")
    print(f"集合搜索结果: {set_result}")