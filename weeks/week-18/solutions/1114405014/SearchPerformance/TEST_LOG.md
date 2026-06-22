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

pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance
plugins: anyio-4.13.0
collected 14 items                                                                                    

test_search_performance.py .............F                                                       [100%]

============================================== FAILURES ==============================================
_______________________________ test_make_radar_chart_creates_png_file _______________________________

tmp_path = WindowsPath('C:/Users/hc105/AppData/Local/Temp/pytest-of-hc105/pytest-20/test_make_radar_chart_creates_0')

    def test_make_radar_chart_creates_png_file(tmp_path):
        metrics = {
            "linear_time": 0.01,
            "binary_time": 0.001,
            "linear_cmp": 100,
            "binary_cmp": 7,
        }
        output_path = tmp_path / "radar.png"
    
>       make_radar_chart(metrics, output_path)

test_search_performance.py:158: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
search_performance.py:163: in make_radar_chart
    fig = plt.figure(figsize=(6, 6))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\pyplot.py:1041: in figure
    manager = new_figure_manager(
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\pyplot.py:551: in new_figure_manager
    return _get_backend_mod().new_figure_manager(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\backend_bases.py:3504: in new_figure_manager
    return cls.new_figure_manager_given_figure(num, fig)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\backend_bases.py:3509: in new_figure_manager_given_figure
    return cls.FigureCanvas.new_manager(figure, num)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\backend_bases.py:1785: in new_manager
    return cls.manager_class.create_with_canvas(cls, figure, num)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\matplotlib\backends\_backend_tk.py:535: in create_with_canvas
    window = tk.Tk(className="matplotlib")
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tkinter.Tk object .>, screenName = None, baseName = 'pytest', className = 'matplotlib'
useTk = True, sync = False, use = None

    def __init__(self, screenName=None, baseName=None, className='Tk',
                 useTk=True, sync=False, use=None):
        """Return a new top level widget on screen SCREENNAME. A new Tcl interpreter will
        be created. BASENAME will be used for the identification of the profile file (see
        readprofile).
        It is constructed from sys.argv[0] without extensions if None is given. CLASSNAME
        is the name of the widget class."""
        self.master = None
        self.children = {}
        self._tkloaded = False
        # to avoid recursions in the getattr code in case of failure, we
        # ensure that self.tk is always _something_.
        self.tk = None
        if baseName is None:
            import os
            baseName = os.path.basename(sys.argv[0])
            baseName, ext = os.path.splitext(baseName)
            if ext not in ('.py', '.pyc'):
                baseName = baseName + ext
        interactive = False
>       self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       _tkinter.TclError: invalid command name "tcl_findLibrary"

C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\tkinter\__init__.py:2484: TclError
====================================== short test summary info =======================================
FAILED test_search_performance.py::test_make_radar_chart_creates_png_file - _tkinter.TclError: invalid command name "tcl_findLibrary"
==================================== 1 failed, 13 passed in 3.75s ====================================

pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance
plugins: anyio-4.13.0
collected 14 items                                                                                    

test_search_performance.py ..............                                                       [100%]

========================================= 14 passed in 1.10s =========================================

PS D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance
plugins: anyio-4.13.0
collected 0 items / 2 errors                                                                          

=============================================== ERRORS ===============================================
___________________________________ ERROR collecting test_plot.py ____________________________________
ImportError while importing test module 'D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance\test_plot.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_plot.py:1: in <module>
    from plot import inverse_score, make_radar_chart
E   ModuleNotFoundError: No module named 'plot'
____________________________ ERROR collecting test_search_performance.py _____________________________
ImportError while importing test module 'D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance\test_search_performance.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\hc105\AppData\Local\Python\pythoncore-3.14-64\Lib\importlib\__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
test_search_performance.py:3: in <module>
    from search_performance import (
search_performance.py:4: in <module>
    from plot import make_radar_chart
E   ModuleNotFoundError: No module named 'plot'
====================================== short test summary info =======================================
ERROR test_plot.py
ERROR test_search_performance.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 2 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
========================================= 2 errors in 0.25s ==========================================

pytest
PS D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance> pytest
======================================== test session starts =========================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: D:\Edwin\program\program-python\2026-python\weeks\week-18\solutions\1114405014\SearchPerformance
plugins: anyio-4.13.0
collected 18 items                                                                                    

test_plot.py ....                                                                               [ 22%]
test_search_performance.py ..............                                                       [100%]

========================================= 18 passed in 1.48s =========================================
