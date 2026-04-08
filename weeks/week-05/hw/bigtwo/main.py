#!/usr/bin/env python3
"""
Big Two Card Game Main Entry Point
大貳紙牌遊戲主程式入口
"""

import sys
import os

# 添加模塊搜尋路徑
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from ui.app import BigTwoApp
    
    if __name__ == "__main__":
        app = BigTwoApp()
        app.run()

except ImportError as e:
    print(f"Error: Missing required module: {e}")
    print("\nPlease install pygame:")
    print("  pip install pygame")
    sys.exit(1)
