"""
R07：OrderedDict（有序字典）

學習目標：
1. 理解 OrderedDict 會記住插入順序。
2. 觀察迭代輸出時順序固定。
3. 了解轉 JSON 後鍵順序同樣可維持。
"""

from collections import OrderedDict
import json


def main():
    print("=== R07 OrderedDict ===")

    d = OrderedDict()
    d["foo"] = 1
    d["bar"] = 2
    d["spam"] = 3
    d["grok"] = 4

    print("[例1] 依插入順序巡覽:")
    for key in d:
        print("  ", key, "->", d[key])

    print("[例2] 轉 JSON（順序不變）:", json.dumps(d, ensure_ascii=False))


if __name__ == "__main__":
    main()
