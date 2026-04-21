"""
主題名：R14 - 物件排序（attrgetter）
學習目標：掌握使用 operator.attrgetter 進行高效的自定義物件排序。

核心概念：
  1. attrgetter 用於從對象中提取指定屬性
  2. 比 lambda 函數更快更簡潔
  3. 支援嵌套屬性訪問
  4. 支援多個屬性的組合排序
  5. 適用於物件列表排序和數據篩選
"""

from operator import attrgetter


class User:
    """
    用戶類
    
    屬性：
      user_id: 用戶 ID
      name: 用戶名
      age: 年齡
      email: 郵箱
    """
    def __init__(self, user_id, name, age=None, email=None):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"User({self.user_id}, '{self.name}', {self.age})"
    
    def __eq__(self, other):
        return self.user_id == other.user_id


class Employee:
    """
    員工類
    
    屬性：
      emp_id: 員工號
      name: 姓名
      department: 部門
      salary: 薪水
    """
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
    
    def __repr__(self):
        return f"Employee({self.emp_id}, '{self.name}', {self.department}, ${self.salary})"


def example_basic_object_sorting():
    """
    示例 1：基本物件排序
    
    說明：
      - 按物件的某個屬性排序
      - 使用 attrgetter 比 lambda 更高效
    """
    print("=== 基本物件排序 ===\n")
    
    # 建立用戶列表
    users = [
        User(23, 'Alice'),
        User(3, 'Charlie'),
        User(99, 'Bob'),
    ]
    
    print("原始用戶列表:")
    for user in users:
        print(f"  {user}")
    
    # 方式 1：使用 attrgetter（推薦）
    print("\n方式 1：使用 attrgetter（推薦）")
    sorted_users_asc = sorted(users, key=attrgetter('user_id'))
    print("按 user_id 升序:")
    for user in sorted_users_asc:
        print(f"  {user}")
    
    # 方式 2：使用 lambda
    print("\n方式 2：使用 lambda")
    sorted_users_lambda = sorted(users, key=lambda x: x.user_id)
    print("按 user_id 升序:")
    for user in sorted_users_lambda:
        print(f"  {user}")
    
    # 降序排列
    print("\n按 user_id 降序:")
    sorted_users_desc = sorted(users, key=attrgetter('user_id'), reverse=True)
    for user in sorted_users_desc:
        print(f"  {user}")


def example_employee_sorting():
    """
    示例 2：員工排序
    
    說明：
      - 按員工的名字或薪水排序
    """
    print("\n" + "="*60)
    print("=== 員工排序 ===\n")
    
    # 員工列表
    employees = [
        Employee(1005, 'David', 'Sales', 45000),
        Employee(1001, 'Alice', 'IT', 60000),
        Employee(1003, 'Charlie', 'HR', 50000),
        Employee(1002, 'Bob', 'IT', 58000),
    ]
    
    print("原始員工列表:")
    for emp in employees:
        print(f"  {emp}")
    
    # 按名字排序
    print("\n按名字排序 (A-Z):")
    by_name = sorted(employees, key=attrgetter('name'))
    for emp in by_name:
        print(f"  {emp.name:10} | {emp.department:8} | ${emp.salary}")
    
    # 按薪水排序（高到低）
    print("\n按薪水排序（高到低）:")
    by_salary = sorted(employees, key=attrgetter('salary'), reverse=True)
    for emp in by_salary:
        print(f"  ${emp.salary:6} | {emp.name:10} | {emp.department}")


def example_sorting_by_nested_attributes():
    """
    示例 3：嵌套屬性排序
    
    說明：
      - attrgetter 支援嵌套屬性訪問
      - 例如：person.address.city
    """
    print("\n" + "="*60)
    print("=== 嵌套屬性排序 ===\n")
    
    class Address:
        def __init__(self, city, country):
            self.city = city
            self.country = country
    
    class Person:
        def __init__(self, name, address):
            self.name = name
            self.address = address
        
        def __repr__(self):
            return f"Person('{self.name}', {self.address.city})"
    
    # 建立人員列表
    people = [
        Person('Alice', Address('Tokyo', 'Japan')),
        Person('Bob', Address('New York', 'USA')),
        Person('Charlie', Address('Berlin', 'Germany')),
    ]
    
    print("原始人員列表:")
    for person in people:
        print(f"  {person}")
    
    # 按城市排序
    print("\n按城市排序:")
    by_city = sorted(people, key=attrgetter('address.city'))
    for person in by_city:
        print(f"  {person.name:10} | {person.address.city}")


def example_sorting_by_multiple_attributes():
    """
    示例 4：按多個屬性排序
    
    說明：
      - 類似 SQL ORDER BY 多列
      - 先按第一個屬性排序，再按第二個屬性排序
    """
    print("\n" + "="*60)
    print("=== 多屬性排序 ===\n")
    
    # 員工列表
    employees = [
        Employee(1001, 'Alice', 'IT', 60000),
        Employee(1002, 'Bob', 'Sales', 50000),
        Employee(1003, 'Charlie', 'IT', 55000),
        Employee(1004, 'David', 'Sales', 52000),
    ]
    
    print("原始員工列表:")
    for emp in employees:
        print(f"  {emp.name:10} | {emp.department:8} | ${emp.salary}")
    
    # 按部門排序，再按名字排序
    print("\n按部門排序，再按名字排序:")
    sorted_emps = sorted(employees, key=attrgetter('department', 'name'))
    for emp in sorted_emps:
        print(f"  {emp.department:8} | {emp.name:10} | ${emp.salary}")
    
    # 按部門排序，再按薪水排序
    print("\n按部門排序，再按薪水排序（高到低）:")
    sorted_emps_salary = sorted(
        employees,
        key=attrgetter('department', 'salary'),
        reverse=True
    )
    for emp in sorted_emps_salary:
        print(f"  {emp.department:8} | {emp.name:10} | ${emp.salary}")


def example_student_grade_sorting():
    """
    示例 5：實際應用 - 學生成績排序
    
    說明：
      - 按成績排序學生
      - 展示排名結果
    """
    print("\n" + "="*60)
    print("=== 應用：學生成績排序 ===\n")
    
    class Student:
        def __init__(self, student_id, name, grade):
            self.student_id = student_id
            self.name = name
            self.grade = grade
        
        def __repr__(self):
            return f"Student({self.name}, 成績={self.grade})"
    
    # 學生列表
    students = [
        Student(1001, '劉明', 85),
        Student(1005, '孫五', 78),
        Student(1002, '王芳', 92),
        Student(1003, '張三', 88),
        Student(1004, '李四', 95),
    ]
    
    print("原始成績表:")
    for student in students:
        print(f"  {student.name:6} | {student.student_id} | 成績 {student.grade}")
    
    # 按成績降序排列
    print("\n按成績排名（高到低）:")
    ranked = sorted(students, key=attrgetter('grade'), reverse=True)
    for rank, student in enumerate(ranked, 1):
        print(f"  第 {rank} 名 | {student.name:6} | {student.grade} 分")
    
    # 按名字排序
    print("\n按名字排序（字母）:")
    by_name = sorted(students, key=attrgetter('name'))
    for student in by_name:
        print(f"  {student.name:6} | 成績 {student.grade}")


def example_product_inventory():
    """
    示例 6：實際應用 - 產品庫存管理
    
    說明：
      - 按庫存或價格排序產品
    """
    print("\n" + "="*60)
    print("=== 應用：產品庫存 ===\n")
    
    class Product:
        def __init__(self, product_id, name, price, stock):
            self.product_id = product_id
            self.name = name
            self.price = price
            self.stock = stock
        
        def __repr__(self):
            return f"Product('{self.name}', ${self.price}, {self.stock} 件)"
    
    # 產品列表
    products = [
        Product(1, 'iPhone', 999, 5),
        Product(2, 'iPad', 799, 15),
        Product(3, 'MacBook', 1299, 2),
        Product(4, 'AirPods', 199, 50),
    ]
    
    print("原始產品列表:")
    for prod in products:
        print(f"  {prod.name:10} | ${prod.price:5} | 庫存 {prod.stock:2} 件")
    
    # 按庫存排序（低到高）- 找出缺貨產品
    print("\n按庫存排序（低到高）- 整理進貨清單:")
    low_stock = sorted(products, key=attrgetter('stock'))
    for prod in low_stock:
        print(f"  {prod.name:10} | 庫存 {prod.stock:2} 件")
    
    # 按價格排序（高到低）
    print("\n按價格排序（高到低）- 高價商品：")
    expensive = sorted(products, key=attrgetter('price'), reverse=True)
    for prod in expensive:
        print(f"  ${prod.price:5} | {prod.name:10} | 庫存 {prod.stock} 件")


def example_performance_attrgetter_vs_lambda():
    """
    示例 7：性能對比
    
    說明：
      - attrgetter vs lambda 的性能差異
    """
    print("\n" + "="*60)
    print("=== 性能對比：attrgetter vs lambda ===\n")
    
    import time
    
    class TestObj:
        def __init__(self, value):
            self.value = value
    
    # 生成測試數據
    data = [TestObj(i % 100) for i in range(10000)]
    
    print(f"測試數據: {len(data)} 個物件\n")
    
    # 方法 1: attrgetter
    start = time.time()
    result1 = sorted(data, key=attrgetter('value'))
    time1 = time.time() - start
    print(f"attrgetter('value'): {time1*1000:.4f} ms")
    
    # 方法 2: lambda
    start = time.time()
    result2 = sorted(data, key=lambda x: x.value)
    time2 = time.time() - start
    print(f"lambda x: x.value: {time2*1000:.4f} ms\n")
    
    if time1 < time2:
        print(f"attrgetter 快 {time2/time1:.1f} 倍")
    else:
        print(f"lambda 快 {time1/time2:.1f} 倍")
    
    print("\n結論：")
    print("  • 兩種方法都很快，差異通常不顯著")
    print("  • attrgetter 略快（通常 5-15%）")
    print("  • attrgetter 代碼更簡潔")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python attrgetter 教學程式\n")
    print("="*60)
    
    example_basic_object_sorting()
    example_employee_sorting()
    example_sorting_by_nested_attributes()
    example_sorting_by_multiple_attributes()
    example_student_grade_sorting()
    example_product_inventory()
    example_performance_attrgetter_vs_lambda()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • attrgetter('attr') 從物件中提取屬性")
    print("  • 比 lambda 式更快更簡潔")
    print("  • attrgetter('attr1', 'attr2') 支援多屬性排序")
    print("  • 支援嵌套屬性訪問，如 attrgetter('obj.nested.attr')")
    print("  • 適用於自定義物件的排序和篩選")
    print("  • 代碼可讀性高，易於維護")
    print("="*60)
