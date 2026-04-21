"""
主題名：R04 - 堆隊列（heapq）- 查找 Top-N 元素
學習目標：掌握如何使用 heapq 模塊高효地查找最大或最小的 N 個元素。

核心概念：
  1. heapq.nlargest(n, iterable) - 查找最大的 n 個元素
  2. heapq.nsmallest(n, iterable) - 查找最小的 n 個元素
  3. 支援 key 參數以自定義比較邏輯
  4. 對於複雜對象（如字典列表），可使用 lambda 提取比較鍵
  5. heapify 將列表原地轉換為堆結構
"""

import heapq


def example_basic_nlargest_nsmallest():
    """
    示例 1：基本的最大值和最小值查找
    
    說明：
      - nlargest 找 N 個最大的元素，按降序返回
      - nsmallest 找 N 個最小的元素，按升序返回
      - 相比排序整個序列再取前 N 個，這種方法更高效
    """
    print("=== 查找最大/最小的 N 個元素 ===\n")
    
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(f"原始數據: {nums}\n")
    
    # 查找最大的 3 個元素
    largest_3 = heapq.nlargest(3, nums)
    print(f"最大的 3 個元素: {largest_3}")
    
    # 查找最小的 3 個元素
    smallest_3 = heapq.nsmallest(3, nums)
    print(f"最小的 3 個元素: {smallest_3}\n")
    
    # 邊界情況
    print("邊界情況:")
    print(f"最大的 1 個: {heapq.nlargest(1, nums)}")
    print(f"最大的 100 個（超過總數）: {len(heapq.nlargest(100, nums))} 個元素")


def example_with_dictionary_list():
    """
    示例 2：查找複雜對象的 Top-N
    
    說明：
      - 在實際應用中，常需要從對象列表中找出最符合條件的 N 個
      - 使用 key 參數指定比較的屬性
      - lambda 表達式提取需要比較的值
    """
    print("\n" + "="*60)
    print("=== 股票投資組合分析 ===\n")
    
    # 股票信息：名稱、股份數、每股價格
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    ]
    
    print("股票投資組合:")
    for stock in portfolio:
        print(f"  {stock['name']}: {stock['shares']} 股 @ ${stock['price']:.2f}")
    
    print("\n--- 按株價找最便宜的 3 支股票 ---")
    cheapest = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    for stock in cheapest:
        print(f"  {stock['name']}: ${stock['price']:.2f}")
    
    print("\n--- 按株價找最昂貴的 2 支股票 ---")
    expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
    for stock in expensive:
        print(f"  {stock['name']}: ${stock['price']:.2f}")
    
    print("\n--- 按持股價值找 Top 3 ---")
    # 持股價值 = 股份數 × 每股價格
    by_value = heapq.nlargest(3, portfolio, key=lambda s: s['shares'] * s['price'])
    for i, stock in enumerate(by_value, 1):
        value = stock['shares'] * stock['price']
        print(f"  {i}. {stock['name']}: {stock['shares']} 股 × ${stock['price']:.2f} = ${value:.2f}")


def example_with_tuples():
    """
    示例 3：元組列表的 Top-N 查詢
    
    說明：
      - 處理成績、排名等元組形式的數據
      - 可以基於不同的元素進行排序
    """
    print("\n" + "="*60)
    print("=== 學生成績排名 ===\n")
    
    # (學號, 姓名, 總成績)
    students = [
        (1001, '劉明', 85),
        (1002, '王芳', 92),
        (1003, '張三', 78),
        (1004, '李四', 95),
        (1005, '孫五', 88),
    ]
    
    print("學生成績:")
    for sid, name, score in students:
        print(f"  {sid} - {name}: {score} 分")
    
    print("\n--- Top 3 高分 ---")
    top_scores = heapq.nlargest(3, students, key=lambda x: x[2])
    for i, (sid, name, score) in enumerate(top_scores, 1):
        print(f"  {i}. {name} ({sid}): {score} 分")
    
    print("\n--- 最低的 2 個分數 ---")
    low_scores = heapq.nsmallest(2, students, key=lambda x: x[2])
    for i, (sid, name, score) in enumerate(low_scores, 1):
        print(f"  {i}. {name} ({sid}): {score} 分")


def example_heapify_and_operations():
    """
    示例 4：堆操作基礎
    
    說明：
      - heapify 將列表轉換為堆結構（最小堆）
      - heappop 移除並返回最小元素
      - heappush 向堆中添加元素
      - 這些操作的時間複雜度都是 O(log n)
    """
    print("\n" + "="*60)
    print("=== 堆操作基礎 ===\n")
    
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(f"原始列表: {nums}")
    
    # 將列表轉換為堆（原地操作）
    heap = list(nums)  # 複製以保持原始列表
    heapq.heapify(heap)
    print(f"轉換為堆: {heap}")
    print("注意：堆不一定是排序的，只保證父節點小於子節點")
    
    # 逐個彈出最小元素（結果自動排序）
    print("\n逐個彈出最小元素:")
    sorted_via_heap = []
    while heap:
        min_val = heapq.heappop(heap)
        sorted_via_heap.append(min_val)
        print(f"  pop: {min_val}, 剩餘堆: {heap}")
    print(f"所有元素已排序: {sorted_via_heap}")


def example_performance_comparison():
    """
    示例 5：性能對比
    
    說明：
      - 對於小 N，heapq.nlargest/nsmallest 效率很高
      - 相比排序整個序列更有效率
      - 對於大規模數據特別明顯
    """
    print("\n" + "="*60)
    print("=== 性能對比：不同方法查找 Top-N ===\n")
    
    import time
    
    # 生成大量數據
    data = list(range(100000))
    import random
    random.shuffle(data)
    
    n = 10  # 查找前 10 大
    
    print(f"數據規模: {len(data):,} 個元素")
    print(f"查找前 {n} 大的元素\n")
    
    # 方法 1: 用 heapq.nlargest
    start = time.time()
    result1 = heapq.nlargest(n, data)
    time1 = time.time() - start
    print(f"heapq.nlargest():      {time1*1000:.4f} ms")
    
    # 方法 2: 排序後取切片
    start = time.time()
    result2 = sorted(data, reverse=True)[:n]
    time2 = time.time() - start
    print(f"sorted()[:n]:          {time2*1000:.4f} ms")
    
    # 驗證結果相同
    assert sorted(result1) == sorted(result2)
    print(f"\n兩種方法結果相同: {sorted(result1) == sorted(result2)}")
    if time1 < time2:
        print(f"heapq 快 {time2/time1:.1f} 倍")
    else:
        print(f"sorted 快 {time1/time2:.1f} 倍")


def example_real_world_use():
    """
    示例 6：實際應用場景
    
    說明：
      - 展示 heapq 在實際應用中的常見用法
    """
    print("\n" + "="*60)
    print("=== 實際應用場景 ===\n")
    
    # 場景 1：熱門文章排行
    print("場景 1：查找熱門文章")
    articles = [
        {'title': 'Python 基礎', 'views': 5000},
        {'title': 'Web 開發', 'views': 12000},
        {'title': '數據分析', 'views': 8500},
        {'title': '機器學習', 'views': 15000},
        {'title': 'API 設計', 'views': 3000},
    ]
    
    top_articles = heapq.nlargest(3, articles, key=lambda x: x['views'])
    for i, article in enumerate(top_articles, 1):
        print(f"  {i}. {article['title']}: {article['views']} 次瀏覽")
    
    # 場景 2：系統資源監控 - 找占用最多內存的進程
    print("\n場景 2：系統監控 - 內存占用最多的進程")
    processes = [
        {'pid': 1234, 'name': 'chrome', 'memory_mb': 512},
        {'pid': 5678, 'name': 'python', 'memory_mb': 256},
        {'pid': 9012, 'name': 'firefox', 'memory_mb': 768},
        {'pid': 3456, 'name': 'vscode', 'memory_mb': 324},
    ]
    
    top_memory = heapq.nlargest(2, processes, key=lambda x: x['memory_mb'])
    for process in top_memory:
        print(f"  {process['name']} (PID: {process['pid']}): {process['memory_mb']} MB")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python heapq Top-N 查詢教學程式\n")
    print("="*60)
    
    example_basic_nlargest_nsmallest()
    example_with_dictionary_list()
    example_with_tuples()
    example_heapify_and_operations()
    example_performance_comparison()
    example_real_world_use()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • heapq.nlargest(n, iterable) 查找最大的 n 個元素")
    print("  • heapq.nsmallest(n, iterable) 查找最小的 n 個元素")
    print("  • 支援 key 參數自定義比較邏輯")
    print("  • 對小 N 查詢效率遠高於完全排序")
    print("  • heapify 將列表轉換為堆結構")
    print("  • heappop/heappush 用於堆操作（O(log n)）")
    print("="*60)
