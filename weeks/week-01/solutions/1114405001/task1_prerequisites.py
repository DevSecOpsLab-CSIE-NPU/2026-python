#!/usr/bin/env python3
"""
Week 01 先備知識綜合練習 - 庫存管理系統
學生：1114405001

本程式展示了 prerequisites 資料夾中的 12 項先備知識：
1. 變數與指定 (Topic 01)
2. 基本型別 (Topic 02)
3. 基本容器 (Topic 03)
4. 迴圈 (Topic 04)
5. 索引與切片 (Topic 05)
6. 可迭代對象基礎 (Topic 06)
7. 函式與 Lambda (Topic 07)
8. 推導式與生成器 (Topic 08)
9. 排序與比較 (Topic 09)
10. 模組、類別、例外 (Topic 10)
11. Hello World (Topic 11)
12. 字串格式化 (Topic 12)
"""

import sys  # Topic 10: import

# Topic 10: class
class Product:
    def __init__(self, name: str, price: float, stock_levels: list):
        # Topic 01 & 02: variables, assignment, and basic types
        self.name = name
        self.price = price
        self.stock_levels = stock_levels
    
    @property
    def total_stock(self):
        # Topic 08: generator expression within sum()
        return sum(qty for qty in self.stock_levels)

    @property
    def stock_value(self):
        return self.total_stock * self.price

def main():
    # Topic 11: print (Hello World style greeting)
    print("--- 庫存管理系統 (Week 01 Prerequisites Demo) ---")

    # Topic 03: basic containers (list of tuples)
    raw_data = [
        ("Laptop", 1200.0, [5, 3, 2]),
        ("Mouse", 25.5, [50, 20, 30]),
        ("Monitor", 300.0, [10, 5]),
        ("Keyboard", 75.0, [15, 10, 5])
    ]

    # Topic 08: List comprehension to create objects
    # Topic 01: unpacking in for loop
    products = [Product(name, price, stocks) for name, price, stocks in raw_data]

    # Topic 04 & 06: for loop and enumerate (iterable basics)
    # Topic 12: f-string formatting
    print("\n[產品庫存清單]")
    for i, p in enumerate(products, 1):
        print(f"{i:02d}. 產品: {p.name:<10} 單價: {p.price:>8.2f} 總庫存: {p.total_stock:>4}")

    # Topic 05: index & slice (取出庫存價值最高的前兩名)
    # Topic 09: sorting with key (lambda)
    print("\n[高價值庫存 (Top 2)]")
    # Topic 07: lambda
    top_valued = sorted(products, key=lambda x: x.stock_value, reverse=True)[:2]
    for p in top_valued:
        print(f"產品: {p.name:<10} 庫存總價值: {p.stock_value:>10.2f}")

    # Topic 10: exception handling
    print("\n[例外處理測試 - 嘗試轉換錯誤型別]")
    try:
        # Topic 02: type conversion
        invalid_input = "not_a_number"
        print(f"嘗試轉換 '{invalid_input}'...")
        val = float(invalid_input)
    except ValueError as e:
        print(f"捕捉到預期錯誤: {e}")

    # Topic 08: Filtering with list comprehension
    print("\n[低庫存警示 (總庫存 < 20)]")
    low_stock_names = [p.name for p in products if p.total_stock < 20]
    # Topic 12: string join
    if low_stock_names:
        print(", ".join(low_stock_names))
    else:
        print("所有產品庫存充足")

    # Topic 01: Multiple assignment
    status_code, message = 200, "系統執行完畢"
    print(f"\n狀態: {status_code} - {message}")

if __name__ == "__main__":
    main()
