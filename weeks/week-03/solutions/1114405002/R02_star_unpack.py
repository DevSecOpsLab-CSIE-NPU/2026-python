"""
主題名：R02 - 星號解包（Extended Unpacking with *）
學習目標：掌握如何使用星號（*）來解包數量不固定的序列。

核心概念：
  1. 星號 * 用於捕獲「剩餘的」元素，適用於序列長度不固定的情況
  2. 星號只能在一個解包表達式中使用一次
  3. 星號捕獲的結果始終是一個列表
  4. 星號可以出現在左、中、右三個位置，靈活應用於不同情境
"""

def example_drop_first_last():
    """
    示例 1：丟棄第一個和最後一個元素
    
    說明：
      - 計算平均成績時，通常需要丟棄最高分和最低分
      - 使用 first, *middle, last 的模式來實現
      - *middle 會捕獲除了第一個和最後一個元素外的所有元素
    """
    print("=== 丟棄首尾元素：計算中間成績平均 ===")
    
    def drop_first_last(grades):
        """
        計算一組成績的平均值（去掉最高分和最低分）
        
        參數：
          grades - 包含成績的序列（元組或列表）
        
        返回：
          中間成績的平均值
        """
        first, *middle, last = grades
        print(f"首個成績: {first}")
        print(f"中間成績: {middle}")
        print(f"最後成績: {last}")
        avg = sum(middle) / len(middle)
        print(f"中間成績平均值: {avg:.2f}\n")
        return avg
    
    # 測試情況1：單個班級成績
    grades1 = (80, 85, 90, 88, 92)
    result1 = drop_first_last(grades1)
    
    # 測試情況2：另一個班級成績
    grades2 = (75, 88, 95, 100, 72)
    result2 = drop_first_last(grades2)


def example_variable_length_records():
    """
    示例 2：處理不同長度的記錄
    
    說明：
      - 電話記錄可能包含多個電話號碼
      - 使用 *phone_numbers 來捕獲所有不確定數量的電話號碼
      - 這樣可以處理可能有不同個數電話的人員記錄
    """
    print("=== 處理不同長度的電話記錄 ===")
    
    # 記錄格式：（名稱, 郵箱, 電話1, 電話2, ...）
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212', '312-555-1212')
    
    # 解包：名稱, 郵箱, 以及所有電話號碼
    name, email, *phone_numbers = record
    
    print(f"名稱: {name}")
    print(f"郵箱: {email}")
    print(f"電話數量: {len(phone_numbers)}")
    for i, phone in enumerate(phone_numbers, 1):
        print(f"  電話 {i}: {phone}")
    print()


def example_trailing_values():
    """
    示例 3：星號位於末尾
    
    說明：
      - *trailing 位於末尾時，捕獲最後面的所有元素（除了指定的當前值）
      - 用於需要處理前面多個元素的情況
    """
    print("=== 星號位於末尾 ===")
    
    # 場景：監控最新的數據，同時保留歷史趨勢
    data = [10, 8, 7, 1, 9, 5, 10, 3]
    
    # 提取歷史值和當前值
    *trailing, current = data
    
    print(f"數據序列: {data}")
    print(f"歷史值: {trailing}")
    print(f"當前值: {current}")
    print(f"上次值: {trailing[-1] if trailing else 'N/A'}")
    print(f"趨勢: {'↑ 上升' if current > trailing[-1] else '↓ 下降'}\n")


def example_star_in_middle():
    """
    示例 4：星號位於中間
    
    說明：
      - star 位於中間時，捕獲開始和結束之間的所有元素
      - 適用於需要保留首尾值，但中間值數量不定的情況
    """
    print("=== 星號位於中間 ===")
    
    # 從文件讀取的程式執行日誌
    log = ['START', 'Step1', 'Step2', 'Step3', 'Validation', 'Step4', 'END']
    
    start, *steps, end = log
    
    print(f"開始標籤: {start}")
    print(f"執行步驟:")
    for i, step in enumerate(steps, 1):
        print(f"  {i}. {step}")
    print(f"結束標籤: {end}\n")


def example_nested_unpacking():
    """
    示例 5：嵌套解包
    
    說明：
      - 可以結合序列解包和星號解包處理複雜的嵌套結構
      - 例如處理包含多行資料的表格
    """
    print("=== 嵌套解包 ===")
    
    # 人員記錄：(姓名, 年齡, (電話1, 電話2, ...))
    records = [
        ('Alice', 25, ('111-1111', '222-2222', '333-3333')),
        ('Bob', 30, ('444-4444', '555-5555')),
    ]
    
    for record in records:
        name, age, (*phones,) = record  # 注意內層也使用星號
        print(f"{name} ({age} 歲): {', '.join(phones)}")
    
    print()


def example_practical_parsing():
    """
    示例 6：實際應用 - 解析命令行參數
    
    說明：
      - 星號解包在解析和處理不同長度的資料非常實用
      - 例如：命令名 + 多個參數
    """
    print("=== 實際應用：解析命令行 ===")
    
    # 模擬命令行輸入
    commands = [
        ('mkdir', '-p', '/home/user/project'),
        ('copy', 'file1.txt', 'dest/'),
        ('echo', 'Hello', 'World', 'Python'),
    ]
    
    for cmd_line in commands:
        command, *args = cmd_line
        print(f"命令: {command}")
        print(f"參數數量: {len(args)}")
        print(f"參數: {args}")
        print()


def example_common_patterns():
    """
    示例 7：常見模式彙總
    
    說明：
      - 展示星號解包的各種常見用法和組合
    """
    print("=== 常見模式彙總 ===\n")
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 模式1：first, *rest
    first, *rest = data
    print(f"模式 first, *rest:")
    print(f"  first={first}, rest={rest}\n")
    
    # 模式2：first, *middle, last
    first, *middle, last = data
    print(f"模式 first, *middle, last:")
    print(f"  first={first}, middle={middle}, last={last}\n")
    
    # 模式3：first, second, *rest
    first, second, *rest = data
    print(f"模式 first, second, *rest:")
    print(f"  first={first}, second={second}, rest={rest}\n")
    
    # 模式4：*head, second_to_last, last
    *head, second_to_last, last = data
    print(f"模式 *head, second_to_last, last:")
    print(f"  head={head}, second_to_last={second_to_last}, last={last}\n")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python 星號解包教學程式\n")
    print("=" * 60)
    
    example_drop_first_last()
    example_variable_length_records()
    example_trailing_values()
    example_star_in_middle()
    example_nested_unpacking()
    example_practical_parsing()
    example_common_patterns()
    
    print("=" * 60)
    print("總結：")
    print("  • 星號 (*) 用於捕獲數量不固定的元素")
    print("  • 每個解包表達式中只能有一個星號")
    print("  • 星號捕獲的結果永遠是一個列表")
    print("  • 星號可以出現在左、中、右位置")
    print("  • 可以組合星號與其他變數進行靈活解包")
    print("=" * 60)
