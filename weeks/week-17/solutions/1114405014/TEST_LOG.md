PS D:\2026-python\weeks\week-17\solutions\1114405014> pytest                      
============================== test session starts ==============================
platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0
rootdir: D:\2026-python\weeks\week-17\solutions\1114405014
plugins: anyio-4.10.0
collected 0 items / 1 error                                                      

==================================== ERRORS =====================================
________________________ ERROR collecting test_timing.py ________________________
ImportError while importing test module 'D:\2026-python\weeks\week-17\solutions\1114405014\test_timing.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\anaconda3\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_timing.py:23: in <module>
    from timing import timeit
E   ModuleNotFoundError: No module named 'timing'
============================ short test summary info ============================ 
ERROR test_timing.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!! 
=============================== 1 error in 0.09s ================================ 

PS D:\2026-python\weeks\week-17\solutions\1114405014> pytest
============================== test session starts ==============================
platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0
rootdir: D:\2026-python\weeks\week-17\solutions\1114405014
plugins: anyio-4.10.0
collected 6 items                                                                

test_timing.py ......                                                      [100%]

=============================== 6 passed in 0.02s ===============================

PS D:\2026-python\weeks\week-17\solutions\1114405014> pytest
============================== test session starts ==============================
platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0
rootdir: D:\2026-python\weeks\week-17\solutions\1114405014
plugins: anyio-4.10.0
collected 6 items / 1 error                                                      

==================================== ERRORS =====================================
________________________ ERROR collecting test_search.py ________________________
ImportError while importing test module 'D:\2026-python\weeks\week-17\solutions\1114405014\test_search.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\User\anaconda3\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_search.py:19: in <module>
    from search import linear_search, binary_search
E   ModuleNotFoundError: No module named 'search'
============================ short test summary info ============================ 
ERROR test_search.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!! 
=============================== 1 error in 0.10s ================================