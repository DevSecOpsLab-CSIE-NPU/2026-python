@echo off
setlocal
cd /d %~dp0

echo [Robot Lost] Running tests...
d:\1114405048\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v

echo.
echo [Robot Lost] Test process finished with exit code %ERRORLEVEL%.
pause

endlocal

