import time
import math
import pytest
from timing import timeit

def test_timeit_preserves_return_and_records_and_last_elapsed():
    """正常情況：return 不變，records 長度等於 repeat，last_elapsed 為該次平均"""
    @timeit(repeat=4)
    def answer():
        """returns 42"""
        time.sleep(0.001)
        return 42

    ret = answer()
    assert ret == 42
    assert hasattr(answer, "records")
    assert isinstance(answer.records, list)
    assert len(answer.records) == 4
    # 每個 record 應為 float 秒數，last_elapsed 為平均
    assert all(isinstance(x, float) for x in answer.records)
    assert isinstance(answer.last_elapsed, float)
    assert math.isclose(
        answer.last_elapsed, sum(answer.records[-4:]) / 4, rel_tol=1e-6
    )

def test_timeit_wraps_preserve_metadata_and_no_print(capsys):
    """檢查 functools.wraps 行為與裝飾器不印出任何東西"""
    def original_func():
        """original-docstring"""
        time.sleep(0.0005)
        return "ok"

    decorated = timeit()(original_func)  # 使用帶括號的預設方式
    # metadata preserved
    assert decorated.__name__ == original_func.__name__
    assert decorated.__doc__ == original_func.__doc__

    # 呼叫時不應該有任何 stdout 輸出
    res = decorated()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert res == "ok"

def test_invalid_repeat_raises_value_error():
    """edge case：repeat < 1 要直接 raise ValueError"""
    with pytest.raises(ValueError):
        timeit(repeat=0)

def test_decorator_without_parentheses_uses_default_repeat():
    """確認不帶括號的 @timeit 也能用（default repeat=3）"""
    @timeit
    def f():
        time.sleep(0.0005)
        return "x"

    val = f()
    assert val == "x"
    assert hasattr(f, "records")
    assert len(f.records) == 3
    assert isinstance(f.last_elapsed, float)