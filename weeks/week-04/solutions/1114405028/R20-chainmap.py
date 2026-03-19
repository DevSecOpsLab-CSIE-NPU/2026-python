# R20. ChainMap 合併映射（1.20）

from collections import ChainMap  # ChainMap：將多個 dict 串接成一個邏輯上的單一映射

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)  # 查找時依序從 a → b 搜尋；寫入操作只作用在第一個 dict（a）

c['x']  # 只在 a 中有 x，回傳 1
c['z']  # a 和 b 都有 z，以排在前面的 a 為準，回傳 3（不是 b 的 4）
        # 適合實作「區域 → 全域」的優先查找鏈（如 scope 查找）
