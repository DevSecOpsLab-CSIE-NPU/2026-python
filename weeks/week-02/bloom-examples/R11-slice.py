# ============================================================================
# R11. 命名切片 - 用 slice() 物件簡化複雜索引（1.11）
# ============================================================================
# 本題展示如何使用 slice 物件取代魔數索引，提高代碼可讀性。
# ============================================================================

print("【背景】處理固定格式文本（如購票收據）\n")

record = '....................100 .......513.25 ..........'
print(f"收據原文：{record}")
print(f"說明：")
print(f"  - 位置 20-23：股票數量 (100)")
print(f"  - 位置 31-37：股票價格 (513.25)")
print()

print("=" * 50)
print("【傳統方法 - 魔數索引】")
print("=" * 50)
print()

print("代碼：")
print("""
cost = int(record[20:23]) * float(record[31:37])
""")
print()

cost_old = int(record[20:23]) * float(record[31:37])
print(f"結果：{cost_old}")
print()
print("問題：")
print("  ❌ 20、23、31、37 是什麼意思？")
print("  ❌ 六個月後還能看懂嗎？")
print("  ❌ 複雜公式難以維護\n")

print("=" * 50)
print("【改進方法 - 命名切片】")
print("=" * 50)
print()

print("代碼：")
print("""
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
""")
print()

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost_new = int(record[SHARES]) * float(record[PRICE])

print(f"結果：{cost_new}")
print()
print("優勢：")
print("  ✓ SHARES 和 PRICE 是自文檔化的")
print("  ✓ 一目瞭然，易於維護")
print("  ✓ 可以在模組層級定義（作為常數）\n")

print("=" * 50)
print("【slice() 物件解析】")
print("=" * 50)
print()

print("slice 的參數：")
print("  slice(start, stop[, step])")
print()

print("等價性：")
print("  record[20:23] == record[slice(20, 23)]")
print()

s = slice(20, 23)
print(f"slice 物件：{s}")
print(f"  start = {s.start}")
print(f"  stop = {s.stop}")
print(f"  step = {s.step}\n")

print("=" * 50)
print("【進階用法】step 參數")
print("=" * 50)
print()

data = list(range(10))
print(f"數據：{data}")
print()

print("每隔兩個取一個（step=2）：")
every_second = slice(None, None, 2)
print(f"  data[slice(None, None, 2)] = {data[every_second]}")
print()

print("反向取值（step=-1）：")
reverse = slice(None, None, -1)
print(f"  data[slice(None, None, -1)] = {data[reverse]}\n")

print("=" * 50)
print("【實戰應用】配置管理")
print("=" * 50)
print()

# 定義固定格式的各字段位置
class FixedWidthRecord:
    """處理固定寬度的文本記錄"""
    
    # 定義字段位置為常數
    NAME = slice(0, 10)
    AGE = slice(10, 13)
    SALARY = slice(13, 23)
    
    def __init__(self, record):
        self.record = record
    
    def parse(self):
        return {
            'name': self.record[self.NAME].strip(),
            'age': int(self.record[self.AGE]),
            'salary': int(self.record[self.SALARY]),
        }

record_data = 'Alice    25 2500000   '
parser = FixedWidthRecord(record_data)
result = parser.parse()
print(f"原始記錄：'{record_data}'")
print(f"解析結果：{result}\n")

print("=" * 50)
print("【最佳實踐】")
print("=" * 50)
print("""
✓ 使用 slice() 物件代替魔數索引
✓ 在模組層級定義 slice 常數
✓ 為 slice 物件取有意義的名稱
✓ 複雜格式解析時特別有用
✓ 增強代碼可讀性和可維護性

適用場景：
  ✓ 固定格式文件解析
  ✓ 二進位資料處理
  ✓ CSV 變種格式
  ✓ 日誌檔案解析
""")
