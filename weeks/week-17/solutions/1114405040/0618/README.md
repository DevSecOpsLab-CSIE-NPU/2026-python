# Week 17 0618 Search Lab

Student: 1114405040

## Files

- `timing.py`: `@timeit` decorator with repeat support, `records`, and `last_elapsed`.
- `search.py`: `linear_search`, `binary_search`, and `set_search`.
- `benchmark.py`: deterministic benchmark runner and JSON read/write helpers.
- `plot.py`: writes `assets/radar.png` from `results.json`.
- `test_*.py`: unittest checks for behavior, plot output, and secure coding points.

## Stage 3 Analysis

Binary search is not automatically faster for every input size. It only wins when the data is already sorted or when the cost of sorting can be shared across many queries. If every query first sorts a new list, that extra `O(n log n)` work can be worse than one `O(n)` linear scan.

In this lab I treated sorted input as a precondition for `binary_search`. That keeps the function honest: it does not mutate the caller's list, and the benchmark measures search cost instead of hiding setup cost. For one-off unsorted data, linear search is simpler. For repeated queries on stable data, binary search or a prepared set-backed lookup usually pays off.

The benchmark also includes Python baselines: `target in data` for linear membership, `bisect` for binary search, and `set_prepared` for the case where a set is built once and reused. The plain `set_search(data, target)` result is slower for large lists because it rebuilds the set on every call; that is the setup cost the analysis is meant to expose.

## Plot Notes

`assets/radar.png` is generated from `results.json`. It compares timing trends across data sizes for linear, binary, per-call set construction, prepared-set lookup, `in`, and `bisect` approaches. The exact numbers vary by machine, but the expected trend is that prepared set membership and binary/bisect search scale better than linear scans as `n` grows.

## Secure Coding Notes

- Input validation uses `raise ValueError`, not `assert`.
- JSON files are read and written with `with` blocks and `encoding="utf-8"`.
- Benchmark data uses deterministic `random.Random(seed)` because this is measurement data, not security-sensitive randomness.
- `results.json` uses JSON rather than pickle to avoid unsafe deserialization.
