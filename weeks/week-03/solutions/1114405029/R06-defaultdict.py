# R6. 多值字典 defaultdict / setdefault（1.6）
#
# 這份程式在示範「一個 key 對多個值」時的兩種常見寫法：
# 1) defaultdict：自動建立缺少 key 的預設容器
# 2) dict.setdefault：手動指定缺少 key 時要放的預設值

from collections import defaultdict


# 1) defaultdict(list)
# - 當你第一次存取不存在的 key（例如 d['a']）時
# - 會自動建立一個空 list 當預設值
d = defaultdict(list)

# 第一次 d['a'] 時會自動變成 []，然後 append(1) -> [1]
# 第二次再 append(2) -> [1, 2]
d['a'].append(1); d['a'].append(2)


# 2) defaultdict(set)
# - 預設容器改成 set，適合「去重複」需求
d = defaultdict(set)

# add() 加入元素；set 天生不允許重複值
# 若重複 add 同一個值，結果仍只保留一份
d['a'].add(1); d['a'].add(2)


# 3) 一般 dict 搭配 setdefault
# - setdefault(key, default)
#   若 key 不存在：建立 key 並放入 default，回傳該值
#   若 key 已存在：直接回傳原本值，不覆蓋
d = {}

# 這行等價概念：
# if 'a' not in d:
#     d['a'] = []
# d['a'].append(1)
d.setdefault('a', []).append(1)


# 讀懂這份程式的重點：
# 1. 目標都是避免 KeyError，並且方便累積多個值。
# 2. defaultdict 寫法通常更簡潔，適合大量累積場景。
# 3. 用 list 還是 set 取決於需求：
#    - list: 保留插入順序，可重複
#    - set : 不保證順序，自動去重
# 4. setdefault 在偶爾初始化 key 時很實用，但高頻累積常用 defaultdict 更直觀。
