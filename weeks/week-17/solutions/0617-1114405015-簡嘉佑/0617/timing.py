"""Timing utilities for 0617 search evaluation."""

from __future__ import annotations

import functools
import time
from typing import Any, Callable, TypeVar

R = TypeVar("R")


def timeit(*, repeat: int = 3) -> Callable[[Callable[..., R]], Callable[..., R]]:
    """Measure function runtime and store per-call timing records.

    Args:
        repeat: Number of runs per call. Must be >= 1.

    Returns:
        A decorator that wraps the target function.

    Raises:
        ValueError: If repeat is less than 1.
    """
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> R:
            elapsed_values: list[float] = []
            result: R | None = None

            for _ in range(repeat):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                elapsed_values.append(time.perf_counter() - start)

            wrapper.records.extend(elapsed_values)
            wrapper.last_elapsed = sum(elapsed_values) / repeat
            return result  # type: ignore[return-value]

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    return decorator
