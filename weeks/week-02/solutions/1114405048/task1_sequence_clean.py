"""
Task 1: Sequence Clean
實現對序列的去重、排序和過濾功能
"""


def deduplicate(numbers):
    """去重後回傳，保留第一次出現順序"""
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def sort_asc(numbers):
    """由小到大排序"""
    return sorted(numbers)


def sort_desc(numbers):
    """由大到小排序"""
    return sorted(numbers, reverse=True)


def filter_evens(numbers):
    """提取偶數，保留原始順序"""
    return [num for num in numbers if num % 2 == 0]


def process_sequence(input_string):
    """主流程：輸入字符串，輸出四項結果"""
    numbers = list(map(int, input_string.split()))
    
    results = {
        'dedupe': deduplicate(numbers),
        'asc': sort_asc(numbers),
        'desc': sort_desc(numbers),
        'evens': filter_evens(numbers)
    }
    
    return results


def format_output(results):
    """格式化輸出為指定格式"""
    lines = []
    for key in ['dedupe', 'asc', 'desc', 'evens']:
        line = f"{key}: {' '.join(map(str, results[key]))}"
        lines.append(line)
    return '\n'.join(lines)


if __name__ == '__main__':
    # 測試預設例子
    test_input = "5 3 5 2 9 2 8 3 1"
    results = process_sequence(test_input)
    print(format_output(results))
