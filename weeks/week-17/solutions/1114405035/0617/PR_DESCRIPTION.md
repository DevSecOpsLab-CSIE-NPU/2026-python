# PR Title
Week 17 - 1114405035 - 賴彥廷

# PR Description
This pull request implements the Week 17 (06/17) pre-run exercise for the search performance evaluation project. It includes the design and implementation of a robust, parameter-based `@timeit` decorator, linear and binary search algorithms, a test suite for correctness and constraints, process logs, and an evaluation report comparing the performance of both search methods.

### Timeit Decorator:
- Implemented a robust `@timeit` decorator in `timing.py` that supports optional `repeat` parameter (default is 3), captures execution times, tracks cumulative records in `f.records`, and computes the average execution time in `f.last_elapsed`.
- Designed defensive input check for `repeat` to raise `ValueError` (rather than `assert`) if it is not an integer or is less than 1.

### Search Algorithms & Benchmarking:
- Implemented `linear_search` and `binary_search` in `search.py` without modifying the input array.
- Defined behavior for unsorted inputs to `binary_search` as undefined behavior (not sorting internally to maintain O(log n) efficiency).
- Wrote a benchmarking script that measures search times under $N = 100,000$ and calculates the average speedup.

### Testing & Verification:
- Created unit tests in `test_timing.py` verifying return values, metadata preservation, cumulative record tracking, and parameter validation.
- Created unit tests in `test_search.py` verifying the correctness of `linear_search` and `binary_search` along with immutability tests.

### Documentation & Process logs:
- Created `README.md` containing performance comparison results and an intuitive analysis of "sorting + binary search" versus linear search.
- Created `AI_LOG.md` tracking the AI collaboration checklist and prompt records.
- Created `TEST_LOG.md` displaying the unit testing logs (both red and green phases).

### References:
- [1] [timing.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0617/timing.py)
- [2] [test_timing.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0617/test_timing.py)
- [3] [search.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0617/search.py)
- [4] [test_search.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0617/test_search.py)
- [5] [README.md](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0617/README.md)
- [6] [AI_LOG.md](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0617/AI_LOG.md)
- [7] [TEST_LOG.md](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0617/TEST_LOG.md)
