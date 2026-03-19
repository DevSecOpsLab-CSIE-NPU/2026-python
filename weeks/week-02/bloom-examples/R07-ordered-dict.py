# ============================================================================
# R7. 有序字典 OrderedDict（1.7）
# ============================================================================
# 本題展示 OrderedDict 在 JSON 序列化中保持鍵序的用法。
# 註：Python 3.7+ 普通 dict 已保持插入順序，但 OrderedDict 仍有其他優勢。
# ============================================================================

from collections import OrderedDict
import json

print("【OrderedDict 的目的】")
print("=" * 50)
print()

print("Python 3.7+ 普通 dict 已保持插入順序")
print("但 OrderedDict 在以下場景仍然重要：")
print("  1. 跨版本相容性（Python < 3.7）")
print("  2. JSON 序列化的可預測性")
print("  3. move_to_end() 等特殊方法\n")

print("=" * 50)
print("【基本用法】")
print("=" * 50)
print()

print("建立 OrderedDict 並設置鍵值：\n")

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

print(f"d = OrderedDict()")
print(f"d['foo'] = 1")
print(f"d['bar'] = 2\n")

print(f"字典內容：{d}\n")

print("說明：")
print("  - 鍵按插入順序維護")
print("  - 迭代時也保持插入順序\n")

print("=" * 50)
print("【JSON 序列化保序】")
print("=" * 50)
print()

print("場景：需要 JSON 輸出按固定順序排列關鍵字\n")

json_str = json.dumps(d)
print(f"json.dumps(d) = {json.str}")
print()

print("說明：")
print("  - OrderedDict 被序列化時保持鍵順")
print("  - 輸出：{\"foo\": 1, \"bar\": 2}")
print("  - 而非隨意排列\n")

print("=" * 50)
print("【為什麼仍需 OrderedDict？】")
print("=" * 50)
print("""
1. 跨版本相容性
   - 代碼需要在 Python < 3.7 運行
   - 必須使用 OrderedDict

2. 語意明確性
   - 使用 OrderedDict 明確表示"順序很重要"
   - 代碼意圖清晰

3. 支援 move_to_end()
   - 可動態調整鍵的位置
   - LRU Cache 實現利用此特性

4. 防守性編程
   - 不依賴 dict 實現細節
   - 確保在所有 Python 版本中行為一致
""")

print("\n" + "=" * 50)
print("【實戰應用】")
print("=" * 50)
print()

print("應用 1：構建配置文件（保持順序）")
config = OrderedDict()
config['database_host'] = 'localhost'
config['database_port'] = 5432
config['database_name'] = 'myapp'
config['debug'] = True

print(f"配置順序：")
for key, value in config.items():
    print(f"  {key}: {value}")
print()

print("應用 2：導出 JSON 時保持美觀")
json_output = json.dumps(config, indent=2)
print(f"導出 JSON：")
print(json_output)
print()

print("=" * 50)
print("【性能提示】")
print("=" * 50)
print("""
OrderedDict vs dict（Python 3.7+）：

操作         dict    OrderedDict
─────────────────────────────────
創建         ✓✓      ✓（稍慢）
插入         ✓✓      ✓（稍慢）
查詢         ✓✓      ✓（稍慢）
刪除         ✓✓      ✓（稍慢）
move_to_end  ✗       ✓（獨有）

結論：
  - 無需特殊操作 → 普通 dict
  - 需要 move_to_end → OrderedDict
  - 需要跨版本相容性 → OrderedDict
""")
