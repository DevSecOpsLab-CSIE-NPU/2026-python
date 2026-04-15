#!/usr/bin/env python3
"""
快速測試執行腳本
用於驗證 test_10062.py 中的所有測試
"""

import sys
import os

# 添加路徑以便導入模塊
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # 導入並執行測試
    from test_10062 import run_tests
    success = run_tests()
    sys.exit(0 if success else 1)
except Exception as e:
    print(f"錯誤: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
