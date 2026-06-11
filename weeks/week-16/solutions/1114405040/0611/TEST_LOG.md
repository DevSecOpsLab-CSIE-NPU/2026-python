# TEST_LOG

Commands were run from:

`C:\Users\洪士閔\Desktop\1111\2026-python\weeks\week-16\solutions\1114405040\0611`

Python interpreter:

`C:\Users\洪士閔\AppData\Local\Programs\Python\Python313\python.exe`

## Results

### Unit Tests

Command:

```powershell
& "C:\Users\洪士閔\AppData\Local\Programs\Python\Python313\python.exe" -m unittest
```

Output:

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 0.267s

OK
```

### Benchmark

Command:

```powershell
& "C:\Users\洪士閔\AppData\Local\Programs\Python\Python313\python.exe" benchmark.py
```

Output:

```text
bubble_sort            n=4000 avg=0.591572s
quick_sort             n=4000 avg=0.003909s
merge_sort             n=4000 avg=0.005787s
optimized_quick_sort   n=4000 avg=0.003984s
builtin_sorted         n=4000 avg=0.000508s
```

### Plot

Command:

```powershell
& "C:\Users\洪士閔\AppData\Local\Programs\Python\Python313\python.exe" plot.py
```

Output:

```text
No terminal output. Verified that assets/benchmark.png exists.
```
