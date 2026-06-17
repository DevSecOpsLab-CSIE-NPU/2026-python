# 0617 Search Evaluation

## Summary

This solution includes:

- `timing.py`: a `timeit(func, repeat=3)` helper that records average elapsed time.
- `search.py`: `linear_search` and `binary_search`.
- `test_timing.py` and `test_search.py`: unittest coverage for normal cases and edge cases.

## Test Result

Run from this folder:

```bash
python -m unittest
```

Expected result:

```text
Ran 10 tests

OK
```

## Timing Observation

`linear_search` checks items one by one, so its time grows roughly with `n`.
`binary_search` only works correctly when the input list is already sorted, but
then it can discard half of the remaining search range each step, so its search
time grows much more slowly.

I did not make `binary_search` check whether `data` is sorted. That check would
require scanning the whole list first, which is `O(n)` and would remove the main
benefit of binary search.

`binary_search` uses Python's standard-library `bisect_left`, which keeps the
search behavior logarithmic for sorted input and returns the first matching
index when duplicates are present.
