# R9. 兩字典共同點：keys/items 集合運算（Finding Commonalities in Two Dictionaries）—— Python Cookbook 1.9

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# ── dict.keys() 支援集合運算 ──────────────────────────────
# dict.keys() 回傳一個「類似集合」的 KeysView 物件，
# 可直接使用 &（交集）、|（聯集）、-（差集）等運算子

# 交集：找出兩個字典都有的 key
a.keys() & b.keys()     # → {'x', 'y'}

# 差集：只在 a 有、b 沒有的 key
a.keys() - b.keys()     # → {'z'}

# ── dict.items() 也支援集合運算 ──────────────────────────
# items() 回傳 (key, value) 配對，所以交集 = key 和 value 都相同的項目
a.items() & b.items()   # → {('y', 2)} — x 雖然兩邊都有，但值不同（1 vs 11），不算

# ── 實用：用集合運算「過濾」字典（字典推導式）─────────────
# 建立新字典：只保留 a 中「不在 {'z', 'w'} 裡」的 key
# a.keys() - {'z', 'w'} = {'x', 'y'}
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
# → c = {'x': 1, 'y': 2}
