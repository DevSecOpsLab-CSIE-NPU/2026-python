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
    去重序列，保留第一次出現的順序
    
    Args:
        numbers: 整數列表
    
    Returns:
        去重後的列表（保持原序）
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def sort_ascending(numbers):
    """由小到大排序"""
    return sorted(numbers)


def sort_descending(numbers):
    """由大到小排序"""
    return sorted(numbers, reverse=True)


def filter_evens(numbers):
    """
    篩選偶數，維持原始順序
    
    Args:
        numbers: 整數列表
    
    Returns:
        只包含偶數的列表（原順序）
    """
    return [num for num in numbers if num % 2 == 0]


def process_sequence(input_line):
    """
    主要處理函式：
    解析輸入、執行所有處理、返回格式化結果
    
    Args:
        input_line: 空白分隔的整數字符串
    
    Returns:
        四行輸出：dedupe, asc, desc, evens
    """
    # 解析輸入
    numbers = list(map(int, input_line.split()))
    
    # 執行各項處理
    dedup = deduplicate(numbers)
    asc = sort_ascending(numbers)
    desc = sort_descending(numbers)
    evens = filter_evens(numbers)
    
    # 格式化輸出
    output = [
        f"dedupe: {' '.join(map(str, dedup))}",
        f"asc: {' '.join(map(str, asc))}",
        f"desc: {' '.join(map(str, desc))}",
        f"evens: {' '.join(map(str, evens))}"
    ]
    
    return output


def main():
    """主程式入口"""
    try:
        input_line = input().strip()
        results = process_sequence(input_line)
        for line in results:
            print(line)
    except EOFError:
        pass


if __name__ == "__main__":
    main()
