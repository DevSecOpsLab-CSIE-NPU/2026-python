"""任務一: 提供可重複量測的 timeit 裝飾器。"""

from __future__ import annotations

import functools
import time
from typing import Any, Callable, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def _validate_repeat(repeat: int) -> None:
    """驗證 repeat 參數合法。"""
    if isinstance(repeat, bool) or not isinstance(repeat, int):
        raise ValueError("repeat 必須是整數")
    if repeat < 1:
        raise ValueError("repeat 必須 >= 1")


def _decorate(func: F, repeat: int) -> F:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        durations: list[float] = []
        result: Any = None

        for _ in range(repeat):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            durations.append(end - start)

        wrapper.records.extend(durations)
        wrapper.last_elapsed = sum(durations) / repeat
        return result

    wrapper.records = []
    wrapper.last_elapsed = 0.0
    return cast(F, wrapper)


def timeit(func: F | None = None, *, repeat: int = 3) -> Callable[[F], F] | F:
    """量測函式執行時間。

    可用法:
    - @timeit
    - @timeit(repeat=5)
    """
    _validate_repeat(repeat)

    if func is None:
        return lambda real_func: _decorate(real_func, repeat)
    return _decorate(func, repeat)
