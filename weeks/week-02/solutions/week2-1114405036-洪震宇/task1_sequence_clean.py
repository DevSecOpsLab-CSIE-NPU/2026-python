"""
Task 1: Sequence Clean
回家作業：去重、排序、篩選序列
"""


def deduplicate(numbers):
    """
    去重，保留第一次出現的順序
    
    Args:
        numbers: list of integers
        
    Returns:
        list: 去重後的列表
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
    由小到大排序
    
    Args:
        numbers: list of integers
        
    Returns:
        list: 排序後的列表
    """
    return sorted(numbers)


def sort_descending(numbers):
    """
    由大到小排序
    
    Args:
        numbers: list of integers
        
    Returns:
        list: 排序後的列表
    """
    return sorted(numbers, reverse=True)


def filter_evens(numbers):
    """
    篩選偶數，維持原始順序
    
    Args:
        numbers: list of integers
        
    Returns:
        list: 偶數列表
    """
    return [num for num in numbers if num % 2 == 0]


def process_sequence(input_string):
    """
    主要處理函式，執行完整的序列清理流程
    
    Args:
        input_string: 以空白分隔的整數字串
        
    Returns:
        dict: 包含 dedupe、asc、desc、evens 的結果
    """
    # 解析輸入
    numbers = list(map(int, input_string.split()))
    
    # 執行各種操作
    dedupe_result = deduplicate(numbers)
    asc_result = sort_ascending(numbers)
    desc_result = sort_descending(numbers)
    evens_result = filter_evens(numbers)
    
    return {
        'dedupe': dedupe_result,
        'asc': asc_result,
        'desc': desc_result,
        'evens': evens_result
    }


def format_output(results):
    """
    格式化輸出結果
    
    Args:
        results: process_sequence 返回的 dict
        
    Returns:
        str: 格式化的輸出字串
    """
    lines = []
    for key, values in results.items():
        values_str = ' '.join(map(str, values))
        lines.append(f"{key}: {values_str}")
    return '\n'.join(lines)


def main():
    """主程式"""
    print("=== Task 1: Sequence Clean ===")
    print("輸入整數序列（空白分隔）:")
    
    input_str = input().strip()
    
    if not input_str:
        print("錯誤：輸入不能為空")
        return
    
    try:
        results = process_sequence(input_str)
        output = format_output(results)
        print("\n輸出:")
        print(output)
    except ValueError as e:
        print(f"錯誤：無效的輸入 - {e}")


if __name__ == "__main__":
    main()
