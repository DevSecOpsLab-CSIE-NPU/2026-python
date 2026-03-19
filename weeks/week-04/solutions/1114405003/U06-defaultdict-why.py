# U6. defaultdict 為何比手動初始化乾淨（1.6）
# 此示例對比使用普通字典和 defaultdict 兩種方式來分組數據
# 重點說明 defaultdict 如何省掉繁瑣的初始化檢查

# 導入 defaultdict 從 collections 模組
from collections import defaultdict

# ===== 準備數據 =====
# 建立包含 (鍵, 值) 對的列表
# 相同的鍵出現多次，需要將對應的值分組在一起
pairs = [('a', 1), ('a', 2), ('b', 3)]

# ===== 方法 1：使用普通字典（手動初始化版本）=====
# 建立空字典
d = {}

# 遍歷每個 (鍵, 值) 對
for k, v in pairs:
    # 每次訪問鍵前，必須檢查該鍵是否已存在
    # 這是因為普通字典中訪問不存在的鍵會拋出 KeyError
    if k not in d:
        # 如果鍵不存在，先初始化一個空列表
        d[k] = []
    # 然後才能將值添加到列表中
    d[k].append(v)

# 結果：d = {'a': [1, 2], 'b': [3]}

# ===== 方法 2：使用 defaultdict（自動初始化版本）=====
# defaultdict(list) 建立一個字典，任何不存在的鍵都會自動初始化為空列表
# defaultdict 接收一個 callable（可調用的函數），用來生成默認值
# list：當訪問不存在的鍵時，自動呼叫 list() 建立空列表
d2 = defaultdict(list)

# 遍歷每個 (鍵, 值) 對
for k, v in pairs:
    # 關鍵差異：無需檢查鍵是否存在
    # 即使 d2[k] 是首次訪問，defaultdict 也會自動建立一個空列表
    # 然後立即對該列表調用 append(v)
    d2[k].append(v)

# 結果：d2 = defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})

# ===== 詳細工作流程 =====
# 使用 defaultdict(list) 時的自動初始化：
# 1. 第一次訪問 d2['a']：鍵不存在 → 自動調用 list() → 返回 []
# 2. 隨即執行 d2['a'].append(1) → d2['a'] = [1]
# 3. 第二次訪問 d2['a']：鍵已存在 → 直接返回 [1]
# 4. 執行 d2['a'].append(2) → d2['a'] = [1, 2]
# 5. 首次訪問 d2['b']：鍵不存在 → 自動調用 list() → 返回 []
# 6. 執行 d2['b'].append(3) → d2['b'] = [3]

# ===== defaultdict 的常見工廠函數 =====
# - defaultdict(list)：默認值為 []（空列表）
# - defaultdict(set)：默認值為 set()（空集合）
# - defaultdict(dict)：默認值為 {}（空字典）
# - defaultdict(int)：默認值為 0（整數零）
# - defaultdict(str)：默認值為 ''（空字符串）
# - defaultdict(lambda: 'missing')：自定義默認值

# ===== 優勢總結 =====
# 手動版本的缺點：
# 1. 需要每次都檢查 if k not in d
# 2. 代碼冗長，容易出錯
# 3. 比較低效（每次都進行檢查）

# defaultdict 的優點：
# 1. 代碼簡潔清晰，無需 if 檢查
# 2. 自動初始化，不會遺漏
# 3. 語義明確：一眼看出該鍵對應空列表
# 4. 適合分組、計數等常見操作
