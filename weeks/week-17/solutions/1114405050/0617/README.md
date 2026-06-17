# 0617 — timeit + Search Performance Evaluation

## Task 1: timing.py

`@timeit(repeat=3)` decorator that measures execution time.

## Task 2: search.py

- `linear_search(data, target)` — O(n)
- `binary_search(data, target)` — O(log n), data must be sorted

## Performance Intuition

- Linear search is simpler and works on unsorted data, O(n).
- Binary search is O(log n) but requires sorted data (O(n log n) sorting cost).
- For a one-time search on small data, linear is usually faster because sorting dominates.
- For many searches on the same data, sorting once then binary searching is worthwhile.
- The exact crossover point depends on data size and search count.
