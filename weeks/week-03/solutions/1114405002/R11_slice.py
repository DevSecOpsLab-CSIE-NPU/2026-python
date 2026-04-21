"""
主題名：R11 - 命名切片（Named Slices）
學習目標：掌握使用 slice() 函數創建命名切片，提高代碼可讀性和可維護性。

核心概念：
  1. slice(start, stop, step) 創建切片對象
  2. 命名切片提高代碼可讀性
  3. 避免在代碼中散佈魔法數字
  4. 切片對象可重複使用
  5. 適用於固定格式的字符串解析
"""


def example_basic_slice_usage():
    """
    示例 1：基本切片對象使用
    
    說明：
      - slice() 返回一個切片對象
      - 可以像普通切片一樣使用
      - 但代碼含義更清晰
    """
    print("=== 基本切片對象使用 ===\n")
    
    data = "0123456789"
    
    # 傳統方式（魔法數字）
    print(f"數據: {data}\n")
    
    print("傳統方式（魔法數字）:")
    print(f"  data[0:3] = {data[0:3]}")
    print(f"  data[3:6] = {data[3:6]}")
    print(f"  data[6:9] = {data[6:9]}\n")
    
    # 使用切片對象
    print("使用 slice 對象:")
    first_part = slice(0, 3)
    middle_part = slice(3, 6)
    last_part = slice(6, 9)
    
    print(f"  first_part = slice(0, 3)")
    print(f"  data[first_part] = {data[first_part]}")
    print(f"  middle_part = slice(3, 6)")
    print(f"  data[middle_part] = {data[middle_part]}")
    print(f"  last_part = slice(6, 9)")
    print(f"  data[last_part] = {data[last_part]}")


def example_structured_format_parsing():
    """
    示例 2：解析固定格式的文本
    
    說明：
      - 固定寬度格式（Fixed-width format）的文本解析
      - 常見於舊系統的數據交換
      - 使用命名切片使代碼自文檔化
    """
    print("\n" + "="*60)
    print("=== 固定格式文本解析 ===\n")
    
    # 模擬股票購買記錄（固定寬度格式）
    record = '....................100 .......513.25 ..........'
    
    print(f"原始記錄:")
    print(f"  {record}")
    print(f"  {' ' * 10}1111111111222222222233333333334444444444}")
    print(f"  {' ' * 10}0123456789012345678901234567890123456789}\n")
    
    # 定義各個字段的位置
    SHARES = slice(20, 23)      # 位置 20-23：股份數
    PRICE = slice(31, 37)       # 位置 31-37：股價
    
    print(f"定義切片:")
    print(f"  SHARES = slice(20, 23)  # {record[SHARES]}")
    print(f"  PRICE = slice(31, 37)   # {record[PRICE]}\n")
    
    # 解析數據
    shares = int(record[SHARES])
    price = float(record[PRICE])
    cost = shares * price
    
    print(f"解析結果:")
    print(f"  股份數: {shares}")
    print(f"  股價: ${price:.2f}")
    print(f"  總成本: ${cost:.2f}")


def example_csv_like_format():
    """
    示例 3：類似 CSV 的固定寬度格式
    
    說明：
      - 處理多行固定格式數據
      - 使用相同的命名切片處理所有行
    """
    print("\n" + "="*60)
    print("=== 固定寬度的表格數據 ===\n")
    
    # 固定寬度格式的表格數據
    data_lines = [
        'Name            Age  City         ',
        'Alice           25   New York     ',
        'Bob             30   Los Angeles  ',
        'Charlie         28   Chicago      ',
    ]
    
    # 定義字段位置
    NAME = slice(0, 15)
    AGE = slice(16, 19)
    CITY = slice(21, 35)
    
    print("表格數據（固定寬度）:")
    for line in data_lines:
        print(f"  {line}")
        print(f"    {' ' * 1}{'|' * 11}{'|' * 3}{'|' * 14}")
    
    print(f"\n字段定義:")
    print(f"  NAME: slice(0, 15)")
    print(f"  AGE: slice(16, 19)")
    print(f"  CITY: slice(21, 35)\n")
    
    print("解析結果:")
    for i, line in enumerate(data_lines):
        if i == 0:  # 跳過標題行
            continue
        name = line[NAME].strip()
        age = int(line[AGE])
        city = line[CITY].strip()
        print(f"  {name:10} - {age:2} 歲 - {city}")


def example_financial_record_parsing():
    """
    示例 4：財務記錄解析（實際應用）
    
    說明：
      - 銀行或財務系統常使用固定格式
      - 命名切片提高代碼維護性
    """
    print("\n" + "="*60)
    print("=== 財務記錄解析 ===\n")
    
    # 銀行交易記錄格式
    # 格式: [日期(8)][帳號(10)][交易類型(2)][金額(10)][餘額(10)]
    records = [
        '20240101GHI12345CD0000150000001500000',
        '20240102GHI12345WD0000100000001400000',
        '20240103GHI12345CR0000050000001450000',
    ]
    
    # 定義字段
    TRANSACTION_DATE = slice(0, 8)      # YYYYMMDD
    ACCOUNT_NUM = slice(8, 18)          # 帳號
    TRANSACTION_TYPE = slice(18, 20)    # CD=卡刷, WD=提款, CR=存款
    AMOUNT = slice(20, 30)              # 金額
    BALANCE = slice(30, 40)             # 餘額
    
    # 交易類型映射
    transaction_types = {
        'CD': '卡刷',
        'WD': '提款',
        'CR': '存款',
    }
    
    print("原始記錄:")
    for record in records:
        print(f"  {record}\n")
    
    print("解析結果:")
    for record in records:
        date = record[TRANSACTION_DATE]
        account = record[ACCOUNT_NUM]
        tx_type = record[TRANSACTION_TYPE]
        amount = float(record[AMOUNT]) / 100  # 以分為單位
        balance = float(record[BALANCE]) / 100
        
        print(f"  日期: {date[0:4]}-{date[4:6]}-{date[6:8]}")
        print(f"  帳號: {account}")
        print(f"  類型: {transaction_types.get(tx_type, '未知')}")
        print(f"  金額: ￥{amount:.2f}")
        print(f"  餘額: ￥{balance:.2f}\n")


def example_log_parsing():
    """
    示例 5：日誌解析
    
    說明：
      - 解析固定格式的應用日誌
      - 提取各個字段進行分析
    """
    print("=" * 60)
    print("=== 應用日誌解析 ===\n")
    
    # 日誌記錄（固定格式）
    # 格式: [IP(15)] [時間(19)] [方法(6)] [路徑(20)]
    logs = [
        '192.168.001.100 2024-01-01 10:30:45 GET    /api/users           ',
        '192.168.001.101 2024-01-01 10:31:00 POST   /api/login           ',
        '192.168.001.102 2024-01-01 10:31:15 GET    /api/products        ',
    ]
    
    # 定義字段
    IP = slice(0, 15)
    TIMESTAMP = slice(16, 35)
    METHOD = slice(36, 42)
    PATH = slice(43, 63)
    
    print("原始日誌:")
    for log in logs:
        print(f"  {log}")
    
    print("\n解析結果:")
    for log in logs:
        ip = log[IP].strip()
        timestamp = log[TIMESTAMP]
        method = log[METHOD].strip()
        path = log[PATH].strip()
        
        print(f"  {timestamp} | {ip:15} | {method:6} | {path}")


def example_step_slicing():
    """
    示例 6：步長切片
    
    說明：
      - slice 還支援第三個參數：步長
      - 用於提取交替出現的元素
    """
    print("\n" + "="*60)
    print("=== 步長切片 ===\n")
    
    # 數據
    data = list(range(10))
    print(f"原始數據: {data}\n")
    
    # 不同的步長切片
    EVERY_OTHER = slice(0, 10, 2)      # 每隔一個步長
    EVERY_THIRD = slice(0, 10, 3)      # 每隔三個步長
    REVERSE = slice(None, None, -1)    # 反轉
    
    print("步長切片範例:")
    print(f"  EVERY_OTHER = slice(0, 10, 2)  # {data[EVERY_OTHER]}")
    print(f"  EVERY_THIRD = slice(0, 10, 3)  # {data[EVERY_THIRD]}")
    print(f"  REVERSE = slice(None, None, -1) # {data[REVERSE]}\n")
    
    # 實際應用：交替顏色
    print("應用：交替顯示行")
    colors = ['黑', '白']
    for i, value in enumerate(data):
        color = colors[i % 2]
        print(f"  [{color}] {value}", end="  ")
    print()


def example_slice_comparison():
    """
    示例 7：傳統索引 vs 命名切片
    
    說明：
      - 比較兩種方式的優缺點
    """
    print("\n" + "="*60)
    print("=== 傳統方式 vs 命名切片 ===\n")
    
    record = "0123456789ABCDEFGHIJ"
    
    print(f"記錄: {record}\n")
    
    print("方式 1：直接硬編碼索引（難以維護）")
    print(f"  第一部分: record[0:5] = {record[0:5]}")
    print(f"  第二部分: record[5:10] = {record[5:10]}")
    print(f"  第三部分: record[10:15] = {record[10:15]}\n")
    
    print("方式 2：使用命名切片（易於維護）")
    PART1 = slice(0, 5)
    PART2 = slice(5, 10)
    PART3 = slice(10, 15)
    
    print(f"  PART1 = slice(0, 5)")
    print(f"  第一部分: record[PART1] = {record[PART1]}")
    print(f"  PART2 = slice(5, 10)")
    print(f"  第二部分: record[PART2] = {record[PART2]}")
    print(f"  PART3 = slice(10, 15)")
    print(f"  第三部分: record[PART3] = {record[PART3]}\n")
    
    print("優勢：")
    print("  ✓ 代碼自文檔化")
    print("  ✓ 易於更改格式規格")
    print("  ✓ 減少硬編碼數字")
    print("  ✓ 便於測試和驗證")


if __name__ == "__main__":
    """主程式入口點"""
    print("Python 命名切片教學程式\n")
    print("="*60)
    
    example_basic_slice_usage()
    example_structured_format_parsing()
    example_csv_like_format()
    example_financial_record_parsing()
    example_log_parsing()
    example_step_slicing()
    example_slice_comparison()
    
    print("\n" + "="*60)
    print("總結：")
    print("  • slice(start, stop, step) 創建切片對象")
    print("  • 命名切片提高代碼可讀性")
    print("  • 適用於固定格式字符串解析")
    print("  • 支援步長參數")
    print("  • 避免散佈魔法數字在代碼中")
    print("  • 便於文檔維護和格式變更")
    print("="*60)
