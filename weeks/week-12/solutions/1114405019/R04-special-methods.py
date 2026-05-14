# R04-special-methods.py
# 實作 __eq__, __lt__, __len__, __iter__ 等特殊方法

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __len__(self):
        # 定義 len(obj) 的行為
        return len(self.members)

    def __eq__(self, other):
        # 定義 == 的行為 (基於成員數量)
        if not isinstance(other, Team): 
            return False
        return len(self.members) == len(other.members)

    def __lt__(self, other):
        # 定義 < 的行為 (用於排序)
        if not isinstance(other, Team): 
            return NotImplemented
        return len(self.members) < len(other.members)

    def __iter__(self):
        # 定義 for x in obj 的行為
        return iter(self.members)

    def __str__(self):
        return f"Team {self.name} with {len(self)} members"

if __name__ == "__main__":
    print("=== 特殊方法 (Magic Methods) 示範 ===")
    t1 = Team("Devs", ["Alice", "Bob", "Charlie"])
    t2 = Team("Ops", ["Dave", "Eve"])
    
    print(t1)
    print(f"小隊 {t1.name} 長度: {len(t1)}")
    
    # 測試比較運算子
    print(f"t1 == t2? {t1 == t2}")
    print(f"t1 > t2? {t1 > t2}")  # 會自動使用 __lt__
    
    # 測試迭代
    print("迭代成員:")
    for m in t1:
        print(f" - {m}")
