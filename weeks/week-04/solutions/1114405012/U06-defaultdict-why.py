# U06. defaultdict 為何比手動初始化更乾淨（1.6）
# 觀念：一般 dict 在 key 初次出現時要先初始化；defaultdict 會自動補預設值。

from collections import defaultdict


def section(title: str) -> None:
    print(f"\n=== {title} ===")


pairs = [("a", 1), ("a", 2), ("b", 3), ("c", 4), ("b", 8)]

section("手動 dict 初始化")
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)
print("手動版結果:", d)

section("defaultdict 自動初始化")
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)
print("defaultdict 結果:", dict(d2))

section("defaultdict(int) 可做計數")
counter = defaultdict(int)
for ch in "mississippi":
    counter[ch] += 1
print("字元計數:", dict(counter))
