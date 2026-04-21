"""
主題名：R13 - 字典列表排序（itemgetter）
學習目標：掌握使用 operator.itemgetter 進行高效的字典列表排序。

核心概念：
  1. itemgetter 是從字典或序列中提取元素的高效工具
  2. operator.itemgetter('key') 速度更快than lambda
  3. 支援多個鍵的組合排序
  4. 比 lambda 函數更簡潔更高效
  5. 適用於數據處理和數據分析任務
"""

from operator import itemgetter


def example_basic_sorting_by_key():
    """
    示例 1：基本字典排序
    
    說明：
      - 按単一鍵排序字典列表
      - 使用 itemgetter 比 lambda 更快
    """
    print("=== 按鍵排序字典列表 ===\n")
    
    # 人員信息
    rows = [
        {'fname': 'Brian', 'uid': 1003},
        {'fname': 'John', 'uid': 1001},
        {'fname': 'Alice', 'uid': 1002},
    ]
    
    print("原始列表:")
    for row in rows:
        print(f"  {row}")
    
    print("\n方式 1：使用 itemgetter（推薦）")
    sorted_by_fname = sorted(rows, key=itemgetter('fname'))
    print("按 fname 排序 (itemgetter):")
    for row in sorted_by_fname:
        print(f"  {row}")
    
    print("\n方式 2：使用 lambda")
    sorted_by_fname_lambda = sorted(rows, key=lambda x: x['fname'])
    print("按 fname 排序 (lambda):")
    for row in sorted_by_fname_lambda:
        print(f"  {row}")
    
    print("\n對比：")
    print("  • itemgetter: 更快，更簡潔")
    print("  • lambda: 更靈活，但略慢")


def example_sorting_by_uid():
    """
    示例 2：按 UID 排序
    
    說明：
      - 按數值鍵排序
    """
    print("\n" + "="*60)
    print("=== 按 UID 排序 ===\n")
    
    rows = [
        {'fname': 'Brian', 'uid': 1003},
        {'fname': 'John', 'uid': 1001},
        {'fname': 'Alice', 'uid': 1002},
    ]
    
    print("原始列表:")
    for row in rows:
        print(f"  uid={row['uid']}, name={row['fname']}")
    
    print("\n按 uid 升序排列:")
    sorted_by_uid = sorted(rows, key=itemgetter('uid'))
    for row in sorted_by_uid:
        print(f"  uid={row['uid']}, name={row['fname']}")
    
    print("\n按 uid 降序排列:")
    sorted_by_uid_desc = sorted(rows, key=itemgetter('uid'), reverse=True)
    for row in sorted_by_uid_desc:
        print(f"  uid={row['uid']}, name={row['fname']}")


def example_sorting_by_multiple_keys():
    """
    示例 3：按多個鍵排序
    
    說明：
      - 可以指定多個鍵進行組合排序
      - 類似 SQL ORDER BY 的多列排序
    """
    print("\n" + "="*60)
    print("=== 按多個鍵排序 ===\n")
    
    # 員工信息
    employees = [
        {'dept': 'Sales', 'name': 'John', 'salary': 50000},
        {'dept': 'IT', 'name': 'Alice', 'salary': 60000},
        {'dept': 'Sales', 'name': 'Bob', 'salary': 55000},
        {'dept': 'IT', 'name': 'Charlie', 'salary': 65000},
    ]
    
    print("原始員工列表:")
    for emp in employees:
        print(f"  {emp['dept']:6} | {emp['name']:10} | ${emp['salary']:6}")
    
    # 先按部門排序，再按姓名排序
    print("\n按部門排序，再按姓名排序:")
    sorted_emps = sorted(employees, key=itemgetter('dept', 'name'))
    for emp in sorted_emps:
        print(f"  {emp['dept']:6} | {emp['name']:10} | ${emp['salary']:6}")
    
    # 先按部門排序，再按薪水降序
    print("\n按部門排序，再按薪水降序:")
    sorted_emps_salary = sorted(
        employees,
        key=itemgetter('dept', 'salary'),
        reverse=True  # 注意：這會反轉所有排序鍵
    )
    for emp in sorted_emps_salary:
        print(f"  {emp['dept']:6} | {emp['name']:10} | ${emp['salary']:6}")


def example_product_sorting():
    """
    示例 4：實際應用 - 商品排序
    
    說明：
      - 根據不同的商品屬性排序
    """
    print("\n" + "="*60)
    print("=== 應用：商品排序 ===\n")
    
    # 商品信息
    products = [
        {'id': 3, 'name': 'iPad', 'category': 'Electronics', 'price': 799},
        {'id': 1, 'name': 'iPhone', 'category': 'Electronics', 'price': 999},
        {'id': 2, 'name': 'MacBook', 'category': 'Electronics', 'price': 1299},
        {'id': 4, 'name': 'AirPods', 'category': 'Accessories', 'price': 199},
    ]
    
    print("原始商品列表:")
    for prod in products:
        print(f"  {prod['id']:2} | {prod['name']:10} | {prod['category']:12} | ${prod['price']:5}")
    
    # 按類別排序，再按價格排序
    print("\n按類別排序，再按價格排序:")
    sorted_prods = sorted(products, key=itemgetter('category', 'price'))
    for prod in sorted_prods:
        print(f"  {prod['id']:2} | {prod['name']:10} | {prod['category']:12} | ${prod['price']:5}")
    
    # 按價格排序
    print("\n按價格從高到低排序:")
    sorted_by_price = sorted(products, key=itemgetter('price'), reverse=True)
    for prod in sorted_by_price:
        print(f"  ${prod['price']:5} | {prod['name']:10} | {prod['id']}")


def example_sorting_tuples():
    """
    示例 5：元組排序
    
    說明：
      - itemgetter 也適用於元組序列
      - 使用索引而非鍵名
    """
    print("\n" + "="*60)
    print("=== 元組排序 ===\n")
    
    # 成績列表：(學號, 姓名, 成績)
    grades = [
        (1001, 'Alice', 85),
        (1003, 'Charlie', 95),
        (1002, 'Bob', 78),
    ]
    
    print("原始成績:")
    for sid, name, score in grades:
        print(f"  {sid} | {name:10} | {score}")
    
    # 按姓名排序（索引 1）
    print("\n按姓名排序:")
    sorted_by_name = sorted(grades, key=itemgetter(1))
    for sid, name, score in sorted_by_name:
        print(f"  {sid} | {name:10} | {score}")
    
    # 按成績排序（索引 2），降序
    print("\n按成績降序排列:")
    sorted_by_score = sorted(grades, key=itemgetter(2), reverse=True)
    for sid, name, score in sorted_by_score:
        print(f"  {sid} | {name:10} | {score}")


def example_performance_comparison():
    """
    示例 6：性能對比
    
    說明：
      - itemgetter 和 lambda 的性能差異
    """
    print("\n" + "="*60)
    print("=== 性能對比 ===\n")
    
    import time
    
    # 生成測試數據
    data = [
        {'name': f'User{i}', 'age': i % 50 + 18, 'score': i % 100}
        for i in range(10000)
    ]
    
    print(f"測試數據: {len(data)} 個字典\n")
    
    # 方法 1: itemgetter
    start = time.time()
    result1 = sorted(data, key=itemgetter('age'))
    time1 = time.time() - start
    print(f"itemgetter('age'): {time1*1000:.4f} ms")
    
    # 方法 2: lambda
    start = time.time()
    result2 = sorted(data, key=lambda x: x['age'])
    time2 = time.time() - start
    print(f"lambda x: x['age']: {time2*1000:.4f} ms")
    
    # 方法 3: 字符串鍵訪問（最慢）
    start = time.time()
    result3 = sorted(data, key=lambda x: x.get('age'))
    time3 = time.time() - start
    print(f"lambda x: x.get('age'): {time3*1000:.4f} ms\n")
    
    print("結果驗證 (結果相同):")
    print(f"  itemgetter == lambda: {result1 == result2}")
    
    if time1 < time2:
        print(f"\nitemgetter 快 {time2/time1:.1f} 倍")
    else:
        print(f"\nlambda 快 {time1/time2:.1f} 倍")


def example_real_world_data_sorting():
    """
    示例 7：實際應用 - 數據分析
    
    說明：
      - 電商平台的訂單排序
    """
    print("\n" + "="*60)
    print("=== 實際應用：訂單管理 ===\n")
    
    # 訂單列表
    orders = [
        {'order_id': 'O001', 'customer': 'Alice', 'amount': 500, 'status': 'Pending'},
        {'order_id': 'O003', 'customer': 'Charlie', 'amount': 1500, 'status': 'Shipped'},
        {'order_id': 'O002', 'customer': 'Bob', 'amount': 800, 'status': 'Pending'},
        {'order_id': 'O004', 'customer': 'David', 'amount': 1000, 'status': 'Shipped'},
    ]
    
    print("原始訂單列表:")
    for order in orders:
        print(f"  {order['order_id']} | {order['customer']:10} | ${order['amount']:5} | {order['status']}")
    
    # 按金額排序（高到低）
    print("\n按金額降序查看最大訂單:")
    high_value_orders = sorted(orders, key=itemgetter('amount'), reverse=True)
    for order in high_value_orders:
        print(f"  {order['customer']:10} | ${order['amount']:5} | {order['status']}")
    
    # 按狀態排序，再按客戶名排序
    print("\n按狀態和客戶號排序:")
    sorted_orders = sorted(orders, key=itemgetter('status', 'customer'))
    for order in sorted_orders:
        print(f"  {order['status']:8} | {order['customer']:10} | ${order['amount']:5}")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python itemgetter 教學程式\n")
    print("="*60)
    
    example_basic_sorting_by_key()
    example_sorting_by_uid()
    example_sorting_by_multiple_keys()
    example_product_sorting()
    example_sorting_tuples()
    example_performance_comparison()
    example_real_world_data_sorting()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • itemgetter('key') 用於快速提取字典元素")
    print("  • 性能優於 lambda（通常快 10-20%）")
    print("  • itemgetter('key1', 'key2') 支援多鍵排序")
    print("  • itemgetter(0, 1, ...) 可用於元組排序")
    print("  • 代碼更簡潔更易讀")
    print("  • 適用於數據科學和分析任務")
    print("="*60)
