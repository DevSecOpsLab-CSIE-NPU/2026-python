"""0617 任务二 — search 搜索评估

规格:search.py 包含
  1. linear_search(data: list, target) -> int
     - 逐一比对,回传 index,找不到回 -1
     - 不可修改传入的 data
  2. binary_search(data: list, target) -> int
     - 前提:data 已排序;回传 index 或 -1
     - 收到未排序 data 时自行排序
     - 不可修改传入的 data
  3. 使用 timeit 进行性能评估
  4. 将评估结果写入 README.md

评估重点:
  - 比较线性搜索和二分搜索的执行时间
  - 评估不同大小的数据集（100、1000、10000个元素）
  - 评估排序是否值得（比较排序后二分搜索的时间）
"""

import time
import bisect

from timing import timeit


class SearchError(Exception):
    """搜索时抛出的异常"""
    pass


@timeit
def linear_search(data, target):
    """线性搜索实现

    参数:
    data: 待搜索的列表
    target: 要搜索的目标

    返回值:
    如果找到目标，返回其 index；否则返回 -1

    注意:
    - 此函数不可修改传入的 data
    - 如果 data 为空，抛出 SearchError 异常
    - 执行时间会记录在 f.records 中，最后平均时间存储在 f.last_elapsed
    """
    if not data:
        raise SearchError("data 不能为空")
    
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


@timeit
def binary_search(data, target):
    """二分搜索实现

    参数:
    data: 待搜索的列表
    target: 要搜索的目标

    返回值:
    如果找到目标，返回其 index；否则返回 -1

    注意:
    - 此函数不可修改传入的 data
    - 如果 data 为空，抛出 SearchError 异常
    - 如果 data 未排序，会自动进行排序
    - 执行时间会记录在 f.records 中，最后平均时间存储在 f.last_elapsed
    """
    if not data:
        raise SearchError("data 不能为空")
    
    # 创建数据副本以避免修改原始 data
    data_copy = list(data)
    # 如果 data 未排序，自动排序
    if data_copy != sorted(data_copy):
        data_copy.sort()

    index = bisect.bisect_left(data_copy, target)
    if index < len(data_copy) and data_copy[index] == target:
        return index
    return -1