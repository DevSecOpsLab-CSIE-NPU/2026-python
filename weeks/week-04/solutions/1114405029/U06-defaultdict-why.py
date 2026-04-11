# U6. defaultdict 為何比手動初始化乾淨（1.6）

from collections import defaultdict

# 準備一組包含重複鍵 (Key) 的資料對
pairs = [('a', 1), ('a', 2), ('b', 3)]

# ── 1. 手動版：傳統字典的寫法 ──────────────────────────
d = {}
for k, v in pairs:
    # 每次存入資料前，都必須先檢查鍵 (k) 是否已經存在於字典中
    if k not in d:
        # 如果不存在，手動初始化一個空列表
        d[k] = []
    # 確定有列表後，才能執行 append 動作
    d[k].append(v)
# 這種寫法雖然邏輯清晰，但程式碼較為臃腫，且在迴圈中增加了判斷式的開銷。

# ── 2. 進階版：使用 defaultdict ───────────────────────
# 初始化時指定「預設工廠函數」(default_factory) 為 list
# 這代表：當程式存取一個「不存在的鍵」時，它會自動呼叫 list() 並將結果存入該鍵
d2 = defaultdict(list)

for k, v in pairs:
    # 不再需要 if k not in d2 的判斷
    # 如果 k 不存在，d2 會自動為你準備好一個新列表，讓你直接 append
    d2[k].append(v)

# 結果與手動版完全一致：{'a': [1, 2], 'b': [3]}
# 優點：程式碼更簡潔（更具 Pythonic 風格），且效能通常更好，因為底層 C 語言會處理初始化。