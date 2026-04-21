"""
主題名：R06 - 多值字典（Multi-value Dictionary）
學習目標：掌握如何使用 defaultdict 和 setdefault 實現一個鍵對應多個值的字典。

核心概念：
  1. defaultdict 可以為缺失的鍵自動創建默認值
  2. defaultdict(list) 用於鍵對應值列表
  3. defaultdict(set) 用於鍵對應唯一值集合
  4. setdefault() 方法也能達到類似效果
  5. 比手動檢查鍵是否存在更簡潔
"""

from collections import defaultdict


def example_defaultdict_list():
    """
    示例 1：defaultdict 配合 list
    
    說明：
      - 最常見的多值字典用法
      - 每個鍵自動對應一個空列表
      - 可以直接調用 append 而無需先檢查鍵
    """
    print("=== defaultdict(list) - 鍵對應值列表 ===\n")
    
    # 不用 defaultdict 的做法（冗長）
    print("傳統方法（需要檢查鍵是否存在）:")
    d_old = {}
    d_old.setdefault('a', []).append(1)
    d_old.setdefault('a', []).append(2)
    d_old.setdefault('b', []).append(3)
    print(f"  結果: {dict(d_old)}\n")
    
    # 使用 defaultdict 的做法（簡潔）
    print("使用 defaultdict(list)（更簡潔）:")
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(3)
    print(f"  結果: {dict(d)}\n")
    
    print("優勢：")
    print("  • 無需檢查鍵是否存在")
    print("  • 代碼更簡潔易讀")
    print("  • 避免 KeyError 異常\n")


def example_defaultdict_set():
    """
    示例 2：defaultdict 配合 set
    
    說明：
      - 當需要存儲唯一值時使用
      - 自動去重，集合中不能有重複元素
    """
    print("=" * 60)
    print("=== defaultdict(set) - 鍵對應唯一值集合 ===\n")
    
    d = defaultdict(set)
    
    # 添加值
    print("添加值：")
    d['fruits'].add('apple')
    d['fruits'].add('banana')
    d['fruits'].add('apple')  # 重複的不會添加
    d['vegetables'].add('carrot')
    d['vegetables'].add('broccoli')
    
    for key, values in d.items():
        print(f"  {key}: {values}")
    
    print("\n優勢:")
    print("  • 自動去重")
    print("  • 可進行集合運算（並集、交集等）")
    print("  • 查詢效率高 O(1)")


def example_setdefault_method():
    """
    示例 3：setdefault 方法替代方案
    
    說明：
      - setdefault 是字典的內置方法
      - 返回存在的值或設定的默認值
      - 無需導入任何模塊
    """
    print("\n" + "="*60)
    print("=== setdefault() 方法 ===\n")
    
    d = {}
    
    print("使用 setdefault 方法:")
    
    # 第一次訪問時創建列表
    d.setdefault('a', []).append(1)
    print(f"  setdefault('a', []).append(1): {d}")
    
    # 再次訪問相同キー時使用已存在的列表
    d.setdefault('a', []).append(2)  # 這裡的 [] 不會被使用
    print(f"  setdefault('a', []).append(2): {d}")
    
    # 新的鍵
    d.setdefault('b', []).append(3)
    print(f"  setdefault('b', []).append(3): {d}\n")
    
    print("補充:")
    print("  • 比 defaultdict 更靈活")
    print("  • 但 defaultdict 對於大量操作更高效")


def example_word_frequency():
    """
    示例 4：實際應用 - 詞頻統計
    
    說明：
      - 統計文本中每個單詞出現的次數
      - 使用 defaultdict(int) 會更簡潔
    """
    print("\n" + "="*60)
    print("=== 實際應用：詞頻統計 ===\n")
    
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    
    # 方法1：defaultdict(int)
    print("使用 defaultdict(int)：")
    d = defaultdict(int)
    for word in words:
        d[word] += 1
    
    print(f"  詞語: {words}")
    for word, count in sorted(d.items(), key=lambda x: x[1], reverse=True):
        print(f"    {word}: {count} 次")


def example_grouping_data():
    """
    示例 5：數據分組
    
    說明：
      - 根據某個屬性將數據分組
      - 每個組對應一個列表
    """
    print("\n" + "="*60)
    print("=== 實際應用：數據分組 ===\n")
    
    # 學生成績數據
    students = [
        {'name': '劉明', 'class': 'A', 'score': 85},
        {'name': '王芳', 'class': 'B', 'score': 92},
        {'name': '張三', 'class': 'A', 'score': 78},
        {'name': '李四', 'class': 'B', 'score': 95},
        {'name': '孫五', 'class': 'A', 'score': 88},
    ]
    
    print("學生信息:")
    for student in students:
        print(f"  {student['name']} - {student['class']} 班 - {student['score']} 分")
    
    print("\n按班級分組:")
    by_class = defaultdict(list)
    for student in students:
        by_class[student['class']].append(student)
    
    for cls, students_in_cls in sorted(by_class.items()):
        total_score = sum(s['score'] for s in students_in_cls)
        avg_score = total_score / len(students_in_cls)
        print(f"  {cls} 班:")
        for student in students_in_cls:
            print(f"    - {student['name']}: {student['score']} 分")
        print(f"    平均分: {avg_score:.1f}\n")


def example_graph_representation():
    """
    示例 6：圖的表示
    
    說明：
      - 使用 defaultdict(list) 表示圖的鄰接表
      - 每個節點對應一個列表，存儲所有連接的節點
    """
    print("=" * 60)
    print("=== 實際應用：圖的表示 ===\n")
    
    # 構建圖的鄰接表
    graph = defaultdict(list)
    
    # 添加邊（無向圖）
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'D'),
    ]
    
    print("邊的連接:")
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        print(f"  {u} -- {v}")
    
    print("\n圖的鄰接表表示:")
    for node in sorted(graph.keys()):
        print(f"  {node}: {sorted(graph[node])}")
    
    # 計算度數
    print("\n節點度數（連接數）:")
    for node in sorted(graph.keys()):
        print(f"  節點 {node}: {len(graph[node])} 條邊")


def example_comparison_and_performance():
    """
    示例 7：defaultdict vs 傳統方式性能對比
    
    說明：
      - 演示 defaultdict 相比傳統方式的優能優勢
    """
    print("\n" + "="*60)
    print("=== defaultdict vs 傳統方式 ===\n")
    
    data = ['a'] * 1000 + ['b'] * 500 + ['c'] * 200
    
    print("方式 1：傳統方式（檢查鍵）")
    d1 = {}
    for key in data:
        if key not in d1:
            d1[key] = []
        d1[key].append(1)
    print(f"  結果: {dict(d1)}\n")
    
    print("方式 2：defaultdict")
    d2 = defaultdict(list)
    for key in data:
        d2[key].append(1)
    print(f"  結果: {dict(d2)}\n")
    
    print("方式 3：setdefault")
    d3 = {}
    for key in data:
        d3.setdefault(key, []).append(1)
    print(f"  結果: {dict(d3)}\n")
    
    print("結論：")
    print("  • 三種方式功能相同")
    print("  • defaultdict：最簡潔，性能最好")
    print("  • setdefault：無需導入，適合簡單場景")


def example_nested_defaultdict():
    """
    示例 8：嵌套 defaultdict
    
    說明：
      - 可以嵌套多層 defaultdict 處理複雜結構
      - 例如：國家 -> 城市 -> 人口
    """
    print("\n" + "="*60)
    print("=== 嵌套 defaultdict ===\n")
    
    # 創建嵌套的 defaultdict
    cities = defaultdict(lambda: defaultdict(list))
    
    data = [
        ('中國', '北京', '劉明'),
        ('中國', '上海', '王芳'),
        ('日本', '東京', '田中'),
        ('中國', '北京', '張三'),
    ]
    
    print("人員分佈數據:")
    for country, city, person in data:
        cities[country][city].append(person)
        print(f"  {country} - {city}: {person}")
    
    print("\n按國家和城市分類:")
    for country in sorted(cities.keys()):
        print(f"  {country}:")
        for city in sorted(cities[country].keys()):
            people = cities[country][city]
            print(f"    {city}: {', '.join(people)}")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python 多值字典教學程式\n")
    print("="*60)
    
    example_defaultdict_list()
    example_defaultdict_set()
    example_setdefault_method()
    example_word_frequency()
    example_grouping_data()
    example_graph_representation()
    example_comparison_and_performance()
    example_nested_defaultdict()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • defaultdict 自動為缺失的鍵創建默認值")
    print("  • defaultdict(list) 用於值列表")
    print("  • defaultdict(set) 用於唯一值集合")
    print("  • setdefault() 是內置替代方案")
    print("  • 適用於分組、計數、圖表示等場景")
    print("  • 可以嵌套多層處理複雜結構")
    print("="*60)
