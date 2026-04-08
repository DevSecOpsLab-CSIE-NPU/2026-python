"""
================================================================================
Task 1: Sequence Clean
================================================================================

題目說明：
    給定一行以空白分隔的整數，請輸出：
    1. 去重後（保留第一次出現順序）的序列
    2. 由小到大排序結果
    3. 由大到小排序結果
    4. 偶數序列（維持原始順序）

================================================================================
"""

from typing import List, Dict


def sequence_clean(input_str: str) -> Dict[str, List[int]]:
    """
    處理序列資料

    參數：
        input_str: 以空白分隔的整數字串

    回傳：
        包含 dedupe, asc, desc, evens 四個鍵的字典
    """
    # 解析輸入
    numbers = list(map(int, input_str.split())) if input_str.strip() else []

    # 去重（保留第一次出現順序）
    seen = set()
    dedupe = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            dedupe.append(num)

    # 由小到大排序
    asc = sorted(numbers)

    # 由大到小排序
    desc = sorted(numbers, reverse=True)

    # 偶數序列（維持原始順序）
    evens = [num for num in numbers if num % 2 == 0]

    return {"dedupe": dedupe, "asc": asc, "desc": desc, "evens": evens}


def main():
    """主函式：讀取輸入並輸出結果"""
    try:
        input_str = input().strip()
        result = sequence_clean(input_str)

        print("dedupe: " + " ".join(map(str, result["dedupe"])))
        print("asc: " + " ".join(map(str, result["asc"])))
        print("desc: " + " ".join(map(str, result["desc"])))
        print("evens: " + " ".join(map(str, result["evens"])))
    except EOFError:
        pass


if __name__ == "__main__":
    main()
