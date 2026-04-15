"""
R09：兩個字典做集合運算

學習目標：
1. 熟悉 keys() 的交集與差集。
2. 熟悉 items() 的交集（鍵值都相同才算相同項）。
3. 使用字典推導式建立過濾後新字典。
"""


def main():
    print("=== R09 字典集合運算 ===")

    a = {"x": 1, "y": 2, "z": 3}
    b = {"w": 10, "x": 11, "y": 2}
    print("[原始] a =", a)
    print("[原始] b =", b)

    print("[例1] 共同 keys =", a.keys() & b.keys())
    print("[例2] a 有但 b 沒有的 keys =", a.keys() - b.keys())
    print("[例3] 共同 items =", a.items() & b.items())

    c = {k: a[k] for k in a.keys() - {"z", "w"}}
    print("[例4] 從 a 排除 z, w 後得到 c =", c)


if __name__ == "__main__":
    main()
