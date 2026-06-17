# TEST_LOG

## Red Test

Command:

```bash
python -m unittest
```

Result:

```text
ERROR: test_search
ModuleNotFoundError: No module named 'search'

ERROR: test_timing
ModuleNotFoundError: No module named 'timing'

FAILED (errors=2)
```

## Green Test

Command:

```bash
python -m unittest
```

Result:

```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```

## Improvement Red Test

Command:

```bash
python -m unittest
```

Result:

```text
FAILED (failures=1, errors=1)
```

The added tests showed two gaps:

- `timeit` did not support `@timeit(repeat=2)` decorator-factory style.
- `binary_search` returned a matching duplicate index, but not the first one.

## Improvement Green Test

Command:

```bash
python -m unittest
```

Result:

```text
..........
----------------------------------------------------------------------
Ran 10 tests

OK
```
