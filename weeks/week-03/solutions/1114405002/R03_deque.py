"""
主題名：R03 - 雙端隊列（Deque）
學習目標：掌握 collections.deque 的使用，了解其在固定大小序列和隊列操作中的優勢。

核心概念：
  1. deque（雙端隊列）是一種允許從兩端快速進行 append 和 pop 操作的資料結構
  2. maxlen 參數用於設定隊列的最大長度，超過時自動丟棄舊元素
  3. appendleft 和 popleft 提供左端操作，append 和 pop 提供右端操作
  4. deque 的時間複雜度遠優於列表的左端操作（O(1) vs O(n)）
"""

from collections import deque


def example_fixed_length_queue():
    """
    示例 1：固定大小的隊列（保留最後 N 個元素）
    
    說明：
      - maxlen 參數限制隊列最大元素數
      - 當新元素超出限制時，自動從隊列另一端丟棄最舊的元素
      - 適合用於保留最近 N 個事件、日誌等場景
    """
    print("=== 固定大小隊列：保留最後 3 個元素 ===\n")
    
    # 創建最大長度為 3 的隊列
    q = deque(maxlen=3)
    
    print(f"初始隊列: {q}")
    print(f"隊列最大容量: {q.maxlen}\n")
    
    # 逐個添加元素
    elements = [1, 2, 3, 4, 5]
    for elem in elements:
        q.append(elem)
        print(f"append({elem}): {list(q)}")
    
    print("\n說明：當添加第 4 個元素時，最舊的元素 1 被自動移除")


def example_bidirectional_operations():
    """
    示例 2：雙端操作
    
    說明：
      - deque 支援從兩端進行 append 和 pop 操作
      - appendleft: 在左端添加元素
      - popleft: 從左端移除元素
      - append: 在右端添加元素
      - pop: 從右端移除元素
    """
    print("\n" + "="*50)
    print("=== 雙端操作示例 ===\n")
    
    q = deque()
    
    # 從左端添加
    q.appendleft('A')
    q.appendleft('B')
    q.appendleft('C')
    print(f"3 次 appendleft: {list(q)}")
    
    # 重置隊列
    q = deque(['A', 'B', 'C', 'D'])
    print(f"\n初始隊列: {list(q)}")
    
    # 左端操作
    left_elem = q.popleft()
    print(f"popleft(): 移除 '{left_elem}'，隊列: {list(q)}")
    
    # 右端操作
    right_elem = q.pop()
    print(f"pop(): 移除 '{right_elem}'，隊列: {list(q)}")
    
    # 重新添加
    q.appendleft('X')
    q.append('Y')
    print(f"appendleft('X'), append('Y'): {list(q)}")


def example_rotating():
    """
    示例 3：循環旋轉
    
    說明：
      - rotate 方法可以將隊列元素循環旋轉
      - 正數旋轉向右，負數旋轉向左
      - 這在處理循環序列時非常有用
    """
    print("\n" + "="*50)
    print("=== 循環旋轉操作 ===\n")
    
    q = deque([1, 2, 3, 4, 5])
    print(f"原始隊列: {list(q)}")
    
    # 右旋轉 2 個位置
    q.rotate(2)
    print(f"rotate(2) 後: {list(q)}")
    
    # 重置
    q = deque([1, 2, 3, 4, 5])
    
    # 左旋轉 2 個位置
    q.rotate(-2)
    print(f"rotate(-2) 後: {list(q)}")


def example_practical_sliding_window():
    """
    示例 4：實際應用 - 滑動窗口
    
    說明：
      - 使用 maxlen 的 deque 可以優雅地實現滑動窗口
      - 計算移動平均值時特別有用
      - 效率遠高於手動管理列表
    """
    print("\n" + "="*50)
    print("=== 實際應用：計算移動平均值 ===\n")
    
    def moving_average(data, window_size):
        """
        計算移動平均值
        
        參數：
          data: 數據序列
          window_size: 窗口大小
        
        返回：
          移動平均值列表
        """
        window = deque(maxlen=window_size)
        averages = []
        
        for value in data:
            window.append(value)
            # 只有當窗口填滿時才計算平均值
            if len(window) == window_size:
                avg = sum(window) / len(window)
                averages.append(avg)
        
        return averages
    
    # 模擬股票價格數據
    prices = [100, 102, 101, 103, 105, 104, 106, 108, 107, 109]
    print(f"股票價格序列: {prices}")
    
    # 計算 3 日移動平均
    moving_avg = moving_average(prices, 3)
    print(f"3 日移動平均: {[f'{avg:.2f}' for avg in moving_avg]}")
    
    # 計算 5 日移動平均
    moving_avg = moving_average(prices, 5)
    print(f"5 日移動平均: {[f'{avg:.2f}' for avg in moving_avg]}")


def example_practical_recent_logs():
    """
    示例 5：實際應用 - 保留最近的日誌
    
    說明：
      - 使用固定大小的 deque 保留最新的 n 條日誌
      - 適用於記錄異常、監控事件等高頻操作
      - 避免了無限增長的內存佔用
    """
    print("\n" + "="*50)
    print("=== 實際應用：保留最近的日誌 ===\n")
    
    # 保留最新的 5 條日誌
    recent_logs = deque(maxlen=5)
    
    # 模擬日誌事件
    events = [
        "用戶登入",
        "文件上傳",
        "資料庫查詢",
        "API 請求",
        "快取更新",
        "使用者登出",
        "系統日誌",
        "性能監控",
    ]
    
    for i, event in enumerate(events, 1):
        recent_logs.append(f"[事件 {i}] {event}")
    
    print("最新的 5 條日誌事件：")
    for log in recent_logs:
        print(f"  {log}")
    
    print(f"\n總共發生了 {len(events)} 個事件，但只保留了最新的 {len(recent_logs)} 個")


def example_comparison_with_list():
    """
    示例 6：Deque vs List 性能對比
    
    說明：
      - 從列表的左端操作效率低（O(n)），需要移動所有元素
      - deque 對兩端的操作效率都很高（O(1)）
      - 這在處理大量數據時差異明顯
    """
    print("\n" + "="*50)
    print("=== Deque vs List 操作效率 ===\n")
    
    # 操作演示
    print("場景：在左端添加 5 個元素\n")
    
    # 使用列表
    lst = []
    print("使用列表 List:")
    for i in range(1, 6):
        lst.insert(0, i)  # 在左端插入（低效，O(n)）
        print(f"  insert(0, {i}): {lst}")
    
    print("\n使用 Deque:")
    dq = deque()
    for i in range(1, 6):
        dq.appendleft(i)  # 在左端加入（高效，O(1)）
        print(f"  appendleft({i}): {list(dq)}")
    
    print("\n結論：")
    print("  • 列表的 insert(0, ...) 需要移動所有元素 - O(n)")
    print("  • deque 的 appendleft(...) 直接在左端操作 - O(1)")


def example_use_cases():
    """
    示例 7：Deque 的各種應用場景
    
    說明：
      - 展示 deque 在不同領域的應用
    """
    print("\n" + "="*50)
    print("=== Deque 的應用場景 ===\n")
    
    applications = [
        ("廣度優先搜索 (BFS)", "作為隊列存儲待訪問節點"),
        ("括號匹配", "使用 deque 將剩餘的括號出隊進行驗證"),
        ("滑動窗口", "維持固定大小的窗口"),
        ("撤銷/重做功能", "分別使用兩個 deque 保存操作歷史"),
        ("任務隊列", "生產者-消費者模式中的任務隊列"),
        ("最小值/最大值查詢", "在滑動窗口中快速查詢"),
    ]
    
    for i, (name, description) in enumerate(applications, 1):
        print(f"{i}. {name}")
        print(f"   {description}\n")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python Deque 教學程式\n")
    print("=" * 50)
    
    example_fixed_length_queue()
    example_bidirectional_operations()
    example_rotating()
    example_practical_sliding_window()
    example_practical_recent_logs()
    example_comparison_with_list()
    example_use_cases()
    
    print("=" * 50)
    print("總結：")
    print("  • Deque 提供從兩端快速操作的資料結構")
    print("  • maxlen 參數可自動管理固定大小隊列")
    print("  • 對兩端操作的時間複雜度都是 O(1)")
    print("  • 相比列表的 insert(0) 效率高得多")
    print("  • 適用於隊列、滑動窗口、BFS 等場景")
    print("=" * 50)
