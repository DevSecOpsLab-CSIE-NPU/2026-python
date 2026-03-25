# ============================================================================
# R16. 過濾操作：推導式 / 生成器 / filter / compress（1.16）
# ============================================================================
# 本題展示四種不同的資料過濾方法及其效能特徵：
# 1. 列表推導式 [... if condition]   - 最常用，返回列表
# 2. 生成器表達式 (... if condition)  - 延遲求值，省記憶體
# 3. filter() 函式                    - 函式式程式設計風格
# 4. itertools.compress()             - 按布林遮罩過濾
# ============================================================================


# ══════════════════════════════════════════════════════════════════════════
# 【方法 1】列表推導式 - 最常用且可讀性最高
# ══════════════════════════════════════════════════════════════════════════
print("【方法 1】列表推導式")
print("-" * 50)

# 原始資料：包含正負數的列表
mylist = [1, 4, -5, 10]
print(f"原始列表: {mylist}\n")

# 【語法】[expression for item in iterable if condition]
# - expression: 要保留的元素（可以進行變換）
# - item: 迭代變數
# - iterable: 可迭代物件（列表、元組、字典等）
# - if condition: 篩選條件（可選）
#
# 執行流程：
# 1. 遍歷 mylist 中的每個元素 n
# 2. 檢查 n > 0 的條件
# 3. 如果條件為真，將 n 加入結果列表
positive_numbers = [n for n in mylist if n > 0]
print(f"篩選條件：n > 0")
print(f"結果: {positive_numbers}")
# 預期: [1, 4, 10]

# 說明：
# ✓ 優點：寫法簡潔，執行速度快，可讀性高
# ✓ 返回完整列表，所有元素都在記憶體中
# ✗ 缺點：對於大資料集會占用較多記憶體

print("\n【進階】列表推導式可包含變換:")
squared_positive = [n**2 for n in mylist if n > 0]
print(f"篩選正數並平方: {squared_positive}")
# 預期: [1, 16, 100]

print()


# ══════════════════════════════════════════════════════════════════════════
# 【方法 2】生成器表達式 - 延遲求值，省記憶體
# ══════════════════════════════════════════════════════════════════════════
print("【方法 2】生成器表達式（Generator Expression）")
print("-" * 50)

# 語法：與列表推導式完全相同，只是用 () 代替 []
# (expression for item in iterable if condition)
#
# 主要區別：
# - 列表推導式 [...]: 立即求值，返回完整列表
# - 生成器表達式 (...): 延遲求值，按需生成元素
#
# 優點：
# ✓ 記憶體效率高（不需一次性載入所有資料）
# ✓ 適合大資料集或無限序列
# ✓ 可與迭代工具鏈接組合

pos = (n for n in mylist if n > 0)
print(f"生成器物件: {pos}")
print(f"型別: {type(pos)}")
# 預期: <generator object <genexpr> at 0x...>

# 逐個提取元素
print("\n逐個迭代生成器元素:")
pos = (n for n in mylist if n > 0)  # 重新建立，因為之前的已耗盡
for num in pos:
    print(f"  - {num}")

# 使用 list() 轉換為列表（僅在需要時）
print("\n轉換為列表（list()）:")
pos = (n for n in mylist if n > 0)
result = list(pos)
print(f"結果: {result}")

print("\n【提示】生成器適用場景：")
print("""
✓ 處理超大資料集（如處理 GB 級別的檔案）
✓ 與其他生成器鏈接組合
✓ 函式式程式設計風格
✗ 需要多次遍歷時（生成器只能遍歷一次）
""")

print()


# ══════════════════════════════════════════════════════════════════════════
# 【方法 3】filter() 函式 - 函式式程式設計風格
# ══════════════════════════════════════════════════════════════════════════
print("【方法 3】filter() 函式")
print("-" * 50)

# 處理複雜的過濾條件：區分可轉換為整數的字符串
values = ['1', '2', '-3', '-', 'N/A']
print(f"原始資料: {values}")
print("說明: 混合了有效整數字符串和無效值\n")

# 定義過濾函式：檢查字符串是否可轉換為整數
def is_int(val):
    """
    判斷字符串是否可以轉換為整數。
    
    使用 try-except 捕捉轉換失敗的情況：
    - 成功轉換：返回 True
    - 轉換失敗（ValueError）：返回 False
    """
    try:
        int(val)
        return True
    except ValueError:
        return False

# 【語法】filter(function, iterable)
# - function: 判斷函式，返回 True/False
# - iterable: 可迭代物件
#
# 返回值：filter 物件（類似生成器，延遲求值）
filter_obj = filter(is_int, values)
print(f"filter() 返回物件: {filter_obj}")
print(f"型別: {type(filter_obj)}\n")

# 使用 list() 轉換為列表
valid_ints = list(filter(is_int, values))
print(f"篩選結果: {valid_ints}")
# 預期: ['1', '2', '-3']

print("\n【對比】filter() vs 列表推導式:")
print("兩者功能相同，但寫法不同：")
print(f"  filter(): list(filter(is_int, values))")
print(f"  推導式:  [v for v in values if is_int(v)]")
print("\n在 Python 中，推導式通常更推薦（更可讀）")

print()


# ══════════════════════════════════════════════════════════════════════════
# 【方法 4】itertools.compress() - 按布林遮罩過濾
# ══════════════════════════════════════════════════════════════════════════
print("【方法 4】itertools.compress() - 布林遮罩過濾")
print("-" * 50)

from itertools import compress

# 場景：已有過濾結果（布林列表），想用它來過濾另一個資料集

# 範例資料
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]
print(f"地址列表: {addresses}")
print(f"計數列表: {counts}\n")

# 【步驟 1】建立布林遮罩：計數 > 5 的位置為 True
print("【步驟 1】建立布林遮罩（計數 > 5）:")
more5 = [n > 5 for n in counts]
print(f"遮罩: {more5}")
# 預期: [False, False, True]
# 說明：0 不 > 5、3 不 > 5、10 > 5

print("\n【步驟 2】使用 compress() 按遮罩過濾地址:")
# 【語法】compress(data, selectors)
# - data: 要過濾的資料
# - selectors: 布林序列（True 保留，False 丟棄）
#
# 返回：compress 物件（迭代器，延遲求值）

result = list(compress(addresses, more5))
print(f"結果: {result}")
# 預期: ['a3']
# 說明：只保留計數 > 5 的地址

print("\n【何時使用 compress()】")
print("""
✓ 已有現成的布林遮罩
✓ 需要根據多個條件組合過濾
✓ 遮罩和資料來自不同來源
✓ 記憶體效率重要（返回迭代器而非列表）

例子：
- 成績評估：按及格標準過濾學生名單
- 臨界值檢測：根據感測器警告過濾數據點
- 多條件篩選：組合多個條件產生遮罩
""")

print()


# ══════════════════════════════════════════════════════════════════════════
# 【進階應用】組合多個過濾條件
# ══════════════════════════════════════════════════════════════════════════
print("【進階應用】組合多個條件")
print("-" * 50)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"原始資料: {data}\n")

# 條件 1：大於 3
cond1 = [x > 3 for x in data]
print(f"條件 1 (x > 3): {cond1}")

# 條件 2：可被 2 整除
cond2 = [x % 2 == 0 for x in data]
print(f"條件 2 (x % 2 == 0): {cond2}")

# 組合條件：同時滿足兩個條件（使用 zip 和 map）
import operator
combined = list(map(operator.and_, cond1, cond2))
print(f"組合 (cond1 AND cond2): {combined}")

# 使用組合遮罩過濾
result = list(compress(data, combined))
print(f"篩選結果 (x > 3 AND x 是偶數): {result}")
# 預期: [4, 6, 8, 10]

print()


# ══════════════════════════════════════════════════════════════════════════
# 【方法比較】效能和使用場景
# ══════════════════════════════════════════════════════════════════════════
print("=" * 50)
print("【方法比較總結】")
print("=" * 50)

comparison = """
方法          語法形式           返回型別    記憶體效率   可讀性   適用場景
──────────────────────────────────────────────────────────────────────────
推導式        [x for x if ...]   列表       中等        ★★★★★  日常過濾（推薦）
生成器        (x for x if ...)   迭代器     ★★★★★      ★★★★   大資料集
filter()      filter(func, lst)  迭代器     ★★★★★      ★★★    複雜條件
compress()    compress(data, m)  迭代器     ★★★★★      ★★★★   有現成遮罩

推薦使用優先順序：
1. 列表推導式 - 最常見，可讀性最高
2. 生成器表達式 - 處理大資料時
3. filter() - 搭配複雜函式時
4. compress() - 已有遮罩時

記憶體比較（處理 1000 萬個元素）：
- 列表推導式: ~80 MB（一次性創建列表）
- 生成器表達式: ~1 KB（按需生成）
- filter(): ~1 KB（按需生成）
- compress(): ~1 KB（按需生成）
"""

print(comparison)
