"""
U03. 字串格式化效能與常見陷阱。

重點：
1. 大量字串串接時，`"".join()` 通常比 `+=` 更有效率。
2. `format_map()` 可搭配自訂 dict 處理缺失欄位。
3. `bytes` 的索引結果和 `str` 不同。
"""

import timeit


# ── 1. join 通常比 += 更適合大量字串串接 ────────────────────
parts = [f"item{i}" for i in range(1000)]


def bad_concat():
    """
    用 `+=` 一段一段加字串。

    因為字串不可變，每次加總都要建立新字串，
    所以在大量資料時成本會逐步升高。
    """

    result = ""
    for part in parts:
        result += part
    return result


def good_join():
    """先把片段放好，再一次 join 起來。"""
    return "".join(parts)


concat_time = timeit.timeit(bad_concat, number=500)
join_time = timeit.timeit(good_join, number=500)
print(f"+串接: {concat_time:.3f}s  join: {join_time:.3f}s")


# ── 2. format_map 可配合 __missing__ 處理不存在的鍵 ──────────
class SafeSub(dict):
    """當欄位缺失時，不直接丟錯，而是保留原佔位符。"""

    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


name = "Guido"
template = "{name} has {n} messages."
print(template.format_map(SafeSub(vars())))


# ── 3. str 與 bytes 的索引結果不同 ──────────────────────────
text_value = "Hello"
byte_value = b"Hello"

# `str[index]` 取回的是單一字元字串。
print(text_value[0])  # 'H'

# `bytes[index]` 取回的是整數，也就是該位元組的數值。
print(byte_value[0])  # 72


# `bytes` 不能直接做 `.format()`。
# 常見做法是先格式化成字串，再 encode 成 bytes。
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
