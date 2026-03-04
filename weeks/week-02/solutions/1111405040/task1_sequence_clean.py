"""
Task 1: Sequence Clean
給定一行以空白分隔的整數，輸出：
1. 去重後（保留第一次出現順序）的序列
2. 由小到大排序結果
3. 由大到小排序結果
4. 偶數序列（維持原始順序）
"""


def deduplicate(numbers):
    """
    去重序列，保留第一次出現的順序。
    
    Args:
        numbers: 整數列表
    
    Returns:
        去重後的列表
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def sort_ascending(numbers):
    """
    將序列由小到大排序。
    
    Args:
        numbers: 整數列表
    
    Returns:
        排序後的列表（遞增）
    """
    return sorted(numbers)


def sort_descending(numbers):
    """
    將序列由大到小排序。
    
    Args:
        numbers: 整數列表
    
    Returns:
        排序後的列表（遞減）
    """
    return sorted(numbers, reverse=True)


def filter_evens(numbers):
    """
    篩選偶數，保持原始順序。
    
    Args:
        numbers: 整數列表
    
    Returns:
        只含偶數的列表，維持原始順序
    """
    return [num for num in numbers if num % 2 == 0]


def sequence_clean(input_line):
    """
    主函式：處理序列清理。
    
    Args:
        input_line: 以空白分隔的整數字串
    
    Returns:
        字典，包含四種結果
    """
    numbers = list(map(int, input_line.split()))
    
    return {
        'dedupe': deduplicate(numbers),
        'asc': sort_ascending(numbers),
        'desc': sort_descending(numbers),
        'evens': filter_evens(numbers)
    }


def format_output(results):
    """
    格式化輸出結果。
    
    Args:
        results: 由 sequence_clean 返回的字典
    
    Returns:
        格式化的字串
    """
    lines = [
        f"dedupe: {' '.join(map(str, results['dedupe']))}",
        f"asc: {' '.join(map(str, results['asc']))}",
        f"desc: {' '.join(map(str, results['desc']))}",
        f"evens: {' '.join(map(str, results['evens']))}"
    ]
    return '\n'.join(lines)


def main():
    """主程式入口。"""
    input_line = input().strip()
    results = sequence_clean(input_line)
    print(format_output(results))


if __name__ == '__main__':
    main()
