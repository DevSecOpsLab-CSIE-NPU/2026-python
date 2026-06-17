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
