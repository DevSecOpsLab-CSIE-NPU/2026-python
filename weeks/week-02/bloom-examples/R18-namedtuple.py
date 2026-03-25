# ============================================================================
# R18. 命名元組 namedtuple（1.18）
# ============================================================================
# 本題展示 namedtuple 的特性：結合了元組的輕量級與字典的易讀性。
# namedtuple 適用場景：
# 1. 簡單的資料結構（無需完整類別）
# 2. 需要名稱化欄位的元組
# 3. 對效能要求高的場景（比普通類別更輕量）
# ============================================================================

from collections import namedtuple


print("【namedtuple 基礎概念】")
print("=" * 50)
print("""
namedtuple = 具名的不可變序列
優点：
✓ 像元組一樣輕量級、可雜湊、不可變
✓ 可用屬性名稱（.field）訪問欄位，比索引更可讀
✓ 可用索引訪問欄位，向後相容普通元組
✓ 支援位置引數和關鍵字引數建構
""")

print("\n" + "=" * 50)
print("【應用 1】使用者訂閱資訊")
print("=" * 50)
print()

# ──────────────────────────────────────────────────────────────────────────
# 【步驟 1】定義 namedtuple
# ──────────────────────────────────────────────────────────────────────────
print("【步驟 1】定義 namedtuple 類別")
print()

# 【語法】namedtuple(typename, field_names)
# - typename: 新類別的名稱
# - field_names: 欄位名稱（可以是字符串、列表或逗號分隔的字符串）
#
# 返回值：一個新的類別，可用於建立具名元組實例

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
print(f"建立類別: Subscriber")
print(f"欄位: ['addr', 'joined']")
print()

# ──────────────────────────────────────────────────────────────────────────
# 【步驟 2】建立實例
# ──────────────────────────────────────────────────────────────────────────
print("【步驟 2】建立實例")
print()

# 可用位置引數
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(f"位置引數: Subscriber('jonesy@example.com', '2012-10-19')")
print(f"實例 sub: {sub}")
print()

# 可用關鍵字引數
sub_kw = Subscriber(joined='2012-10-19', addr='jonesy@example.com')
print(f"關鍵字引數: Subscriber(joined='2012-10-19', addr='jonesy@example.com')")
print(f"實例 sub_kw: {sub_kw}")
print()

# ──────────────────────────────────────────────────────────────────────────
# 【步驟 3】訪問欄位
# ──────────────────────────────────────────────────────────────────────────
print("【步驟 3】訪問欄位")
print()

print("方法 A：使用屬性名稱（推薦）")
print(f"  sub.addr = {sub.addr}")
print(f"  sub.joined = {sub.joined}")
print()

print("方法 B：使用索引（向後相容）")
print(f"  sub[0] = {sub[0]}")
print(f"  sub[1] = {sub[1]}")
print()

print("方法 C：解包")
addr, joined = sub
print(f"  addr, joined = sub")
print(f"  addr = {addr}, joined = {joined}")
print()

# ──────────────────────────────────────────────────────────────────────────
# 【namedtuple 的不可變性】
# ──────────────────────────────────────────────────────────────────────────
print("【重要】namedtuple 是不可變的")
print("-" * 50)
print()

try:
    sub.addr = 'new@example.com'  # ✗ 會失敗
except AttributeError as e:
    print(f"❌ 嘗試修改欄位會報錯：{e}")
    print()

print("解決方案：使用 _replace() 方法建立新實例")
print()

# ──────────────────────────────────────────────────────────────────────────
# 【應用 2】股票資訊（使用 _replace()）
# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【應用 2】股票資訊 - 使用 _replace()")
print("=" * 50)
print()

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
print(f"建立類別: Stock")
print(f"欄位: ['name', 'shares', 'price']")
print()

# 建立原始實例
s = Stock('ACME', 100, 123.45)
print(f"原始股票: {s}")
print()

# 【_replace() 方法】建立一個新的實例，替換指定欄位
# 返回值：一個新的 namedtuple 實例（原實例不變）
s_updated = s._replace(shares=75)
print(f"使用 _replace(shares=75):")
print(f"  原實例 s: {s}")
print(f"  新實例 s_updated: {s_updated}")
print(f"說明：原 s 未改變（不可變性），created 新實例")
print()

print("多個欄位同時替換:")
s_multi = s._replace(shares=50, price=150.0)
print(f"  s._replace(shares=50, price=150.0)")
print(f"  結果: {s_multi}")
print()

# ──────────────────────────────────────────────────────────────────────────
# 【其他有用方法】
# ──────────────────────────────────────────────────────────────────────────
print("\n【其他有用方法】")
print("-" * 50)
print()

print("1. _fields - 獲取欄位名稱元組")
print(f"   Stock._fields = {Stock._fields}")
print()

print("2. _asdict() - 轉換為字典")
dict_s = s._asdict()
print(f"   s._asdict() = {dict_s}")
print(f"   型別: {type(dict_s)}")
print()

print("3. _make() - 從可迭代物件建立實例")
data = ['AAPL', 200, 175.5]
s_new = Stock._make(data)
print(f"   Stock._make({data}) = {s_new}")
print()

# ──────────────────────────────────────────────────────────────────────────
# 【與一般類別的比較】
# ──────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("【namedtuple vs 一般類別】")
print("=" * 50)
print("""
namedtuple：
✓ 輕量級，記憶體效率高
✓ 不可變，可用作字典的鍵
✓ 可雜湊（hashable）
✗ 無隱私性（所有欄位都是公開的）
✗ 無方法支援（需要額外函式）

一般類別：
✓ 支援方法和屬性
✓ 可實現私有欄位（_prefix）
✓ 支援繼承
✗ 更重（記憶體使用量較高）
✗ 預設可變

選擇建議：
✓ namedtuple：簡單資料結構、需要不可變性
✓ 一般類別：複雜邏輯、需要方法支援
""")
