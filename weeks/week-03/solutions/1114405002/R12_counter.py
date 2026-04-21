"""
主題名：R12 - 計數器（Counter）- 元素統計和頻率分析
學習目標：掌握使用 collections.Counter 進行元素計數和頻率統計。

核心概念：
  1. Counter 是字典的子類，用於計數可雜湊對象
  2. most_common(n) 返回出現最頻繁的 n 個元素
  3. 支援集合運算（加法、減法等）
  4. 比手動使用字典計數更簡潔
  5. 適用於詞頻統計、投票計數等場景
"""

from collections import Counter


def example_basic_counter():
    """
    示例 1：基本計數
    
    說明：
      - Counter 自動計算元素出現次數
      - 結果是以元素為鍵、次數為值的字典
    """
    print("=== 基本計數 ===\n")
    
    # 單詞列表
    words = ['look', 'into', 'my', 'eyes', 'look']
    print(f"源數據: {words}\n")
    
    # 傳統方法（冗長）
    print("傳統方法（使用字典）:")
    counts_dict = {}
    for word in words:
        counts_dict[word] = counts_dict.get(word, 0) + 1
    print(f"  結果: {counts_dict}\n")
    
    # 使用 Counter（簡潔）
    print("使用 Counter（推薦）:")
    word_counts = Counter(words)
    print(f"  結果: {word_counts}\n")
    
    print(f"類型: {type(word_counts)}")
    print(f"word_counts['look'] = {word_counts['look']}")
    print(f"word_counts['python'] = {word_counts['python']}  # 不存在時返回 0")


def example_most_common():
    """
    示例 2：找最常見的元素
    
    說明：
      - most_common(n) 返回最常見的 n 個元素
      - 結果是 (元素, 計數) 元組的列表
      - 按頻率降序排列
    """
    print("\n" + "="*60)
    print("=== 最常見元素 ===\n")
    
    words = ['look', 'into', 'my', 'eyes', 'look', 'my']
    print(f"詞語列表: {words}\n")
    
    word_counts = Counter(words)
    print(f"計數結果: {word_counts}\n")
    
    # 找最常見的 2 個詞
    print("最常見的 2 個詞：")
    most_common_2 = word_counts.most_common(2)
    print(f"  {most_common_2}\n")
    
    print("前 3 最常見的詞：")
    for word, count in word_counts.most_common(3):
        print(f"  {word}: {count} 次")
    
    # 按出現次數降序打印所有元素
    print("\n所有詞按頻率降序：")
    for word, count in word_counts.most_common():
        print(f"  {word}: {count} 次")


def example_counter_update():
    """
    示例 3：更新計數
    
    說明：
      - 使用 update() 添加新的計數
      - 計數會累加
    """
    print("\n" + "="*60)
    print("=== 更新計數 ===\n")
    
    # 第一批詞
    words1 = ['apple', 'banana', 'apple']
    counter = Counter(words1)
    print(f"第一批: {words1}")
    print(f"計數: {counter}\n")
    
    # 第二批詞
    words2 = ['apple', 'cherry', 'banana']
    counter.update(words2)
    print(f"第二批: {words2}")
    print(f"更新後: {counter}\n")
    
    print("最常見的詞：")
    for word, count in counter.most_common():
        print(f"  {word}: {count} 次")


def example_counter_arithmetic():
    """
    示例 4：計數運算
    
    說明：
      - Counter 支援加法和減法
      - 相加時計數也相加
      - 相減時只保留正計數
    """
    print("\n" + "="*60)
    print("=== 計數運算 ===\n")
    
    # 兩個計數器
    c1 = Counter({'a': 3, 'b': 1})
    c2 = Counter({'a': 1, 'c': 2})
    
    print(f"計數器 1: {c1}")
    print(f"計數器 2: {c2}\n")
    
    # 加法
    print("加法（c1 + c2）:")
    c_sum = c1 + c2
    print(f"  結果: {c_sum}")
    print(f"  說明: 'a' 的計數為 3 + 1 = 4\n")
    
    # 減法
    print("減法（c1 - c2）:")
    c_diff = c1 - c2
    print(f"  結果: {c_diff}")
    print(f"  說明: 計數為 0 或負數的元素被忽略\n")
    
    # 交集
    print("交集（& 運算符）:")
    c_intersect = c1 & c2
    print(f"  結果: {c_intersect}")
    print(f"  說明: 取每個元素計數的最小值\n")
    
    # 並集
    print("並集（| 運算符）:")
    c_union = c1 | c2
    print(f"  結果: {c_union}")
    print(f"  說明: 取每個元素計數的最大值")


def example_voting_system():
    """
    示例 5：實際應用 - 投票系統
    
    說明：
      - 統計投票結果
      - 找出獲得最多票的候選人
    """
    print("\n" + "="*60)
    print("=== 應用：投票系統 ===\n")
    
    # 模擬投票
    votes = [
        'Alice', 'Bob', 'Alice', 'Charlie',
        'Bob', 'Alice', 'David', 'Alice',
        'Charlie', 'Bob'
    ]
    
    print(f"投票結果: {votes}\n")
    
    vote_counts = Counter(votes)
    print(f"計票結果:")
    for candidate, count in vote_counts.most_common():
        print(f"  {candidate}: {count} 票")
    
    # 獲勝者
    winner, votes_won = vote_counts.most_common(1)[0]
    print(f"\n獲勝者: {winner}（{votes_won} 票）")


def example_word_frequency():
    """
    示例 6：詞頻分析
    
    說明：
      - 分析文本中的詞頻
      - 找出最常見的詞
      - 適用於 NLP 應用
    """
    print("\n" + "="*60)
    print("=== 應用：詞頻分析 ===\n")
    
    # 示例文本
    text = """
    To be or not to be that is the question
    Whether it is nobler in the mind to suffer
    """
    
    # 分詞並轉換為小寫
    words = text.lower().split()
    # 移除標點
    words = [w.strip('.,!?;:') for w in words]
    
    print(f"文本:\n{text}\n")
    print(f"詞列表: {words}\n")
    
    # 統計詞頻
    word_freq = Counter(words)
    
    print(f"詞頻統計 (出現 2 次或以上):")
    for word, freq in word_freq.most_common():
        if freq >= 2:
            print(f"  {word}: {freq} 次")
    
    print(f"\n最常見的 3 個詞:")
    for word, freq in word_freq.most_common(3):
        print(f"  {word}: {freq} 次")


def example_inventory_analysis():
    """
    示例 7：庫存分析
    
    說明：
      - 分析不同商品的銷售數量
      - 找出暢銷產品
    """
    print("\n" + "="*60)
    print("=== 應用：銷售分析 ===\n")
    
    # 每天的銷售記錄
    sales = [
        'iPhone', 'iPad', 'iPhone', 'MacBook',
        'iPhone', 'iPad', 'iPhone', 'AirPods',
        'iPad', 'iPhone'
    ]
    
    print(f"銷售記錄: {sales}\n")
    
    product_sales = Counter(sales)
    
    print("銷售統計:")
    for product, count in product_sales.most_common():
        print(f"  {product}: {count} 件")
    
    print(f"\n暢銷商品 TOP 3:")
    for i, (product, count) in enumerate(product_sales.most_common(3), 1):
        print(f"  {i}. {product}: {count} 件")
    
    total_sales = sum(product_sales.values())
    print(f"\n總銷售量: {total_sales} 件")


def example_missing_elements():
    """
    示例 8：缺失元素分析
    
    說明：
      - 減法可用於找出缺失的元素
    """
    print("\n" + "="*60)
    print("=== 缺失元素分析 ===\n")
    
    # 預期的收貨商品
    expected = Counter(['A', 'B', 'C', 'A', 'B'])
    print(f"預期收貨: {expected}\n")
    
    # 實際收貨
    received = Counter(['A', 'B', 'A'])
    print(f"實際收貨: {received}\n")
    
    # 找缺失
    missing = expected - received
    print(f"缺失商品 (expected - received):")
    for item, count in missing.items():
        print(f"  {item}: 缺少 {count} 件")
    
    # 多收
    extra = received - expected
    print(f"\n多收商品 (received - expected):")
    if extra:
        for item, count in extra.items():
            print(f"  {item}: 多收 {count} 件")
    else:
        print("  無")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python Counter 教學程式\n")
    print("="*60)
    
    example_basic_counter()
    example_most_common()
    example_counter_update()
    example_counter_arithmetic()
    example_voting_system()
    example_word_frequency()
    example_inventory_analysis()
    example_missing_elements()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • Counter 是元素計數的最佳工具")
    print("  • most_common(n) 返回最常見的 n 個元素")
    print("  • update() 可增量更新計數")
    print("  • 支援算術運算（+、-、&、|）")
    print("  • 應用：投票、詞頻、銷售分析等")
    print("  • 返回 0 而非 KeyError 對缺失鍵")
    print("="*60)
