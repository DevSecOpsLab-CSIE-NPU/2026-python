"""
主題名：R07 - 有序字典（OrderedDict）
學習目標：掌握 OrderedDict 的使用，理解其不同於普通字典的有序特性。

核心概念：
  1. OrderedDict 保持鍵的插入順序（Python 3.7+ 的普通 dict 也保序）
  2. 在某些序列化場景中仍然有用
  3. 支援 move_to_end() 方法重新排序元素
  4. 相等性判斷時不僅比較內容，還比較順序
  5. 與 JSON 序列化配合時更容易預測順序
"""

from collections import OrderedDict
import json


def example_basic_ordered_dict():
    """
    示例 1：基本的有序字典
    
    說明：
      - OrderedDict 保持插入順序
      - 在 Python 3.7 之前，普通 dict 不保序
      - 現在通常使用普通 dict（已保序）
    """
    print("=== OrderedDict 基礎 ===\n")
    
    # 創建 OrderedDict
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['baz'] = 3
    
    print("插入順序: foo -> bar -> baz")
    print(f"OrderedDict: {d}\n")
    
    print("遍歷順序（保持插入順序）:")
    for key, value in d.items():
        print(f"  {key}: {value}")
    
    print("\n普通 dict（Python 3.7+ 也保序）:")
    d_normal = {}
    d_normal['foo'] = 1
    d_normal['bar'] = 2
    d_normal['baz'] = 3
    
    print(f"普通 dict: {d_normal}")
    print("在 Python 3.7 及更新版本中，普通 dict 也保持插入順序")


def example_move_to_end():
    """
    示例 2：使用 move_to_end() 重新排序
    
    說明：
      - OrderedDict 的獨特功能：可以移動元素位置
      - last=True 移到末尾（默認）
      - last=False 移到開頭
    """
    print("\n" + "="*60)
    print("=== move_to_end() 方法 ===\n")
    
    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    d['c'] = 3
    d['d'] = 4
    
    print(f"原始順序: {list(d.keys())}")
    
    # 將 'b' 移到末尾
    d.move_to_end('b')
    print(f"move_to_end('b'): {list(d.keys())}")
    
    # 將 'c' 移到開頭
    d.move_to_end('c', last=False)
    print(f"move_to_end('c', last=False): {list(d.keys())}\n")
    
    # 實際應用：LRU 緩存
    print("應用：使用 move_to_end 實現 LRU（最近最少使用）緩存")
    cache = OrderedDict()
    cache['user_1'] = 'Alice'
    cache['user_2'] = 'Bob'
    cache['user_3'] = 'Charlie'
    print(f"初始緩存: {list(cache.keys())}")
    
    # 訪問 user_1，將其標記為最近使用
    cache.move_to_end('user_1')
    print(f"訪問 user_1 後: {list(cache.keys())}")


def example_json_serialization():
    """
    示例 3：JSON 序列化
    
    說明：
      - OrderedDict 與 JSON 的結合很有用
      - 確保序列化的順序可預測
      - 對於保存配置文件等場景有利
    """
    print("\n" + "="*60)
    print("=== JSON 序列化 ===\n")
    
    # 創建有序的配置字典
    config = OrderedDict()
    config['version'] = '1.0.0'
    config['name'] = 'MyApp'
    config['author'] = 'John Doe'
    config['license'] = 'MIT'
    
    print("OrderedDict 配置:")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    # 序列化為 JSON
    json_str = json.dumps(config)
    print(f"\nJSON 序列化:\n{json_str}\n")
    
    # 驗證順序被保留
    print("JSON 中的順序:")
    data = json.loads(json_str)
    for key in data.keys():
        print(f"  {key}: {data[key]}")


def example_comparison_semantics():
    """
    示例 4：相等性判斷
    
    說明：
      - OrderedDict 的相等性判斷同時考慮順序
      - 相同內容但不同順序的 OrderedDict 被認為不相等
    """
    print("\n" + "="*60)
    print("=== OrderedDict 的相等性判斷 ===\n")
    
    # 方案1：相同順序
    d1 = OrderedDict()
    d1['a'] = 1
    d1['b'] = 2
    
    d2 = OrderedDict()
    d2['a'] = 1
    d2['b'] = 2
    
    print(f"d1 = {dict(d1)}")
    print(f"d2 = {dict(d2)}")
    print(f"d1 == d2: {d1 == d2} （相同順序）\n")
    
    # 方案2：不同順序
    d3 = OrderedDict()
    d3['b'] = 2
    d3['a'] = 1
    
    print(f"d3 = {dict(d3)}")
    print(f"d1 == d3: {d1 == d3} （順序不同）\n")
    
    # 普通 dict 的比較（不考慮順序）
    regular_dict_1 = {'a': 1, 'b': 2}
    regular_dict_3 = {'b': 2, 'a': 1}
    print(f"普通 dict 比較:")
    print(f"regular_dict_1 == regular_dict_3: {regular_dict_1 == regular_dict_3} （普通 dict 不考慮順序）")


def example_lru_cache_implementation():
    """
    示例 5：實作 LRU 緩存
    
    說明：
      - OrderedDict 最實用的應用場景之一
      - LRU：Least Recently Used，最近最少使用緩存策略
    """
    print("\n" + "="*60)
    print("=== 實作 LRU 緩存 ===\n")
    
    class LRUCache:
        """
        使用 OrderedDict 實作的 LRU 緩存
        
        特點：
          - 容量有限，一旦滿載，訪問新元素會移除最舊的
          - 訪問元素時將其標記為最近使用
        """
        def __init__(self, capacity):
            self.cache = OrderedDict()
            self.capacity = capacity
        
        def get(self, key):
            """取得值，並將其標記為最近使用"""
            if key not in self.cache:
                return -1
            # 移到末尾表示最近使用
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key, value):
            """存儲鍵值對"""
            if key in self.cache:
                # 更新現有鍵
                self.cache[key] = value
                self.cache.move_to_end(key)
            else:
                # 添加新鍵
                self.cache[key] = value
                if len(self.cache) > self.capacity:
                    # 移除最舊的（最不最近使用）
                    removed_key, _ = self.cache.popitem(last=False)
                    print(f"  緩存滿，移除最舊的: {removed_key}\n")
        
        def show(self):
            """顯示緩存狀態"""
            print(f"  緩存 [{len(self.cache)}/{self.capacity}]: {list(self.cache.keys())}")
    
    print("LRU 緩存演示（容量=3）:")
    lru = LRUCache(capacity=3)
    
    operations = [
        ('put', 1, 'Alice'),
        ('put', 2, 'Bob'),
        ('put', 3, 'Charlie'),
        ('get', 1, None),      # 訪問 1，移到末尾
        ('put', 4, 'David'),   # 容量滿，需要移除 2
    ]
    
    for op in operations:
        if op[0] == 'put':
            _, key, value = op
            print(f"put({key}, '{value}')")
            lru.put(key, value)
            lru.show()
        else:
            _, key, _ = op
            result = lru.get(key)
            print(f"get({key}) = '{result}'")
            lru.show()


def example_preserving_order_configuration():
    """
    示例 6：保序的配置文件
    
    說明：
      - 在配置管理中，有序的鍵很重要
      - 便於人工閱讀和維護
    """
    print("=" * 60)
    print("=== 應用：有序配置文件 ===\n")
    
    # 創建有序的應用配置
    app_config = OrderedDict()
    app_config['description'] = '應用配置文件'
    app_config['version'] = '2.1.0'
    app_config['database'] = {
        'host': 'localhost',
        'port': 5432,
        'name': 'mydb',
    }
    app_config['logging'] = {
        'level': 'INFO',
        'format': '[%(levelname)s] %(message)s',
    }
    app_config['security'] = {
        'ssl_enabled': True,
        'min_tls_version': '1.2',
    }
    
    print("應用配置（有序）:")
    for key in app_config:
        if isinstance(app_config[key], dict):
            print(f"  {key}:")
            for sub_key, sub_value in app_config[key].items():
                print(f"    {sub_key}: {sub_value}")
        else:
            print(f"  {key}: {app_config[key]}")
    
    # 序列化為 JSON，保持順序
    print("\nJSON 序列化（保持配置順序）:")
    config_json = json.dumps(app_config, indent=2)
    print(config_json)


if __name__ == "__main__":
    """主程式入口點"""
    print("Python OrderedDict 教學程式\n")
    print("="*60)
    
    example_basic_ordered_dict()
    example_move_to_end()
    example_json_serialization()
    example_comparison_semantics()
    example_lru_cache_implementation()
    example_preserving_order_configuration()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • OrderedDict 保持插入順序")
    print("  • Python 3.7+ 的普通 dict 也保序")
    print("  • move_to_end() 可重新排列元素")
    print("  • 相等性判斷考慮順序")
    print("  • 主要應用：LRU 緩存、有序配置等")
    print("  • JSON 序列化時保持順序便於閱讀")
    print("="*60)
