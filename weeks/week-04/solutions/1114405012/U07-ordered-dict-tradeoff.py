# U07. OrderedDict 的取捨：保序但有額外成本（1.7）
# 觀念：OrderedDict 會記錄插入順序，適合需要穩定輸出順序的場景。
# 但它通常比一般 dict 需要更多記憶體與維護成本。

from collections import OrderedDict


def section(title: str) -> None:
    print(f"\n=== {title} ===")


section("插入順序保留")
od = OrderedDict()
od["foo"] = 1
od["bar"] = 2
od["spam"] = 3
print("OrderedDict:", od)
print("依序走訪 key:", list(od.keys()))

section("一般 dict 在現代 Python 也會保序")
# 補充：Python 3.7+ 的內建 dict 也保留插入順序。
# 因此平常多數情境下可先用 dict；
# 若你需要 OrderedDict 的專用 API（如 move_to_end）再選它。
d = {}
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
print("dict:", d)
print("dict key 順序:", list(d.keys()))

section("OrderedDict 專用操作 move_to_end")
od.move_to_end("foo")
print("把 foo 移到尾端後:", list(od.keys()))
