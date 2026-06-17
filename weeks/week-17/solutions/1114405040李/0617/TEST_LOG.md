# TEST_LOG

## 2026-06-17

Command:

```bash
python -m unittest
```

Result:

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

Command:

```bash
python temporary benchmark script
```

Result summary:

```text
linear_search and binary_search both returned index 99999.
linear_average: 0.0026701999999659163
binary_average: 0.0000024199999643315096
binary_search was much faster because it halves the search range each step.
```
