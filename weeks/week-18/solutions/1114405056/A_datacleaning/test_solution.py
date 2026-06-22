import os
import sys
import subprocess

HERE = os.path.dirname(__file__)
SCRIPT = os.path.join(HERE, "solution.py")


def run_input(inp: str) -> str:
    """執行程式並返回輸出結果。"""
    p = subprocess.run(
        [sys.executable, SCRIPT],
        input=inp,
        capture_output=True,
        text=True
    )
    return p.stdout


def test_intentional_fail():
    """故意失敗的測試（紅燈）：錯誤期望造成 fail。"""
    # 真正輸出為 "4 8\n"，這裡錯誤地期望 "8 4\n"
    assert run_input("5 8 4 2 4 8 0") == "8 4\n"


def test_single_case():
    """測試：去重、保序、篩除非 4 的倍數、排序。"""
    assert run_input("5 8 4 2 4 8 0") == "4 8\n"


def test_none_case():
    """測試：沒有符合條件時輸出 NONE。"""
    assert run_input("3 1 3 5 0") == "NONE\n"


def test_multiple_cases():
    """測試：多組輸入。"""
    assert run_input("8 4 7 4 2 9 2 6 7 3 1 3 5 0") == "4\nNONE\n"
