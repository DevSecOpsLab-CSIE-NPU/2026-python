pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\BaseDigitRoot> pytest

======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\BaseDigitRoot
plugins: anyio-4.13.0
collected 0 items / 1 error                                                                           

=============================================== ERRORS ===============================================
______________________________ ERROR collecting test_base_digit_root.py ______________________________
ImportError while importing test module 'D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\BaseDigitRoot\test_base_digit_root.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_base_digit_root.py:3: in <module>
    from base_digit_root import to_base_digits, digit_root_in_base, solve
E   ModuleNotFoundError: No module named 'base_digit_root'
====================================== short test summary info =======================================
ERROR test_base_digit_root.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================== 1 error in 0.45s ==========================================

pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\BaseDigitRoot> pytest

======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\BaseDigitRoot
plugins: anyio-4.13.0
collected 14 items                                                                                    

test_base_digit_root.py ..............                                                          [100%]

========================================= 14 passed in 0.06s =========================================
