pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\CaesarCipher> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\CaesarCipher
plugins: anyio-4.13.0
collected 0 items / 1 error                                                                           

=============================================== ERRORS ===============================================
_______________________________ ERROR collecting test_caesar_cipher.py _______________________________
ImportError while importing test module 'D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\CaesarCipher\test_caesar_cipher.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_caesar_cipher.py:3: in <module>
    from caesar_cipher import caesar_cipher, process_text
E   ModuleNotFoundError: No module named 'caesar_cipher'
====================================== short test summary info =======================================
ERROR test_caesar_cipher.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================== 1 error in 0.23s ==========================================

pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\CaesarCipher> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\CaesarCipher
plugins: anyio-4.13.0
collected 10 items                                                                                    

test_caesar_cipher.py ..........                                                                [100%]

========================================= 10 passed in 0.05s =========================================
