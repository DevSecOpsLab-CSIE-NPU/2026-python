"""Week 05 in-class: enumerate 與 zip 練習（標準版）

此檔案將教學示範整理成可重複使用的函式，
方便單元測試與後續複習。
"""

from itertools import zip_longest


def enumerate_colors(colors, start=0):
    """回傳帶索引的顏色字串列表。"""
    result = []
    for i, color in enumerate(colors, start):
        result.append(f"{i}: {color}")
    return result


def number_lines(lines, start=1):
    """模擬行號輸出，常見於讀檔時為每行加上編號。"""
    result = []
    for lineno, line in enumerate(lines, start):
        result.append(f"行 {lineno}: {line}")
    return result


def pair_names_scores(names, scores):
    """使用 zip 將姓名與分數配對。"""
    return [f"{name}: {score}" for name, score in zip(names, scores)]


def sum_zipped_three(a, b, c):
    """同時遍歷三個序列，回傳每組元素的加總。"""
    return [x + y + z for x, y, z in zip(a, b, c)]


def zip_shortest(x, y):
    """zip 在長度不同時會以較短序列為準。"""
    return list(zip(x, y))


def zip_longest_with_fill(x, y, fillvalue=0):
    """zip_longest 會補齊較短序列，空缺處使用 fillvalue。"""
    return list(zip_longest(x, y, fillvalue=fillvalue))


def build_dict(keys, values):
    """常見技巧：把 keys 與 values 合併成字典。"""
    return dict(zip(keys, values))


def demo():
    """示範執行輸出，保留教學可讀性。"""
    colors = ["red", "green", "blue"]
    print("--- enumerate() 基本用法 ---")
    for line in enumerate_colors(colors):
        print(line)

    print("\n--- enumerate(start=1) ---")
    for line in enumerate_colors(colors, 1):
        print(f"第{line}")

    print("\n--- enumerate with 檔案 ---")
    for line in number_lines(["line1", "line2", "line3"]):
        print(line)

    print("\n--- zip() 基本用法 ---")
    for line in pair_names_scores(["Alice", "Bob", "Carol"], [90, 85, 92]):
        print(line)

    print("\n--- zip() 多個序列 ---")
    for total in sum_zipped_three([1, 2, 3], [10, 20, 30], [100, 200, 300]):
        print(total)

    print("\n--- zip() 長度不同 ---")
    print(zip_shortest([1, 2], ["a", "b", "c"]))
    print(zip_longest_with_fill([1, 2], ["a", "b", "c"], fillvalue=0))

    print("\n--- 建立字典 ---")
    print(build_dict(["name", "age", "city"], ["John", "30", "NYC"]))


if __name__ == "__main__":
    demo()
