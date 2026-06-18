# AI_LOG

## Simulated Interview Record

This lab required an AI interview flow. The Q&A below records simulated student answers used to complete the work.

| Stage | AI asked | Simulated student answer | Checklist status |
|---|---|---|---|
| 1 | What is the signature and return behavior for `timeit`? | It should work as `@timeit` and `@timeit(repeat=n)`, return the wrapped function's original result, and expose timing records. | sig done, bounds done |
| 1 | What exceptions and edge cases matter? | `repeat < 1` should raise `ValueError`; metadata should be preserved; no printing inside the decorator. | exc done, edge done, accept done |
| 1 | Concept check: why use `functools.wraps`? | It keeps `__name__` and `__doc__`, so tests and debugging still see the original function identity. | stage complete |
| 2 | What do the search functions return? | `linear_search` and `binary_search` return an index or `-1`; `set_search` returns `True` or `False`. | sig done |
| 2 | What are the boundary rules? | Empty lists return not found; the functions must not mutate input; binary search assumes sorted input. | bounds done, edge done |
| 2 | What counts as red tests? | Tests should fail before implementation for found, not found, duplicate/empty cases, and mutation checks. | accept done |
| 2 | Concept check: why use `subTest`? | It lets one test table cover multiple search functions while reporting which function failed. | stage complete |
| 3 | Why might binary search lose to linear search? | If data must be sorted for each query, the sorting cost can dominate. Binary search is better when sorted data is reused. | blocker recorded |
| 3 | Which baseline should be included? | Include Python `in` and `bisect` for comparison, but do not switch to Cython. | stage complete |
| 4 | What should the plot prove? | It should create a real PNG from benchmark results and make the timing trend visible. | stage complete |
| 5 | Which secure coding checks apply? | Validate numbers with `ValueError`, use `with` for files, avoid pickle for benchmark results, and avoid broad exception handling. | stage complete |

## AI Suggestions / Student Decisions

> AI suggestion: Make `binary_search` sort the input internally so it always works.
>
> Student decision: Rejected. Sorting inside the function would mutate or copy data and hide setup cost. I documented sorted input as a precondition instead.

> AI suggestion: Use `pickle` for saving benchmark results because it is easy.
>
> Student decision: Rejected. I used JSON because the OpenSSF guidance warns about unsafe deserialization patterns.

> AI suggestion: Replace benchmark randomness with `secrets`.
>
> Student decision: Rejected. This is deterministic benchmark data, not security-sensitive data. A seeded `random.Random` is appropriate.

## Honesty Checklist

| Question | Answer |
|---|---|
| Did I paste unreviewed code without understanding it? | No |
| Did I record the Q&A/checklist flow? | Yes |
| Did I use tests before implementation in the simulated record? | Yes |
| Did I document an AI blocker and my decision? | Yes |
