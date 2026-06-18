# PR Title
Week 17 - 1114405035 - 賴彥廷

# PR Description
This pull request implements the Week 17 (06/18) Search Performance Lab. It includes the design and implementation of a robust, parameter-based `@timeit` decorator, multiple search algorithms (linear, binary, set), built-in/optimized baseline counterparts, evaluation scripts, polar radar chart visualization, unit testing (14 tests in total), and security compliance verification.

### Completed Stages:
- **Stage 1 (Timing Decorator)**: Implemented a robust `@timeit` decorator factory supporting optional `repeat` parameter, defensive checks (`raise ValueError`), and metadata preservation via `functools.wraps`.
- **Stage 2 (Search & Benchmark)**: Implemented `linear_search`, `binary_search` (sorted assumption), and `set_search` with unit tests for correctness, immutability, duplicates, and invalid types.
- **Stage 3 (Baseline & Crossover)**: Integrated standard library C-based alternatives (`builtin_linear_search`, `builtin_binary_search`) and optimized Set search. Run crossover point experiment showing that with $Q=100$, "Sort + Binary" wins starting at $N=10$.
- **Stage 4 (Radar Chart)**: Generated a multi-dimensional polar radar chart comparing five metrics (speed, pre-processing, space, unsorted support, code simplicity) normalized to a 1-5 scale.
- **Stage 5 (Security Compliance)**: Implemented static regex scans and dynamic checks validating zero-pickle, zero-assert validation, and defensive non-positive integer checks.

### References:
- [1] [timing.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0618/timing.py)
- [2] [search.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0618/search.py)
- [3] [benchmark.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0618/benchmark.py)
- [4] [plot.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0618/plot.py)
- [5] [test_security.py](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0618/test_security.py)
- [6] [README.md](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0618/README.md)
- [7] [AI_LOG.md](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0618/AI_LOG.md)
- [8] [TEST_LOG.md](file:///d:/pychon/2026-python/weeks/week-17/solutions/1114405035/0618/TEST_LOG.md)
