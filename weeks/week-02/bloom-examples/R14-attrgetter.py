# ============================================================================
# R14. 物件排序 - 用 attrgetter() 提取屬性（1.14）
# ============================================================================
# 本題展示 attrgetter 如何高效地排序物件集合。
# ============================================================================

from operator import attrgetter

print("【場景】管理用戶物件\n")

class User:
    """用戶類"""
    def __init__(self, user_id, name=None):
        self.user_id = user_id
        self.name = name
    
    def __repr__(self):
        return f"User(id={self.user_id}, name={self.name})"

print("建立用戶物件：\n")

users = [
    User(23, 'Alice'),
    User(3, 'Charlie'),
    User(99, 'Bob'),
]

for user in users:
    print(f"  {user}")
print()

print("=" * 50)
print("【方法 1】使用 lambda（直觀但較慢）")
print("=" * 50)
print()

print("按用戶 id 排序：")
print("  sorted(users, key=lambda x: x.user_id)\n")

sorted_lambda = sorted(users, key=lambda x: x.user_id)
for user in sorted_lambda:
    print(f"  {user}")
print()

print("=" * 50)
print("【方法 2】使用 attrgetter（更快優雅）")
print("=" * 50)
print()

print("按用戶 id 排序：")
print("  sorted(users, key=attrgetter('user_id'))\n")

sorted_attr = sorted(users, key=attrgetter('user_id'))
for user in sorted_attr:
    print(f"  {user}")
print()

print("=" * 50)
print("【多屬性排序】")
print("=" * 50)
print()

print("擴展用戶類：")
class Employee:
    def __init__(self, emp_id, name, dept):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
    
    def __repr__(self):
        return f"Employee(id={self.emp_id}, {self.name}, {self.dept})"

emps = [
    Employee(1003, 'John', 'IT'),
    Employee(1001, 'Alice', 'HR'),
    Employee(1002, 'Bob', 'IT'),
]

print("原始順序：")
for emp in emps:
    print(f"  {emp}")
print()

print("按部門和員工號排序：")
print("  sorted(emps, key=attrgetter('dept', 'emp_id'))\n")

sorted_multi = sorted(emps, key=attrgetter('dept', 'emp_id'))
for emp in sorted_multi:
    print(f"  {emp}")
print()

print("說明：")
print("  - 先按 dept 排序（HR 在前）")
print("  - 同 dept 內按 emp_id 排序\n")

print("=" * 50)
print("【attrgetter vs lambda 性能】")
print("=" * 50)
print("""
操作                lambda           attrgetter
────────────────────────────────────────────────
x -> x.user_id      每次都定義          靜態編譯
性能                ✓ 慢              ✓✓ 快 20-30%
可讀性              ★★★☆☆            ★★★☆☆
複雜邏輯            ✓ 支援             ✗ 只提取

性能基準（百萬次排序）：
  lambda:       約 1000 ms
  attrgetter:   約 700-800 ms   ✓ 快 20-30%
""")

print("\n" + "=" * 50)
print("【直接使用 attrgetter】")
print("=" * 50)
print()

print("不必排序，直接提取屬性：")
get_id = attrgetter('emp_id')
get_name = attrgetter('name')

for emp in emps:
    emp_id = get_id(emp)
    name = get_name(emp)
    print(f"  {emp_id}: {name}")
print()

print("多個屬性：")
get_info = attrgetter('name', 'dept')
for emp in emps:
    name, dept = get_info(emp)
    print(f"  {name} works in {dept}")
print()

print("=" * 50)
print("【attrgetter vs itemgetter 比較】")
print("=" * 50)
print("""
情況              attrgetter          itemgetter
────────────────────────────────────────────────
物件屬性          ✓✓ 完美              ✗ 不適用
字典              ✗ 不行               ✓✓ 使用
列表              ✗ 不行               ✓  可用
性能              ✓✓ 稍快              ✓  稍慢

選擇準則：
  物件屬性 → attrgetter
  字典鍵值 → itemgetter
  列表索引 → itemgetter
""")

print("\n" + "=" * 50)
print("【實戰應用】")
print("=" * 50)
print("""
✓ 排序物件集合
✓ 按屬性分組
✓ 建立索引
✓ GUI 資料繫結
✓ ORM 查詢優化

最佳實踐：
  ✓ 對物件用 attrgetter
  ✓ 對字典用 itemgetter
  ✓ 性能關鍵時用這兩個
  ✓ 複雜邏輯時用 lambda
""")
