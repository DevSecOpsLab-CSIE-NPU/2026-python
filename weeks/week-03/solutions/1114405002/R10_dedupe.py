"""
主題名：R10 - 去重且保序（Deduplication with Order Preservation）
學習目標：掌握如何移除序列中的重複元素，同時保持原始順序。

核心概念：
  1. 使用生成器和集合實現高效的去重
  2. 保持元素的原始順序
  3. 支援自定義去重邏輯（key 參數）
  4. 相比使用 set 或字典，此方法更靈活
  5. 時間複雜度 O(n)，空間複雜度 O(n)
"""


def dedupe(items):
    """
    基礎去重函數
    
    說明：
      - 移除序列中的重複元素
      - 保留首次出現的元素
      - 保持原始順序
      - 生成器方式，適合大數據集
    
    參數：
      items - 可迭代的序列
    
    返回：
      生成器，逐個產生去重後的元素
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_with_key(items, key=None):
    """
    支援自定義去重邏輯的去重函數
    
    說明：
      - 允許指定去重的比較鍵
      - 可以基於對象的某個屬性去重
      - 例如：根據對象 ID 去重，但保留原始數據
    
    參數：
      items - 可迭代的序列
      key - 提取比較值的函數（默認為 None 表示直接比較元素）
    
    返回：
      生成器，逐個產生去重後的元素
    """
    seen = set()
    for item in items:
        # 如果未提供 key，則比較元素本身
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def example_basic_deduplication():
    """
    示例 1：基本去重
    
    說明：
      - 最常見的去重場景
      - 簡單的值去重
    """
    print("=== 基本去重 ===\n")
    
    # 包含重複元素的列表
    data = [1, 5, 2, 5, 3, 1, 4]
    print(f"原始數據: {data}")
    
    # 使用實敗的方式
    print("\n方法 1：dedupe 生成器")
    result = list(dedupe(data))
    print(f"去重結果: {result}")
    
    print("\n方法 2：使用 set（丟失順序）")
    result_set = list(set(data))
    print(f"使用 set: {result_set}")
    
    print("\n方式 3：使用字典（Python 3.7+）")
    result_dict = list(dict.fromkeys(data))
    print(f"使用字典: {result_dict}\n")
    
    print("對比：")
    print("  • dedupe：保持順序 ✓")
    print("  • set: 丟失順序 ✗")
    print("  • dict: 保持順序 ✓")


def example_string_deduplication():
    """
    示例 2：字符串去重
    
    說明：
      - 對字符或單詞進行去重
      - 常見於數據清理
    """
    print("\n" + "="*60)
    print("=== 字符串/單詞去重 ===\n")
    
    # 文本行
    lines = ['hello', 'world', 'hello', 'python', 'world', 'code']
    print(f"原始行: {lines}")
    
    unique_lines = list(dedupe(lines))
    print(f"去重後: {unique_lines}\n")
    
    # 句子中的單詞
    sentence = "the quick brown fox jumps over the lazy dog over"
    words = sentence.split()
    print(f"句子: {sentence}")
    print(f"單詞列表: {words}")
    
    unique_words = list(dedupe(words))
    print(f"去重單詞: {unique_words}\n")
    
    # 字符去重
    text = "mississippi"
    print(f"文本: {text}")
    unique_chars = list(dedupe(text))
    print(f"去重字符: {unique_chars}")
    print(f"去重字符（字符串）: {''.join(unique_chars)}")


def example_case_insensitive_deduplication():
    """
    示例 3：不區分大小寫去重
    
    說明：
      - 使用 key 參數實現自訂去重邏輯
      - 根據轉換後的值進行去重，保留原始值
    """
    print("\n" + "="*60)
    print("=== 不區分大小寫去重 ===\n")
    
    names = ['ALICE', 'bob', 'Alice', 'BOB', 'Charlie', 'alice']
    print(f"原始名單: {names}\n")
    
    print("區分大小寫去重:")
    result_case_sensitive = list(dedupe(names))
    print(f"  結果: {result_case_sensitive}\n")
    
    print("不區分大小寫去重（保留首個出現）:")
    result_case_insensitive = list(dedupe_with_key(names, key=str.lower))
    print(f"  結果: {result_case_insensitive}\n")
    
    print("說明：")
    print("  • 區分大小寫時，ALICE、Alice、alice 被視為不同")
    print("  • 不區分大小寫時，它們被視為同一個")
    print("  • 保留首個出現的形式（ALICE）")


def example_dedup_dictionaries():
    """
    示例 4：字典列表去重
    
    說明：
      - 根據字典的某個字段去重
      - 保留首次出現的完整字典
      - 常用於數據清理
    """
    print("\n" + "="*60)
    print("=== 字典列表去重 ===\n")
    
    # 用戶列表（某些 ID 重複）
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 1, 'name': 'Alice'},      # 重複的 ID 1
        {'id': 3, 'name': 'Charlie'},
        {'id': 2, 'name': 'Bob'},        # 重複的 ID 2
    ]
    
    print("原始用戶列表:")
    for user in users:
        print(f"  {user}")
    
    print("\n根據 ID 去重:")
    unique_users = list(dedupe_with_key(users, key=lambda x: x['id']))
    for user in unique_users:
        print(f"  {user}\n")
    
    print("說明：")
    print("  • 根據 'id' 字段進行去重")
    print("  • 保留首次出現的完整用戶信息")


def example_custom_objects_dedup():
    """
    示例 5：自定義對象去重
    
    說明：
      - 對象列表的去重
      - 根據對象的特定屬性去重
    """
    print("\n" + "="*60)
    print("=== 自定義對象去重 ===\n")
    
    class Product:
        def __init__(self, product_id, name, price):
            self.product_id = product_id
            self.name = name
            self.price = price
        
        def __repr__(self):
            return f"Product({self.product_id}, '{self.name}', ${self.price})"
    
    # 產品列表
    products = [
        Product(1, '筆記本', 999),
        Product(2, '鼠標', 49),
        Product(1, '筆記本', 999),      # 重複
        Product(3, '鍵盤', 149),
        Product(2, '鼠標', 49),         # 重複
    ]
    
    print("原始產品列表:")
    for product in products:
        print(f"  {product}")
    
    print("\n根據產品 ID 去重:")
    unique_products = list(dedupe_with_key(products, key=lambda x: x.product_id))
    for product in unique_products:
        print(f"  {product}")


def example_large_file_deduplication():
    """
    示例 6：大文件去重
    
    說明：
      - 生成器特別適合處理大數據集
      - 不需要一次性將所有數據加載到內存中
      - 逐行讀取文件並去重
    """
    print("\n" + "="*60)
    print("=== 大文件去重（模擬）===\n")
    
    # 模擬日誌數據流
    def log_data_generator():
        """生成日誌數據的生成器"""
        logs = [
            'ERROR: Connection timeout',
            'INFO: User logged in',
            'ERROR: Connection timeout',  # 重複
            'WARNING: Low memory',
            'INFO: User logged in',       # 重複
            'ERROR: Database error',
        ]
        for log in logs:
            yield log
    
    print("原始日誌數據流：")
    log_iter = log_data_generator()
    for log in log_iter:
        print(f"  {log}")
    
    print("\n去重後的日誌：")
    log_iter = log_data_generator()
    unique_logs = dedupe(log_iter)
    for log in unique_logs:
        print(f"  {log}")
    
    print("\n優勢：")
    print("  • 使用生成器逐個處理")
    print("  • 內存佔用少")
    print("  • 可用於流式數據處理")


def example_performance_comparison():
    """
    示例 7：性能對比
    
    說明：
      - 不同去重方法的性能特性
    """
    print("\n" + "="*60)
    print("=== 性能對比 ===\n")
    
    import time
    
    # 生成測試數據
    data = list(range(10000)) * 2  # 20000 個元素，半數重複
    
    print(f"測試數據: {len(data)} 個元素，{len(set(data))} 個唯一值\n")
    
    # 方法 1: dedupe
    start = time.time()
    result1 = list(dedupe(data))
    time1 = time.time() - start
    print(f"dedupe 生成器: {time1*1000:.4f} ms, 結果: {len(result1)} 個元素")
    
    # 方法 2: set
    start = time.time()
    result2 = list(set(data))
    time2 = time.time() - start
    print(f"set(): {time2*1000:.4f} ms, 結果: {len(result2)} 個元素")
    
    # 方法 3: dict.fromkeys
    start = time.time()
    result3 = list(dict.fromkeys(data))
    time3 = time.time() - start
    print(f"dict.fromkeys(): {time3*1000:.4f} ms, 結果: {len(result3)} 個元素")
    
    print("\n結論：")
    print("  • dedupe: 保序，適合需要原始順序的場景")
    print("  • set: 最快但丟失順序")
    print("  • dict.fromkeys: 保序且相對高效")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python 去重且保序教學程式\n")
    print("="*60)
    
    example_basic_deduplication()
    example_string_deduplication()
    example_case_insensitive_deduplication()
    example_dedup_dictionaries()
    example_custom_objects_dedup()
    example_large_file_deduplication()
    example_performance_comparison()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • dedupe 函數保持順序去除重複")
    print("  • dedupe_with_key 支援自定義去重邏輯")
    print("  • 使用集合追蹤已見元素，時間複雜度 O(n)")
    print("  • 生成器方式適合大數據集")
    print("  • 比 set 更靈活，比循環更高效")
    print("="*60)
