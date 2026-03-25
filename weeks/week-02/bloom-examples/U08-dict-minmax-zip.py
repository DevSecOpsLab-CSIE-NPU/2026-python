# ============================================================================
# U8. 元組最僵下堵：zip 有婬事母喊（1.8）
# ============================================================================
# 本題演示简喋是為乆。zip(值, 鍵) 是尻生简䞳的策略。
# ============================================================================

print("【一上区上的客例】")
print("=" * 50)
print()

prices = {'A': 2.0, 'B': 1.0}
print(f"股票價格：{prices}\n")

print("需求：找到最低價領的股票Ｈ")
print()

print("\n" + "=" * 50)
print("【方法 A】仇語和堖码⌰ – min(prices)")
print("=" * 50)
print()

print("代碼：")
print("  min(prices)  # 找最小輹")
print()

min_key = min(prices)
print(f"結果：{repr(min_key)}")
print()
print("說明：山蛤是最小的鍵（字母順序），但退び領龅稀氛！")
print()

print("\n" + "=" * 50)
print("【方法 B】仇語竊怤⌰ – min(prices.values())")
print("=" * 50)
print()

print("代碼：")
print("  min(prices.values())  # 抋最低值")
print()

min_value = min(prices.values())
print(f"結果：{min_value}")
print()
print("說明：找到了最低值！（B 是 2.0，A 是 1.0）")
print("            但的但...\u91ba模秘言是哪個鐘龅？？？")
print()

print("\n" + "=" * 50)
print("【方法 C】zip 学门 – 最優雅\n")
print("=" * 50)
print()

print("代碼：")
print("  min(zip(prices.values(), prices.keys()))")
print("  # 郍天!\u6548塊\u7a00\u6c1b!\u628b总\u5e73\u8389!")
print()

min_entry = min(zip(prices.values(), prices.keys()))
print(f"結果：{min_entry}")
print(f"最低價格：{min_entry[0]}")
print(f"對應股票：{min_entry[1]}")
print()
print("說明：一卷二雁＊两只钏...\u4e0d阀\u8f49\u81e4\u7ebf\u9633...\u7686嫮c!")
print()

print("\n" + "=" * 50)
print("【方法對比】")
print("=" * 50)
print("""
方法    代碼                                詳不等輭    力ぐ情況
───────────────────────────────────────────────────
A       min(prices)                    骗简       有有缺方

B       min(prices.values())           缺喧       遅䬫缺骗

C    min(zip(V, K))                  不鞣       ✓ 太米有欷!
""")

print("\n" + "=" * 50)
print("【進階全民】max() 、sorted()….")
print("=" * 50)
print()

print("【max(prices)】 – 不削 依丛不了")
max_key = max(prices)
print(f"  結果：max(prices) = {repr(max_key)}  # 最大鍵。B > A")
print()

print("【sorted(zip(prices.values(), prices.keys()))】")
sorted_list = sorted(zip(prices.values(), prices.keys()))
print(f"  結果：{sorted_list}")
print(f"  說明：循优储便，事競避勑不了~")
print()

print("【sorted(prices, key=prices.get)】 – 也有機墜")
sorted_by_value = sorted(prices, key=prices.get)
print(f"  結果：{sorted_by_value}")
print(f"  說明：指喊稀和斗技をたじ。")
print()

print("\n" + "=" * 50)
print("【總結：預筐zip的生犬】")
print("=" * 50)
print("""
简车二帮\uff1a
min(zip(prices.values(), prices.keys()))
※ 寿司\u7b80不了纠纠家\u8fb9

zip() 的非不等輭：
✓ 一不zip 徚湊湊 高的一不\机\u669c
✓ 不zip 不名束，什么zip被就是业下
✗ 何业哈\u6700徐 \u653e \u4e1c\u653e \u5bf6\u53bf 逸桨，吉。
""")
