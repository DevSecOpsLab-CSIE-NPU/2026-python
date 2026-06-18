# Stage 3 Prediction

This stage measures search performance on the local machine and records the data in `results.json`.

## Prediction

- Query-only ranking: `set_contains` should be fastest, then `bisect_left`, then built-in `in`, then `set_search`, `binary_search`, and `linear_search`.
- If I include setup cost, I expect `binary_with_sort` to beat `linear_search` only after the data size becomes large enough and the query count is high enough to amortize sorting.
- My initial crossover guess is around `n = 20000` with `queries = 100`.

## Method

- `make_data(n, seed=42)` creates a shuffled list of `range(n)`.
- Queries are generated deterministically from a seed so repeated runs stay comparable.
- Each measurement is repeated three times with the project `timeit` decorator.
- The benchmark also records a prebuilt `set` membership check so the cost of building the set can be compared with repeated lookups.

## Output

- Run `python benchmark.py` to print the table and write `results.json`.