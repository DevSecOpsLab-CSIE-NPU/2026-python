"""第四題測試：二分搜尋與線性搜尋。"""

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
SCRIPT = HERE / "solution.py"


def run_program(inp: str = "") -> str:
    """執行程式並返回輸出。"""
    p = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=inp,
        capture_output=True,
        text=True,
        timeout=10
    )
    return p.stdout.strip()


def test_large_array():
    """測試大型陣列（預設 100000 元素）。"""
    output = run_program()
    lines = output.split('\n')
    
    # 檢查輸出格式
    assert len(lines) >= 4, f"預期至少 4 行輸出，得到 {len(lines)} 行"
    
    # 第一行：搜尋結果
    result_line = lines[0]
    assert "FOUND" in result_line or "NOT FOUND" in result_line
    assert "cmp=" in result_line
    
    # 第二、三行：時間
    assert "linear:" in lines[1]
    assert "binary:" in lines[2]
    
    # 第四行：比較結果
    assert "binary faster" in lines[3] or "linear faster" in lines[3] or "same speed" in lines[3]
    
    print("✓ test_large_array 通過")


def test_custom_array():
    """測試自訂陣列。"""
    # 產生小型升冪陣列
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    n = len(arr)
    inp = f"{n}\n{' '.join(map(str, arr))}"
    
    output = run_program(inp)
    lines = output.split('\n')
    
    # 應該找不到 156（因為陣列最大只有 100）
    assert "NOT FOUND" in lines[0]
    
    print("✓ test_custom_array 通過")


def test_target_in_array():
    """測試目標在陣列中的情況。"""
    # 產生包含 156 的陣列
    arr = list(range(100, 200, 2))  # [100, 102, 104, ..., 198]
    if 156 in arr:
        n = len(arr)
        inp = f"{n}\n{' '.join(map(str, arr))}"
        
        output = run_program(inp)
        lines = output.split('\n')
        
        # 應該找到 156
        assert "FOUND" in lines[0]
        
        # 檢查索引
        result_line = lines[0]
        idx = int(result_line.split()[1])
        assert 0 <= idx < n
        
        print("✓ test_target_in_array 通過")


if __name__ == "__main__":
    test_large_array()
    test_custom_array()
    test_target_in_array()
    print("\n✓ 所有測試通過！")
