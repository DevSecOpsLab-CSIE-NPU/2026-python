pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance
plugins: anyio-4.13.0
collected 0 items / 1 error                                                                           

=============================================== ERRORS ===============================================
____________________________ ERROR collecting test_search_performance.py _____________________________
ImportError while importing test module 'D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance\test_search_performance.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_search_performance.py:3: in <module>
    from search_performance import (
E   ModuleNotFoundError: No module named 'search_performance'
====================================== short test summary info =======================================
ERROR test_search_performance.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================== 1 error in 0.27s ==========================================
