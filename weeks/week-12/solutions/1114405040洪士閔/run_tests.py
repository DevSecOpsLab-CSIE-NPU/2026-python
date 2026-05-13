"""
執行完整測試並生成詳細的測試紀錄

此程式運行所有單元測試，並將結果保存到文件中。
"""

import sys
import unittest
from io import StringIO
from datetime import datetime


def run_all_tests():
    """
    運行所有單元測試並捕獲詳細的輸出結果。
    
    返回：
        tuple: (測試結果, 詳細輸出文本)
    """
    # 創建測試套件
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    
    # 捕獲詳細輸出
    test_output = StringIO()
    runner = unittest.TextTestRunner(stream=test_output, verbosity=2)
    
    # 運行測試
    result = runner.run(suite)
    
    # 獲取輸出
    output_text = test_output.getvalue()
    
    return result, output_text


def generate_test_record(result, output_text):
    """
    生成詳細的測試記錄。
    
    參數：
        result: unittest 的測試結果對象
        output_text (str): 測試的詳細輸出文本
    
    返回：
        str: 完整的測試記錄文本
    """
    
    record = f"""
{'='*80}
  題目 10908 - Largest Square 完整測試紀錄
  測試執行時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*80}

【執行摘要】
✓ 測試框架: Python unittest
✓ 測試檔案: test_10908.py
✓ 主程式: q10908_solution.py
✓ 運行環境: Python 3.15+

【測試統計】
- 執行測試數: {result.testsRun}
- 通過數: {result.testsRun - len(result.failures) - len(result.errors)}
- 失敗數: {len(result.failures)}
- 錯誤數: {len(result.errors)}
- 成功率: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%

【測試結果】
"""
    
    if result.wasSuccessful():
        record += "✓ 所有測試均通過 - PASS\n"
    else:
        record += "✗ 有測試失敗 - FAIL\n"
    
    record += f"""
{'='*80}
  詳細測試輸出
{'='*80}

{output_text}

"""
    
    if result.failures:
        record += f"""
{'='*80}
  失敗測試詳情
{'='*80}

"""
        for test, traceback in result.failures:
            record += f"""
測試: {test}
詳情:
{traceback}
"""
    
    if result.errors:
        record += f"""
{'='*80}
  錯誤測試詳情
{'='*80}

"""
        for test, traceback in result.errors:
            record += f"""
測試: {test}
詳情:
{traceback}
"""
    
    record += f"""
{'='*80}
  測試完成
  完成時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*80}
"""
    
    return record


def main():
    """
    主程式：運行測試並保存紀錄。
    """
    print("開始運行測試...")
    print("=" * 80)
    
    try:
        # 運行所有測試
        result, output_text = run_all_tests()
        
        # 生成測試記錄
        record = generate_test_record(result, output_text)
        
        # 保存到文件
        with open('TEST_LOG_10908.txt', 'w', encoding='utf-8') as f:
            f.write(record)
        
        # 輸出到控制台
        print(record)
        
        # 返回状态码
        if result.wasSuccessful():
            print("\n✓ 所有測試通過！測試紀錄已保存到 TEST_LOG_10908.txt")
            return 0
        else:
            print("\n✗ 有測試失敗！請查看 TEST_LOG_10908.txt 中的詳情")
            return 1
            
    except Exception as e:
        print(f"✗ 運行測試時發生錯誤: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
