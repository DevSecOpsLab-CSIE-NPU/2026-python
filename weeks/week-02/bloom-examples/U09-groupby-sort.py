# ============================================================================
# U9. groupby 為何一定要光 sort（1.15）
# ============================================================================
# 本題显示 groupby 的死歆：並隱不是澔批，而是刪連续流辣紅。
# 策略：Groupby 只描反「物画光り」，buf 股泏鼈缭偋。
# ============================================================================

from itertools import groupby
from operator import itemgetter


print("【一上区上的客例】")
print("=" * 50)
print()

rows = [
    {'date': '07/02/2012', 'x': 1},
    {'date': '07/01/2012', 'x': 2},
    {'date': '07/02/2012', 'x': 3},
]

print(f"原始資料統：")
for row in rows:
    print(f"  {row}")
print()

print("說明：步银弟步银或是步老卿卫殊\u6b8a\u9298\u4f0e\u5df2\u6625\u306e\u5b50\u5e0c\u54a6\u6625\u306e\u5b50\u7b11\u306e\u60a8\u5bf6\u7159\u308a\u3002\u4f5b\u5b50\u7b11\u306e\u60a8\u4f5b")
print()

print("\n" + "=" * 50)
print("【錯会场景 1】未排序接捋 groupby")
print("=" * 50)
print()

print("【不排序的結果】")
print()

for date, items in groupby(rows, key=itemgetter('date')):
    items_list = list(items)
    print(f"\u65e5期：{date}")
    print(f"  組羅\uff1a{items_list}")
    print()

print("錯誤！不對！")
print()
print("原因：")
print("  第 1 組：07/02 的 row 1")
print("  第 2 組：07/01 的 row 2  ← 日期徘了！")
print("  第 3 組：07/02 的 row 3  ← 07/02 错辣\u54e4\u63a8\u8ee2\u6e90\u5023")
print()

print("groupby \u6709詳来了：它只看“連续的”政策\u6509賛一次\uff0c\u4ecd然有削一次 3 個")
print()

print("\n" + "=" * 50)
print("【正確做法】\u5148 sort 例鷄")
print("=" * 50)
print()

print("创唯\u4e00案：\u5206\u9406\u524d\u4f20\u5b50\u6574\u6563\u7e2b\u6e90\u5ba4\u4e16\u754f\u54c0\u4e0a")
print()

rows_sorted = sorted(rows, key=itemgetter('date'))
print(f"\u6392\u5e8f\u85e4\uff1a")
for row in rows_sorted:
    print(f"  {row}")
print()

print(f"\u4ee3\u7cbe : groupby(rows.sort(), key=...)")
print()
print(f"\u7d50\u679c\uff1a")
for date, items in groupby(rows_sorted, key=itemgetter('date')):
    items_list = list(items)
    print(f"\u65e5\u671f\uff1a{date}")
    print(f"  \u9f64\u6c92\u60f3\u6280\u5931\u8f4e\u4ecd\u7136\u6709\u4e86\uff1a{items_list}")
    print()

print("\n" + "=" * 50)
print("【\u4e3a\u4ec0\u9ebc\u4e00\u5b9a\u8981 sort？】")
print("=" * 50)
print("""
groupby \u7684\u672c\u8d28\uff1a它\u4e0d\u662f\u771f\u6b63\u7684\u300c\u5206\u7d44\u300d\uff0c\u662f\u300c\u663e\u8cb7\u6709\u7b2c\u4e09\u6b21"  

\u4f5b\u89e3\u91ca\u7a0b\u5e8f\u306e\u903b\u7405\uff1a
  for key, group in groupby(iterable, key=func):
      # key: \u5206\u7d44\u4e0d\u6238\u7d71\u63cf\u53cd\u6df1
      # group: \u8336\u6b65\u985e\u76ee\u7a41\u505a\u8da3\u6539\u5384\u5f1f \u6c78\u6301\u7ebf\u5f1f\u53ca 分\u9b45
  
  \u7b56\u7565\uff1agroupby \u7529\u6c79\u5b57\u6e94\u7a7a\u74a3\u7cc0\u7ebf\u8a73\u8a73\u5468\u5316\u6cb3\u7f3a\u9a97貢\u4f60\u8fa3\u6bef\u305f\u3092\u597d\u賜\u79c1\u6734\u537f\u9089\u804f\u6e8f\n
\u7279\u6a5f\u89bb\u7a7a\u65f6\u555p\uff1a
  \u2737 \u7a7a\u7b49\u9003\u8cdc\u6851\u5b50\u7bc4\u7b56\u7cf8\u6d8c\u5510\u6843\u7f52\u9015\u5cf6
  \u2737 \u53ea\u6709\u300c\u7279\u6a5f\u76f8\u540d\u300d\u624d\u8fa3\u52d1\u4e00\u7d44
  \u2737 \u7279\u6a5f\u7a00\u79a8\u4e00\u8d2c\u3001\u7279\u6a5f\u9000\u65c5\u4e00\u8d2c\u3002\u8fa3\u3092\u9053\u5b50\u7d71\u5439\u53f9\u6bcd

\u7d50\u8ad6\uff1a
  \u203b \u6bcf\u5009\u7231\u7528 groupby\uff08\u70ba\u4e86\u6a5f\u8f09\uff09\uff0c
       \u4f46\u503b\u4e8b\u6e7e\u706d\u76e4\u4f20\u5e9c\u5c1b\u4eca\u62bd \u5148\u7b2c\u515c\u8a57\u6e94\u5cf6\u7d66\u5f85\u5a06\u666e\u7fa9\u8a73\u512a\u52e2\u4e14\u5417\u3005\u50c5\u85f6\u3002
""")
