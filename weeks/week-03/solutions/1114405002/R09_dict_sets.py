"""
主題名：R09 - 字典集合運算
學習目標：掌握如何使用集合運算進行字典的鍵和值的比較操作。

核心概念：
  1. 字典的 keys() 視圖可以進行集合運算：& | - 
  2. 字典的 items() 視圖也支援集合運算
  3. 使用 & 找公共鍵，使用 - 找差集，使用 | 找並集
  4. 字典值的比較需要轉換為集合
  5. 這種方式比循環更高效且代碼更簡潔
"""


def example_key_intersection():
    """
    示例 1：找兩個字典的公共鍵
    
    說明：
      - 使用 & 運算符找交集
      - 返回兩個字典都有的鍵
    """
    print("=== 字典集合運算：交集（&）===\n")
    
    # 兩個字典
    a = {'x': 1, 'y': 2, 'z': 3}
    b = {'w': 10, 'x': 11, 'y': 2}
    
    print(f"字典 a: {a}")
    print(f"字典 b: {b}\n")
    
    # 找公共鍵
    print("方法 1：使用 & 運算符（推薦）")
    common_keys = a.keys() & b.keys()
    print(f"  a.keys() & b.keys() = {common_keys}\n")
    
    # 傳統方法進行比較
    print("方法 2：使用 set() 和 & 運算符")
    common_keys_alt = set(a) & set(b)
    print(f"  set(a) & set(b) = {common_keys_alt}\n")
    
    # 傳統循環方法
    print("方法 3：使用循環（較冗長）")
    common_keys_loop = [k for k in a if k in b]
    print(f"  [k for k in a if k in b] = {common_keys_loop}")


def example_key_difference():
    """
    示例 2：找只在一個字典中的鍵
    
    說明：
      - 使用 - 運算符找差集
      - a.keys() - b.keys() 返回只在 a 中的鍵
    """
    print("\n" + "="*60)
    print("=== 字典集合運算：差集（-）===\n")
    
    a = {'x': 1, 'y': 2, 'z': 3}
    b = {'w': 10, 'x': 11, 'y': 2}
    
    print(f"字典 a: {a}")
    print(f"字典 b: {b}\n")
    
    # 只在 a 中的鍵
    print("在 a 中但不在 b 中的鍵:")
    only_in_a = a.keys() - b.keys()
    print(f"  a.keys() - b.keys() = {only_in_a}")
    
    # 只在 b 中的鍵
    print("\n在 b 中但不在 a 中的鍵:")
    only_in_b = b.keys() - a.keys()
    print(f"  b.keys() - a.keys() = {only_in_b}")
    
    # 應用：找出需要添加或刪除的字段
    print("\n應用：數據遷移")
    print(f"  需要添加到 a 的字段: {only_in_b}")
    print(f"  需要從 a 刪除的字段: {only_in_a}")


def example_key_union():
    """
    示例 3：合併字典的所有鍵
    
    說明：
      - 使用 | 運算符找並集
      - 返回任一字典中的鍵
    """
    print("\n" + "="*60)
    print("=== 字典集合運算：並集（|）===\n")
    
    a = {'x': 1, 'y': 2, 'z': 3}
    b = {'w': 10, 'x': 11, 'y': 2}
    
    print(f"字典 a: {a}")
    print(f"字典 b: {b}\n")
    
    # 所有鍵的集合
    all_keys = a.keys() | b.keys()
    print(f"a.keys() | b.keys() = {all_keys}")
    print(f"共有 {len(all_keys)} 個不同的鍵\n")
    
    # 應用：合併字典
    print("應用：合併兩個字典的信息")
    merged = {}
    for key in all_keys:
        a_val = a.get(key, 'N/A')
        b_val = b.get(key, 'N/A')
        print(f"  {key}: a={a_val}, b={b_val}")


def example_items_intersection():
    """
    示例 4：比較鍵值對
    
    說明：
      - items() 視圖也支援集合運算
      - 可以找出兩個字典中完全相同的項目
    """
    print("\n" + "="*60)
    print("=== 項目集合運算：items() ===\n")
    
    a = {'x': 1, 'y': 2, 'z': 3}
    b = {'w': 10, 'x': 11, 'y': 2}
    
    print(f"字典 a: {a}")
    print(f"字典 b: {b}\n")
    
    # 找相同的鍵值對
    print("相同的鍵值對（鍵和值都相同）:")
    common_items = a.items() & b.items()
    print(f"  a.items() & b.items() = {common_items}\n")
    
    # 找不同的項目
    print("只在 a 中的項目:")
    only_in_a = a.items() - b.items()
    print(f"  a.items() - b.items() = {only_in_a}\n")
    
    print("只在 b 中的項目:")
    only_in_b = b.items() - a.items()
    print(f"  b.items() - a.items() = {only_in_b}")


def example_dict_filtering():
    """
    示例 5：使用集合運算過濾字典
    
    說明：
      - 基於鍵集合構造新字典
      - 保留特定鍵的字段
    """
    print("\n" + "="*60)
    print("=== 字典過濾應用 ===\n")
    
    user_data = {
        'name': 'Alice',
        'email': 'alice@example.com',
        'phone': '123-456-7890',
        'address': '123 Main St',
        'age': 30,
        'salary': 80000,
    }
    
    # 定義需要的字段
    public_fields = {'name', 'email', 'phone'}
    private_fields = {'salary', 'address'}
    
    print(f"完整資料: {user_data}\n")
    
    print("公開字段（公開即可）:")
    public_data = {k: user_data[k] for k in user_data.keys() & public_fields}
    print(f"  {public_data}\n")
    
    print("隱私字段（不公開）:")
    private_data = {k: user_data[k] for k in user_data.keys() & private_fields}
    print(f"  {private_data}\n")
    
    print("其他字段（既非公開也非隱私）:")
    other_fields = user_data.keys() - public_fields - private_fields
    other_data = {k: user_data[k] for k in other_fields}
    print(f"  {other_data}")


def example_config_comparison():
    """
    示例 6：配置文件比較
    
    說明：
      - 比較不同版本的配置變更
      - 找出新增、刪除、修改的配置項
    """
    print("\n" + "="*60)
    print("=== 應用：配置版本對比 ===\n")
    
    # V1 配置
    config_v1 = {
        'database_host': 'localhost',
        'database_port': 5432,
        'api_timeout': 30,
        'log_level': 'INFO',
    }
    
    # V2 配置
    config_v2 = {
        'database_host': 'db.example.com',
        'database_port': 5432,
        'cache_enabled': True,
        'cache_ttl': 3600,
        'log_level': 'DEBUG',
    }
    
    print("配置 V1:")
    for k, v in config_v1.items():
        print(f"  {k}: {v}")
    
    print("\n配置 V2:")
    for k, v in config_v2.items():
        print(f"  {k}: {v}")
    
    print("\n版本差異分析：")
    
    # 新增的配置
    new_options = config_v2.keys() - config_v1.keys()
    print(f"\n新增選項:")
    for key in new_options:
        print(f"  + {key}: {config_v2[key]}")
    
    # 刪除的配置
    removed_options = config_v1.keys() - config_v2.keys()
    print(f"\n刪除選項:")
    for key in removed_options:
        print(f"  - {key}: {config_v1[key]}")
    
    # 修改的配置
    common_keys = config_v1.keys() & config_v2.keys()
    modified_options = {k for k in common_keys if config_v1[k] != config_v2[k]}
    print(f"\n修改選項:")
    for key in modified_options:
        print(f"  ~ {key}: {config_v1[key]} → {config_v2[key]}")


def example_multiple_dict_operations():
    """
    示例 7：多個字典的操作
    
    說明：
      - 處理多於兩個字典的情況
    """
    print("\n" + "="*60)
    print("=== 多字典操作 ===\n")
    
    # 三個用戶的技能集
    alice_skills = {'Python', 'JavaScript', 'SQL', 'Docker'}
    bob_skills = {'Python', 'Java', 'SQL', 'Git'}
    charlie_skills = {'Python', 'JavaScript', 'C++', 'Git'}
    
    print("技能集：")
    print(f"  Alice: {alice_skills}")
    print(f"  Bob: {bob_skills}")
    print(f"  Charlie: {charlie_skills}\n")
    
    # 所有人都會的技能
    common_skills = alice_skills & bob_skills & charlie_skills
    print(f"所有人都會的技能: {common_skills}\n")
    
    # 任何人都會的技能
    all_skills = alice_skills | bob_skills | charlie_skills
    print(f"全部技能集: {all_skills}\n")
    
    # 只有 Alice 會的技能
    unique_alice = alice_skills - bob_skills - charlie_skills
    print(f"只有 Alice 會: {unique_alice}\n")
    
    # Alice 或 Bob 會但 Charlie 不會的技能
    alice_or_bob_not_charlie = (alice_skills | bob_skills) - charlie_skills
    print(f"Alice 或 Bob 會，但 Charlie 不會: {alice_or_bob_not_charlie}")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python 字典集合運算教學程式\n")
    print("="*60)
    
    example_key_intersection()
    example_key_difference()
    example_key_union()
    example_items_intersection()
    example_dict_filtering()
    example_config_comparison()
    example_multiple_dict_operations()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • a.keys() & b.keys() - 公共鍵")
    print("  • a.keys() - b.keys() - 差集鍵")
    print("  • a.keys() | b.keys() - 所有鍵")
    print("  • a.items() & b.items() - 相同項目")
    print("  • 可用於過濾、比較和分析")
    print("  • 比循環更高效更簡潔")
    print("="*60)
