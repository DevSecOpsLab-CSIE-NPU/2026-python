"""Week 05 in-class: enumerate 與 zip 練習（好記版）

此版本強調「少函式、少語法」，
以最直覺的寫法幫助初學者記憶。
"""

from itertools import zip_longest


def run_enumerate_zip_examples():
    """一次回傳所有範例結果，方便測試與比對。"""
    data = {}

    # enumerate：索引 + 值
    colors = ["red", "green", "blue"]
    data["enumerate0"] = [f"{i}: {color}" for i, color in enumerate(colors)]
    data["enumerate1"] = [f"{i}: {color}" for i, color in enumerate(colors, 1)]

    # 用 enumerate 做行號
    lines = ["line1", "line2", "line3"]
    data["lines"] = [f"行 {i}: {line}" for i, line in enumerate(lines, 1)]

    # zip：把兩個列表一組一組配對
    names = ["Alice", "Bob", "Carol"]
    scores = [90, 85, 92]
    data["name_scores"] = [f"{name}: {score}" for name, score in zip(names, scores)]

    # zip 可同時走三個序列
    a = [1, 2, 3]
    b = [10, 20, 30]
    c = [100, 200, 300]
    data["sum_three"] = [x + y + z for x, y, z in zip(a, b, c)]

    # 長度不同時，zip 只走到最短
    x = [1, 2]
    y = ["a", "b", "c"]
    data["zip_short"] = list(zip(x, y))

    # 想補齊就用 zip_longest
    data["zip_long"] = list(zip_longest(x, y, fillvalue=0))

    # 常見應用：兩個列表轉字典
    keys = ["name", "age", "city"]
    values = ["John", "30", "NYC"]
    data["dict"] = dict(zip(keys, values))

    return data


if __name__ == "__main__":
    result = run_enumerate_zip_examples()
    for key, value in result.items():
        print(f"{key}: {value}")
