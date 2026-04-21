"""
主題名：R08 - 字典的最小值/最大值查詢
學習目標：掌握使用 min/max/sorted 和 zip 進行效率高的字典排序操作。

核心概念：
  1. 使用 zip 將鍵和值配對後排序
  2. min/max 配合 lambda 直接查詢最小/最大值
  3. sorted 配合 zip 進行完整排序
  4. 原始字典的查詢使用鍵而非值
  5. zip 實現鍵值互換的優雅方式
"""


def example_min_max_with_values():
    """
    示例 1：根據值查找最小/最大的鍵
    
    說明：
      - 字典通常根據值進行排序
      - 使用 min/max 結合 zip 實現優雅排序
    """
    print("=== 字典排序：根據值查找最小/最大 ===\n")
    
    prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}
    print(f"股票價格: {prices}\n")
    
    # 方法 1：使用 zip + min/max
    print("使用 zip + min/max (推薦):")
    print(f"  prices.values(): {list(prices.values())}")
    print(f"  prices.keys(): {list(prices.keys())}")
    
    # 創建 (值, 鍵) 元組
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    
    print(f"\n  min(zip(prices.values(), prices.keys()))")
    print(f"    結果: {min_price}")
    print(f"    最低價: {min_price[0]}, 股票: {min_price[1]}")
    
    print(f"\n  max(zip(prices.values(), prices.keys()))")
    print(f"    結果: {max_price}")
    print(f"    最高價: {max_price[0]}, 股票: {max_price[1]}\n")
    
    # 方法 2：使用 lambda（比較慢）
    print("使用 lambda 方式（較慢）:")
    min_key = min(prices, key=lambda k: prices[k])
    max_key = max(prices, key=lambda k: prices[k])
    print(f"  min key: {min_key} -> ${prices[min_key]}")
    print(f"  max key: {max_key} -> ${prices[max_key]}\n")
    
    print("比較：")
    print("  • zip 方式：直接比較值，效率高")
    print("  • lambda 方式：需要查表，效率較低")


def example_sorted_with_zip():
    """
    示例 2：完整排序
    
    說明：
      - 將字典按值排序
      - 支援升序和降序排序
    """
    print("\n" + "="*60)
    print("=== 完整排序：sorted + zip ===\n")
    
    prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75, 'IBM': 91.10}
    print(f"股票價格: {prices}\n")
    
    # 升序排列（從低到高）
    print("升序排列（價格從低到高）:")
    sorted_asc = sorted(zip(prices.values(), prices.keys()))
    for price, stock in sorted_asc:
        print(f"  ${price:7.2f} - {stock}")
    
    # 降序排列（從高到低）
    print("\n降序排列（價格從高到低）:")
    sorted_desc = sorted(zip(prices.values(), prices.keys()), reverse=True)
    for price, stock in sorted_desc:
        print(f"  ${price:7.2f} - {stock}")


def example_get_top_n_items():
    """
    示例 3：取前 N 個項目
    
    說明：
      - 不需要完整排序，只需要前 N 個最大/最小值
      - 可以使用 heapq 或直接排序後取切片
    """
    print("\n" + "="*60)
    print("=== 前 N 個最值 ===\n")
    
    prices = {
        'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75, 'IBM': 91.10,
        'GOOGL': 2800.00, 'MSFT': 320.00
    }
    
    print(f"股票價格 ({len(prices)} 只):")
    for stock, price in prices.items():
        print(f"  {stock}: ${price:.2f}")
    
    # 取前 3 個最便宜的股票
    print("\n最便宜的 3 只股票:")
    cheapest_3 = sorted(zip(prices.values(), prices.keys()))[:3]
    for i, (price, stock) in enumerate(cheapest_3, 1):
        print(f"  {i}. {stock}: ${price:.2f}")
    
    # 取前 2 個最昂貴的股票
    print("\n最昂貴的 2 只股票:")
    expensive_2 = sorted(zip(prices.values(), prices.keys()), reverse=True)[:2]
    for i, (price, stock) in enumerate(expensive_2, 1):
        print(f"  {i}. {stock}: ${price:.2f}")


def example_complex_sorting():
    """
    示例 4：複雜的排序
    
    說明：
      - 根據字典值中的複合字段排序
      - 字典值本身也是字典或對象
    """
    print("\n" + "="*60)
    print("=== 複雜結構排序 ===\n")
    
    # 股票信息：(名稱) -> {股份數, 價格}
    portfolio = {
        'IBM': {'shares': 100, 'price': 91.10},
        'AAPL': {'shares': 50, 'price': 543.22},
        'FB': {'shares': 200, 'price': 21.09},
        'HPQ': {'shares': 35, 'price': 31.75},
    }
    
    print("投資組合:")
    for stock, info in portfolio.items():
        value = info['shares'] * info['price']
        print(f"  {stock}: {info['shares']} 股 × ${info['price']:.2f} = ${value:.2f}")
    
    # 按總價值排序
    print("\n按總價值排序（降序）:")
    sorted_by_value = sorted(
        zip([s * p['shares'] * p['price'] for s, p in 
             [(1, portfolio[k]) for k in portfolio]],
            portfolio.keys()),
        reverse=True
    )
    
    # 簡單版本
    print("\n簡化版本（按總價值排序）:")
    sorted_portfolio = sorted(
        portfolio.items(),
        key=lambda x: x[1]['shares'] * x[1]['price'],
        reverse=True
    )
    
    for i, (stock, info) in enumerate(sorted_portfolio, 1):
        value = info['shares'] * info['price']
        print(f"  {i}. {stock}: ${value:.2f}")


def example_real_world_analysis():
    """
    示例 5：實際應用 - 數據分析
    
    說明：
      - 展示在實際應用中的排序使用
    """
    print("\n" + "="*60)
    print("=== 實際應用：電商排序 ===\n")
    
    # 商品信息
    products = {
        'iPhone': {'price': 999, 'sales': 5000},
        'Samsung': {'price': 799, 'sales': 3000},
        'Pixel': {'price': 899, 'sales': 2000},
        'OnePlus': {'price': 499, 'sales': 1500},
    }
    
    print("商品庫存:")
    for name, info in products.items():
        print(f"  {name}: ${info['price']}, 銷量: {info['sales']}")
    
    # 按價格排序
    print("\n按價格升序排列:")
    by_price = sorted(zip(map(lambda x: products[x]['price'], products),
                          products.keys()))
    for price, name in by_price:
        print(f"  ${price:4} - {name}")
    
    # 按銷量排序
    print("\n按銷量降序排列：")
    by_sales = sorted([(products[name]['sales'], name) for name in products],
                      reverse=True)
    for sales, name in by_sales:
        print(f"  {sales:5} 件 - {name}")
    
    # 按性價比排序（銷量/價格）
    print("\n性價比排序（銷量/價格，降序）:")
    by_ratio = sorted(
        [(products[name]['sales'] / products[name]['price'], name) 
         for name in products],
        reverse=True
    )
    for ratio, name in by_ratio:
        print(f"  {ratio:.3f} - {name}")


def example_comparison_methods():
    """
    示例 6：不同方法的比較
    
    說明：
      - 對比不同的實現方式
      - 理解何時選擇哪種方法
    """
    print("\n" + "="*60)
    print("=== 不同方法對比 ===\n")
    
    prices = {'A': 100, 'B': 50, 'C': 75, 'D': 25}
    
    print(f"字典: {prices}\n")
    
    print("方法 1：zip + sorted")
    result1 = sorted(zip(prices.values(), prices.keys()))
    print(f"  paired: {result1}")
    print(f"  最便宜: {result1[0]}")
    print(f"  最昂貴: {result1[-1]}\n")
    
    print("方法 2：複製值並排序")
    values = sorted(prices.values())
    print(f"  sorted values: {values}")
    print(f"  最小值: {values[0]}")
    print(f"  最大值: {values[-1]}\n")
    
    print("方法 3：使用 lambda")
    min_key = min(prices, key=prices.get)
    max_key = max(prices, key=prices.get)
    print(f"  min key: {min_key} ({prices[min_key]})")
    print(f"  max key: {max_key} ({prices[max_key]})\n")
    
    print("性能提示：")
    print("  • 查找最值：zip 方式最快")
    print("  • 完整排序：三種方式性能相近")
    print("  • 可讀性：lambda 方式最直觀")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python 字典最值操作教學程式\n")
    print("="*60)
    
    example_min_max_with_values()
    example_sorted_with_zip()
    example_get_top_n_items()
    example_complex_sorting()
    example_real_world_analysis()
    example_comparison_methods()
    
    print("="*60)
    print("總結：")
    print("  • zip 配合 values/keys 優雅地排序字典")
    print("  • min/max 配合 zip 快速查找最值")
    print("  • sorted 進行完整排序")
    print("  • lambda 用於複雜的排序條件")
    print("  • 性能提示：zip 方式對最值查詢最快")
    print("="*60)
