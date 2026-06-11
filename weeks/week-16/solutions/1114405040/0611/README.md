# Week 16 0611 Sorting Lab

## Files

- `timing.py`: `@timeit` decorator, records `last_elapsed` and `records` without printing.
- `sorts.py`: bubble sort, quick sort, and merge sort. Each returns a new sorted list and keeps the input unchanged.
- `sorts_fast.py`: Stage 3 optimized quick sort using median-of-three pivot selection and in-place partitioning on a private copy.
- `benchmark.py`: deterministic benchmark runner that writes `results.json`.
- `plot.py`: loads `results.json` and writes `assets/benchmark.png` with a log-scale y-axis.
- `test_*.py`: unittest coverage for timing, sorting, plotting, and security practices.

## Benchmark Notes

Bubble sort grows close to O(n^2), so it becomes much slower as input size doubles. Quick sort, merge sort, optimized quick sort, and Python's built-in `sorted()` follow the expected O(n log n) shape, with `sorted()` fastest because it uses CPython's highly optimized Timsort implementation.

The optimized quick sort avoids building many temporary `less/equal/greater` lists and uses a median-of-three pivot to reduce bad partitions. In this run it was close to the simple quick sort, while the built-in baseline remained much faster.

## Security Notes

- `results.json` is read and written with `json`, not `pickle`, to avoid unsafe deserialization.
- File operations use `with` blocks so files are closed even if an error occurs.
- Public inputs such as negative sizes and invalid repeat counts raise `ValueError` instead of silently producing misleading results.
- Benchmark randomness uses deterministic `random.Random(seed)` because the data is not security-sensitive.

## Run

```powershell
python -m unittest
python benchmark.py
python plot.py
```
