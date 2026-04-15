"""
R06：defaultdict 與 setdefault

學習目標：
1. defaultdict(list) 自動建立空 list，省去 if key not in d。
2. defaultdict(set) 自動建立空 set，並體會 set 的去重特性。
3. 對照 setdefault 的等價寫法。
"""

from collections import defaultdict


def main():
    print("=== R06 defaultdict / setdefault ===")

    d_list = defaultdict(list)
    d_list["a"].append(1)
    d_list["a"].append(2)
    d_list["b"].append(100)
    print("[例1] defaultdict(list) =", dict(d_list))

    d_set = defaultdict(set)
    d_set["a"].add(1)
    d_set["a"].add(2)
    d_set["a"].add(2)  # set 會自動去重
    print("[例2] defaultdict(set)（2 只會留一個）=", {k: sorted(v) for k, v in d_set.items()})

    d = {}
    d.setdefault("a", []).append(1)
    d.setdefault("a", []).append(2)
    print("[例3] setdefault 寫法 =", d)


if __name__ == "__main__":
    main()
