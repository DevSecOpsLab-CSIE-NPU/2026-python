"""
訊息名：R01 - 序列解包（Sequence Unpacking）
學習目標：掌握如何在 Python 中方便地將序列中的元素解包到多個變數中。

核心概念：
  1. 序列解包允許將元組、列表或其他可迭代對象的元素直接分配給多個變數
  2. Python 會依序比對數量，必須左右兩邊元素數量相等
  3. 可以使用 _ 作為占位符來丟棄不需要的值
  4. 支援嵌套解包，可以對複合結構進行遞迴式解包
"""

def example_basic_unpacking():
    """
    示例 1：基本的序列解包
    
    說明：
      - 從元組中解包兩個元素到變數 x 和 y
      - 這是最簡單的解包方式，適用於固定長度的序列
    """
    print("=== 基本序列解包 ===")
    
    # 將元組中的元素解包到變數中
    p = (4, 5)
    x, y = p
    print(f"元組 {p} 解包為 x={x}, y={y}")
    
    # 對列表進行解包
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(f"列表解包：名稱={name}, 股份={shares}, 價格={price}, 日期={date}")
    
    # 嵌套解包：將複合結構中的每個部分分解
    name, shares, price, (year, mon, day) = data
    print(f"嵌套解包：日期 = {year}/{mon}/{day}")


def example_discard_values():
    """
    示例 2：丟棄不需要的值
    
    說明：
      - 在解包時，某些值可能不需要使用
      - 使用單獨的下劃線 _ 作為占位符，表示該位置的值被忽略
      - 這樣可以保持代碼簡潔，避免創建不必要的變數
    """
    print("\n=== 丟棄不需要的值 ===")
    
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    
    # 只需要股份和價格，其他部分用 _ 代替
    _, shares, price, _ = data
    print(f"只需要：股份={shares}, 價格={price}")
    
    # 解包後的結果驗證：未使用的值被忽略了
    print("仍然可以訪問原始資料：", data)


def example_practical_use_case():
    """
    示例 3：實際應用場景
    
    說明：
      - 在處理坐標、日期、颜色 RGB 等多值資料時非常有用
      - 使表達式更加清晰易讀，代碼意圖明確
    """
    print("\n=== 實際應用場景 ===")
    
    # 場景1：處理坐標資料
    point = (10, 20)
    x, y = point
    print(f"點的坐標：({x}, {y})")
    
    # 場景2：處理 RGB 顏色
    color = (255, 128, 0)  # 橙色
    red, green, blue = color
    print(f"檢測顏色：R={red}, G={green}, B={blue}")
    
    # 場景3：处理完整的記錄
    record = ('Alice', '1990-05-15', 'engineer', 85000)
    name, birthday, position, salary = record
    print(f"員工資訊：{name} ({position})")


def example_error_cases():
    """
    示例 4：常見的錯誤情況
    
    說明：
      - 解包時元素數量不匹配會導致 ValueError
      - 理解這些錯誤有助於寫出正確的代碼
    """
    print("\n=== 錯誤情況示例 ===")
    
    data = [1, 2, 3]
    
    # 錯誤：求解之多，變數太少
    try:
        x, y = data  # 有 3 個元素，但只有 2 個變數
    except ValueError as e:
        print(f"❌ 錯誤：{e}")
    
    # 正確的方式：使用正確數量的變數
    x, y, z = data
    print(f"✓ 正確解包：x={x}, y={y}, z={z}")
    
    # 錯誤：變數太多
    try:
        x, y, z, w = data  # 有 3 個元素，但要 4 個變數
    except ValueError as e:
        print(f"❌ 錯誤：{e}")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python 序列解包教學程式\n")
    
    example_basic_unpacking()
    example_discard_values()
    example_practical_use_case()
    example_error_cases()
    
    print("\n" + "="*50)
    print("總結：")
    print("  • 序列解包使代碼更簡潔、更具可讀性")
    print("  • 使用 _ 作為占位符丟棄不需要的值")
    print("  • 注意左右兩邊元素數量必須相等")
    print("  • 支援嵌套解包可以處理複雜的資料結構")
    print("="*50)
